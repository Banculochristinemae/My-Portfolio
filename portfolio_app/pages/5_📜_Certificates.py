# pages/5_📜_Certificates.py
import streamlit as st
import base64

st.set_page_config(page_title="Certificates", page_icon="📜")

st.markdown("""
<style>
    .stApp {
        background: radial-gradient(ellipse at center, #0a0f2a 0%, #060914 100%);
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
    
    .cert-card {
        background: rgba(15, 25, 45, 0.6);
        backdrop-filter: blur(8px);
        border-radius: 16px;
        border: 1px solid rgba(100, 150, 255, 0.25);
        padding: 20px;
        margin: 15px;
        text-align: center;
        transition: all 0.3s ease;
        cursor: pointer;
        height: 100%;
    }
    .cert-card:hover {
        transform: translateY(-5px);
        border-color: rgba(100, 150, 255, 0.8);
        box-shadow: 0 0 25px rgba(100, 150, 255, 0.5), 0 0 40px rgba(100, 150, 255, 0.2);
    }
    
    /* Certificate image styling */
    .cert-img {
        width: 100%;
        height: 140px;
        object-fit: contain;
        border-radius: 10px;
        margin-bottom: 10px;
        cursor: pointer;
        transition: transform 0.3s ease;
    }
    .cert-img:hover {
        transform: scale(1.05);
    }
    
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
    
    /* Certificates Title - matching About Me */
    .certificates-title {
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
    
    /* Full size image container - ABOVE certificates */
    .fullsize-container {
        background: rgba(0, 0, 0, 0.95);
        backdrop-filter: blur(10px);
        padding: 25px;
        border-radius: 20px;
        margin: 20px 0;
        text-align: center;
        border: 2px solid rgba(100, 150, 255, 0.5);
        animation: fadeIn 0.3s ease;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: scale(0.95); }
        to { opacity: 1; transform: scale(1); }
    }
    
    .fullsize-img {
        max-width: 100%;
        max-height: 60vh;
        border-radius: 10px;
        box-shadow: 0 0 40px rgba(100,150,255,0.4);
    }
    
    .fullsize-title {
        color: #ffd700;
        font-size: 1.5rem;
        margin-bottom: 15px;
        font-family: 'Courier New', monospace;
    }
    
    h1, h2, h3 {
        color: #e0e8ff !important;
        font-family: 'Courier New', monospace;
    }
    p, li {
        color: #c8d4f0 !important;
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
    
    /* Dropdown - Black Text */
    .stSelectbox div[data-baseweb="select"] div {
        color: #000000 !important;
        background-color: #ffffff !important;
    }
    .stSelectbox div[data-baseweb="select"] div:hover {
        background-color: #f0f0f0 !important;
    }
    .stSelectbox ul {
        color: #000000 !important;
        background-color: #ffffff !important;
    }
    .stSelectbox li {
        color: #000000 !important;
    }
    
    .stSelectbox label {
        color: #ffffff !important;
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

# New Title
st.markdown('<h1 class="certificates-title">Certificates</h1>', unsafe_allow_html=True)
st.markdown("*I have earned professional certifications to validate my technical knowledge*")

# Stats Cards
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""<div class="stats-card"><span style="font-size:3rem;">📜</span><h1 style="color:#7eb6ff; font-size:2.5rem;">6</h1><p>Total Certifications</p></div>""", unsafe_allow_html=True)
with col2:
    st.markdown("""<div class="stats-card"><span style="font-size:3rem;">🐍</span><h1 style="color:#7eb6ff; font-size:2.5rem;">3</h1><p>Python Courses</p></div>""", unsafe_allow_html=True)
with col3:
    st.markdown("""<div class="stats-card"><span style="font-size:3rem;">🔒🤖</span><h1 style="color:#7eb6ff; font-size:2.5rem;">2</h1><p>Security/AI</p></div>""", unsafe_allow_html=True)

st.markdown("---")

# Helper function to load image and return base64
def get_image_base64(img_path):
    try:
        with open(img_path, "rb") as img_file:
            img_data = img_file.read()
            img_base64 = base64.b64encode(img_data).decode()
            if img_path.endswith('.png'):
                return f"data:image/png;base64,{img_base64}"
            else:
                return f"data:image/jpeg;base64,{img_base64}"
    except FileNotFoundError:
        return None

