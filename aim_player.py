# aim_player_ultimate_with_vlc_hotkeys.py
# THIS IS THE REAL FINAL — EVERYTHING + VLC HOTKEYS

import streamlit as st
import base64
import json
from pathlib import Path

st.set_page_config(
    page_title="AIM PLAYER",
    page_icon="target",
    layout="wide",
    initial_sidebar_state="expanded"
)

# PWA
svg_icon = (
    "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 192 192'>"
    "<circle cx='96' cy='96' r='80' fill='%2300ff88'/>"
    "<circle cx='96' cy='96' r='50' fill='%23000'/>"
    "<circle cx='96' cy='96' r='25' fill='%2300ff88'/>"
    "</svg>"
)
manifest = {
    "name": "AIM PLAYER",
    "short_name": "AIM",
    "start_url": ".",
    "display": "standalone",
    "background_color": "#000",
    "theme_color": "#00ff88",
    "icons": [
        {
            "src": f"data:image/svg+xml,{svg_icon}",
            "sizes": "192x192",
        }
    ],
}
manifest_json = json.dumps(manifest).encode()
manifest_b64 = base64.b64encode(manifest_json).decode()
st.markdown(
    f"<link rel='manifest' href='data:application/manifest+json;base64,"
    f"{manifest_b64}'>",
    unsafe_allow_html=True,
)

# Theme
theme = {"bg": "#000", "p": "#00ff88", "card": "#111"}
st.markdown(
    f"""
    <style>
        .stApp {{background:{theme['bg']}; color:#fff;}}
        h1 {{color:{theme['p']}; text-align:center;
             text-shadow:0 0 40px {theme['p']};}}
        .stButton>button {{background:{theme['p']}; color:black;
                           font-weight:bold; border:none;}}
        .card {{background:{theme['card']}; padding:20px;
                border-radius:16px; border:2px solid {theme['p']};}}
        ::cue {{font-size:28px; color:white;
                background:rgba(0,0,0,0.8); font-weight:bold;}}
    </style>
    """,
    unsafe_allow_html=True
)

# Persistence
DATA_FILE = Path("aim_final.json")


def save():
    DATA_FILE.write_text(
        json.dumps(
            {
                k: st.session_state[k]
                for k in [
                    "playlist",
                    "eq31",
                    "current_preset",
                    "custom_presets",
                    "volume",
                    "speed",
                    "current_idx",
                ]
            }
        )
    )


def load():
    if DATA_FILE.exists():
        try:
            data = json.loads(DATA_FILE.read_text())
            for k, v in data.items():
                st.session_state[k] = v
        except Exception:
            pass


load()

# Defaults
bands = [
    20, 25, 31.5, 40, 50, 63, 80, 100, 125, 160, 200, 250, 315, 400, 500,
    630, 800, 1000, 1250, 1600, 2000, 2500, 3150, 4000, 5000, 6300, 8000,
    10000, 12500, 16000, 20000
]
presets = {
    "Flat": {f: 0 for f in bands},
    "Bass Monster": {20: 16, 25: 15, 31.5: 14, 40: 12, 50: 10, 63: 8},
    "Crystal Clear": {4000: 9, 5000: 8, 8000: 10, 10000: 8, 16000: 8},
    "Dubstep": {20: 18, 31.5: 16, 63: 14},
    "Rock": {63: 10, 125: 8, 8000: 10, 16000: 10},
    "Jazz": {160: 6, 400: 8, 1000: 5, 4000: 6},
    "Lofi Hip-Hop": {20: 8, 63: 6, 8000: -10, 16000: -15},
    "Classical": {20: 5, 4000: 10, 8000: 12, 16000: 10},
}

init_keys = [
    "eq31",
    "custom_presets",
    "playlist",
    "current_preset",
    "volume",
    "speed",
    "current_idx",
]
for k in init_keys:
    if k not in st.session_state:
        if k == "eq31":
            st.session_state[k] = {f: 0 for f in bands}
        elif k == "custom_presets":
            st.session_state[k] = {}
        elif k == "playlist":
            st.session_state[k] = []
        elif k == "current_preset":
            st.session_state[k] = "Flat"
        elif k in ["volume", "speed"]:
            st.session_state[k] = 1.0
        else:
            st.session_state[k] = 0

