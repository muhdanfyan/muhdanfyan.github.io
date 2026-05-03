const fs = require('fs');
const path = require('path');

const TULISAN_DIR = './tulisan';

function unifyCategoryField() {
    const folders = fs.readdirSync(TULISAN_DIR);
    
    folders.forEach(slug => {
        const idFile = path.join(TULISAN_DIR, slug, 'index.mdoc');
        if (!fs.existsSync(idFile)) return;

        let content = fs.readFileSync(idFile, 'utf-8');
        const parts = content.split('\n---\n');
        if (parts.length < 2) return;

        let frontmatter = parts[1];
        const body = parts.slice(2).join('\n---\n');

        // Extract old category_id value
        const catMatch = frontmatter.match(/category_id: "(.*)"/);
        const categoryValue = catMatch ? catMatch[1] : 'Technology';

        // Remove old category fields
        frontmatter = frontmatter.replace(/category_id: ".*"\n?/, '');
        frontmatter = frontmatter.replace(/category_en: ".*"\n?/, '');

        // Add new unified category field
        frontmatter += `category: ${JSON.stringify(categoryValue)}\n`;

        fs.writeFileSync(idFile, parts[0] + '\n---\n' + frontmatter + '\n---\n' + body);
        console.log(`Unified category for: ${slug}`);
    });
}

unifyCategoryField();