# Certificate data
certificates_data = [
    {"img": "images/Cisco_CSS.png", "icon": "🎨", "title": "CSS Essentials", "type": "Web Dev", "desc": "CSS styling, responsive design"},
    {"img": "images/Cisco_py.png", "icon": "🐍", "title": "Python Essential 1", "type": "Python", "desc": "Python fundamentals"},
    {"img": "images/intro_to_AI.png", "icon": "🤖", "title": "Introduction to AI", "type": "AI", "desc": "AI/ML concepts"},
    {"img": "images/Cyber_sec.png", "icon": "🔒", "title": "Intro to Cyber Security", "type": "Security", "desc": "Security fundamentals"},
    {"img": "images/python.png", "icon": "🐍", "title": "Python for Beginners", "type": "Python", "desc": "Python basics"},
    {"img": "images/django.png", "icon": "🌐", "title": "Python Django 101", "type": "Python", "desc": "Django framework"}
]

# Session state to track which certificate is being viewed
if 'show_fullsize' not in st.session_state:
    st.session_state.show_fullsize = False
if 'fullsize_img' not in st.session_state:
    st.session_state.fullsize_img = None
if 'fullsize_title' not in st.session_state:
    st.session_state.fullsize_title = None

# DISPLAY FULL SIZE CERTIFICATE ABOVE THE LIST (if selected)
if st.session_state.show_fullsize and st.session_state.fullsize_img:
    st.markdown(f"""
    <div class="fullsize-container">
        <div class="fullsize-title">📄 {st.session_state.fullsize_title}</div>
        <div>
            <img src="{st.session_state.fullsize_img}" class="fullsize-img">
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("❌ Close Certificate View", use_container_width=True):
            st.session_state.show_fullsize = False
            st.session_state.fullsize_img = None
            st.session_state.fullsize_title = None
            st.rerun()
    
    st.markdown("---")

# My Certificates Section
st.subheader("📜 My Certificates")
st.markdown("*Click 'View Certificate' below any certificate to see it full size*")

# Display certificates in 2 rows of 3 columns
for row_start in range(0, len(certificates_data), 3):
    cols = st.columns(3)
    for idx, col in enumerate(cols):
        cert_idx = row_start + idx
        if cert_idx < len(certificates_data):
            cert = certificates_data[cert_idx]
            img_src = get_image_base64(cert["img"])
            
            if img_src:
                with col:
                    # Certificate card
                    st.markdown(f"""
                    <div class="cert-card">
                        <img src="{img_src}" class="cert-img">
                        <div style="font-size:3rem;">{cert['icon']}</div>
                        <h3>{cert['title']}</h3>
                        <p><span style="background:rgba(100,150,255,0.3); padding:3px 10px; border-radius:20px;">{cert['type']}</span></p>
                        <p style="font-size:0.8rem;">{cert['desc']}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # View button
                    if st.button(f"🔍 View Certificate", key=f"view_btn_{cert_idx}"):
                        st.session_state.show_fullsize = True
                        st.session_state.fullsize_img = img_src
                        st.session_state.fullsize_title = cert['title']
                        st.rerun()
            else:
                with col:
                    st.markdown(f"""
                    <div class="cert-card">
                        <div style="font-size:3rem;">{cert['icon']}</div>
                        <h3>{cert['title']}</h3>
                        <p><span style="background:rgba(100,150,255,0.3); padding:3px 10px; border-radius:20px;">{cert['type']}</span></p>
                        <p style="font-size:0.8rem;">{cert['desc']}</p>
                    </div>
                    """, unsafe_allow_html=True)

# Summary
st.markdown("---")
st.subheader("📊 Certification Summary")
st.markdown("""
<div class="stats-card" style="text-align:left;">
    <ul>
        <li>🐍 <strong>Python Courses:</strong> Python Essential 1, Python for Beginners, Python Django 101 (3)</li>
        <li>🔒 <strong>Security:</strong> Introduction to Cyber Security (1)</li>
        <li>🤖 <strong>AI:</strong> Introduction to Artificial Intelligence (1)</li>
        <li>🎨 <strong>Web Dev:</strong> CSS Essentials (1)</li>
    </ul>
    <p><strong>Total: 6 Certifications</strong></p>
</div>
""", unsafe_allow_html=True)

# Interactive
st.markdown("---")
st.subheader("🔍 Explore a Certification")
cert_titles = [c['title'] for c in certificates_data]
selected_cert = st.selectbox("Select a certification:", cert_titles)
cert_details = {
    "CSS Essentials": "CSS styling, responsive design, flexbox, grid layouts.",
    "Python Essential 1": "Variables, data types, loops, functions, data structures.",
    "Introduction to AI": "Machine learning, neural networks, NLP, computer vision.",
    "Intro to Cyber Security": "Threat detection, encryption, network security.",
    "Python for Beginners": "Syntax, problem-solving, basic algorithms.",
    "Python Django 101": "Models, views, templates, URL routing, databases."
}
if selected_cert:
    st.info(f"📘 **{selected_cert}:** {cert_details.get(selected_cert, 'Certification details available upon request.')}")

st.success("💫 *Each certification represents dedicated learning and practice!*")