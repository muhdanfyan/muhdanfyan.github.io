#!/bin/bash
set -e
echo "🚀 Building..."
npm run build
echo "🚀 Deploying to gh-pages..."
cd /tmp
rm -rf gh-pages-deploy
mkdir gh-pages-deploy
cp -r /home/pondokinformatika/.openclaw/workspace/muhdanfyan-github-io/dist/* gh-pages-deploy/
cd gh-pages-deploy
touch .nojekyll
git init
git config user.name "muhdanfyan"
git config user.email "muhdanfyan@gmail.com"
git add -A
git commit -m "deploy: $(date +%Y-%m-%d_%H%M)"
git remote add origin https://github.com/muhdanfyan/muhdanfyan.github.io.git
git branch -m master gh-pages
git push -f origin gh-pages
echo "✅ Deployed!"
gh api repos/muhdanfyan/muhdanfyan.github.io/pages/builds -X POST > /dev/null
echo "✅ Pages build triggered!"
