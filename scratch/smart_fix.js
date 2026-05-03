const fs = require('fs');
const path = require('path');

const TULISAN_DIR = './tulisan';
const MANIFEST_PATH = './data/manifest.json';

function smartestBodyExtraction() {
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
        
        // Find if there is frontmatter
        // Check if it starts with ---
        if (fullContent.trim().startsWith('---')) {
            const firstDashes = fullContent.indexOf('---');
            const secondDashes = fullContent.indexOf('---', firstDashes + 3);
            
            if (secondDashes !== -1) {
                // Has frontmatter, take everything after the second dashes
                idBody = fullContent.substring(secondDashes + 3).trim();
            } else {
                // Only one dashes found, or malformed, take everything
                idBody = fullContent.trim();
            }
        } else {
            // NO FRONTMATTER at start, the WHOLE file is the body
            idBody = fullContent.trim();
        }
        
        // Clean body from stars only at start of line
        idBody = idBody.replace(/^\*/gm, '-').replace(/^\*\*/gm, '__');

        const fields = {
            slug: slug,
            title_id: manifestItem.title,
            title_en: manifestItem.title_en,
            date: manifestItem.date,
            category: manifestItem.category,
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
        console.log(`Smartly Fixed: ${slug}`);
    });
}

smartestBodyExtraction();
