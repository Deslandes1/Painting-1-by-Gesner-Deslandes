import streamlit as st
from PIL import Image
import io
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
    @media print {
        .stApp, .print-button, header, footer, [data-testid="stToolbar"] {
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

# ---------- APP TITLE ----------
st.markdown('<div class="gallery-container">', unsafe_allow_html=True)
st.markdown("<h1 style='text-align:center; color:#ffd966;'>🎨 GlobalInternet.py Art Gallery</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#ddd;'>Where code meets creativity – a digital exhibition space</p>", unsafe_allow_html=True)

# ---------- PAINTING UPLOAD (or use placeholder) ----------
st.markdown("### 🖼️ Upload your painting (or use the demo description)")
uploaded_file = st.file_uploader("Choose an image file (JPG, PNG)", type=["jpg", "jpeg", "png"], label_visibility="collapsed")

# If no image uploaded, show a placeholder with the description text instead of an image?
# Better to provide a default generated image? But we can display a gray box with text.
# I'll create a placeholder image with PIL that shows a descriptive text.
def create_placeholder_image():
    img = Image.new('RGB', (800, 600), color='#d4a373')
    # We can't draw text easily with PIL without font, so we'll use st.image with caption.
    return img

if uploaded_file is not None:
    image = Image.open(uploaded_file)
else:
    # Use a placeholder image (brown background with text description)
    image = create_placeholder_image()
    st.info("No image uploaded. A placeholder is shown. Please upload your painting to replace it.")

# ---------- DISPLAY PAINTING ----------
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown('<div class="painting-frame">', unsafe_allow_html=True)
    st.image(image, use_container_width=True, caption="'Mango Girl' – Original Painting", output_format="JPEG")
    st.markdown('</div>', unsafe_allow_html=True)

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

# ---------- PRINT BUTTON (prints the entire page content) ----------
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
st.markdown('<p style="text-align:center; color:#aaa; margin-top:2rem;">© 2026 GlobalInternet.py – Digital art exhibition software</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
