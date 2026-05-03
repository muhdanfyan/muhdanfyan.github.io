const fs = require('fs');
const path = require('path');

const TULISAN_DIR = './tulisan';

function fixSlugs() {
    const folders = fs.readdirSync(TULISAN_DIR);
    
    folders.forEach(slug => {
        const filePath = path.join(TULISAN_DIR, slug, 'tulisan.md');
        if (!fs.existsSync(filePath)) return;

        let content = fs.readFileSync(filePath, 'utf-8');
        
        // Extract frontmatter
        const match = content.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);
        
        if (match) {
            let frontmatter = match[1];
            const body = match[2];
            
            // Check if slug field already exists
            if (!frontmatter.includes('slug:')) {
                // Add slug field at the top
                frontmatter = `slug: "${slug}"\n${frontmatter}`;
                fs.writeFileSync(filePath, `---\n${frontmatter}---\n${body}`);
                console.log(`Added slug to: ${slug}`);
            }
        }
    });
}

fixSlugs();
