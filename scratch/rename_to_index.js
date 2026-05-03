const fs = require('fs');
const path = require('path');

const TULISAN_DIR = './tulisan';

function renameToIndex() {
    const folders = fs.readdirSync(TULISAN_DIR);
    
    folders.forEach(slug => {
        const oldPath = path.join(TULISAN_DIR, slug, 'tulisan.md');
        const newPath = path.join(TULISAN_DIR, slug, 'index.md');
        
        if (fs.existsSync(oldPath)) {
            fs.renameSync(oldPath, newPath);
            console.log(`Renamed: ${slug}/tulisan.md -> index.md`);
        }
    });
}

renameToIndex();
