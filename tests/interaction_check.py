from pathlib import Path
import os, sys
from playwright.sync_api import sync_playwright
html=Path(__file__).resolve().parents[1]/'runs/round1/deck.html'
with sync_playwright() as p:
    launch={}
    if Path('/usr/bin/chromium').exists(): launch['executable_path']='/usr/bin/chromium'
    b=p.chromium.launch(**launch)
    page=b.new_page(viewport={'width':1280,'height':720})
    errors=[]
    page.on('pageerror',lambda e:errors.append(str(e)))
    page.set_content(html.read_text(encoding='utf-8'),wait_until='domcontentloaded')
    assert page.locator('.slide').count()==12, 'slide count'
    assert page.locator('.slide.active').count()==1, 'active slide'
    assert 'English Mastery' in page.locator('.slide.active').inner_text(), 'cover active'
    page.locator('#next').click()
    assert '多益 L&R' in page.locator('.slide.active h2').inner_text(),'next control'
    page.keyboard.press('ArrowRight')
    assert '理解聽力' in page.locator('.slide.active h2').inner_text(),'keyboard next'
    page.locator('#prev').click()
    assert '多益 L&R' in page.locator('.slide.active h2').inner_text(),'prev control'
    for i in range(3):page.locator('#next').click()
    assert page.locator('.slide.active').get_attribute('data-claims').startswith('AI-01'), 'quiz slide'
    page.locator('.slide.active .answer[data-correct="true"]').click()
    assert '正確' in page.locator('.slide.active .feedback').inner_text(), 'quiz feedback'
    assert not errors, errors
    print('PASS: 12 slides, next, previous, keyboard, quiz correct-feedback, no JS exception (set_content limited mode)')
    b.close()
