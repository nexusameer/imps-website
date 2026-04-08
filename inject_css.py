import os
import glob
import re

html_files = glob.glob('*.html')
skip_files = ['navbar.html', 'footer.html']

for filepath in html_files:
    if filepath in skip_files:
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if "theme-modern.css" not in content:
        # Inject right after style.css
        content = content.replace('<link rel="stylesheet" href="css/style.css">', '<link rel="stylesheet" href="css/style.css">\n  <link rel="stylesheet" href="css/theme-modern.css">')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
    else:
        print(f"Already updated {filepath}")
