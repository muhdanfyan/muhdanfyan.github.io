const fs = require('fs');
const path = require('path');

const TULISAN_DIR = './tulisan';

function superCleanContent() {
    const folders = fs.readdirSync(TULISAN_DIR);
    
    folders.forEach(slug => {
        const files = ['index.mdoc', 'index.en.mdoc'];
        
        files.forEach(fileName => {
            const filePath = path.join(TULISAN_DIR, slug, fileName);
            if (!fs.existsSync(filePath)) return;

            let content = fs.readFileSync(filePath, 'utf-8');
            
            // 1. Identify Frontmatter
            const parts = content.split('\n---\n');
            if (parts.length < 2) return;
            
            const frontmatter = parts[0] + '\n---\n' + parts[1] + '\n---\n';
            let body = parts.slice(2).join('\n---\n');
            
            // 2. PROTECT BODY: Replace all '---' dividers in body with '***' 
            // so they don't break YAML parsing
            body = body.replace(/\n---\n/g, '\n***\n');
            body = body.replace(/^---\n/gm, '***\n');
            
            fs.writeFileSync(filePath, frontmatter + body);
            console.log(`Super Cleaned: ${slug}/${fileName}`);
        });
    });
}

superCleanContent();
