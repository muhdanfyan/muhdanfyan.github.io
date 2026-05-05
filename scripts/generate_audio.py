import os
import re
import json
from gtts import gTTS
import frontmatter
from bs4 import BeautifulSoup
import markdown

def clean_text(content):
    # Convert markdown to HTML first to handle markdown-specific syntax
    html = markdown.markdown(content)
    # Remove HTML tags
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text()
    # Remove URLs
    text = re.sub(r'http\S+', '', text)
    # Remove special characters often found in code or technical writing
    text = re.sub(r'[_*`#]', '', text)
    # Clean up whitespace
    text = " ".join(text.split())
    return text

def generate_audio():
    tulisan_dir = 'tulisan'
    output_dir = 'public/audio'
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    print(f"🚀 Memulai ekstraksi suara ke {output_dir}...")
    
    for slug in os.listdir(tulisan_dir):
        content_path = os.path.join(tulisan_dir, slug)
        if not os.path.isdir(content_path):
            continue
            
        # Files to process: (filename, lang_code, suffix)
        files_to_process = [
            ('index.mdoc', 'id', 'id'),
            ('index.en.mdoc', 'en', 'en'),
            ('tulisan.en.md', 'en', 'en'),
            ('tulisan.md', 'id', 'id')
        ]
        
        for filename, lang, suffix in files_to_process:
            file_path = os.path.join(content_path, filename)
            if os.path.exists(file_path):
                output_file = f"{slug}_{suffix}.mp3"
                output_path = os.path.join(output_dir, output_file)
                
                # Skip if already exists (optional, remove if you want to force regenerate)
                # if os.path.exists(output_path):
                #    print(f"⏩ Skip {output_file} (sudah ada)")
                #    continue
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        post = frontmatter.load(f)
                        text = clean_text(post.content)
                        
                        if text:
                            print(f"🎙️ Generating {output_file}...")
                            tts = gTTS(text=text, lang=lang)
                            tts.save(output_path)
                except Exception as e:
                    print(f"❌ Gagal memproses {file_path}: {e}")

if __name__ == "__main__":
    # Ensure dependencies are available for clean_text
    try:
        import markdown
    except ImportError:
        os.system('python3 -m pip install python-markdown --break-system-packages')
        import markdown
        
    try:
        import frontmatter
    except ImportError:
        os.system('python3 -m pip install python-frontmatter --break-system-packages')
        import frontmatter
        
    generate_audio()
    print("✅ Selesai!")
