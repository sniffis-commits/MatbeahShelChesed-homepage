"""Create English title/caption cards for the instructional video."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
CARDS = HERE / "cards"
CARDS.mkdir(exist_ok=True)

GREEN = (12, 42, 30)
CREAM = (247, 243, 232)
GOLD = (217, 164, 65)
FONT = "C:/Windows/Fonts/arial.ttf"


def f(size, bold=False):
    name = "C:/Windows/Fonts/arialbd.ttf" if bold else FONT
    try:
        return ImageFont.truetype(name, size)
    except OSError:
        return ImageFont.load_default()


def centered(d, text, y, font, color):
    box = d.textbbox((0, 0), text, font=font)
    d.text((640 - (box[2] - box[0]) / 2, y), text, font=font, fill=color)


def card(filename, eyebrow, title, subtitle):
    img = Image.new("RGB", (1280, 720), GREEN)
    d = ImageDraw.Draw(img)
    d.rectangle((0, 0, 1280, 12), fill=GOLD)
    d.rectangle((0, 708, 1280, 720), fill=GOLD)
    if eyebrow:
        centered(d, eyebrow, 150, f(30, True), GOLD)
    centered(d, title, 245, f(72, True), CREAM)
    if subtitle:
        centered(d, subtitle, 390, f(32), (200, 220, 205))
    img.save(CARDS / filename)


card("00-intro.png", "DEVELOPMENT DEMO · NO REAL MONEY", "Matbeah Shel Chesed", "A digital charity box for web, Android and kiosk")
card("02-add-coins.png", "STEP 01", "Add virtual coins", "Tap or drag Israeli coins into your charity box")
card("04-choose.png", "STEP 02", "Choose your amount", "Approve a monthly donation — nothing is charged")
card("06-verify.png", "STEP 03", "Verify every event", "An append-only ledger shows each balance change")
card("09-kiosk.png", "PUBLIC STATIONS", "Kiosk mode", "Large touch targets, QR link and automatic reset")
card("10-outro.png", "TEST / DEMO ONLY", "Transparent by design", "Balances change only after a verified successful payment")

print("Cards written to", CARDS)
