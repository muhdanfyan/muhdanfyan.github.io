const fs = require('fs');
const path = require('path');

const TULISAN_DIR = './tulisan';
const MANIFEST_PATH = './data/manifest.json';

function fixContentExtraction() {
    const manifest = JSON.parse(fs.readFileSync(MANIFEST_PATH, 'utf-8'));
    const writings = manifest.writing || [];

    writings.forEach(item => {
        const slug = item.slug;
        const folderPath = path.join(TULISAN_DIR, slug);
        const mdocFile = path.join(folderPath, 'index.mdoc');
        const enFile = path.join(folderPath, 'index.en.mdoc');

        // Fix ID content
        if (fs.existsSync(mdocFile)) {
            let currentContent = fs.readFileSync(mdocFile, 'utf-8');
            // Find the SECOND '---' which marks the end of the frontmatter
            const firstDashes = currentContent.indexOf('---\n');
            const secondDashes = currentContent.indexOf('\n---\n', firstDashes + 4);
            
            if (secondDashes !== -1) {
                // The body is EVERYTHING after the second dashes
                const body = currentContent.substring(secondDashes + 5).trim();
                
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
                console.log(`Fixed ID Body for: ${slug}`);
            }
        }
    });
}

fixContentExtraction();
