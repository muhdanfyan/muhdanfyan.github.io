
import json

manifest_path = '/Users/pondokit/Herd/muhdanfyan.github.io/data/manifest.json'

with open(manifest_path, 'r') as f:
    data = json.load(f)

for project in data['portfolio']:
    if project.get('slug') == 'demopisantri':
        project['url'] = 'https://demopisantri.vercel.app'
        project['image'] = 'img/screenshots/demopisantri.png'
        project['is_featured'] = True
    elif 'pisantri' in str(project.get('title', '')).lower():
        # Update other pisantri entries if needed
        pass

with open(manifest_path, 'w') as f:
    json.dump(data, f, indent=2)

print('Manifest updated with demopisantri URL.')
