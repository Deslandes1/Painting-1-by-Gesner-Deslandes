import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import base64

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Art Gallery - Gesner Deslandes",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- CUSTOM CSS FOR GALLERY STYLE ----------
st.markdown(
    """
    <style>
    /* Background – elegant dark gallery */
    .stApp {
        background: linear-gradient(145deg, #2c2c2c 0%, #1a1a1a 100%);
    }
    /* Main container */
    .gallery-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 2rem;
    }
    /* Painting frame */
    .painting-frame {
        background: #f5e6d3;
        padding: 1.5rem;
        border-radius: 40px;
        box-shadow: 0 30px 40px rgba(0,0,0,0.4);
        border: 1px solid #d4a373;
        text-align: center;
    }
    .painting-image {
        max-width: 100%;
        border-radius: 20px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.3);
        cursor: pointer;
    }
    /* Description card */
    .description-card {
        background: #fffef7;
        border-radius: 30px;
        padding: 1.8rem;
        margin-top: 2rem;
        border-left: 10px solid #c0392b;
        font-family: 'Georgia', serif;
        color: #2c2c2c;
    }
    .artwork-title {
        font-size: 2rem;
        font-weight: bold;
        color: #c0392b;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .artwork-detail {
        font-size: 1.1rem;
        line-height: 1.6;
        text-align: justify;
    }
    .signature {
        margin-top: 2rem;
        text-align: right;
        font-family: 'Brush Script MT', cursive;
        font-size: 1.5rem;
        color: #2c3e50;
        border-top: 1px solid #ccc;
        padding-top: 1rem;
    }
    .contact-info {
        font-family: monospace;
        font-size: 0.9rem;
        color: #555;
        text-align: center;
        margin-top: 1rem;
    }
    .print-button {
        text-align: center;
        margin: 2rem 0;
    }
    .regenerate-btn {
        text-align: center;
        margin-top: 1rem;
    }
    @media print {
        .stApp, .print-button, .regenerate-btn, header, footer, [data-testid="stToolbar"] {
            display: none !important;
        }
        .gallery-container {
            margin: 0;
            padding: 0;
        }
        .painting-frame {
            box-shadow: none;
            padding: 0;
        }
        .description-card {
            box-shadow: none;
            border: 1px solid #ccc;
        }
        .print-only {
            display: block !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- PROMPT FOR AI PAINTING (detailed description) ----------
prompt = (
    "A five-year-old Haitian girl with dark skin, curly black hair, sitting on a torn, faded rug on a slightly dirty floor. "
    "She is eating a ripe mango, juice dripping from her mouth, staining her torn, colorful little dress. "
    "Behind her, a camp city with multiple tarps and makeshift homes made of corrugated metal and wood, other families visible. "
    "The setting is Port-au-Prince, Haiti, under a bright sky. Realistic oil painting style, fine art, detailed, warm colors, "
    "emotional, professional gallery quality."
)

# ---------- FUNCTION TO GENERATE IMAGE FROM POLLINATIONS.AI (free, no key) ----------
def generate_painting(prompt):
    # Pollinations.ai endpoint – returns a generated image directly
    url = f"https://image.pollinations.ai/prompt/{requests.utils.quote(prompt)}?width=1024&height=1024&nologo=true"
    response = requests.get(url, timeout=60)
    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    else:
        return None

# ---------- SESSION STATE TO REMEMBER LAST IMAGE ----------
if "painting_img" not in st.session_state:
    with st.spinner("🎨 Creating your painting... Please wait (may take 20-30 seconds)."):
        st.session_state.painting_img = generate_painting(prompt)

# ---------- UI ----------
st.markdown('<div class="gallery-container">', unsafe_allow_html=True)
st.markdown("<h1 style='text-align:center; color:#ffd966;'>🎨 GlobalInternet.py Art Gallery</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#ddd;'>'Mango Girl' – Original AI‑assisted painting by Gesner Deslandes</p>", unsafe_allow_html=True)

# Display painting
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown('<div class="painting-frame">', unsafe_allow_html=True)
    if st.session_state.painting_img:
        st.image(st.session_state.painting_img, use_container_width=True, caption="'Mango Girl' – Original Painting")
    else:
        st.error("Failed to generate painting. Please check your internet connection and try again.")
    st.markdown('</div>', unsafe_allow_html=True)

# Regenerate button
with col2:
    if st.button("🎨 Regenerate Painting (new version)", use_container_width=True, key="regenerate"):
        with st.spinner("Creating a new version..."):
            st.session_state.painting_img = generate_painting(prompt)
            st.rerun()

# ---------- ARTWORK DESCRIPTION ----------
st.markdown('<div class="description-card">', unsafe_allow_html=True)
st.markdown('<div class="artwork-title">🍋 “Mango Girl” – Five Years Old, Camp City, Port‑au‑Prince</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="artwork-detail">
    A five‑year‑old girl sits on a torn rug, her bare feet touching the slightly dirty floor of a makeshift camp city.  
    In her small hands, a ripe mango – its sweet juice drips down her chin, staining her already torn little outfit.  
    Behind her, a patchwork of tarps and corrugated metal shelters other families living in the same precarious dignity.  
    Yet her eyes hold no despair – only the simple joy of eating a fruit under the Haitian sun.  
    This painting captures childhood resilience in the face of poverty, the beauty of a moment stolen from hardship.
    </div>
    """,
    unsafe_allow_html=True
)

# Artist signature and contact
st.markdown(
    f"""
    <div class="signature">
    Artist: Gesner Deslandes<br>
    GlobalInternet.py
    </div>
    <div class="contact-info">
    📞 +509 4738-5663 &nbsp;&nbsp;|&nbsp;&nbsp; ✉️ deslandes78@gmail.com<br>
    🌐 https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)

# ---------- PRINT BUTTON ----------
st.markdown('<div class="print-button">', unsafe_allow_html=True)
if st.button("🖨️ Print this artwork for exhibition", use_container_width=True):
    st.markdown(
        """
        <script>
        window.print();
        </script>
        """,
        unsafe_allow_html=True
    )
st.markdown('</div>', unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown('<p style="text-align:center; color:#aaa; margin-top:2rem;">© 2026 GlobalInternet.py – AI‑enhanced digital art exhibition software</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
