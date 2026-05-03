const fs = require('fs');
const path = require('path');

const TULISAN_DIR = './tulisan';
const MANIFEST_PATH = './data/manifest.json';

function verySafeMigrate() {
    const manifest = JSON.parse(fs.readFileSync(MANIFEST_PATH, 'utf-8'));
    const writings = manifest.writing || [];

    writings.forEach(item => {
        const slug = item.slug;
        const folderPath = path.join(TULISAN_DIR, slug);
        const mdocFile = path.join(folderPath, 'index.mdoc');
        const enFile = path.join(folderPath, 'tulisan.en.md');

        if (!fs.existsSync(mdocFile)) return;

        // Clean body (Indonesian)
        let currentContent = fs.readFileSync(mdocFile, 'utf-8');
        let body = currentContent.split('\n---\n').pop().trim();

        // Clean English content
        let contentEnRaw = "";
        if (fs.existsSync(enFile)) {
            contentEnRaw = fs.readFileSync(enFile, 'utf-8');
            contentEnRaw = contentEnRaw.replace(/^---[\s\S]*?---\n/m, '');
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
            // Just use the filename for the image
            image: path.basename(item.image)
        };

        let yaml = '---\n';
        for (const [key, value] of Object.entries(fields)) {
            yaml += `${key}: ${JSON.stringify(value)}\n`;
        }
        
        // Use 4 spaces indentation for content_en_markdown to be SUPER safe
        yaml += `content_en_markdown: |\n${contentEnRaw.split('\n').map(l => '    ' + l).join('\n')}\n`;
        yaml += '---\n';

        fs.writeFileSync(mdocFile, yaml + '\n' + body);
    });
}

verySafeMigrate();
