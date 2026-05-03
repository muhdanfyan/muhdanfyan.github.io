const fs = require('fs');
const path = require('path');

const TULISAN_DIR = './tulisan';
const MANIFEST_PATH = './data/manifest.json';

function smartestBodyExtractionWithUrlSupport() {
    const folders = fs.readdirSync(TULISAN_DIR);
    const manifest = JSON.parse(fs.readFileSync(MANIFEST_PATH, 'utf-8'));
    const writings = manifest.writing || [];

    folders.forEach(slug => {
        const folderPath = path.join(TULISAN_DIR, slug);
        if (!fs.lstatSync(folderPath).isDirectory()) return;

        const idSource = path.join(folderPath, 'tulisan.md');
        if (!fs.existsSync(idSource)) return;

        const manifestItem = writings.find(w => w.slug === slug);
        if (!manifestItem) return;

        const fullContent = fs.readFileSync(idSource, 'utf-8');
        
        let idBody = "";
        if (fullContent.trim().startsWith('---')) {
            const firstDashes = fullContent.indexOf('---');
            const secondDashes = fullContent.indexOf('---', firstDashes + 3);
            if (secondDashes !== -1) {
                idBody = fullContent.substring(secondDashes + 3).trim();
            } else {
                idBody = fullContent.trim();
            }
        } else {
            idBody = fullContent.trim();
        }
        
        idBody = idBody.replace(/^\*/gm, '-').replace(/^\*\*/gm, '__');

        // SMART IMAGE HANDLING: 
        // If it starts with http, keep it. Otherwise, just take the basename for local storage.
        const originalImage = manifestItem.image || '';
        const finalImage = originalImage.startsWith('http') ? originalImage : path.basename(originalImage);

        const fields = {
            slug: slug,
            title_id: manifestItem.title,
            title_en: manifestItem.title_en,
            date: manifestItem.date,
            category: manifestItem.category,
            description_id: manifestItem.description,
            description_en: manifestItem.description_en,
            image: finalImage
        };

        let yaml = '---\n';
        for (const [key, value] of Object.entries(fields)) {
            yaml += `${key}: ${JSON.stringify(value)}\n`;
        }
        yaml += '---\n';

        fs.writeFileSync(path.join(folderPath, 'index.mdoc'), yaml + '\n' + idBody);
        console.log(`Smartly Fixed with URL support: ${slug}`);
    });
}

smartestBodyExtractionWithUrlSupport();
