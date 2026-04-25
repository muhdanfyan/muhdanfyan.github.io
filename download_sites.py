import json
import os
import subprocess

with open('data/manifest.json') as f:
    data = json.load(f)

for project in data['portfolio']:
    if project.get('category') == 'Netlify':
        slug = project['slug']
        url = project['url']
        domain = url.split('//')[-1]
        
        target_dir = f'portofolio/{slug}'
        os.makedirs(target_dir, exist_ok=True)
        
        print(f'Downloading {slug} from {url}')
        
        # We'll use wget with options to recursively download the site, 
        # convert links for local viewing, and rename the root file to index.html 
        # inside the slug folder.
        
        subprocess.run([
            'wget', 
            '--recursive', 
            '--no-clobber', 
            '--page-requisites', 
            '--html-extension', 
            '--convert-links', 
            '--restrict-file-names=windows', 
            '--no-parent',
            '--no-host-directories',
            '--directory-prefix=' + target_dir,
            url
        ])
