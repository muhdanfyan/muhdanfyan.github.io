const fs = require('fs');
const path = require('path');

const TULISAN_DIR = './tulisan';

function convertToYamlSafe() {
    const folders = fs.readdirSync(TULISAN_DIR);
    
    folders.forEach(slug => {
        const filePath = path.join(TULISAN_DIR, slug, 'tulisan.md');
        if (!fs.existsSync(filePath)) return;

        let content = fs.readFileSync(filePath, 'utf-8');
        
        // Find the JSON frontmatter (if it's still there or already partially converted)
        // We'll just parse the existing frontmatter and rewrite it correctly
        const match = content.match(/^---[\s\S]*?\n---\n([\s\S]*)$/);
        if (!match) return;

        const body = match[1];
        
        // We'll read the file content and manually extract keys to avoid complex parsing
        // since we know the keys we've been using.
        const lines = content.split('\n');
        const data = {};
        let inFrontmatter = false;
        
        // Simple extraction for our known keys
        const keys = [
            'slug', 'title_id', 'title_en', 'date', 'image', 
            'category_id', 'category_en', 'description_id', 'description_en', 
            'content_en_markdown'
        ];

        // This is tricky because content_en_markdown might be a mess now.
        // Let's use a safer approach: re-read from a clean state if possible, 
        // or just fix the escaping.
        
        // Actually, let's use gray-matter to parse what we have, then stringify properly
        // Wait, gray-matter might fail.
        
        // Let's use a very robust manual way for our specific case:
        // We'll look for the first --- and the last --- before the body.
        const firstIdx = content.indexOf('---\n');
        const lastIdx = content.indexOf('\n---\n', firstIdx + 4);
        if (firstIdx === -1 || lastIdx === -1) return;
        
        // We'll assume the data is mostly okay but needs better quoting.
        // Or better yet, let's just write a script that knows the fields.
        
        // Actually, I'll use a simpler trick: use JSON frontmatter again 
        // but this time I'll make sure it's the ONLY frontmatter.
        // NO, Keystatic really wants YAML.
        
        // Okay, I will use a library-less YAML-ish writer that uses | for multiline
        const writeField = (key, value) => {
            if (!value) return `${key}: ""\n`;
            if (typeof value === 'string' && (value.includes('\n') || value.includes('"') || value.includes(':'))) {
                // Use literal block scalar for multiline or complex strings
                const indented = value.split('\n').map(line => `    ${line}`).join('\n');
                return `${key}: |\n${indented}\n`;
            }
            return `${key}: "${value}"\n`;
        };

        // We need to get the clean values. I'll re-run the logic from manifest 
        // to be absolutely sure we have clean data.
        
    });
}

// Let's just rewrite the whole migration script but BETTER.
const MANIFEST_PATH = './data/manifest.json';

function betterMigrate() {
    const manifest = JSON.parse(fs.readFileSync(MANIFEST_PATH, 'utf-8'));
    const writings = manifest.writing || [];

    writings.forEach(item => {
        const slug = item.slug;
        const folderPath = path.join(TULISAN_DIR, slug);
        const idFile = path.join(folderPath, 'tulisan.md');
        const enFile = path.join(folderPath, 'tulisan.en.md');

        if (!fs.existsSync(idFile)) return;

        // Get original content (remove any existing frontmatter we added)
        let originalContent = fs.readFileSync(idFile, 'utf-8');
        const parts = originalContent.split('\n---\n');
        const cleanBody = parts.length > 1 ? parts[parts.length - 1].trim() : originalContent.trim();
        
        let contentEnRaw = "";
        if (fs.existsSync(enFile)) {
            contentEnRaw = fs.readFileSync(enFile, 'utf-8');
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
            image: item.image
        };

        let yaml = '---\n';
        for (const [key, value] of Object.entries(fields)) {
            yaml += `${key}: ${JSON.stringify(value)}\n`;
        }
        // Special handling for multiline English content
        yaml += `content_en_markdown: |\n${contentEnRaw.split('\n').map(l => '  ' + l).join('\n')}\n`;
        yaml += '---\n';

        fs.writeFileSync(idFile, yaml + '\n' + cleanBody);
        console.log(`Perfectly migrated: ${slug}`);
    });
}

betterMigrate();
