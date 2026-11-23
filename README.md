# Matbeah ShelChesed — promotional homepage

A standalone, **HTML-only** promotional site for the *Matbeah Shel Chesed* (מטבע של חסד) digital charity box project. It lives in its own repository and has no build step, no JavaScript and no external dependencies — open `index.html` in a browser or serve the folder with any static host (GitHub Pages included).

> This is a **development demo**. No real money, no real payments, and no false compliance claims.

## Contents

```
index.html                     single self-contained page (HTML + embedded CSS)
assets/
  screens/*.png                real screenshots captured from the running app
  cards/*.png                  English caption cards for the video
  instructional.mp4            24.5 s silent walkthrough (H.264, 1280x720, ~0.5 MB)
  make_cards.py                generates the caption cards (Pillow)
  make_video.ps1               builds the MP4 from screenshots with ffmpeg
```

## Screenshots

All images in `assets/screens/` were captured from the actual running web application via the browser screenshot tool — they are not mockups. They cover the English and Hebrew (RTL) landing pages, the dashboard, the animated charity box, donation selection, donation history, the admin panel and the kiosk in both languages.

## Video

`assets/instructional.mp4` is a **silent slideshow compiled from those real screenshots** with ffmpeg and English caption cards. It is not a screen recording and not AI-generated footage. To reproduce it:

```bash
python assets/make_cards.py
powershell -ExecutionPolicy Bypass -File assets/make_video.ps1
```

Requirements: Python + Pillow for the cards, ffmpeg on `PATH` for the video. The script is deterministic: 12 slides, 2.5 s each, 0.5 s crossfade, H.264 CRF 27, 24 fps, no audio.

## Sections

- Hero with Hebrew RTL and English LTR copy
- Feature and platform overview (web PWA / Android / kiosk)
- Screenshot gallery with links to full-size images
- Embedded instructional video
- Demo account credentials
- Honest safety notes: no real payments, debug-only APK, no compliance claim

## Hosting

Copy the folder contents to any static host. For GitHub Pages: repository settings → Pages → deploy from `main` / root. No configuration file is needed.
