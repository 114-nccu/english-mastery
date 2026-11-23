from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image, ImageOps, ImageDraw
r=Path(__file__).resolve().parents[1]
html=(r/'runs/round2/deck.html').read_text(encoding='utf-8')
folder=r/'runs/round2/live-slides';folder.mkdir(exist_ok=True)
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 page=b.new_page(viewport={'width':1440,'height':900})
 page.set_content(html,wait_until='domcontentloaded')
 for i in range(12):
  page.evaluate('(i)=>goto(i)',i)
  page.locator('.slide.active').screenshot(path=str(folder/f'slide-{i+1:02d}.png'))
 b.close()
imgs=[]
for i in range(1,13):
 im=Image.open(folder/f'slide-{i:02d}.png').convert('RGB')
 im.thumbnail((500,282))
 tile=Image.new('RGB',(518,303),'#f6f6f6')
 tile.paste(im,((518-im.width)//2,6))
 d=ImageDraw.Draw(tile)
 d.text((10,286),f'PAGE {i:02d}',fill='#333333')
 imgs.append(tile)
contact=Image.new('RGB',(518*3,303*4),'white')
for idx,im in enumerate(imgs):contact.paste(im,((idx%3)*518,(idx//3)*303))
contact.save(r/'docs/preview-contact-sheet.png',optimize=True)
print('Created',r/'docs/preview-contact-sheet.png')
