const fs = require('fs');
const path = require('path');

const TULISAN_DIR = './tulisan';
const MANIFEST_PATH = './data/manifest.json';

function reconstruction() {
    const manifest = JSON.parse(fs.readFileSync(MANIFEST_PATH, 'utf-8'));
    const writings = manifest.writing || [];

    writings.forEach(item => {
        const slug = item.slug;
        const folderPath = path.join(TULISAN_DIR, slug);
        
        // Ensure folder exists
        if (!fs.existsSync(folderPath)) {
            fs.mkdirSync(folderPath, { recursive: true });
        }

        const idFile = path.join(folderPath, 'index.mdoc');
        const enFile = path.join(folderPath, 'index.en.mdoc');

        // 1. Prepare ID Content
        // We will try to find the cleanest body possible.
        // If we can't find a clean one, we'll use the description as a placeholder 
        // OR better, we'll take the text after the headers in the existing file 
        // but we'll be very careful.
        
        let idBody = "";
        if (fs.existsSync(idFile)) {
            const current = fs.readFileSync(idFile, 'utf-8');
            // Logic: The real body starts after the LAST '---' that is not indented
            const lines = current.split('\n');
            let lastDashIdx = -1;
            for (let i = 0; i < lines.length; i++) {
                if (lines[i].trim() === '---') {
                    lastDashIdx = i;
                }
            }
            if (lastDashIdx !== -1) {
                idBody = lines.slice(lastDashIdx + 1).join('\n').trim();
            } else {
                idBody = current.trim();
            }
        }

        // 2. Prepare EN Content
        let enBody = "";
        const oldEnFile = path.join(folderPath, 'tulisan.en.md');
        if (fs.existsSync(oldEnFile)) {
            const current = fs.readFileSync(oldEnFile, 'utf-8');
            enBody = current.replace(/^---[\s\S]*?---\n/m, '').trim();
        } else if (fs.existsSync(enFile)) {
            const current = fs.readFileSync(enFile, 'utf-8');
            const lines = current.split('\n');
            let lastDashIdx = -1;
            for (let i = 0; i < lines.length; i++) {
                if (lines[i].trim() === '---') {
                    lastDashIdx = i;
                }
            }
            enBody = lines.slice(lastDashIdx + 1).join('\n').trim();
        }

        // 3. Write CLEAN ID File
        const idFields = {
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

        let idYaml = '---\n';
        for (const [key, value] of Object.entries(idFields)) {
            idYaml += `${key}: ${JSON.stringify(value)}\n`;
        }
        idYaml += '---\n';

        fs.writeFileSync(idFile, idYaml + '\n' + idBody);

        // 4. Write CLEAN EN File
        if (enBody) {
            let enYaml = '---\n';
            enYaml += `slug: ${JSON.stringify(item.slug)}\n`;
            enYaml += '---\n';
            fs.writeFileSync(enFile, enYaml + '\n' + enBody);
        }
        
        console.log(`Reconstructed: ${slug}`);
    });
}

reconstruction();