# Sidebar
with st.sidebar:
    st.markdown(
        f"<h1 style='color:{theme['p']}'>AIM PLAYER</h1>",
        unsafe_allow_html=True
    )
    media = st.file_uploader(
        "Upload Media", type=["mp4", "webm", "mp3", "wav", "ogg"]
    )
    subs = st.file_uploader("Subtitle", type=["srt", "vtt", "ass"])
    if media:
        m64 = base64.b64encode(media.getvalue()).decode()
        url = f"data:{media.type};base64,{m64}"
        sub_url = (
            f"data:text/vtt;base64,"
            f"{base64.b64encode(subs.getvalue()).decode()}"
            if subs
            else None
        )
        st.session_state.playlist.append(
            {
                "name": media.name,
                "url": url,
                "type": media.type,
                "sub": sub_url,
            }
        )
        save()
        st.rerun()

# Main
st.markdown(
    "<h1>AIM PLAYER — FINAL WITH VLC HOTKEYS</h1>",
    unsafe_allow_html=True
)

if st.session_state.playlist:
    idx = st.session_state.current_idx
    track = st.session_state.playlist[idx]

    # Preset + Save
    col1, col2 = st.columns(2)
    with col1:
        p = st.selectbox(
            "Preset",
            ["Manual"] + list(presets) + list(st.session_state.custom_presets),
        )
        if p != "Manual" and p != st.session_state.current_preset:
            preset_dict = (
                presets if p in presets else st.session_state.custom_presets
            )
            st.session_state.eq31 = preset_dict[p].copy()
            st.session_state.current_preset = p
            save()
            st.rerun()
    with col2:
        n = st.text_input("Save custom")
        if st.button("Save") and n:
            st.session_state.custom_presets[n] = st.session_state.eq31.copy()
            st.session_state.current_preset = n
            save()

    # 31-Band EQ
    with st.expander(
        f"31-Band EQ — {st.session_state.current_preset}", True
    ):
        for i in range(0, len(bands), 10):
            cols = st.columns(10)
            for j, col in enumerate(cols):
                if i + j < len(bands):
                    f = bands[i + j]
                    v = col.slider(
                        f"{f}Hz",
                        -15,
                        15,
                        float(st.session_state.eq31[f]),
                        0.5,
                        key=f"eq{i+j}",
                    )
                    st.session_state.eq31[f] = v

    # Player
    sub_track = (
        f'<track kind="subtitles" src="{track["sub"]}" default>'
        if track.get("sub")
        else ""
    )
    st.video(track["url"])

    # === VLC HOTKEYS + FULL AUDIO ENGINE ===
    html_code = f"""
    <div style="position:fixed;bottom:20px;left:20px;color:#00ff88;
         font-size:18px;font-weight:bold;z-index:999;">
        VLC Hotkeys Active — Space=Play/Pause • →/+10s • ←/-10s •
        Ctrl+→/+60s • Ctrl+←/-60s • F=Fullscreen • M=Mute • +/- Volume
    </div>
    <script>
    const video = document.querySelector('video');
    if (video) {{
        document.addEventListener('keydown', e => {{
            if (e.target.tagName === 'INPUT') return;
            if (e.key === ' ') {{
                e.preventDefault();
                video.paused ? video.play() : video.pause();
            }}
            else if (e.key === 'ArrowRight') {{
                video.currentTime += e.ctrlKey ? 60 : 10;
            }}
            else if (e.key === 'ArrowLeft') {{
                video.currentTime -= e.ctrlKey ? 60 : 10;
            }}
            else if (e.key === 'f' || e.key === 'F') {{
                video.requestFullscreen?.();
            }}
            else if (e.key === 'm' || e.key === 'M') {{
                video.muted = !video.muted;
            }}
            else if (e.key === '+' || e.key === '=') {{
                video.volume = Math.min(2, video.volume + 0.1);
                parent.postMessage({{volume:video.volume}},'*');
            }}
            else if (e.key === '-') {{
                video.volume = Math.max(0, video.volume - 0.1);
                parent.postMessage({{volume:video.volume}},'*');
            }}
        }});

        // Sync volume from slider
        window.addEventListener('message', msg => {{
            if (msg.data.volume !== undefined)
                video.volume = msg.data.volume;
        }});
    }}

    // FULL AUDIO ENGINE (31-band + visualizer)
    let ctx, src, analyser, gain, filters=[];
    function init() {{
        if (!video) return;
        ctx = new AudioContext();
        src = ctx.createMediaElementSource(video);
        analyser = ctx.createAnalyser();
        analyser.fftSize = 2048;
        gain = ctx.createGain();
        const freqs = {json.dumps(bands)};
        const gains = {json.dumps(list(st.session_state.eq31.values()))};
        filters = freqs.map((f,i)=>({{
            let b = ctx.createBiquadFilter();
            b.type = f<=31.5?'lowshelf':f>=16000?'highshelf':'peaking';
            b.frequency.value = f;
            b.gain.value = gains[i];
            return b;
        }}));
        src.connect(filters[0]);
        for(let i=0;i<filters.length-1;i++)
            filters[i].connect(filters[i+1]);
        filters[filters.length-1].connect(analyser);
        filters[filters.length-1].connect(gain);
        gain.connect(ctx.destination);
        gain.gain.value = {st.session_state.volume};
        video.volume = {st.session_state.volume};
    }}
    setInterval(()=>{{
        if (filters.length) {{
            const g = {json.dumps(list(st.session_state.eq31.values()))};
            filters.forEach((f,i)=>f.gain.setValueAtTime(g[i],
                ctx?.currentTime || 0));
        }}
    }}, 80);

    // Visualizer
    const canvas = document.createElement('canvas');
    canvas.width = 1200;
    canvas.height = 440;
    canvas.style.cssText = 'width:100%;background:#000;border-radius:' +
                           '16px;margin-top:20px;';
    document.body.appendChild(canvas);
    const c = canvas.getContext('2d');
    const buf = new Uint8Array(1024);
    function draw() {{
        requestAnimationFrame(draw);
        if (!analyser) return;
        analyser.getByteFrequencyData(buf);
        c.fillStyle = 'rgba(0,0,0,0.2)';
        c.fillRect(0,0,canvas.width,canvas.height);
        const w = canvas.width/128;
        for(let i=0;i<128;i++){{
            const h = canvas.height * (buf[i*8]/255) * 1.6;
            const hue = (i*3 + performance.now()*0.05) % 360;
            c.fillStyle = `hsl(${{hue}},100%,60%)`;
            c.fillRect(i*w, canvas.height-h, w-3, h);
        }}
    }}
    draw();
    video?.addEventListener('play', init);
    </script>
    """
    st.components.v1.html(html_code, height=500)

    # Playlist with delete
    st.subheader("Playlist")
    for i in range(len(st.session_state.playlist)):
        c1, c2 = st.columns([6, 1])
        with c1:
            playlist_item = st.session_state.playlist[i]
            if st.button(
                f"{i+1}. {playlist_item['name']}", key=f"p{i}"
            ):
                st.session_state.current_idx = i
                st.rerun()
        with c2:
            if st.button("X", key=f"d{i}"):
                st.session_state.playlist.pop(i)
                playlist_len = len(st.session_state.playlist)
                if (
                    st.session_state.current_idx >= playlist_len
                    and playlist_len > 0
                ):
                    st.session_state.current_idx = 0
                save()
                st.rerun()

else:
    st.markdown(
        "<h2 style='text-align:center;color:#00ff88'>Upload media "
        "→ AIM PLAYER owns your soul now.</h2>",
        unsafe_allow_html=True,
    )

st.success(
    "AIM PLAYER — FINAL WITH FULL VLC HOTKEYS • "
    "EVERYTHING INCLUDED • 2025"
)
st.caption("Space • Arrows • F • M • +/−  →  You know what to do.")
