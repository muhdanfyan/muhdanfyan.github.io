const fs = require('fs');
const path = require('path');

const TULISAN_DIR = './tulisan';

function convertToYaml() {
    const folders = fs.readdirSync(TULISAN_DIR);
    
    folders.forEach(slug => {
        const filePath = path.join(TULISAN_DIR, slug, 'tulisan.md');
        if (!fs.existsSync(filePath)) return;

        const content = fs.readFileSync(filePath, 'utf-8');
        const match = content.match(/^---json\n([\s\S]*?)\n---\n([\s\S]*)$/);
        
        if (match) {
            const jsonData = JSON.parse(match[1]);
            const body = match[2];
            
            // Simple YAML generator for our specific keys
            let yaml = '---\n';
            for (const [key, value] of Object.entries(jsonData)) {
                if (typeof value === 'string') {
                    // Escape quotes and newlines
                    const escaped = value.replace(/"/g, '\\"').replace(/\n/g, '\\n');
                    yaml += `${key}: "${escaped}"\n`;
                } else if (Array.isArray(value)) {
                    yaml += `${key}: [${value.map(v => `"${v}"`).join(', ')}]\n`;
                } else {
                    yaml += `${key}: ${value}\n`;
                }
            }
            yaml += '---\n';
            
            fs.writeFileSync(filePath, yaml + body);
            console.log(`Converted to YAML: ${slug}`);
        }
    });
}

convertToYaml();
