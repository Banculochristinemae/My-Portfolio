# pages/4_📁_Projects.py
import streamlit as st
import base64
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="Projects", page_icon="📁")

# Custom CSS for image modal
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
    
    .project-card {
        background: rgba(15, 25, 45, 0.6);
        backdrop-filter: blur(8px);
        border-radius: 16px;
        border: 1px solid rgba(100, 150, 255, 0.25);
        padding: 20px;
        margin: 20px 0;
        transition: all 0.3s ease;
    }
    .project-card:hover {
        transform: translateY(-5px);
        border-color: rgba(100, 150, 255, 0.8);
        box-shadow: 0 0 25px rgba(100, 150, 255, 0.5), 0 0 40px rgba(100, 150, 255, 0.2);
    }
    
    .project-img-container {
        background: rgba(20, 30, 60, 0.6);
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        cursor: pointer;
        border: 1px solid rgba(100, 150, 255, 0.25);
        margin: 10px 0;
        transition: all 0.3s;
    }
    .project-img-container:hover {
        border-color: rgba(100, 150, 255, 0.9);
        transform: scale(1.02);
        box-shadow: 0 0 25px rgba(100, 150, 255, 0.5), 0 0 40px rgba(100, 150, 255, 0.2);
    }
    
    .project-img {
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-radius: 10px;
        cursor: pointer;
        transition: transform 0.3s ease;
    }
    .project-img:hover {
        transform: scale(1.02);
    }
    
    /* Modal/Lightbox styling */
    .modal {
        display: none;
        position: fixed;
        z-index: 9999;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0,0,0,0.95);
        backdrop-filter: blur(10px);
    }
    .modal-content {
        margin: auto;
        display: block;
        max-width: 80%;
        max-height: 80%;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        border-radius: 20px;
        box-shadow: 0 0 50px rgba(100,150,255,0.5);
    }
    .close {
        position: absolute;
        top: 20px;
        right: 35px;
        color: #ffffff;
        font-size: 40px;
        font-weight: bold;
        cursor: pointer;
        z-index: 10000;
        background: rgba(0,0,0,0.5);
        width: 50px;
        height: 50px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: 0.3s;
    }
    .close:hover {
        color: #ff8888;
        transform: scale(1.1);
    }
    
    .tech-tag {
        background: rgba(33, 38, 45, 0.8);
        color: #7eb6ff;
        padding: 3px 10px;
        border-radius: 15px;
        font-size: 0.75rem;
        display: inline-block;
        margin: 3px;
        border: 1px solid rgba(100, 150, 255, 0.3);
    }
    
    .description-box {
        background: rgba(10, 20, 40, 0.7);
        padding: 15px;
        border-radius: 10px;
        margin-top: 15px;
        border-left: 3px solid #7eb6ff;
        color: #ffffff !important;
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
    
    /* Projects Title - matching About Me */
    .projects-title {
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
    
    /* ===== SELECTBOX - BLACK TEXT FOR OPTIONS ===== */
    .stSelectbox div[data-baseweb="select"] div {
        color: #000000 !important;
        background-color: #ffffff !important;
    }
    .stSelectbox div[data-baseweb="select"] div:hover {
        background-color: #f0f0f0 !important;
    }
    .stSelectbox div[data-baseweb="select"] div[aria-selected="true"] {
        background-color: #e0e0e0 !important;
    }
    .stSelectbox ul {
        color: #000000 !important;
        background-color: #ffffff !important;
    }
    .stSelectbox li {
        color: #000000 !important;
    }
    .stSelectbox li:hover {
        background-color: #f0f0f0 !important;
    }
    
    /* Slider text white */
    .stSlider p, .stSlider label {
        color: #ffffff !important;
    }
    
    /* Selectbox label white */
    .stSelectbox label {
        color: #ffffff !important;
    }
</style>

<!-- Modal for enlarged images -->
<div id="imageModal" class="modal">
    <span class="close" onclick="document.getElementById('imageModal').style.display='none'">&times;</span>
    <img class="modal-content" id="modalImg">
</div>

<script>
    function openModal(imgSrc) {
        var modal = document.getElementById('imageModal');
        var modalImg = document.getElementById('modalImg');
        modal.style.display = 'block';
        modalImg.src = imgSrc;
    }
    
    document.getElementById('imageModal').onclick = function(event) {
        if (event.target === this) {
            this.style.display = 'none';
        }
    }
    
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape') {
            document.getElementById('imageModal').style.display = 'none';
        }
    });
</script>
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
st.markdown('<h1 class="projects-title">Projects</h1>', unsafe_allow_html=True)
st.markdown("*Click on any project image to reveal the description*")

# Initialize session states
if 'show_hotel' not in st.session_state:
    st.session_state.show_hotel = False
if 'show_math' not in st.session_state:
    st.session_state.show_math = False
if 'show_store' not in st.session_state:
    st.session_state.show_store = False
if 'show_photo' not in st.session_state:
    st.session_state.show_photo = False

# Helper function to load image
def load_image(img_path):
    try:
        image = Image.open(img_path)
        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        img_base64 = base64.b64encode(buffered.getvalue()).decode()
        return f"data:image/jpeg;base64,{img_base64}"
    except FileNotFoundError:
        return None

