# Home.py
import streamlit as st
import base64
from PIL import Image
from io import BytesIO

# Page configuration - MUST be first Streamlit command
st.set_page_config(
    page_title="Christine Mae Banculo | Galaxy Portfolio",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Galaxy Theme with Hover-Only Glow Effects
st.markdown("""
<style>
    .stApp {
        background: radial-gradient(ellipse at center, #0a0f2a 0%, #060914 100%);
        background-attachment: fixed;
    }
    
    /* HIDE DEFAULT STREAMLIT NAVIGATION */
    [data-testid="stSidebarNav"] {
        display: none !important;
    }
    
    [data-testid="stSidebar"] {
        background: rgba(5, 10, 25, 0.85);
        backdrop-filter: blur(12px);
        border-right: 1px solid rgba(100, 150, 255, 0.3);
    }
    
    /* Cards - Glow on Hover Only */
    .card, .about-card {
        background: rgba(15, 25, 45, 0.6);
        backdrop-filter: blur(8px);
        border-radius: 16px;
        border: 1px solid rgba(100, 150, 255, 0.25);
        padding: 24px;
        margin: 15px 0;
        transition: all 0.3s ease;
    }
    .card:hover, .about-card:hover {
        transform: translateY(-5px);
        border-color: rgba(100, 150, 255, 0.8);
        box-shadow: 0 0 25px rgba(100, 150, 255, 0.5), 0 0 40px rgba(100, 150, 255, 0.2);
    }
    
    /* Photo Container - BIGGER CIRCLE with Glow on Hover Only */
    .photo-container {
        display: flex;
        justify-content: center;
        margin: 20px 0 30px 0;
    }
    .circle-photo {
        width: 320px;
        height: 320px;
        border-radius: 50%;
        background: linear-gradient(135deg, rgba(100, 150, 255, 0.4), rgba(150, 100, 255, 0.4));
        display: flex;
        align-items: center;
        justify-content: center;
        border: 3px solid rgba(100, 150, 255, 0.5);
        box-shadow: 0 0 10px rgba(100, 150, 255, 0.2);
        transition: all 0.3s ease;
        overflow: hidden;
    }
    .circle-photo:hover {
        transform: scale(1.02);
        border-color: rgba(100, 150, 255, 0.9);
        box-shadow: 0 0 35px rgba(100, 150, 255, 0.8), 0 0 60px rgba(100, 150, 255, 0.4);
    }
    .circle-photo-inner {
        width: 100%;
        height: 100%;
        border-radius: 50%;
        overflow: hidden;
    }
    .circle-photo-inner img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
            
    /* Cards - Glow on Hover Only */
    .card {
        background: rgba(15, 25, 45, 0.6);
        backdrop-filter: blur(8px);
        border-radius: 16px;
        border: 1px solid rgba(100, 150, 255, 0.25);
        padding: 24px;
        margin: 15px 0;
        transition: all 0.3s ease;
    }
    .card:hover {
        transform: translateY(-5px);
        border-color: rgba(100, 150, 255, 0.8);
        box-shadow: 0 0 25px rgba(100, 150, 255, 0.5), 0 0 40px rgba(100, 150, 255, 0.2);
    }
    
    /* Stats Cards - Glow on Hover Only */
    .stats-card {
        background: rgba(20, 30, 60, 0.6);
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        border: 1px solid rgba(100, 150, 255, 0.25);
        transition: all 0.3s ease;
    }
    .stats-card:hover {
        transform: translateY(-3px);
        border-color: rgba(100, 150, 255, 0.8);
        box-shadow: 0 0 20px rgba(100, 150, 255, 0.5), 0 0 30px rgba(100, 150, 255, 0.2);
    }
    
    /* Timeline Items - WHITE TEXT */
    .timeline-item {
        background: rgba(10, 20, 40, 0.7);
        padding: 12px;
        border-radius: 10px;
        margin: 8px 0;
        border-left: 3px solid #7eb6ff;
        transition: all 0.3s ease;
        color: #ffffff !important;
    }
    .timeline-item strong, .timeline-item span {
        color: #ffffff !important;
    }
    .timeline-item:hover {
        border-left: 3px solid #aaccff;
        box-shadow: 0 0 15px rgba(100, 150, 255, 0.3);
        transform: translateX(5px);
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
    
    h1, h2, h3 {
        color: #e0e8ff !important;
        font-family: 'Courier New', monospace;
    }
    p, li {
        color: #c8d4f0 !important;
    }
    .highlight {
        color: #7eb6ff !important;
        font-weight: bold;
    }
    .stButton > button {
        background: rgba(30, 50, 80, 0.5);
        backdrop-filter: blur(8px);
        border-radius: 30px;
        border: 1px solid rgba(100, 150, 255, 0.4);
        color: #e0e8ff !important;
    }
    .stButton > button:hover {
        background: rgba(100, 150, 255, 0.35);
        border-color: rgba(150, 200, 255, 0.9);
        transform: translateY(-2px);
        box-shadow: 0 0 15px rgba(100, 150, 255, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation - EXACTLY SAME as other pages
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

# Colored print statement in sidebar
st.sidebar.markdown("""
<div class="colored-code">
    <span class="code-keyword">print</span><span class="code-parenthesis">(</span><span class="code-string">"Hello World!"</span><span class="code-parenthesis">)</span>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🔗 Quick Links")
st.sidebar.markdown("[📧 Email Me](mailto:christinemaebanculo45@gmail.com)")
st.sidebar.markdown("[🐙 GitHub](https://github.com/Banculochristinemae)")
st.sidebar.markdown("[📘 Facebook](https://www.facebook.com/share/1DWzombwNQ/)")

# Load image and convert to base64
try:
    image = Image.open("images/ID.png")
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode()
    image_loaded = True
except FileNotFoundError:
    image_loaded = False

# Main content for Home
# Center Top Photo Container - BIGGER CIRCLE with image
if image_loaded:
    st.markdown(f"""
    <div class="photo-container">
        <div class="circle-photo">
            <div class="circle-photo-inner">
                <img src="data:image/png;base64,{img_base64}" alt="Christine Mae">
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
else:
    # Fallback to emoji if image not found
    st.markdown("""
    <div class="photo-container">
        <div class="circle-photo">
            <div class="circle-photo-inner">
                <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100%;">
                    <span style="font-size:4rem;">👩‍💻</span>
                    <p><strong>Christine Mae</strong></p>
                    <p class="small-text">BSCS - 3rd Year</p>
                    <p class="small-text">DEBESMSCAT</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.info("📸 **Tip:** Make sure 'images/ID.png' exists in the images folder to display your photo!")

st.markdown('<p style="font-size:2.5rem; color:#e0e8ff; text-align:center; font-family: monospace; text-shadow: 0 0 10px rgba(100,150,255,0.4);">🌌 Christine Mae C. Banculo</p>', unsafe_allow_html=True)
st.markdown('<p style="font-size:1.2rem; color:#a8b8e0; text-align:center; margin-bottom: 30px;">Third Year Computer Science Student | Aspiring Full Stack Developer</p>', unsafe_allow_html=True)

# Welcome Card
st.markdown("""
<div class="card">
    <h3>🚀 Welcome to My Portfolio</h3>
    <p>Hi! I'm <span class="highlight">Christine Mae C. Banculo</span>, a passionate Computer Science student 
    at Dr. Emilio B. Espinosa Sr. Memorial State College of Agriculture and Technology</span> <span class="highlight">(DEBESMSCAT).</p>
    <p>I love turning ideas into functional, efficient, and user-friendly applications through clean code 
    and creative problem-solving. Programming is not just a subject for me — it's a passion that allows me 
    to create solutions that make a difference.</p>
    <p>This portfolio showcases my journey as a developer, my technical projects, skills, certifications, 
    and creative work.</p>
</div>
""", unsafe_allow_html=True)

# Quick Stats Row
st.markdown("---")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="stats-card">
        <span style="font-size:2rem;">🎓</span>
        <h3>3rd Year</h3>
        <p>BSCS Student</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stats-card">
        <span style="font-size:2rem;">💻</span>
        <h3>4+</h3>
        <p>Major Projects</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stats-card">
        <span style="font-size:2rem;">📜</span>
        <h3>6</h3>
        <p>Certifications</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="stats-card">
        <span style="font-size:2rem;">🔧</span>
        <h3>7</h3>
        <p>Languages/Tools</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("### 💫 Developer Quote")
st.code("""
> "The stars are the limit when you code with passion."
> — Christine Mae Banculo
""", language="bash")

st.success("✨ Use the sidebar navigation to explore my galaxy portfolio! Need a to take a break? Try the Stargazing page! 🌙")