import streamlit as st

st.set_page_config(page_title="RGB Color Mixer | Yahya", page_icon="🎨", layout="wide")

# Student profile
STUDENT_NAME = "Yahya"
ROLL_NUMBER = "25-23TE28"
DEPARTMENT = "Textile Engineering"

st.sidebar.title("Student Profile")
st.sidebar.write(f"**Name:** {STUDENT_NAME}")
st.sidebar.write(f"**Roll No:** {ROLL_NUMBER}")
st.sidebar.write(f"**Department:** {DEPARTMENT}")
st.sidebar.divider()
st.sidebar.caption("RGB Color Mixer")

st.title("🎨 RGB Color Mixer")
st.write("Mix Red, Green, and Blue values to create a color. The preview updates as you move the sliders.")

presets = {
    "Custom": (120, 90, 200),
    "Red": (255, 0, 0),
    "Green": (0, 255, 0),
    "Blue": (0, 0, 255),
    "Yellow": (255, 255, 0),
    "Cyan": (0, 255, 255),
    "Magenta": (255, 0, 255),
    "White": (255, 255, 255),
    "Black": (0, 0, 0),
    "Orange": (255, 165, 0),
    "Purple": (128, 0, 128),
}

preset = st.selectbox("Choose a basic color", list(presets.keys()))
defaults = presets[preset]

col_r, col_g, col_b = st.columns(3)
with col_r:
    red = st.slider("🔴 Red (R)", 0, 255, defaults[0], key=f"red_{preset}")
with col_g:
    green = st.slider("🟢 Green (G)", 0, 255, defaults[1], key=f"green_{preset}")
with col_b:
    blue = st.slider("🔵 Blue (B)", 0, 255, defaults[2], key=f"blue_{preset}")

hex_color = f"#{red:02X}{green:02X}{blue:02X}"

st.subheader("Generated Color Preview")
st.markdown(
    f'''<div style="height:260px; width:100%; background:{hex_color}; border-radius:16px;
    border:1px solid rgba(128,128,128,.5);"></div>''',
    unsafe_allow_html=True,
)

m1, m2, m3, m4 = st.columns(4)
m1.metric("Red", red)
m2.metric("Green", green)
m3.metric("Blue", blue)
m4.metric("HEX Code", hex_color)
st.code(f"RGB({red}, {green}, {blue})  |  {hex_color}", language="text")

st.subheader("Student Project")
st.write(f"**Name:** {STUDENT_NAME}  ")
st.write(f"**Roll Number:** {ROLL_NUMBER}  ")
st.write(f"**Department:** {DEPARTMENT}")

st.caption("Note: This app displays additive RGB screen colors. It is a learning tool and does not predict physical dye or pigment mixtures.")