# Project 1 - Hotel Management System
with st.container():
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    col_img, col_info = st.columns([1, 1])
    with col_img:
        if st.button("🏨 Click to View Details", key="btn_hotel", use_container_width=True):
            st.session_state.show_hotel = not st.session_state.show_hotel
        
        img_src = load_image("images/HMS.jpg")
        if img_src:
            st.markdown(f'<div class="project-img-container"><img src="{img_src}" class="project-img" onclick="openModal(\'{img_src}\')"></div>', unsafe_allow_html=True)
        else:
            st.markdown("""<div class="project-img-container"><div class="project-placeholder">🏨<br>Hotel Management System</div></div>""", unsafe_allow_html=True)
        
        if st.session_state.show_hotel:
            st.markdown("""<div class="description-box"><strong>📝 Description:</strong><br>My first major project. Using Python, we created a system to manage hotel operations including booking, check-in/out, and customer records. Helped me understand programming logic and problem-solving.</div>""", unsafe_allow_html=True)
    with col_info:
        st.markdown("### 🏨 Hotel Management System")
        st.markdown("*Case Study 1 | 2nd Semester*")
        st.markdown("**Technologies:** " + '<span class="tech-tag">Python</span> <span class="tech-tag">File I/O</span>', unsafe_allow_html=True)
        st.markdown("**Key Features:** Booking management, customer database, billing system")
    st.markdown('</div>', unsafe_allow_html=True)

# Project 2 - Math Game
with st.container():
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    col_img, col_info = st.columns([1, 1])
    with col_img:
        if st.button("🎮 Click to View Details", key="btn_math", use_container_width=True):
            st.session_state.show_math = not st.session_state.show_math
        
        img_src = load_image("images/math_game.jpg")
        if img_src:
            st.markdown(f'<div class="project-img-container"><img src="{img_src}" class="project-img" onclick="openModal(\'{img_src}\')"></div>', unsafe_allow_html=True)
        else:
            st.markdown("""<div class="project-img-container"><div class="project-placeholder">🎮<br>Math Game</div></div>""", unsafe_allow_html=True)
        
        if st.session_state.show_math:
            st.markdown("""<div class="description-box"><strong>📝 Description:</strong><br>A mobile app that makes learning math fun! Users solve problems to earn points and unlock trivia questions as rewards.</div>""", unsafe_allow_html=True)
    with col_info:
        st.markdown("### 🎮 Math Game")
        st.markdown("*Case Study 2 | Mobile App*")
        st.markdown("**Technologies:** " + '<span class="tech-tag">Mobile Dev</span> <span class="tech-tag">Game Logic</span>', unsafe_allow_html=True)
        st.markdown("**Key Features:** Progressive difficulty, reward system, trivia integration")
    st.markdown('</div>', unsafe_allow_html=True)

# Project 3 - Store Management System
with st.container():
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    col_img, col_info = st.columns([1, 1])
    with col_img:
        if st.button("🏪 Click to View Details", key="btn_store", use_container_width=True):
            st.session_state.show_store = not st.session_state.show_store
        
        img_src = load_image("images/SMS.jpg")
        if img_src:
            st.markdown(f'<div class="project-img-container"><img src="{img_src}" class="project-img" onclick="openModal(\'{img_src}\')"></div>', unsafe_allow_html=True)
        else:
            st.markdown("""<div class="project-img-container"><div class="project-placeholder">🏪<br>Store Management System</div></div>""", unsafe_allow_html=True)
        
        if st.session_state.show_store:
            st.markdown("""<div class="description-box"><strong>📝 Description:</strong><br>Database project using MS Access to track inventory, sales, and customer records. Gained experience with relational databases and SQL queries.</div>""", unsafe_allow_html=True)
    with col_info:
        st.markdown("### 🏪 Store Management System")
        st.markdown("*Database Project*")
        st.markdown("**Technologies:** " + '<span class="tech-tag">MS Access</span> <span class="tech-tag">SQL</span>', unsafe_allow_html=True)
        st.markdown("**Key Features:** Inventory management, sales reports, customer database")
    st.markdown('</div>', unsafe_allow_html=True)

# Project 4 - Photobooth Web App
with st.container():
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    col_img, col_info = st.columns([1, 1])
    with col_img:
        if st.button("📸 Click to View Details", key="btn_photo", use_container_width=True):
            st.session_state.show_photo = not st.session_state.show_photo
        
        img_src = load_image("images/photobooth.jpg")
        if img_src:
            st.markdown(f'<div class="project-img-container"><img src="{img_src}" class="project-img" onclick="openModal(\'{img_src}\')"></div>', unsafe_allow_html=True)
        else:
            st.markdown("""<div class="project-img-container"><div class="project-placeholder">📸<br>Photobooth Web App</div></div>""", unsafe_allow_html=True)
        
        if st.session_state.show_photo:
            st.markdown("""<div class="description-box"><strong>📝 Description:</strong><br>Web app where users can take and customize photos with filters, photostrip designs, and save images. Improved my HTML/CSS/JS skills.</div>""", unsafe_allow_html=True)
    with col_info:
        st.markdown("### 📸 Photobooth Web App")
        st.markdown("*Case Study 3 | Web Development*")
        st.markdown("**Technologies:** " + '<span class="tech-tag">HTML5</span> <span class="tech-tag">CSS3</span> <span class="tech-tag">JavaScript</span>', unsafe_allow_html=True)
        st.markdown("**Key Features:** Real-time filters, photostrip customization, image saving")
    st.markdown('</div>', unsafe_allow_html=True)

# Feedback
st.markdown("---")
st.subheader("⭐ Rate My Projects")

selected = st.selectbox("Which project impressed you the most?", ["Hotel Management System", "Math Game", "Store Management System", "Photobooth Web App"])
rating = st.slider("Rate this project (1-5 stars)", 1, 5, 3)

if st.button("Submit Rating", type="primary"):
    st.success(f"Thanks for rating {selected} with {'⭐' * rating}!")