const fs = require('fs');
const path = require('path');

const TULISAN_DIR = './tulisan';
const MANIFEST_PATH = './data/manifest.json';

function finalCleanup() {
    const manifest = JSON.parse(fs.readFileSync(MANIFEST_PATH, 'utf-8'));
    const writings = manifest.writing || [];

    writings.forEach(item => {
        const slug = item.slug;
        const folderPath = path.join(TULISAN_DIR, slug);
        const mdocFile = path.join(folderPath, 'index.mdoc');
        const enFile = path.join(folderPath, 'tulisan.en.md');

        if (!fs.existsSync(mdocFile)) return;

        // Read English content
        let contentEnRaw = "";
        if (fs.existsSync(enFile)) {
            contentEnRaw = fs.readFileSync(enFile, 'utf-8');
            // Remove frontmatter from English file if exists
            contentEnRaw = contentEnRaw.replace(/^---[\s\S]*?---\n/m, '');
        }

        // Get clean ID content (body only)
        // To get the real clean body, we might need to go back to the original source 
        // but since we've already modified it, let's try to extract from the current mdoc
        let currentContent = fs.readFileSync(mdocFile, 'utf-8');
        let body = currentContent.split('\n---\n').pop().trim();

        // CLEANUP HTML in body (Keystatic visual editor likes clean Markdown)
        body = body.replace(/<p class="dropcap">/g, '');
        body = body.replace(/<\/p>/g, '\n');
        body = body.replace(/<span class="highlight">/g, '**');
        body = body.replace(/<\/span>/g, '**');
        body = body.replace(/<a href="([^"]*)" target="_blank">/g, '[$1](');
        body = body.replace(/<\/a>/g, ')');
        body = body.replace(/<i>/g, '*');
        body = body.replace(/<\/i>/g, '*');
        body = body.replace(/<b>/g, '**');
        body = body.replace(/<\/b>/g, '**');
        // Remove remaining HTML tags
        body = body.replace(/<[^>]*>?/gm, '');

        const fields = {
            slug: item.slug,
            title_id: item.title,
            title_en: item.title_en,
            date: item.date,
            category_id: item.category,
            category_en: item.category_en,
            description_id: item.description,
            description_en: item.description_en,
            image: item.image
        };

        let yaml = '---\n';
        for (const [key, value] of Object.entries(fields)) {
            yaml += `${key}: ${JSON.stringify(value)}\n`;
        }
        // content_en_markdown
        yaml += `content_en_markdown: |\n${contentEnRaw.split('\n').map(l => '  ' + l).join('\n')}\n`;
        yaml += '---\n';

        fs.writeFileSync(mdocFile, yaml + '\n' + body);
        console.log(`Cleaned and Fixed: ${slug}`);
    });
}

finalCleanup();
