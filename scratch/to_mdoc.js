const fs = require('fs');
const path = require('path');

const TULISAN_DIR = './tulisan';

function convertToMdoc() {
    const folders = fs.readdirSync(TULISAN_DIR);
    
    folders.forEach(slug => {
        const oldPath = path.join(TULISAN_DIR, slug, 'index.md');
        const newPath = path.join(TULISAN_DIR, slug, 'index.mdoc');
        
        if (fs.existsSync(oldPath)) {
            fs.renameSync(oldPath, newPath);
            console.log(`Converted to Markdoc: ${slug}/index.mdoc`);
        }
    });
}

convertToMdoc();
