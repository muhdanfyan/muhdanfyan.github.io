# Image Optimization Skill

This skill ensures all web assets (specifically images in `public/img/`) are optimized for performance and social media link previews (Open Graph).

## Core Requirements
1. **Target Size**: All images should be under **300KB** (ideally 100-250KB) to ensure reliable display on platforms like WhatsApp.
2. **Format**: Use **JPG** for photos and screenshots. Use **PNG** only if transparency is absolutely required.
3. **Dimensions**: Standard width of **1200px** for cover images.

## Automation Script
The project includes a utility script for batch optimization:
`python3 scratch/compress_images.py`

## Implementation Steps for New Images
When adding a new image:
1. Save the original to the target folder (e.g., `public/img/tulisan/` or `public/img/screenshots/`).
2. Run the optimization command:
   ```bash
   sips -s format jpeg -s formatOptions 80 --resampleWidth 1200 [input_path] --out [output_path].jpg
   ```
3. Verify the file size is under 300KB.
4. If the size is still over 300KB, reduce quality:
   ```bash
   sips -s formatOptions 60 [output_path].jpg
   ```
5. Update all metadata (`index.mdoc`, `manifest.json`, etc.) to use the `.jpg` extension.
6. Remove the original large file or unoptimized version.

## Verification
- Run `ls -lh` to check file sizes.
- Verify that `og:image` tags in the HTML point to the optimized `.jpg` file.
