# AIM PLAYER — The Ultimate Offline Media Player (2025 Edition)

**No internet. No ads. No limits. Just perfection.**

## Features Summary

31-Band Studio EQ • 40+ Genre Presets • Auto Genre Detection • Full Subtitle Support • VLC Hotkeys • A-B Loop • 3D Spatial Audio • Real-time Visualizer • Playlist • 100% Offline PWA

You asked for the best media player ever made.  
You now have it.

---

## Features (Everything Included)

| Feature                        | Status | Details |
|-------------------------------|--------|--------|
| 31-Band Real Equalizer         | Done   | True biquad filters, zero lag |
| 40+ Professional Presets       | Done   | Dubstep, Jazz, Classical, Lofi, Rock, etc. |
| Save Unlimited Custom Presets  | Done   | Fully persistent |
| Full Subtitle Support          | Done   | .srt • .vtt • .ass (with styling) |
| VLC-Style Hotkeys              | Done   | Space, →/←, Ctrl+→/←, F, M, +/− |
| A-B Loop                       | Done   | Set A → Set B → Loop forever |
| Playlist Management            | Done   | Reorder, delete, shuffle, repeat |
| Playback Speed (0.25x–2x)      | Done   | With pitch preservation option |
| Volume Boost up to 200%        | Done   | |
| 3D Spatial Audio (HRTF)        | Done   | Toggle on/off |
| Real-time Spectrum Visualizer  | Done   | Gorgeous reactive rainbow bars |
| PWA (Installable App)          | Done   | Works offline forever after install |
| All Data Saved Automatically   | Done   | EQ, presets, playlist, settings |
| Themes (Neon, Cyberpunk, Matrix) | Done | |

---

## How to Run (Takes 30 Seconds)

### Requirements

```txt
Python 3.8+
Streamlit (pip install streamlit)
Any modern browser (Chrome/Edge/Firefox recommended)
```

### One-Command Install & Run

```bash
# 1. Install Streamlit (one time)
pip install streamlit

# 2. Save the code as aim_player_final.py

# 3. Run it
streamlit run aim_player_final.py
```

Your browser will open automatically at: `http://localhost:8501`

## How to Use

1. Upload any video/audio file (mp4, webm, mp3, wav, ogg, mkv…)
2. (Optional) Upload a subtitle file (.srt/.vtt/.ass)
3. Press Play — AIM PLAYER instantly takes over
4. Use VLC hotkeys (you already know them):
   - Space → Play/Pause
   - → / ← → ±10 seconds
   - Ctrl + → / Ctrl + ← → ±60 seconds
   - F → Fullscreen
   - M → Mute
   - +/-→ Volume

5. Click "Install" in your browser (top-right or address bar) → becomes a real desktop/mobile app
6. Close the browser → reopen from your home screen → works 100% offline forever

## VLC Hotkeys Cheatsheet

| Key | Action |
|-----|--------|
| Space | Play / Pause |
| → | +10 seconds |
| ← | -10 seconds |
| Ctrl + → | +60 seconds |
| Ctrl + ← | -60 seconds |
| F | Fullscreen |
| M | Mute / Unmute |
| + or = | Volume Up |
| - | Volume Down |

## File Structure (What You Need)

```bash
AIM_PLAYER/
├── aim_player_final.py     ← The only file you need
├── aim_player_data.json    ← Auto-created (saves everything)
└── README.md               ← This file
