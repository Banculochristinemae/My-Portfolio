# pages/7_✨_Stargazing.py
import streamlit as st
import random
import base64

st.set_page_config(
    page_title="Stargazing | Relax & Explore",
    page_icon="✨",
    layout="wide"
)

st.markdown("""
<style>
    .stApp {
        background: radial-gradient(ellipse at center, #030618 0%, #000000 100%);
        background-attachment: fixed;
    }
    
    [data-testid="stSidebarNav"] {
        display: none !important;
    }
    
    [data-testid="stSidebar"] {
        background: rgba(5, 10, 25, 0.85);
        backdrop-filter: blur(12px);
        border-right: 1px solid rgba(100, 150, 255, 0.3);
    }
    
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    
    [data-testid="stSidebar"] .stButton > button {
        background: rgba(20, 30, 60, 0.5);
        backdrop-filter: blur(8px);
        border-radius: 30px;
        border: 1px solid rgba(100, 150, 255, 0.3);
        color: #ffffff !important;
        width: 100%;
        margin: 5px 0;
        transition: all 0.3s ease;
    }
    
    [data-testid="stSidebar"] .stButton > button:hover {
        background: rgba(100, 150, 255, 0.4);
        border-color: rgba(150, 200, 255, 0.8);
        transform: translateX(5px);
        box-shadow: 0 0 15px rgba(100, 150, 255, 0.3);
    }
    
    .star-bg {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 0;
    }
    
    .star {
        position: absolute;
        background-color: white;
        border-radius: 50%;
        animation: twinkle 3s infinite ease-in-out;
    }
    
    @keyframes twinkle {
        0%, 100% { opacity: 0.3; }
        50% { opacity: 1; }
    }
    
    .info-card {
        background: rgba(15, 25, 45, 0.7);
        backdrop-filter: blur(12px);
        border-radius: 20px;
        border: 1px solid rgba(100, 150, 255, 0.3);
        padding: 20px;
        margin: 15px 0;
        transition: all 0.3s ease;
        position: relative;
        z-index: 10;
    }
    .info-card:hover {
        transform: translateY(-5px);
        border-color: rgba(150, 200, 255, 0.8);
        box-shadow: 0 0 25px rgba(100, 150, 255, 0.5);
    }
    
    /* ALL TEXT PURE WHITE */
    .info-card p, .info-card li, .info-card span, .info-card h1, .info-card h2, .info-card h3, .info-card h4 {
        color: #ffffff !important;
    }
    
    .music-card {
        background: rgba(15, 25, 45, 0.7);
        backdrop-filter: blur(12px);
        border-radius: 20px;
        border: 1px solid rgba(100, 150, 255, 0.3);
        padding: 20px;
        margin: 15px 0;
        transition: all 0.3s ease;
        text-align: center;
    }
    .music-card:hover {
        transform: translateY(-5px);
        border-color: rgba(150, 200, 255, 0.8);
        box-shadow: 0 0 25px rgba(100, 150, 255, 0.5);
    }
    
    /* Music card ALL TEXT PURE WHITE */
    .music-card h4, .music-card p {
        color: #ffffff !important;
    }
    
    .display-container {
        display: flex;
        flex-direction: row;
        gap: 30px;
        align-items: center;
        justify-content: center;
        background: rgba(10, 20, 40, 0.9);
        backdrop-filter: blur(12px);
        border-radius: 30px;
        border: 2px solid rgba(150, 200, 255, 0.8);
        padding: 30px;
        margin: 20px 0;
        min-height: 450px;
    }
    
    .animation-side {
        flex: 1;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        text-align: center;
    }
    
    /* Animation side text PURE WHITE */
    .animation-side p {
        color: #ffffff !important;
    }
    
    .info-side {
        flex: 1;
        padding: 20px;
        text-align: left;
    }
    
    /* Info side ALL TEXT PURE WHITE */
    .info-side p, .info-side strong, .info-side span, .info-side h2 {
        color: #ffffff !important;
    }
    
    /* Fascinating fact box - ALL TEXT PURE WHITE */
    .info-fact {
        background: rgba(100,150,255,0.2);
        padding: 15px;
        border-radius: 15px;
        margin-top: 15px;
        border-left: 3px solid #7eb6ff;
    }
    
    .info-fact strong, .info-fact, .info-fact span {
        color: #ffffff !important;
    }
    
    /* Title PURE WHITE */
    .info-title {
        color: #ffffff !important;
        font-size: 1.8rem;
        margin-bottom: 15px;
    }
    
    .colored-code {
        font-family: 'Courier New', monospace;
        font-size: 0.9rem;
        background: rgba(10, 20, 40, 0.8);
        padding: 8px;
        border-radius: 8px;
        text-align: center;
    }
    .code-keyword { color: #ff79c6; }
    .code-string { color: #f1fa8c; }
    .code-parenthesis { color: #ffb86c; }
    
    /* ALL HEADERS PURE WHITE */
    h1, h2, h3, h4, h5, h6, .stHeader, .stSubheader {
        color: #ffffff !important;
        font-family: 'Courier New', monospace;
        text-shadow: 0 0 10px rgba(100, 150, 255, 0.5);
        position: relative;
        z-index: 10;
    }
    
    /* ALL TEXT ELEMENTS PURE WHITE */
    p, li, span, div, label, .stMarkdown, .stText, .stCaption {
        color: #ffffff !important;
    }
    
    /* Expander header PURE WHITE */
    .streamlit-expanderHeader {
        color: #ffffff !important;
        background: rgba(15, 25, 45, 0.7);
    }
    
    /* Expander content PURE WHITE */
    .streamlit-expanderContent p, .streamlit-expanderContent li {
        color: #ffffff !important;
    }
    
    /* Alert messages PURE WHITE */
    .stAlert, .stAlert p, .stInfo, .stInfo p, .stSuccess, .stSuccess p, .stWarning, .stWarning p, .stError, .stError p {
        color: #ffffff !important;
    }
    
    /* Button text PURE WHITE */
    .stButton > button, .stButton > button p {
        color: #ffffff !important;
    }
    
    /* Slider text PURE WHITE */
    .stSlider label, .stSlider p {
        color: #ffffff !important;
    }
    
    /* Selectbox label PURE WHITE */
    .stSelectbox label {
        color: #ffffff !important;
    }
    
    /* Text input labels PURE WHITE */
    .stTextInput label, .stTextArea label {
        color: #ffffff !important;
    }
    
    .main-content {
        position: relative;
        z-index: 10;
    }
    
    .stButton > button {
        background: rgba(30, 50, 80, 0.5);
        backdrop-filter: blur(8px);
        border-radius: 30px;
        border: 1px solid rgba(100, 150, 255, 0.4);
        color: #ffffff !important;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background: rgba(100, 150, 255, 0.35);
        border-color: rgba(150, 200, 255, 0.9);
        transform: translateY(-2px);
        box-shadow: 0 0 15px rgba(100, 150, 255, 0.3);
        color: #ffffff !important;
    }
    
    audio {
        width: 100%;
        border-radius: 30px;
        margin-top: 10px;
    }
    
    .animation-img {
        border-radius: 20px;
        box-shadow: 0 0 30px rgba(100,150,255,0.4);
    }
    
    /* Dropdown text (options) - keep black for readability */
    .stSelectbox div[data-baseweb="select"] div {
        color: #000000 !important;
        background-color: #ffffff !important;
    }
    
    /* Caption PURE WHITE */
    .stCaption, caption {
        color: #ffffff !important;
    }
    
    /* hr line */
    hr {
        border-color: rgba(100, 150, 255, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# Generate random twinkling stars in background
def generate_stars():
    stars_html = '<div class="star-bg">'
    for i in range(200):
        size = random.randint(1, 3)
        left = random.randint(0, 100)
        top = random.randint(0, 100)
        delay = random.uniform(0, 3)
        duration = random.uniform(2, 5)
        stars_html += f'<div class="star" style="width:{size}px;height:{size}px;left:{left}%;top:{top}%;animation-delay:{delay}s;animation-duration:{duration}s;"></div>'
    stars_html += '</div>'
    return stars_html

# ========== SVG ANIMATIONS as BASE64 DATA URLS ==========

def get_animation_svg(object_key):
    if object_key == "Sun":
        svg = """<svg width="250" height="250" viewBox="0 0 250 250" xmlns="http://www.w3.org/2000/svg">
            <defs><radialGradient id="g" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#ffff66"/><stop offset="50%" stop-color="#ffcc33"/><stop offset="100%" stop-color="#ff8800"/></radialGradient></defs>
            <g transform="translate(125,125)"><circle cx="0" cy="0" r="50" fill="url(#g)"><animate attributeName="r" values="45;55;45" dur="1.5s" repeatCount="indefinite"/></circle>
            <circle cx="0" cy="0" r="60" fill="#ffcc33" opacity="0.3"><animate attributeName="r" values="55;65;55" dur="1.5s" repeatCount="indefinite"/></circle></g></svg>"""
    elif object_key == "Sirius":
        svg = """<svg width="250" height="250" viewBox="0 0 250 250" xmlns="http://www.w3.org/2000/svg">
            <defs><radialGradient id="g" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#ffffff"/><stop offset="50%" stop-color="#aaccff"/><stop offset="100%" stop-color="#6688cc"/></radialGradient></defs>
            <g transform="translate(125,125)"><circle cx="0" cy="0" r="45" fill="url(#g)"><animate attributeName="r" values="40;50;40" dur="1.2s" repeatCount="indefinite"/></circle>
            <circle cx="0" cy="0" r="70" fill="#aaccff" opacity="0.2"><animate attributeName="r" values="60;75;60" dur="1.2s" repeatCount="indefinite"/></circle></g></svg>"""
    elif object_key == "Betelgeuse":
        svg = """<svg width="250" height="250" viewBox="0 0 250 250" xmlns="http://www.w3.org/2000/svg">
            <defs><radialGradient id="g" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#ff6644"/><stop offset="70%" stop-color="#ff3300"/><stop offset="100%" stop-color="#cc0000"/></radialGradient></defs>
            <g transform="translate(125,125)"><circle cx="0" cy="0" r="65" fill="url(#g)"><animate attributeName="r" values="55;75;55" dur="2s" repeatCount="indefinite"/></circle>
            <circle cx="0" cy="0" r="85" fill="#ff3300" opacity="0.3"><animate attributeName="r" values="70;95;70" dur="2s" repeatCount="indefinite"/></circle></g></svg>"""
    elif object_key == "Rigel":
        svg = """<svg width="250" height="250" viewBox="0 0 250 250" xmlns="http://www.w3.org/2000/svg">
            <defs><radialGradient id="g" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#88aaff"/><stop offset="60%" stop-color="#4466cc"/><stop offset="100%" stop-color="#2244aa"/></radialGradient></defs>
            <g transform="translate(125,125)"><circle cx="0" cy="0" r="50" fill="url(#g)"><animate attributeName="r" values="45;55;45" dur="1.8s" repeatCount="indefinite"/></circle></g></svg>"""
    elif object_key == "Moon":
        svg = """<svg width="250" height="250" viewBox="0 0 250 250" xmlns="http://www.w3.org/2000/svg">
            <g transform="translate(125,125)"><circle cx="0" cy="0" r="55" fill="#c0c0c0"><animate attributeName="cy" values="0;-8;0" dur="3s" repeatCount="indefinite"/></circle>
            <circle cx="-15" cy="-15" r="10" fill="#999"/><circle cx="20" cy="10" r="8" fill="#999"/><circle cx="-5" cy="25" r="12" fill="#999"/>
            <circle cx="30" cy="-20" r="6" fill="#999"/><circle cx="-25" cy="15" r="7" fill="#999"/><circle cx="10" cy="-30" r="9" fill="#999"/></g></svg>"""
    elif object_key == "Saturn":
        svg = """<svg width="250" height="250" viewBox="0 0 250 250" xmlns="http://www.w3.org/2000/svg">
            <defs><radialGradient id="g" cx="30%" cy="30%" r="60%"><stop offset="0%" stop-color="#f0e6cc"/><stop offset="100%" stop-color="#c4a66a"/></radialGradient></defs>
            <g transform="translate(125,125)"><ellipse cx="0" cy="0" rx="85" ry="25" fill="none" stroke="#d4be8c" stroke-width="6"/>
            <ellipse cx="0" cy="0" rx="72" ry="20" fill="none" stroke="#c4ae7c" stroke-width="4"/>
            <circle cx="0" cy="0" r="45" fill="url(#g)"><animate attributeName="cy" values="0;-3;0" dur="3s" repeatCount="indefinite"/></circle></g></svg>"""
    elif object_key == "Jupiter":
        svg = """<svg width="250" height="250" viewBox="0 0 250 250" xmlns="http://www.w3.org/2000/svg">
            <g transform="translate(125,125)"><ellipse cx="0" cy="0" rx="65" ry="55" fill="#8B5A2B"/>
            <ellipse cx="0" cy="-20" rx="60" ry="12" fill="#6B3A1B" opacity="0.6"/><ellipse cx="0" cy="-5" rx="62" ry="10" fill="#A0724A" opacity="0.5"/>
            <ellipse cx="0" cy="15" rx="58" ry="14" fill="#7B4A2B" opacity="0.6"/><ellipse cx="0" cy="30" rx="50" ry="10" fill="#6B3A1B" opacity="0.5"/>
            <ellipse cx="20" cy="5" rx="18" ry="12" fill="#CD5C5C" opacity="0.9"><animate attributeName="cx" values="20;25;20" dur="8s" repeatCount="indefinite"/></ellipse></g></svg>"""
    elif object_key == "Milky Way":
        svg = """<svg width="250" height="250" viewBox="0 0 250 250" xmlns="http://www.w3.org/2000/svg">
            <g transform="translate(125,125)"><g><animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="20s" repeatCount="indefinite"/>
            <ellipse cx="0" cy="-50" rx="60" ry="20" fill="#aa88cc" opacity="0.5"/><ellipse cx="0" cy="-50" rx="60" ry="20" fill="#aa88cc" opacity="0.4" transform="rotate(72)"/>
            <ellipse cx="0" cy="-50" rx="60" ry="20" fill="#aa88cc" opacity="0.4" transform="rotate(144)"/><ellipse cx="0" cy="-50" rx="60" ry="20" fill="#aa88cc" opacity="0.3" transform="rotate(216)"/>
            <ellipse cx="0" cy="-50" rx="60" ry="20" fill="#aa88cc" opacity="0.3" transform="rotate(288)"/></g>
            <circle cx="0" cy="0" r="20" fill="#ffdd88"><animate attributeName="r" values="18;23;18" dur="2s" repeatCount="indefinite"/></circle></g></svg>"""
    elif object_key == "Andromeda":
        svg = """<svg width="250" height="250" viewBox="0 0 250 250" xmlns="http://www.w3.org/2000/svg">
            <g transform="translate(125,125)"><g><animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="25s" repeatCount="indefinite"/>
            <ellipse cx="0" cy="-40" rx="45" ry="15" fill="#dd99cc" opacity="0.5"/><ellipse cx="0" cy="-40" rx="45" ry="15" fill="#dd99cc" opacity="0.4" transform="rotate(60)"/>
            <ellipse cx="0" cy="-40" rx="45" ry="15" fill="#dd99cc" opacity="0.4" transform="rotate(120)"/><ellipse cx="0" cy="-40" rx="45" ry="15" fill="#dd99cc" opacity="0.3" transform="rotate(180)"/>
            <ellipse cx="0" cy="-40" rx="45" ry="15" fill="#dd99cc" opacity="0.3" transform="rotate(240)"/><ellipse cx="0" cy="-40" rx="45" ry="15" fill="#dd99cc" opacity="0.2" transform="rotate(300)"/></g>
            <circle cx="0" cy="0" r="25" fill="#ffccaa"><animate attributeName="r" values="22;28;22" dur="3s" repeatCount="indefinite"/></circle></g></svg>"""
    elif object_key == "Orion Nebula":
        svg = """<svg width="250" height="250" viewBox="0 0 250 250" xmlns="http://www.w3.org/2000/svg">
            <defs><filter id="b"><feGaussianBlur stdDeviation="8"/></filter></defs>
            <g transform="translate(125,125)"><ellipse cx="0" cy="0" rx="80" ry="60" fill="#ff6699" opacity="0.4" filter="url(#b)"><animate attributeName="rx" values="75;85;75" dur="5s" repeatCount="indefinite"/></ellipse>
            <ellipse cx="15" cy="-10" rx="60" ry="45" fill="#6699ff" opacity="0.4" filter="url(#b)"><animate attributeName="cx" values="15;0;15" dur="6s" repeatCount="indefinite"/></ellipse>
            <ellipse cx="-10" cy="15" rx="55" ry="40" fill="#66ff99" opacity="0.3" filter="url(#b)"><animate attributeName="cy" values="15;0;15" dur="7s" repeatCount="indefinite"/></ellipse>
            <circle cx="-20" cy="-15" r="4" fill="white" opacity="0.9"><animate attributeName="opacity" values="0.5;1;0.5" dur="1s" repeatCount="indefinite"/></circle>
            <circle cx="15" cy="20" r="3" fill="white" opacity="0.8"><animate attributeName="opacity" values="0.8;1;0.8" dur="1.3s" repeatCount="indefinite"/></circle></g></svg>"""
    elif object_key == "Pleiades":
        svg = """<svg width="250" height="250" viewBox="0 0 250 250" xmlns="http://www.w3.org/2000/svg">
            <g transform="translate(125,125)"><circle cx="-35" cy="-30" r="10" fill="#aaccff"><animate attributeName="r" values="8;12;8" dur="1.2s" repeatCount="indefinite"/></circle>
            <circle cx="25" cy="-40" r="8" fill="#aaccff"><animate attributeName="r" values="6;10;6" dur="1.5s" repeatCount="indefinite" begin="0.3s"/></circle>
            <circle cx="45" cy="5" r="9" fill="#aaccff"><animate attributeName="r" values="7;11;7" dur="1.8s" repeatCount="indefinite" begin="0.6s"/></circle>
            <circle cx="-15" cy="35" r="7" fill="#aaccff"><animate attributeName="r" values="5;9;5" dur="1.3s" repeatCount="indefinite" begin="0.9s"/></circle>
            <circle cx="0" cy="-5" r="14" fill="#bbddff"><animate attributeName="r" values="11;16;11" dur="2s" repeatCount="indefinite" begin="0.2s"/></circle>
            <circle cx="-50" cy="10" r="6" fill="#aaccff"><animate attributeName="r" values="4;8;4" dur="1.1s" repeatCount="indefinite" begin="0.5s"/></circle>
            <circle cx="15" cy="40" r="7" fill="#aaccff"><animate attributeName="r" values="5;9;5" dur="1.6s" repeatCount="indefinite" begin="0.8s"/></circle></g></svg>"""
    else:
        svg = """<svg width="200" height="200" viewBox="0 0 200 200"><circle cx="100" cy="100" r="40" fill="#88aaff"><animate attributeName="r" values="35;45;35" dur="2s" repeatCount="indefinite"/></circle></svg>"""
    
    # Encode SVG to base64 data URL
    svg_base64 = base64.b64encode(svg.encode()).decode()
    return f"data:image/svg+xml;base64,{svg_base64}"

# Sidebar Navigation
st.sidebar.markdown("# 🌌 Christine Mae Banculo")
st.sidebar.markdown("---")

if st.sidebar.button("🌌 Home", use_container_width=True):
    st.switch_page("Home.py")
if st.sidebar.button("👩‍💻 About", use_container_width=True):
    st.switch_page("pages/2_👩‍💻_About.py")
if st.sidebar.button("📊 Skills", use_container_width=True):
    st.switch_page("pages/3_📊_Skills.py")
if st.sidebar.button("📁 Projects", use_container_width=True):
    st.switch_page("pages/4_📁_Projects.py")
if st.sidebar.button("📜 Certificates", use_container_width=True):
    st.switch_page("pages/5_📜_Certificates.py")
if st.sidebar.button("📞 Contact", use_container_width=True):
    st.switch_page("pages/6_📞_Contact.py")
if st.sidebar.button("✨ Stargazing", use_container_width=True):
    st.switch_page("pages/7_✨_Stargazing.py")

st.sidebar.markdown("---")
st.sidebar.markdown("""
<div class="colored-code">
    <span class="code-keyword">print</span><span class="code-parenthesis">(</span><span class="code-string">"Hello Galaxy!"</span><span class="code-parenthesis">)</span>
</div>
""", unsafe_allow_html=True)
st.sidebar.markdown("---")
st.sidebar.markdown("### 🔗 Quick Links")
st.sidebar.markdown("[📧 Email Me](mailto:christinemaebanculo45@gmail.com)")
st.sidebar.markdown("[🐙 GitHub](https://github.com/Banculochristinemae)")
st.sidebar.markdown("[📘 Facebook](https://www.facebook.com/share/1DWzombwNQ/)")

# Display twinkling stars
st.markdown(generate_stars(), unsafe_allow_html=True)

# Main content
st.markdown('<div class="main-content">', unsafe_allow_html=True)
st.markdown('<h1 style="text-align:center; font-size:3rem; color:#ffffff;">✨ Welcome to Your Stargazing Corner ✨</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; font-size:1.2rem; color:#ffffff;">Take a deep breath... Look up at the stars... Let the universe embrace you.</p>', unsafe_allow_html=True)
st.markdown("---")


st.markdown("---")

# Celestial Objects
celestial_objects = {
    "☀️ Sun": {"key": "Sun", "type": "Yellow Dwarf Star", "age": "~4.6 billion years", "distance": "149.6 million km", "temperature": "~5,500°C", "size": "1,392,700 km diameter", "fact": "The Sun contains 99.86% of all mass in our solar system! It takes about 8 minutes for light to travel from the Sun to Earth."},
    "⭐ Sirius": {"key": "Sirius", "type": "Binary Star System", "age": "~242 million years", "distance": "8.6 light-years", "temperature": "~9,940°C", "size": "~1.7 times larger than Sun", "fact": "Sirius is the brightest star in Earth's night sky and has a white dwarf companion called Sirius B, about the size of Earth but as massive as our Sun!"},
    "🔴 Betelgeuse": {"key": "Betelgeuse", "type": "Red Supergiant", "age": "~8.5 million years", "distance": "640 light-years", "temperature": "~3,500°C", "size": "~1,400 times larger than Sun", "fact": "Betelgeuse is so massive that if placed at the center of our solar system, its surface would extend past Jupiter's orbit! It's expected to go supernova within 100,000 years."},
    "💙 Rigel": {"key": "Rigel", "type": "Blue Supergiant", "age": "~8 million years", "distance": "860 light-years", "temperature": "~12,100°C", "size": "~79 times larger than Sun", "fact": "Rigel shines with the intensity of 120,000 Suns and is actually a triple star system!"},
    "🌙 Moon": {"key": "Moon", "type": "Natural Satellite", "age": "~4.53 billion years", "distance": "384,400 km", "temperature": "-173°C to 127°C", "size": "3,474 km diameter", "fact": "The Moon is slowly moving away from Earth at about 3.8 cm per year - about the rate your fingernails grow! Only 12 people have ever walked on its surface."},
    "🪐 Saturn": {"key": "Saturn", "type": "Gas Giant Planet", "age": "~4.5 billion years", "distance": "1.2 billion km", "temperature": "-178°C", "size": "120,536 km diameter", "fact": "Saturn's rings are made almost entirely of water ice, ranging from tiny grains to house-sized chunks, but they're only about 30 feet thick! Saturn has 82 confirmed moons."},
    "🟤 Jupiter": {"key": "Jupiter", "type": "Gas Giant Planet", "age": "~4.5 billion years", "distance": "778 million km", "temperature": "-145°C", "size": "139,820 km diameter", "fact": "Jupiter's Great Red Spot is a storm that has been raging for over 400 years and is twice the size of Earth! Jupiter has 79 known moons."},
    "🌌 Milky Way": {"key": "Milky Way", "type": "Barred Spiral Galaxy", "age": "~13.6 billion years", "distance": "We're inside it!", "stars": "~100-400 billion stars", "size": "105,700 light-years across", "fact": "The Milky Way rotates once every 200 million years and contains over 100 billion planets. We can only see about 0.000004% of it with the naked eye!"},
    "🌀 Andromeda Galaxy": {"key": "Andromeda", "type": "Spiral Galaxy", "age": "~10 billion years", "distance": "2.537 million light-years", "stars": "~1 trillion stars", "size": "220,000 light-years across", "fact": "Andromeda will merge with our Milky Way in about 4.5 billion years to form a giant elliptical galaxy! It's the most distant object visible to the naked eye."},
    "✨ Orion Nebula": {"key": "Orion Nebula", "type": "Diffuse Nebula", "age": "~3 million years", "distance": "1,344 light-years", "temperature": "~10,000°C", "size": "24 light-years across", "fact": "It's a stellar nursery where new stars are being born! The Trapezium cluster in its center contains very young stars only about 300,000 years old."},
    "🌠 Pleiades": {"key": "Pleiades", "type": "Open Star Cluster", "age": "~100 million years", "distance": "444 light-years", "stars": "~1,000 stars", "size": "~12 light-years across", "fact": "Only 7 stars are visible to the naked eye - hence 'Seven Sisters'! In Japanese, it's called Subaru, which is why the car logo has six stars."}
}

if 'selected_object' not in st.session_state:
    st.session_state.selected_object = None

st.subheader("🌠 Click on any star, planet, or galaxy to see its realistic animated representation:")

# Create buttons in rows of 2
all_objects = list(celestial_objects.keys())
for i in range(0, len(all_objects), 2):
    cols = st.columns(2)
    for j in range(2):
        if i + j < len(all_objects):
            name = all_objects[i + j]
            with cols[j]:
                if st.button(f"{name}", key=name, use_container_width=True):
                    st.session_state.selected_object = name

st.markdown("---")

# Display selected object with animation and information side by side
if st.session_state.selected_object:
    obj = celestial_objects[st.session_state.selected_object]
    svg_data_url = get_animation_svg(obj["key"])
    
    info_html = f"""
    <div class="info-side">
        <h2 style="color:#ffffff;">{st.session_state.selected_object}</h2>
        <p style="color:#ffffff;"><strong>🌟 Type:</strong> {obj['type']}</p>
        <p style="color:#ffffff;"><strong>📅 Age:</strong> {obj['age']}</p>
        <p style="color:#ffffff;"><strong>📏 Distance:</strong> {obj['distance']}</p>
    """
    
    if 'temperature' in obj:
        info_html += f'<p style="color:#ffffff;"><strong>🌡️ Temperature:</strong> {obj["temperature"]}</p>'
    if 'size' in obj:
        info_html += f'<p style="color:#ffffff;"><strong>📐 Size:</strong> {obj["size"]}</p>'
    if 'stars' in obj:
        info_html += f'<p style="color:#ffffff;"><strong>⭐ Stars:</strong> {obj["stars"]}</p>'
    
    info_html += f"""
        <div class="info-fact">
            <strong style="color:#ffffff;">✨ Fascinating Fact:</strong><br>
            <span style="color:#ffffff;">{obj['fact']}</span>
        </div>
    </div>
    """
    
    st.markdown(f"""
    <div class="display-container">
        <div class="animation-side">
            <img src="{svg_data_url}" width="250" height="250" class="animation-img">
        </div>
        {info_html}
    </div>
    """, unsafe_allow_html=True)
    
else:
    st.markdown("""
    <div class="info-card" style="text-align:center;">
        <span style="font-size:3rem;">🔭</span>
        <h3 style="color:#ffffff;">Choose a celestial object above</h3>
        <p style="color:#ffffff;">Click on any star, planet, or galaxy to see its realistic animated representation and detailed information!</p>
        <p style="color:#ffffff; font-size:0.9rem;">✨ Each object has a unique, scientifically-inspired animation ✨</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Relaxing Facts Section
st.subheader("🌌 Relaxing Space Facts")

with st.expander("🌟 Stars"):
    st.markdown("""
    <span style="color:#ffffff;">- Stars are born in nebulae, giant clouds of gas and dust.</span><br>
    <span style="color:#ffffff;">- A star's color tells you its temperature: blue is hottest (30,000°C+), red is coolest (3,000°C).</span><br>
    <span style="color:#ffffff;">- The largest known star (UY Scuti) is over 1,700 times larger than our Sun!</span><br>
    <span style="color:#ffffff;">- When you look at stars, you're looking back in time because their light takes years to reach us.</span><br>
    <span style="color:#ffffff;">- A teaspoon of neutron star material would weigh about 10 million tons.</span>
    """, unsafe_allow_html=True)

with st.expander("🌙 The Moon"):
    st.markdown("""
    <span style="color:#ffffff;">- The Moon has moonquakes caused by Earth's gravitational pull.</span><br>
    <span style="color:#ffffff;">- Only 12 people have ever walked on the Moon.</span><br>
    <span style="color:#ffffff;">- The Moon has no atmosphere, so there's no wind or sound.</span><br>
    <span style="color:#ffffff;">- A day on the Moon lasts about 29.5 Earth days.</span><br>
    <span style="color:#ffffff;">- The Moon is about 4.5 billion years old - the same age as Earth!</span>
    """, unsafe_allow_html=True)

with st.expander("🌌 Galaxies"):
    st.markdown("""
    <span style="color:#ffffff;">- There are an estimated 100-200 billion galaxies in the observable universe.</span><br>
    <span style="color:#ffffff;">- The Milky Way and Andromeda are moving toward each other at 110 km/s.</span><br>
    <span style="color:#ffffff;">- Most galaxies have supermassive black holes at their centers.</span><br>
    <span style="color:#ffffff;">- Galaxies come in three shapes: spiral, elliptical, and irregular.</span><br>
    <span style="color:#ffffff;">- The Hubble Space Telescope has captured galaxies over 13 billion light-years away.</span>
    """, unsafe_allow_html=True)

with st.expander("🪐 Planets & Space"):
    st.markdown("""
    <span style="color:#ffffff;">- A day on Venus is longer than its year (243 Earth days vs 225 Earth days).</span><br>
    <span style="color:#ffffff;">- Jupiter's Great Red Spot is a storm that has been raging for over 400 years.</span><br>
    <span style="color:#ffffff;">- Saturn would float if placed in a bathtub - it's less dense than water!</span><br>
    <span style="color:#ffffff;">- Neptune has the strongest winds in the solar system, reaching 2,100 km/h.</span><br>
    <span style="color:#ffffff;">- There may be a 'Planet Nine' lurking in the outer solar system waiting to be discovered.</span>
    """, unsafe_allow_html=True)

st.markdown("---")


# Real-time Music Player Section
st.subheader("🎵 Relaxing Space Music")
st.markdown("""
<div class="info-card">
    <p>🌠 Click the play button on any track below to start listening immediately.</p>
</div>
""", unsafe_allow_html=True)

music_tracks = [
    {"name": "🌠 Deep Space Ambient", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"},
    {"name": "🎹 Peaceful Piano Dreams", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"},
    {"name": "🌌 Celestial Meditation", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"},
    {"name": "🎻 String Serenity", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3"},
    {"name": "🌙 Moonlight Sonata Style", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3"},
    {"name": "🚀 Interstellar Journey", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3"}
]

cols = st.columns(3)
for idx, track in enumerate(music_tracks):
    with cols[idx % 3]:
        st.markdown(f"""
        <div class="music-card">
            <h4 style="color:#ffffff;">{track['name']}</h4>
            <p style="color:#ffffff; font-size:0.8rem;">Click play to listen</p>
            <audio controls style="width:100%; margin-top:10px;">
                <source src="{track['url']}" type="audio/mpeg">
            </audio>
        </div>
        """, unsafe_allow_html=True)


cosmic_quotes = [
    "We are made of star-stuff. — Carl Sagan",
    "The cosmos is within us. — Carl Sagan",
    "Look up at the stars and not down at your feet. — Stephen Hawking",
    "The stars are the street lights of eternity. — unknown",
    "Somewhere, something incredible is waiting to be known. — Carl Sagan"
]
st.info(f"✨ *Cosmic Thought:* {random.choice(cosmic_quotes)}")

st.success("🌠 *Thank you for visiting the Stargazing Corner!*")

st.markdown('</div>', unsafe_allow_html=True)