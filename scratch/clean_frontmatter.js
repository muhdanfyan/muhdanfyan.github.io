const fs = require('fs');
const path = require('path');

const TULISAN_DIR = './tulisan';

function cleanDoubleFrontmatter() {
    const folders = fs.readdirSync(TULISAN_DIR);
    
    folders.forEach(slug => {
        const filePath = path.join(TULISAN_DIR, slug, 'tulisan.md');
        if (!fs.existsSync(filePath)) return;

        let content = fs.readFileSync(filePath, 'utf-8');
        
        // Split by '---'
        const parts = content.split('---\n');
        
        // parts[0] should be empty (before first ---)
        // parts[1] should be the real frontmatter
        // The rest should be content, but we need to remove any subsequent frontmatter blocks
        
        if (parts.length > 2) {
            console.log(`Cleaning: ${slug}`);
            
            const realFrontmatter = parts[1];
            // Join everything else, but if it starts with another frontmatter block, strip it
            let remaining = parts.slice(2).join('---\n');
            
            // Remove any remaining frontmatter blocks (the ones that look like frontmatter)
            // Typically they start with title: or similar
            remaining = remaining.replace(/^title: [\s\S]*?\n---\n/m, '');
            remaining = remaining.replace(/^---\ntitle: [\s\S]*?\n---\n/m, '');
            
            // Write back
            const newContent = `---\n${realFrontmatter}---\n${remaining}`;
            fs.writeFileSync(filePath, newContent);
        }
    });
}

cleanDoubleFrontmatter();
