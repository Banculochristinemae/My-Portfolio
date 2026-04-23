<div align="center">

# 🌌 Galaxy Portfolio  
### *Christine Mae C. Banculo*

[![Streamlit App](https://img.shields.io/badge/LIVE_DEMO-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://your-app-url.streamlit.app)
[![GitHub](https://img.shields.io/badge/SOURCE_CODE-GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Banculochristinemae/portfolio_app)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)

</div>

---

# 📋 Table of Contents

- Repository Description  
- Overview  
- Features  
- Pages  
- Technologies Used  
- Project Structure  
- Installation  
- Image Requirements  
- How to Use  
- Customization  
- Deployment  
- Troubleshooting  
- Contact  
- Acknowledgments  
- License  

---

# 📝 Repository Description

| Property | Value |
|----------|------|
| **Repository Name** | `portfolio_app` |
| **Owner** | Christine Mae C. Banculo |
| **Purpose** | Personal portfolio website showcasing skills, projects, certificates, and creative work |
| **Tech Stack** | Python, Streamlit, HTML/CSS, SVG, Pillow |
| **Pages** | 7 interactive pages |
| **Theme** | Galaxy-themed with gradients and animations |
| **Status** | 🟢 Live |

## Key Features

- ✅ 7 Fully Functional Pages  
- ✅ Interactive Animations (UFO, celestial objects)  
- ✅ Real-time Music Player  
- ✅ Click-to-Enlarge Images  
- ✅ Responsive Design  
- ✅ Contact Form with Validation  
- ✅ Progress Bars  
- ✅ Project Rating System  

---

# 📌 Overview

**Galaxy Portfolio** is an interactive, multi-page portfolio website built using **Streamlit** that showcases the journey, skills, projects, and creative work of **Christine Mae C. Banculo**, a third-year Computer Science student.

## Purpose

| Area | Description |
|------|------------|
| 🎓 Academic | Showcase programming projects and certifications |
| 💼 Professional | Demonstrate technical skills and web development abilities |
| 🎨 Creative | Share calligraphy and crochet artwork |
| 🌌 Experience | Provide a relaxing stargazing corner with music |

---

# ✨ Features

## Design and User Interface

| Feature | Description |
|--------|-------------|
| 🌠 Galaxy Background | Radial gradients with twinkling star animations |
| 🔮 Glassmorphism | Frosted glass effects with blur and glow |
| 📱 Responsive Design | Works on desktop, tablet, and mobile |
| 🧭 Custom Sidebar | Navigation across all pages |
| ✨ Hover Effects | Interactive feedback on clickable elements |

## Interactive Elements

| Feature | Description |
|--------|-------------|
| 🖼️ Click-to-Enlarge | View certificates and projects in full size |
| 🪐 Animated Objects | SVG animations of celestial objects |
| 🎵 Music Player | Relaxing space ambient tracks |
| 🛸 UFO Animation | Flying animation after form submission |
| 📊 Progress Bars | Visual skill indicators |
| ⭐ Rating System | Rate projects from 1 to 5 stars |

---

# 📄 Pages

| # | Page | Description |
|---|------|------------|
| 1 | Home | Welcome section with profile and statistics |
| 2 | About | Personal background and education |
| 3 | Skills | Technical and creative skills |
| 4 | Projects | Portfolio of completed projects |
| 5 | Certificates | Professional certifications |
| 6 | Contact | Contact form and social links |
| 7 | Stargazing | Space-themed interactive section |

---

# 🛠️ Technologies Used

| Technology | Version | Purpose |
|-----------|--------|--------|
| Python | 3.9+ | Backend logic |
| Streamlit | 1.28+ | Web framework |
| Pillow (PIL) | 9.0+ | Image processing |
| HTML/CSS | — | Styling and layout |
| SVG | — | Animations |
| GitHub | — | Version control |

---

# 📁 Project Structure

```text
portfolio_app/

├── Home.py
├── requirements.txt
├── README.md

├── images/
│   ├── ID.png
│   ├── HMS.jpg
│   ├── math_game.jpg
│   ├── SMS.jpg
│   ├── photbooth.jpg
│   ├── Cisco_CSS.png
│   ├── Cisco_py.png
│   ├── intro_to_AI.png
│   ├── Cyber_sec.png
│   ├── python.png
│   ├── django.png

└── pages/
    ├── About.py
    ├── Skills.py
    ├── Projects.py
    ├── Certificates.py
    ├── Contact.py
    ├── Stargazing.py
```

---

# 🚀 Installation

## Prerequisites

- Python 3.9 or higher  
- pip package manager  

---

## Step 1 — Clone Repository

```bash
git clone https://github.com/Banculochristinemae/portfolio_app.git
cd portfolio_app
```

---

## Step 2 — Create Virtual Environment (Optional)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 4 — Run Application

```bash
streamlit run Home.py
```

---

## Step 5 — Open Browser

```
http://localhost:8501
```

---

# requirements.txt

```txt
streamlit>=1.28.0
pillow>=9.0.0
```

---

# 🖼️ Image Requirements

## Profile Photo

| Property | Value |
|----------|------|
| Filename | ID.png |
| Location | images/ID.png |
| Format | PNG |

---

## Project Images

| Project | Filename |
|--------|----------|
| Hotel Management System | HMS.jpg |
| Math Game | math_game.jpg |
| Store Management System | SMS.jpg |
| Photobooth | photbooth.jpg |

---

## Certificate Images

| Certificate | Filename |
|------------|----------|
| CSS Essentials | Cisco_CSS.png |
| Python Essential | Cisco_py.png |
| Introduction to AI | intro_to_AI.png |
| Cyber Security | Cyber_sec.png |
| Python Beginner | python.png |
| Django 101 | django.png |

---

# 🎯 How to Use

## Navigation

Use the sidebar to switch between pages.

### Home Page

- View profile  
- See statistics  

### About Page

- Read personal story  
- View education timeline  

### Skills Page

- See programming skills  
- View creative works  

### Projects Page

- Explore completed projects  
- View descriptions  

### Certificates Page

- View certifications  

### Contact Page

- Submit contact form  

### Stargazing Page

- Explore animations  
- Listen to music  

---

# 🎨 Customization

## Change Background

```css
background: radial-gradient(
ellipse at center,
#0a0f2a 0%,
#060914 100%
);
```

---

## Add New Skill

```python
new_skill = {
"icon": "✨",
"title": "New Skill",
"desc": "Description"
}
```

---

## Add New Project

Update:

```
pages/Projects.py
```

---

# ☁️ Deployment

## Steps

1. Push code to GitHub  

```bash
git add .
git commit -m "Initial commit"
git push origin main
```

2. Go to:

```
https://share.streamlit.io
```

3. Deploy application  

---

# 🔧 Troubleshooting

| Issue | Solution |
|------|----------|
| Images not showing | Check file paths |
| Streamlit not found | Install dependencies |
| Page not loading | Verify file structure |
| Animation not working | Enable browser scripts |

---

# 📬 Contact

| Platform | Details |
|----------|--------|
| Email | christinemaebanculo45@gmail.com |
| GitHub | Banculochristinemae |

---

# 🙏 Acknowledgments

| Source | Contribution |
|-------|-------------|
| Streamlit | Web framework |
| GitHub | Repository hosting |
| Educational Institution | Learning support |

---

# 📄 License

This project is for personal portfolio purposes.  
All rights reserved.

---

<div align="center">

# 💫 Quote

**"The stars are the limit when you code with passion."**  

— *Christine Mae C. Banculo*

⭐ If you like this project, please give it a star on GitHub! ⭐  

Created with 💜 using Python and Streamlit  

</div>
