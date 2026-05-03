const fs = require('fs');
const path = require('path');

const TULISAN_DIR = './tulisan';
const MANIFEST_PATH = './data/manifest.json';

function finalSeparateMigrate() {
    const manifest = JSON.parse(fs.readFileSync(MANIFEST_PATH, 'utf-8'));
    const writings = manifest.writing || [];

    writings.forEach(item => {
        const slug = item.slug;
        const folderPath = path.join(TULISAN_DIR, slug);
        const mdocFile = path.join(folderPath, 'index.mdoc');

        if (!fs.existsSync(mdocFile)) return;

        // Get clean ID content (body only)
        // We'll extract the clean body (everything after the frontmatter)
        let currentContent = fs.readFileSync(mdocFile, 'utf-8');
        const parts = currentContent.split('\n---\n');
        const body = parts.pop().trim();

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
            yaml += `${key}: ${JSON.stringify(value)}\n`;
        }
        yaml += '---\n';

        fs.writeFileSync(mdocFile, yaml + '\n' + body);
        console.log(`Final ID cleaned: ${slug}`);
    });
}

finalSeparateMigrate();
