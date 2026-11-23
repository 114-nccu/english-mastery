from pathlib import Path
from playwright.sync_api import sync_playwright
import json
root=Path(__file__).resolve().parents[1]
html=(root/'runs/round2/deck.html').read_text(encoding='utf-8')
shots=root/'runs/round2/viewport-review'
shots.mkdir(exist_ok=True)
results=[]
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 for width,height in [(1366,768),(1440,900),(390,844)]:
  page=b.new_page(viewport={'width':width,'height':height},device_scale_factor=1)
  page.set_content(html,wait_until='domcontentloaded')
  page.evaluate('goto(3)')
  # Verify navigation is separate from current footer, visually and geometrically.
  rects=page.evaluate('''() => {const s=document.querySelector('.slide.active'),foot=s.querySelector('.foot'),control=document.querySelector('#controls');let r=x=>{const b=x.getBoundingClientRect();return [b.left,b.top,b.right,b.bottom]};return {slide:r(s),foot:r(foot),controls:r(control),docOverflow:document.documentElement.scrollWidth-innerWidth}}''')
  def overlap(a,c):return a[0]<c[2] and a[2]>c[0] and a[1]<c[3] and a[3]>c[1]
  rects['controls_foot_overlap']=overlap(rects['controls'],rects['foot'])
  rects['controls_slide_overlap']=overlap(rects['controls'],rects['slide'])
  page.screenshot(path=str(shots/f'live-{width}x{height}-p4.png'),full_page=(width<=700))
  # navigation & quiz functionality
  page.locator('#next').click();page.locator('#next').click();page.locator('#prev').click()
  assert page.locator('.slide.active').get_attribute('aria-label')=='第5頁'
  page.locator('.slide.active button[data-correct="true"]').click()
  assert '正確' in page.locator('.slide.active .feedback').inner_text()
  results.append(dict(viewport=f'{width}x{height}',**rects,quiz='PASS'))
  page.close()
 b.close()
(shots/'results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(results,ensure_ascii=False,indent=2))
assert not any(r['controls_foot_overlap'] for r in results), 'controls overlapping footer'
assert not any(r['docOverflow']>2 for r in results), 'horizontal overflow'
