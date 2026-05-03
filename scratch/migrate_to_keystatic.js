const fs = require('fs');
const path = require('path');

const MANIFEST_PATH = './data/manifest.json';
const TULISAN_DIR = './tulisan';

function migrate() {
    if (!fs.existsSync(MANIFEST_PATH)) {
        console.log("Manifest not found.");
        return;
    }

    const manifest = JSON.parse(fs.readFileSync(MANIFEST_PATH, 'utf-8'));
    const writings = manifest.writing || [];
    console.log(`Found ${writings.length} writings to migrate.`);

    writings.forEach(item => {
        const slug = item.slug;
        if (!slug) return;

        const folderPath = path.join(TULISAN_DIR, slug);
        const idFile = path.join(folderPath, 'tulisan.md');
        const enFile = path.join(folderPath, 'tulisan.en.md');

        if (!fs.existsSync(idFile)) {
            console.log(`Warning: ${idFile} not found. Skipping.`);
            return;
        }

        const contentId = fs.readFileSync(idFile, 'utf-8');
        
        let contentEnRaw = "";
        if (fs.existsSync(enFile)) {
            contentEnRaw = fs.readFileSync(enFile, 'utf-8');
        }

        const frontmatter = {
            title_id: item.title,
            title_en: item.title_en,
            date: item.date,
            category_id: item.category,
            category_en: item.category_en,
            description_id: item.description,
            description_en: item.description_en,
            image: item.image,
            // We store EN content as a simple markdown string for now
            // To be compatible with our updated Keystatic config
            content_en_markdown: contentEnRaw 
        };

        const newContent = `---json
${JSON.stringify(frontmatter, null, 2)}
---

${contentId}`;

        fs.writeFileSync(idFile, newContent);
        console.log(`Migrated: ${slug}`);
    });
}

migrate();
