# pages/6_📞_Contact.py
import streamlit as st
import re

st.set_page_config(page_title="Contact", page_icon="📞")

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
    
    .contact-card {
        background: rgba(15, 25, 45, 0.6);
        backdrop-filter: blur(8px);
        border-radius: 16px;
        border: 1px solid rgba(100, 150, 255, 0.25);
        padding: 20px;
        margin: 15px 0;
        transition: all 0.3s ease;
    }
    .contact-card:hover {
        transform: translateY(-5px);
        border-color: rgba(100, 150, 255, 0.8);
        box-shadow: 0 0 25px rgba(100, 150, 255, 0.5), 0 0 40px rgba(100, 150, 255, 0.2);
    }
    
    .social-btn {
        display: inline-block;
        background: rgba(33, 38, 45, 0.7);
        backdrop-filter: blur(5px);
        color: #c9d1d9;
        padding: 12px 25px;
        margin: 10px;
        border-radius: 30px;
        text-decoration: none;
        border: 1px solid rgba(100, 150, 255, 0.3);
        transition: 0.2s;
    }
    .social-btn:hover {
        border-color: #7eb6ff;
        color: #7eb6ff;
        background: rgba(100, 150, 255, 0.2);
        box-shadow: 0 0 15px rgba(100, 150, 255, 0.3);
        transform: scale(1.02);
    }
    
    .faq-humble {
        background: rgba(10, 20, 40, 0.7);
        padding: 15px;
        border-radius: 15px;
        margin: 10px 0;
        border-left: 3px solid #7eb6ff;
        color: #c8d4f0 !important;
        transition: all 0.3s ease;
    }
    .faq-humble:hover {
        border-left: 3px solid #aaccff;
        box-shadow: 0 0 10px rgba(100, 150, 255, 0.3);
    }
    
    /* Contact Me Title - matching About Me */
    .contact-title {
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
    
    /* UFO Animation */
    @keyframes flyUFO {
        0% {
            transform: translateX(-200px) translateY(0px);
            opacity: 0;
        }
        10% {
            opacity: 1;
        }
        90% {
            opacity: 1;
        }
        100% {
            transform: translateX(calc(100vw + 200px)) translateY(-80px);
            opacity: 0;
        }
    }
    
    .ufo-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 9999;
        overflow: visible;
    }
    
    .ufo {
        position: absolute;
        animation: flyUFO 2s ease-in-out forwards;
        filter: drop-shadow(0 0 15px rgba(0, 255, 100, 0.6));
    }
    
    .ufo-body {
        width: 70px;
        height: 25px;
        border-radius: 50%;
        position: relative;
    }
    .ufo-dome {
        position: absolute;
        top: -12px;
        left: 20px;
        width: 25px;
        height: 17px;
        border-radius: 50% 50% 40% 40%;
    }
    .ufo-light {
        position: absolute;
        width: 5px;
        height: 5px;
        border-radius: 50%;
        bottom: -4px;
        animation: blink 0.3s infinite alternate;
    }
    .light1 { left: 8px; animation-delay: 0s; }
    .light2 { left: 20px; animation-delay: 0.1s; }
    .light3 { left: 32px; animation-delay: 0.2s; }
    .light4 { left: 44px; animation-delay: 0.15s; }
    .light5 { left: 56px; animation-delay: 0.25s; }
    
    @keyframes blink {
        0% { opacity: 0.3; box-shadow: 0 0 2px currentColor; }
        100% { opacity: 1; box-shadow: 0 0 10px currentColor, 0 0 15px currentColor; }
    }
    
    .ufo-beam {
        position: absolute;
        bottom: -20px;
        left: 25px;
        width: 15px;
        height: 0;
        border-radius: 0 0 8px 8px;
        animation: beamPulse 0.4s infinite alternate;
    }
    
    @keyframes beamPulse {
        0% { height: 0px; opacity: 0; }
        100% { height: 35px; opacity: 0.7; }
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
    .stTextInput > div > div > input, .stTextArea > div > div > textarea, .stSelectbox > div > div {
        background: rgba(10, 20, 40, 0.7);
        color: #e0e8ff !important;
        border-radius: 10px;
        border: 1px solid rgba(100, 150, 255, 0.3);
    }
    /* Dropdown - Black Text */
    .stSelectbox div[data-baseweb="select"] div {
        color: #000000 !important;
        background-color: #ffffff !important;
    }
</style>
""", unsafe_allow_html=True)

# Function to trigger 3 UFOs with different colors
def trigger_ufos():
    ufos_html = """
    <div class="ufo-container" id="ufoContainer">
        <!-- Pink UFO -->
        <div class="ufo" style="top: 25%; animation-delay: 0s; animation-duration: 2s;">
            <div class="ufo-body" style="background: linear-gradient(135deg, #ff69b4, #ff99cc); box-shadow: 0 0 20px rgba(255,105,180,0.6);">
                <div class="ufo-dome" style="background: linear-gradient(135deg, #ffccdd, #ff99bb); box-shadow: inset 0 2px 5px rgba(255,255,255,0.5), 0 0 10px rgba(255,105,180,0.8);"></div>
                <div class="ufo-beam" style="background: linear-gradient(180deg, rgba(255,105,180,0.6), rgba(255,105,180,0));"></div>
                <div class="ufo-light light1" style="background: #ff1493; color: #ff1493;"></div>
                <div class="ufo-light light2" style="background: #ff69b4; color: #ff69b4;"></div>
                <div class="ufo-light light3" style="background: #ff1493; color: #ff1493;"></div>
                <div class="ufo-light light4" style="background: #ff69b4; color: #ff69b4;"></div>
                <div class="ufo-light light5" style="background: #ff1493; color: #ff1493;"></div>
            </div>
        </div>
        <!-- Purple UFO -->
        <div class="ufo" style="top: 45%; animation-delay: 1s; animation-duration: 2s;">
            <div class="ufo-body" style="background: linear-gradient(135deg, #9b59b6, #bb8fce); box-shadow: 0 0 20px rgba(155,89,182,0.6);">
                <div class="ufo-dome" style="background: linear-gradient(135deg, #dcc6f0, #c39bd3); box-shadow: inset 0 2px 5px rgba(255,255,255,0.5), 0 0 10px rgba(155,89,182,0.8);"></div>
                <div class="ufo-beam" style="background: linear-gradient(180deg, rgba(155,89,182,0.6), rgba(155,89,182,0));"></div>
                <div class="ufo-light light1" style="background: #8e44ad; color: #8e44ad;"></div>
                <div class="ufo-light light2" style="background: #9b59b6; color: #9b59b6;"></div>
                <div class="ufo-light light3" style="background: #8e44ad; color: #8e44ad;"></div>
                <div class="ufo-light light4" style="background: #9b59b6; color: #9b59b6;"></div>
                <div class="ufo-light light5" style="background: #8e44ad; color: #8e44ad;"></div>
            </div>
        </div>
        <!-- Green UFO -->
        <div class="ufo" style="top: 65%; animation-delay: 2s; animation-duration: 2s;">
            <div class="ufo-body" style="background: linear-gradient(135deg, #2ecc71, #6fcf97); box-shadow: 0 0 20px rgba(46,204,113,0.6);">
                <div class="ufo-dome" style="background: linear-gradient(135deg, #a9dfbf, #7dcea0); box-shadow: inset 0 2px 5px rgba(255,255,255,0.5), 0 0 10px rgba(46,204,113,0.8);"></div>
                <div class="ufo-beam" style="background: linear-gradient(180deg, rgba(46,204,113,0.6), rgba(46,204,113,0));"></div>
                <div class="ufo-light light1" style="background: #27ae60; color: #27ae60;"></div>
                <div class="ufo-light light2" style="background: #2ecc71; color: #2ecc71;"></div>
                <div class="ufo-light light3" style="background: #27ae60; color: #27ae60;"></div>
                <div class="ufo-light light4" style="background: #2ecc71; color: #2ecc71;"></div>
                <div class="ufo-light light5" style="background: #27ae60; color: #27ae60;"></div>
            </div>
        </div>
    </div>
    <script>
        setTimeout(() => {
            const container = document.getElementById('ufoContainer');
            if (container) {
                setTimeout(() => {
                    container.remove();
                }, 100);
            }
        }, 4100);
    </script>
    """
    return ufos_html

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

# New Title - Contact Me
st.markdown('<h1 class="contact-title">Contact Me</h1>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""<div class="contact-card"><h3>📧 Send a Message</h3><p>Have a project idea, want to collaborate, or interested in my creative work? Reach out!</p></div>""", unsafe_allow_html=True)
    
    with st.form("contact_form"):
        name = st.text_input("Name *", placeholder="Enter your full name")
        email = st.text_input("Email *", placeholder="your.email@example.com")
        subject = st.selectbox("Subject", ["Programming Project", "Calligraphy/Crochet", "Collaboration", "Internship", "General", "Feedback"])
        message = st.text_area("Message *", placeholder="Type your message...", height=150)
        
        submitted = st.form_submit_button("Send Message", use_container_width=True)
        
        if submitted:
            if name and email and message:
                if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
                    st.markdown(trigger_ufos(), unsafe_allow_html=True)
                    st.success(f"✅ Thank you {name}! I'll reply to {email} within 48 hours.")
                else:
                    st.error("❌ Please enter a valid email.")
            else:
                st.error("❌ Please fill all required fields.")

