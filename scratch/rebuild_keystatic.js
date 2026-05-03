const fs = require('fs');
const path = require('path');

const TULISAN_DIR = './tulisan';
const MANIFEST_PATH = './data/manifest.json';

function rebuildKeystatic() {
    const folders = fs.readdirSync(TULISAN_DIR);
    const manifest = JSON.parse(fs.readFileSync(MANIFEST_PATH, 'utf-8'));
    const writings = manifest.writing || [];

    folders.forEach(slug => {
        const folderPath = path.join(TULISAN_DIR, slug);
        if (!fs.lstatSync(folderPath).isDirectory()) return;

        // 1. Delete broken files
        ['index.mdoc', 'index.en.mdoc'].forEach(f => {
            const p = path.join(folderPath, f);
            if (fs.existsSync(p)) fs.unlinkSync(p);
        });

        // 2. Find clean source
        const idSource = path.join(folderPath, 'tulisan.md');
        const enSource = path.join(folderPath, 'tulisan.en.md');
        
        if (!fs.existsSync(idSource)) return;

        const manifestItem = writings.find(w => w.slug === slug);
        if (!manifestItem) return;

        // 3. Prepare ID content
        let idFull = fs.readFileSync(idSource, 'utf-8');
        let idBody = idFull.split('\n---\n').pop().trim();
        // Clean body from stars to avoid YAML alias issues if any
        idBody = idBody.replace(/^\*/gm, '-').replace(/^\*\*/gm, '__');

        const fields = {
            slug: slug,
            title_id: manifestItem.title,
            title_en: manifestItem.title_en,
            date: manifestItem.date,
            category: manifestItem.category, // Unified category
            description_id: manifestItem.description,
            description_en: manifestItem.description_en,
            image: path.basename(manifestItem.image)
        };

        let yaml = '---\n';
        for (const [key, value] of Object.entries(fields)) {
            yaml += `${key}: ${JSON.stringify(value)}\n`;
        }
        yaml += '---\n';

        fs.writeFileSync(path.join(folderPath, 'index.mdoc'), yaml + '\n' + idBody);

        // 4. Prepare EN content if exists
        if (fs.existsSync(enSource)) {
            let enFull = fs.readFileSync(enSource, 'utf-8');
            let enBody = enFull.replace(/^---[\s\S]*?---\n/m, '').trim();
            enBody = enBody.replace(/^\*/gm, '-').replace(/^\*\*/gm, '__');

            let enYaml = '---\n';
            enYaml += `slug: ${JSON.stringify(slug)}\n`;
            enYaml += '---\n';

            fs.writeFileSync(path.join(folderPath, 'index.en.mdoc'), enYaml + '\n' + enBody);
        }

        console.log(`Successfully Rebuilt: ${slug}`);
    });
}

rebuildKeystatic();
