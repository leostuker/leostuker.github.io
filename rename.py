import os
import glob
from pathlib import Path

for md_path in glob.glob('posts-*/**/*.md', recursive=True):
    with open(md_path, 'r', encoding='utf-8') as f:
        title = None
        for line in f:
            if line.startswith('# '):
                title = line.replace('# ', '').strip()
                break
    if title:
        new_name = title.replace(' ', '_').lower() + '.md'
        new_path = os.path.join(os.path.dirname(md_path), new_name)
        
        if md_path != new_path:
            print(f'Renaming {md_path} -> {new_path}')
            os.rename(md_path, new_path)
