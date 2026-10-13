import re
import streamlit as st

st.set_page_config(
    page_title="Color Mixer | Adil Mangsi",
    page_icon="🎨",
    layout="wide",
)

# Student / project information
STUDENT_NAME = "Adil Mangsi"
ROLL_NUMBER = "25TE065"
DEPARTMENT = "Textile Engineering"

PRESETS = {
    "Red": (255, 0, 0),
    "Green": (0, 255, 0),
    "Blue": (0, 0, 255),
    "Yellow": (255, 255, 0),
    "Magenta": (255, 0, 255),
    "Cyan": (0, 255, 255),
    "White": (255, 255, 255),
    "Black": (0, 0, 0),
    "Orange": (255, 128, 0),
    "Purple": (128, 0, 128),
    "Pink": (255, 105, 180),
    "Gray": (128, 128, 128),
}


def rgb_to_hex(r: int, g: int, b: int) -> str:
    return f"#{r:02X}{g:02X}{b:02X}"


def hex_to_rgb(value: str):
    value = value.strip()
    if not value.startswith("#"):
        value = "#" + value
    if re.fullmatch(r"#[0-9a-fA-F]{6}", value):
        return tuple(int(value[i:i + 2], 16) for i in (1, 3, 5))
    return None


def relative_luminance(r: int, g: int, b: int) -> float:
    channels = []
    for c in (r, g, b):
        c = c / 255
        channels.append(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * channels[0] + 0.7152 * channels[1] + 0.0722 * channels[2]


st.markdown(
    """
    <style>
      .main-title {font-size:2.25rem;font-weight:800;letter-spacing:-0.03em;margin-bottom:0.1rem;}
      .sub-title {color:#64748b;font-size:1rem;margin-bottom:1.2rem;}
      .swatch {height:250px;border-radius:18px;border:1px solid rgba(120,120,120,.35);}
      .small-swatch {height:42px;border-radius:8px;border:1px solid rgba(120,120,120,.3);}
      .profile {padding:14px 16px;border:1px solid rgba(120,120,120,.25);border-radius:14px;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="main-title">🎨 RGB Color Mixer</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-title">Mix Red, Green, and Blue values and see your new color instantly.</div>',
    unsafe_allow_html=True,
)

with st.sidebar:
    st.header("Project Profile")
    st.markdown(
        f"**Name:** {STUDENT_NAME}  \n"
        f"**Roll No.:** {ROLL_NUMBER}  \n"
        f"**Department:** {DEPARTMENT}"
    )
    st.divider()
    st.subheader("Quick Color Presets")
    preset_name = st.selectbox("Choose a basic color", list(PRESETS.keys()))
    if st.button("Apply Preset", use_container_width=True):
        pr, pg, pb = PRESETS[preset_name]
        st.session_state["red"] = pr
        st.session_state["green"] = pg
        st.session_state["blue"] = pb
        st.rerun()
    st.caption("Tip: use the sliders to mix your own shade.")

# Initialize slider values before rendering widgets
for key, default in (("red", 225), ("green", 225), ("blue", 0)):
    if key not in st.session_state:
        st.session_state[key] = default

left, right = st.columns([1.05, 1], gap="large")
with left:
    st.subheader("Adjust RGB Values")
    red = st.slider("🔴 Red (R)", min_value=0, max_value=255, key="red")
    green = st.slider("🟢 Green (G)", min_value=0, max_value=255, key="green")
    blue = st.slider("🔵 Blue (B)", min_value=0, max_value=255, key="blue")

    st.markdown("#### Enter a HEX code (optional)")
    hex_input = st.text_input("HEX color", value=rgb_to_hex(red, green, blue), help="Example: #E1E100")
    if st.button("Apply HEX", use_container_width=True):
        parsed = hex_to_rgb(hex_input)
        if parsed is None:
            st.error("Please enter a valid HEX code, for example #E1E100.")
        else:
            st.session_state["red"], st.session_state["green"], st.session_state["blue"] = parsed
            st.rerun()

with right:
    st.subheader("Generated Color Preview")
    hex_value = rgb_to_hex(red, green, blue)
    st.markdown(f'<div class="swatch" style="background:{hex_value};"></div>', unsafe_allow_html=True)
    st.markdown(f"### `{hex_value}`")
    st.caption("The preview updates automatically when you change the sliders.")

st.divider()
st.subheader("Color Values")
metric_cols = st.columns(4)
metric_cols[0].metric("Red (R)", red)
metric_cols[1].metric("Green (G)", green)
metric_cols[2].metric("Blue (B)", blue)
metric_cols[3].metric("HEX Code", hex_value)

lum = relative_luminance(red, green, blue)
text_color = "black" if lum > 0.45 else "white"
st.markdown(
    f'<div style="background:{hex_value};color:{text_color};padding:16px;border-radius:12px;">'
    f'<strong>RGB:</strong> ({red}, {green}, {blue}) &nbsp; | &nbsp; '
    f'<strong>HEX:</strong> {hex_value} &nbsp; | &nbsp; '
    f'<strong>Relative luminance:</strong> {lum:.3f}</div>',
    unsafe_allow_html=True,
)

st.subheader("Basic RGB Color Reference")
cols = st.columns(4)
for index, (name, values) in enumerate(PRESETS.items()):
    preset_hex = rgb_to_hex(*values)
    with cols[index % 4]:
        st.markdown(f'<div class="small-swatch" style="background:{preset_hex};"></div>', unsafe_allow_html=True)
        st.markdown(f"**{name}** · `{preset_hex}`")
        st.caption(f"RGB{values}")

st.divider()
st.markdown(
    f'<div class="profile"><strong>Developed by:</strong> {STUDENT_NAME} '
    f'&nbsp; | &nbsp; <strong>Roll No.:</strong> {ROLL_NUMBER} '
    f'&nbsp; | &nbsp; <strong>Department:</strong> {DEPARTMENT}</div>',
    unsafe_allow_html=True,
)
st.caption("Educational project · Built with Python and Streamlit")
