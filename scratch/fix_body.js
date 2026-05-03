const fs = require('fs');
const path = require('path');

const TULISAN_DIR = './tulisan';
const MANIFEST_PATH = './data/manifest.json';

function fixBodyExtractionOnceAndForAll() {
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

        // READ FULL CONTENT
        const fullContent = fs.readFileSync(idSource, 'utf-8');
        
        // BETTER LOGIC: Find the second occurrence of '---'
        // The first is at the start (line 1), the second is the end of frontmatter
        const firstDashes = fullContent.indexOf('---');
        const secondDashes = fullContent.indexOf('---', firstDashes + 3);
        
        if (secondDashes === -1) return;
        
        // The body is EVERYTHING after the second '---'
        let idBody = fullContent.substring(secondDashes + 3).trim();
        
        // Clean body from stars only at start of line to avoid YAML alias issues
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

        // Write the perfect file
        fs.writeFileSync(path.join(folderPath, 'index.mdoc'), yaml + '\n' + idBody);
        console.log(`Perfectly Restored Body for: ${slug}`);
    });
}

fixBodyExtractionOnceAndForAll();
