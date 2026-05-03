const fs = require('fs');
const path = require('path');

const TULISAN_DIR = './tulisan';

function prepareSeparateEn() {
    const folders = fs.readdirSync(TULISAN_DIR);
    
    folders.forEach(slug => {
        const oldEnPath = path.join(TULISAN_DIR, slug, 'tulisan.en.md');
        const newEnPath = path.join(TULISAN_DIR, slug, 'index.en.mdoc');
        
        if (fs.existsSync(oldEnPath)) {
            const content = fs.readFileSync(oldEnPath, 'utf-8');
            // Remove old frontmatter if exists and ensure clean Markdoc
            const cleanContent = content.replace(/^---[\s\S]*?---\n/m, '');
            
            // We need a simple frontmatter for Keystatic to identify it
            const frontmatter = `---\nslug: "${slug}"\n---\n`;
            
            fs.writeFileSync(newEnPath, frontmatter + cleanContent);
            console.log(`Prepared separate EN file: ${slug}/index.en.mdoc`);
        }
    });
}

prepareSeparateEn();
