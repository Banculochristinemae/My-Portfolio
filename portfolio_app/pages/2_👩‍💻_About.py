# pages/2_👩‍💻_About.py
import streamlit as st
import base64
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="About Me", page_icon="👩‍💻")

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
        width: 250px;
        height: 250px;
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
        box-shadow: 0 0 30px rgba(100, 150, 255, 0.7), 0 0 50px rgba(100, 150, 255, 0.3);
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
    
    /* About Me Title Styling */
    .about-title {
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        font-family: 'Courier New', monospace;
        background: linear-gradient(135deg, #e0e8ff, #a0b8ff);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        text-shadow: 0 0 20px rgba(100, 150, 255, 0.5);
        margin-bottom: 20px;
    }
    
    /* Quote styling */
    .quote-text {
        font-style: italic;
        font-size: 1.1rem;
        text-align: center;
        color: #c8d4f0 !important;
        border-left: 3px solid #7eb6ff;
        padding-left: 20px;
        margin: 20px 0;
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

# Center Top Photo Container with Image
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
    st.markdown("""
    <div class="photo-container">
        <div class="circle-photo">
            <div class="circle-photo-inner">
                <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100%;">
                    <span style="font-size:4rem;">👩‍💻</span>
                    <p><strong>Christine Mae</strong></p>
                    <p>BSCS - 3rd Year</p>
                    <p>DEBESMSCAT</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# About Me Title
st.markdown('<h1 class="about-title">About Me</h1>', unsafe_allow_html=True)

# Personal Story Card
st.markdown("""
<div class="about-card">
    <h3>✨ My Journey</h3>
    <p>I am <span class="highlight">Christine Mae C. Banculo</span>, currently taking a Bachelor of Science in Computer Science at <span class="highlight">Dr. Emilio B. Espinosa Sr. Memorial State College of Agriculture and Technology (DEBESMSCAT)</span>. I am a third-year student who may not be the best at programming yet, but I remain passionate and determined to learn.</p>
    <p>I once dreamed of becoming a software engineer because it sounded so cool. However, when I entered college, especially during my first year, I realized how challenging programming truly is. Still, I enjoy learning it, and I am committed to improving until I master it.</p>
    <p>During my free time, I love watching anime and K-dramas. I also enjoy listening to music, singing, dancing, crocheting, and doing calligraphy, which serves as my stress reliever.</p>
    <p>I am a person who treasures being with my family and friends. I love talking and laughing with them because they make me feel safe, comfortable, and truly belong. They are my strength and the reason I keep moving forward in life, and I am deeply grateful to have them.</p>
</div>
""", unsafe_allow_html=True)


# Education Section
st.markdown("""
<div class="card">
    <h3>🎓 Education</h3>
    <ul>
        <li><strong>Elementary:</strong> Baleno Central School - 2009 to 2017</li>
        <li><strong>Junior High School:</strong> Liceo de Baleno - 2017 to 2021</li>
        <li><strong>Senior High School:</strong> Liceo de Baleno - 2021 to 2023</li>
        <li><strong>College: </strong> DEBESMSCAT - 2023 to Present (BSCS)</li>
""", unsafe_allow_html=True)

# Career Goals
st.markdown("""
<div class="card">
    <h3>🎯 Career Goals</h3>
    <ul>
        <li> Become a <span class="highlight">Full Stack Developer</span></li>
        <li> Build scalable and efficient web applications</li>
        <li> Contribute to open-source projects</li>
        <li> Create tech solutions that benefit local communities</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Developer Statistics
st.markdown("""
<div class="card">
    <h3>📊 Developer Statistics</h3>
    <ul>
        <li>💻 Lines of code written: <strong>10,000+</strong></li>
        <li>📁 Major projects completed: <strong>4+</strong></li>
        <li>📜 Certifications earned: <strong>6</strong></li>
        <li>🐍 Primary language: <strong>Python</strong></li>
        <li>🌐 Web stack: <strong>HTML, CSS, JavaScript</strong></li>
        <li>🗄️ Databases: <strong>MySQL, Microsoft Access</strong></li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.subheader("📅 Development Journey")

timeline = {
    "2022": "Started BSCS at DEBESMSCAT · First 'Hello World!' program",
    "2023": "Hotel Management System · Fundamentals of Programming",
    "2024": "Math Game App · Database Projects · OOP Concepts",
    "2025": "Web Development · Photobooth App · Advanced Algorithms",
    "2026": "Graduation & Beyond! 🚀"
}

for year, event in timeline.items():
    st.markdown(f'<div class="timeline-item"><strong>{year}</strong> → {event}</div>', unsafe_allow_html=True)

st.info("💫 *\"The stars are the limit when you code with passion.\" — Christine Mae Banculo*")