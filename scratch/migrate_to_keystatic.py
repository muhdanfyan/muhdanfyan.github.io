import json
import os
import yaml

# Path setup
MANIFEST_PATH = 'data/manifest.json'
TULISAN_DIR = 'tulisan'

def migrate():
    if not os.path.exists(MANIFEST_PATH):
        print("Manifest not found.")
        return

    with open(MANIFEST_PATH, 'r') as f:
        manifest = json.load(f)

    writings = manifest.get('writing', [])
    print(f"Found {len(writings)} writings to migrate.")

    for item in writings:
        slug = item.get('slug')
        if not slug:
            continue
        
        folder_path = os.path.join(TULISAN_DIR, slug)
        id_file = os.path.join(folder_path, 'tulisan.md')
        en_file = os.path.join(folder_path, 'tulisan.en.md')

        if not os.path.exists(id_file):
            print(f"Warning: {id_file} not found. Skipping.")
            continue

        # Read ID content
        with open(id_file, 'r') as f:
            lines = f.readlines()
            # Remove existing frontmatter if any (unlikely based on check)
            content = "".join(lines)

        # Read EN content if exists
        content_en_raw = ""
        if os.path.exists(en_file):
            with open(en_file, 'r') as f:
                content_en_raw = f.read()

        # Prepare Frontmatter
        # We'll convert the EN raw text into a simple Keystatic Document JSON format
        # [{ "type": "paragraph", "children": [{ "text": "..." }] }]
        # For simplicity in migration, we'll store it as a single paragraph or multiple 
        # But Keystatic renderer likes the structure.
        
        # Actually, let's keep it as raw markdown for now and update the config 
        # to use a simple text field for EN content to ensure 100% data fidelity 
        # during migration.
        
        frontmatter = {
            'title_id': item.get('title'),
            'title_en': item.get('title_en'),
            'date': item.get('date'),
            'category_id': item.get('category'),
            'category_en': item.get('category_en'),
            'description_id': item.get('description'),
            'description_en': item.get('description_en'),
            'image': item.get('image'),
            'content_en_markdown': content_en_raw # Temporary field
        }

        # Write back to tulisan.md
        with open(id_file, 'w') as f:
            f.write('---\n')
            yaml.dump(frontmatter, f, allow_unicode=True)
            f.write('---\n\n')
            f.write(content)
        
        print(f"Migrated: {slug}")

if __name__ == '__main__':
    migrate()
