"""Generate per-slide English narration with edge-tts (natural neural voice)."""
import asyncio
from pathlib import Path
import edge_tts

HERE = Path(__file__).resolve().parent / "narration"
HERE.mkdir(exist_ok=True)

VOICE = "en-US-JennyNeural"
RATE = "+8%"

LINES = [
    "Matbeah Shel Chesed. A digital charity box.",
    "Hebrew and English, on the web.",
    "Step one: add virtual coins.",
    "Five Israeli coins. Tap or drag.",
    "Step two: choose your amount.",
    "Approve. Nothing is charged.",
    "Balances are server computed.",
    "Step three: verify every event.",
    "The ledger is append only.",
    "Public kiosk mode.",
    "Large buttons. QR link. Auto reset.",
    "Transparent by design. Demo only.",
]


async def main():
    for index, line in enumerate(LINES):
        out = HERE / f"{index:02d}.mp3"
        await edge_tts.Communicate(line, VOICE, rate=RATE).save(str(out))
        print(f"{out.name}: {line}")


if __name__ == "__main__":
    asyncio.run(main())
