# .pptx template

`tcu-deck.pptx` is python-pptx's default template set to 16:9 with a dark
master (ATNI dark ground, #010B13). `python tcu/templates/pptx/make_template.py`
rebuilds it. The engine (`tcu/engine/pptx_deck.py`) adds one slide per HTML
deck slide, with speaker notes, on the blank layout.

Fonts: the slides name League Spartan (titles) and Lexend Deca (body), the
ATNI Climate design system fonts. PowerPoint does not embed them; on a
machine where they are not installed, it shows a fallback font. The layout
still holds. The HTML decks carry the fonts inside the file.

Long slide text is cut near 900 characters; the rest moves to the speaker
notes so nothing is lost.