with col2:
    st.markdown("""<div class="contact-card"><h3>🔗 Connect With Me</h3></div>""", unsafe_allow_html=True)
    st.markdown('<a href="https://github.com/Banculochristinemae" target="_blank"><div class="social-btn">🐙 GitHub: /Banculochristinemae</div></a>', unsafe_allow_html=True)
    st.markdown('<a href="https://www.facebook.com/share/1DWzombwNQ/" target="_blank"><div class="social-btn">📘FB Page:/ Mae’s Craft & Calligraphy</div></a>', unsafe_allow_html=True)
    st.markdown("""<div class="contact-card"><code>christinemaebanculo45@gmail.com</code></div>""", unsafe_allow_html=True)

st.markdown("---")
st.subheader("❓ Frequently Asked Questions")

with st.expander("What kind of programming projects do you work on?"):
    st.markdown("""<div class="faq-humble">I'm still learning — not very good at Streamlit yet (this is my first attempt!), and still getting comfortable with databases/MySQL. But I'm confident in Canva design! I focus on Python basics, HTML/CSS/JS, and front-end development.</div>""", unsafe_allow_html=True)

with st.expander("Are you open to collaboration?"):
    st.markdown("""<div class="faq-humble">Yes! I'm upfront — I'm still a beginner at complex coding. But I excel at UI/UX design in Canva, front-end basics, and I'm a quick learner. If you're patient and willing to mentor, I'd love to collaborate!</div>""", unsafe_allow_html=True)

with st.expander("Do you take commissions for calligraphy or crochet?"):
    st.write("Yes! Custom pieces available. Message me via Facebook or email.")

with st.expander("How quickly do you respond?"):
    st.write("Within 24-48 hours. I'm a full-time student, so I check messages in the evenings.")


st.success("💫 *Thank you for visiting my galaxy portfolio! Let's connect!*")