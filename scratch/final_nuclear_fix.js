const fs = require('fs');
const path = require('path');

const TULISAN_DIR = './tulisan';
const MANIFEST_PATH = './data/manifest.json';

function finalAttempt() {
    const manifest = JSON.parse(fs.readFileSync(MANIFEST_PATH, 'utf-8'));
    const writings = manifest.writing || [];

    writings.forEach(item => {
        const slug = item.slug;
        const folderPath = path.join(TULISAN_DIR, slug);
        const idFile = path.join(folderPath, 'index.mdoc');
        const enFile = path.join(folderPath, 'index.en.mdoc');

        // Extract body by looking for the first occurrence of the actual text
        // We'll use a very safe way: look for the first line that doesn't look like frontmatter
        let body = "";
        if (fs.existsSync(idFile)) {
            const content = fs.readFileSync(idFile, 'utf-8');
            const parts = content.split('\n---\n');
            // We'll take the largest part as the body
            body = parts.reduce((a, b) => a.length > b.length ? a : b);
            
            // CLEAN BODY: Remove all '*' at the start of lines to avoid YAML alias errors
            body = body.replace(/^\*/gm, '-'); 
            // Also replace '**' to avoid issues
            body = body.replace(/^\*\*/gm, '__');
        }

        const fields = {
            slug: item.slug,
            title_id: item.title,
            title_en: item.title_en,
            date: item.date,
            category_id: item.category,
            category_en: item.category_en,
            description_id: item.description,
            description_en: item.description_en,
            image: path.basename(item.image)
        };

        let yaml = '---\n';
        for (const [key, value] of Object.entries(fields)) {
            // Using JSON.stringify makes it safe for YAML
            yaml += `${key}: ${JSON.stringify(value)}\n`;
        }
        yaml += '---\n';

        fs.writeFileSync(idFile, yaml + '\n' + body);
        console.log(`Final Fix Applied: ${slug}`);
    });
}

finalAttempt();
