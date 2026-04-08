import os
import re
import glob

# Files to skip
skip_files = ['index.html', 'navbar.html', 'footer.html']

html_files = glob.glob('*.html')

nav_pattern = re.compile(r'<nav class="navbar .*?</nav>', re.DOTALL)
footer_pattern = re.compile(r'<footer class="ftco-footer .*?</footer>', re.DOTALL)

for filepath in html_files:
    if filepath in skip_files:
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace navbar
    content = nav_pattern.sub('  <div id="navbar-placeholder"></div>', content)
    # Replace footer
    content = footer_pattern.sub('  <div id="footer-placeholder"></div>', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Replaced navbars and footers in all relevant HTML files.")
