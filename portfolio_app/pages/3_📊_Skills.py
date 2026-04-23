# pages/3_📊_Skills.py
import streamlit as st
import base64
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="Skills", page_icon="📊")

# Custom CSS for image modal (lightbox effect)
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
    
    .skill-card {
        background: rgba(15, 25, 45, 0.6);
        backdrop-filter: blur(8px);
        border-radius: 16px;
        border: 1px solid rgba(100, 150, 255, 0.25);
        padding: 20px;
        margin: 15px 0;
        transition: all 0.3s ease;
    }
    .skill-card:hover {
        transform: translateY(-3px);
        border-color: rgba(100, 150, 255, 0.8);
        box-shadow: 0 0 25px rgba(100, 150, 255, 0.5), 0 0 40px rgba(100, 150, 255, 0.2);
    }
    
    .creative-card {
        background: rgba(15, 25, 45, 0.5);
        backdrop-filter: blur(8px);
        border-radius: 12px;
        padding: 15px;
        text-align: center;
        margin: 8px;
        border: 1px solid rgba(100, 150, 255, 0.2);
        transition: all 0.3s;
        cursor: pointer;
    }
    .creative-card:hover {
        border-color: rgba(100, 150, 255, 0.8);
        transform: translateY(-3px);
        box-shadow: 0 0 20px rgba(100, 150, 255, 0.4), 0 0 30px rgba(100, 150, 255, 0.2);
    }
    
    /* Square image styling - original size */
    .creative-img {
        width: 100%;
        height: 120px;
        object-fit: cover;
        border-radius: 12px;
        margin-bottom: 10px;
        cursor: pointer;
        transition: transform 0.3s ease;
    }
    .creative-img:hover {
        transform: scale(1.02);
    }
    
    /* Modal/Lightbox styling for enlarged image */
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
    
    /* ALL TEXT PURE WHITE */
    .creative-card h4, .creative-card p, .skill-card p, .skill-card li, .skill-card ul {
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
    
    /* Title styling - matching About Me */
    .skills-title {
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        font-family: 'Courier New', monospace;
        background: linear-gradient(135deg, #e0e8ff, #a0b8ff);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        text-shadow: 0 0 20px rgba(100, 150, 255, 0.5);
        margin-bottom: 30px;
    }
    
    h1, h2, h3, h4 {
        color: #ffffff !important;
        font-family: 'Courier New', monospace;
    }
    p, li {
        color: #ffffff !important;
    }
    
    .stButton > button {
        background: rgba(30, 50, 80, 0.5);
        backdrop-filter: blur(8px);
        border-radius: 30px;
        border: 1px solid rgba(100, 150, 255, 0.4);
        color: #ffffff !important;
    }
    .stButton > button:hover {
        background: rgba(100, 150, 255, 0.35);
        border-color: rgba(150, 200, 255, 0.9);
        transform: translateY(-2px);
        box-shadow: 0 0 15px rgba(100, 150, 255, 0.3);
    }
    .stProgress > div > div {
        background: linear-gradient(90deg, #4a8cff, #7eb6ff) !important;
    }
    
    .stProgress label {
        color: #ffffff !important;
    }
    
    .streamlit-expanderHeader {
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
    
    // Close modal when clicking outside the image
    document.getElementById('imageModal').onclick = function(event) {
        if (event.target === this) {
            this.style.display = 'none';
        }
    }
    
    // Close modal with Escape key
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
st.markdown('<h1 class="skills-title">My Skills</h1>', unsafe_allow_html=True)

# Programming Languages
st.markdown("### 💻 Programming Languages")

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="skill-card">', unsafe_allow_html=True)
    st.markdown("**Python**")
    st.progress(40)
    st.markdown("**JavaScript**")
    st.progress(25)
    st.markdown("**C++**")
    st.progress(30)
    st.markdown("**C**")
    st.progress(30)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="skill-card">', unsafe_allow_html=True)
    st.markdown("**HTML**")
    st.progress(70)
    st.markdown("**CSS**")
    st.progress(75)
    st.markdown("**MySQL**")
    st.progress(50)
    st.markdown('</div>', unsafe_allow_html=True)

# Web Technologies
st.markdown("### 🌐 Web Technologies & Tools")

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="skill-card">', unsafe_allow_html=True)
    st.markdown("**Frontend**")
    st.write("- HTML5")
    st.write("- CSS3")
    st.write("- JavaScript (ES6+)")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="skill-card">', unsafe_allow_html=True)
    st.markdown("**Tools & Version Control**")
    st.write("- Git")
    st.write("- GitHub")
    st.write("- VS Code")
    st.write("- Canva")
    st.markdown('</div>', unsafe_allow_html=True)

# Other Skills Label
st.markdown("---")
st.markdown("### 🎨 Other Skills")
st.markdown("*Beyond programming, I also enjoy these creative crafts:*")

# Calligraphy
st.markdown("#### ✍️ Calligraphy")

st.markdown('<div class="skill-card">', unsafe_allow_html=True)
st.markdown("I create beautiful hand-lettered pieces for various occasions:")

col1, col2, col3, col4 = st.columns(4)

# Calligraphy items with images - ORIGINAL CONTAINER DESIGN
calligraphy_items = [
    {"icon": "🏷️", "title": "Name Tags", "desc": "Custom name tags", "img": "images/name_tag.png"},
    {"icon": "📖", "title": "Bookmarkers", "desc": "Hand-lettered bookmarks", "img": "images/bookmark.jpg"},
    {"icon": "💬", "title": "Quote Art", "desc": "Inspirational wall art", "img": "images/quote.jpg"},
    {"icon": "💌", "title": "Greeting Cards", "desc": "Custom greetings", "img": "images/greeting.jpg"}
]

for idx, item in enumerate(calligraphy_items):
    with [col1, col2, col3, col4][idx]:
        # Try to load image
        try:
            image = Image.open(item["img"])
            buffered = BytesIO()
            image.save(buffered, format="PNG" if item["img"].endswith('.png') else "JPEG")
            img_base64 = base64.b64encode(buffered.getvalue()).decode()
            mime = "image/png" if item["img"].endswith('.png') else "image/jpeg"
            img_src = f"data:{mime};base64,{img_base64}"
            img_html = f'<img src="{img_src}" class="creative-img" onclick="openModal(\'{img_src}\')">'
        except FileNotFoundError:
            img_html = f'<span style="font-size:3rem;">{item["icon"]}</span>'
        
        st.markdown(f"""
        <div class="creative-card">
            {img_html}
            <span style="font-size:2rem;">{item['icon']}</span>
            <h4 style="color:#ffffff;">{item['title']}</h4>
            <p style="font-size:0.7rem; color:#ffffff;">{item['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Crochet
st.markdown("#### 🧶 Crochet")

st.markdown('<div class="skill-card">', unsafe_allow_html=True)
st.markdown("Handmade crochet items created with love:")

col1, col2, col3, col4 = st.columns(4)

# Crochet items with images - ORIGINAL CONTAINER DESIGN
crochet_items = [
    {"icon": "🔑", "title": "Keychains", "desc": "Mini keychains", "img": "images/keychain.jpg"},
    {"icon": "🎀", "title": "Hair Accessories", "desc": "Headbands", "img": "images/hair_acc.jpg"},
    {"icon": "👜", "title": "Bags", "desc": "Tote and market bags", "img": "images/bag.jpg"},
    {"icon": "🎁", "title": "Custom Gifts", "desc": "Personalized crochet", "img": "images/custom_gift.jpg"}
]

for idx, item in enumerate(crochet_items):
    with [col1, col2, col3, col4][idx]:
        # Try to load image
        try:
            image = Image.open(item["img"])
            buffered = BytesIO()
            image.save(buffered, format="PNG" if item["img"].endswith('.png') else "JPEG")
            img_base64 = base64.b64encode(buffered.getvalue()).decode()
            mime = "image/png" if item["img"].endswith('.png') else "image/jpeg"
            img_src = f"data:{mime};base64,{img_base64}"
            img_html = f'<img src="{img_src}" class="creative-img" onclick="openModal(\'{img_src}\')">'
        except FileNotFoundError:
            img_html = f'<span style="font-size:3rem;">{item["icon"]}</span>'
        
        st.markdown(f"""
        <div class="creative-card">
            {img_html}
            <span style="font-size:2rem;">{item['icon']}</span>
            <h4 style="color:#ffffff;">{item['title']}</h4>
            <p style="font-size:0.7rem; color:#ffffff;">{item['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Currently Learning
st.markdown("---")
st.markdown("### 📚 Currently Learning")

st.markdown("""
<div class="skill-card">
<ul>
    <li>⚡ <strong>Django</strong> - Web framework for Python</li>
    <li>⚡ <strong>PHP</strong> - Server-side scripting language</li>
    <li>⚡ <strong>Facial Recognition API</strong> - AI/Computer vision integration</li>
</ul>
</div>
""", unsafe_allow_html=True)