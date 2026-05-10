from pathlib import Path
import re
path = Path(r'c:\Users\11\321\index.html')
text = path.read_text(encoding='utf-8', errors='replace')
style_match = re.search(r'<style>([\s\S]*?)</style>', text)
if not style_match:
    raise SystemExit('Style block not found')
style_css = style_match.group(1).strip() + '\n'
script_matches = list(re.finditer(r'<script(?![^>]*src)([^>]*)>([\s\S]*?)</script>', text))
inline_scripts = []
for m in script_matches:
    script = m.group(2).strip()
    if script:
        inline_scripts.append(script)
new_html = text
new_html = re.sub(r'<style>[\s\S]*?</style>', '<link rel="stylesheet" href="style.css">', new_html, count=1)
new_html = re.sub(r'<script(?![^>]*src)([^>]*)>[\s\S]*?</script>', '', new_html)
if '<link rel="stylesheet" href="style.css">' not in new_html:
    new_html = new_html.replace('</head>', '  <link rel="stylesheet" href="style.css">\n</head>', 1)
if '<script src="app.js" defer></script>' not in new_html:
    new_html = new_html.replace('</body>', '  <script src="app.js" defer></script>\n</body>', 1)
new_html = re.sub(r'\n{3,}', '\n\n', new_html)
out_dir = Path(r'c:\Users\11\321')
out_dir.joinpath('index.html').write_text(new_html, encoding='utf-8')
out_dir.joinpath('style.css').write_text(style_css, encoding='utf-8')
app_js = '\n\n'.join(inline_scripts) + '\n'
out_dir.joinpath('app.js').write_text(app_js, encoding='utf-8')
print('done', len(inline_scripts), 'scripts extracted')
