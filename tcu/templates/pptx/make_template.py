"""Make tcu-deck.pptx: python-pptx's default template, 16:9, with a dark master.

python tcu/templates/pptx/make_template.py
"""
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.util import Emu

prs = Presentation()
prs.slide_width, prs.slide_height = Emu(12192000), Emu(6858000)
fill = prs.slide_master.background.fill
fill.solid()
fill.fore_color.rgb = RGBColor(0x01, 0x0B, 0x13)
prs.core_properties.title = 'TCU course deck template'
prs.core_properties.author = 'Patrick A. Freeland (module author), with ATNI Climate'
prs.core_properties.comments = ('ATNI Climate design system: League Spartan and Lexend Deca on ATNI dark ground. '
                                'The fonts fall back to system fonts where they are not installed.')
prs.save(str(Path(__file__).with_name('tcu-deck.pptx')))
print('wrote tcu-deck.pptx')
