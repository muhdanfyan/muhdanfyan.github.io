const fs = require('fs');
const path = require('path');

const TULISAN_DIR = './tulisan';
const PUBLIC_IMG_DIR = './public/img/tulisan';

// Ensure directory exists
if (!fs.existsSync(PUBLIC_IMG_DIR)) {
    fs.mkdirSync(PUBLIC_IMG_DIR, { recursive: true });
}

function fixImages() {
    const folders = fs.readdirSync(TULISAN_DIR);
    
    folders.forEach(slug => {
        const mdocFile = path.join(TULISAN_DIR, slug, 'index.mdoc');
        if (!fs.existsSync(mdocFile)) return;

        let content = fs.readFileSync(mdocFile, 'utf-8');
        const match = content.match(/^---\n([\s\S]*?)\n---\n/);
        
        if (match) {
            let frontmatter = match[1];
            
            // Look for image field
            const imgMatch = frontmatter.match(/image: "(.*)"/);
            if (imgMatch) {
                let imgPath = imgMatch[1];
                
                // If it's a local path and not already in the new dir
                if (!imgPath.startsWith('http') && !imgPath.startsWith('/img/tulisan')) {
                    const oldFullPath = path.join('./public', imgPath);
                    const fileName = path.basename(imgPath);
                    const newFullPath = path.join(PUBLIC_IMG_DIR, fileName);
                    
                    if (fs.existsSync(oldFullPath)) {
                        fs.copyFileSync(oldFullPath, newFullPath);
                        console.log(`Moved image for ${slug}: ${fileName}`);
                        
                        // Update frontmatter to just the filename (Keystatic expects this for fields.image)
                        frontmatter = frontmatter.replace(`image: "${imgPath}"`, `image: "${fileName}"`);
                        const newContent = content.replace(/^---\n[\s\S]*?\n---\n/, `---\n${frontmatter}---\n`);
                        fs.writeFileSync(mdocFile, newContent);
                    }
                }
            }
        }
    });
}

fixImages();
