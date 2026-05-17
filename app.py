import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Art Gallery - Gesner Deslandes",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- TRANSLATIONS (English, French, Spanish, Haitian Creole) ----------
def get_translations(lang):
    texts = {
        "en": {
            "gallery_title": "GlobalInternet.py Art Gallery",
            "subtitle": "'Mango Girl' – Original AI‑assisted painting by Gesner Deslandes",
            "artwork_title": "🍋 “Mango Girl” – Five Years Old, Camp City, Port‑au‑Prince",
            "description": "A five‑year‑old girl sits on a torn rug, her bare feet touching the slightly dirty floor of a makeshift camp city.\nIn her small hands, a ripe mango – its sweet juice drips down her chin, staining her already torn little outfit.\nBehind her, a patchwork of tarps and corrugated metal shelters other families living in the same precarious dignity.\nYet her eyes hold no despair – only the simple joy of eating a fruit under the Haitian sun.\nThis painting captures childhood resilience in the face of poverty, the beauty of a moment stolen from hardship.",
            "artist": "Artist: Gesner Deslandes",
            "company": "GlobalInternet.py",
            "phone": "📞 +509 4738-5663",
            "email": "✉️ deslandes78@gmail.com",
            "website": "🌐 https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/",
            "regenerate_btn": "🎨 Regenerate Painting (new version)",
            "print_btn": "🖨️ Print this artwork for exhibition",
            "footer": "© 2026 GlobalInternet.py – AI‑enhanced digital art exhibition software",
            "loading": "🎨 Creating your painting... Please wait (may take 20-30 seconds).",
            "error": "Failed to generate painting. Please check your internet connection and try again.",
            "sidebar_title": "🌐 Language",
            "sidebar_instruction": "Select your language"
        },
        "fr": {
            "gallery_title": "Galerie d'art GlobalInternet.py",
            "subtitle": "« Mango Girl » – Peinture originale assistée par IA par Gesner Deslandes",
            "artwork_title": "🍋 « Mango Girl » – Cinq ans, Camp City, Port‑au‑Prince",
            "description": "Une fillette de cinq ans est assise sur un tapis déchiré, ses pieds nus touchant le sol légèrement sale d'une ville de campement précaire.\nDans ses petites mains, une mangue mûre – son jus sucré coule sur son menton, tachant sa petite tenue déjà déchirée.\nDerrière elle, un patchwork de bâches et de tôles ondulées abrite d'autres familles vivant dans la même dignité précaire.\nPourtant, ses yeux ne montrent aucun désespoir – seulement la joie simple de manger un fruit sous le soleil haïtien.\nCette peinture capture la résilience de l'enfance face à la pauvreté, la beauté d'un moment volé à la difficulté.",
            "artist": "Artiste : Gesner Deslandes",
            "company": "GlobalInternet.py",
            "phone": "📞 +509 4738-5663",
            "email": "✉️ deslandes78@gmail.com",
            "website": "🌐 https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/",
            "regenerate_btn": "🎨 Regénérer la peinture (nouvelle version)",
            "print_btn": "🖨️ Imprimer cette œuvre pour exposition",
            "footer": "© 2026 GlobalInternet.py – Logiciel d'exposition d'art numérique assisté par IA",
            "loading": "🎨 Création de votre peinture... Veuillez patienter (20-30 secondes).",
            "error": "Échec de la génération. Vérifiez votre connexion internet et réessayez.",
            "sidebar_title": "🌐 Langue",
            "sidebar_instruction": "Choisissez votre langue"
        },
        "es": {
            "gallery_title": "Galería de arte GlobalInternet.py",
            "subtitle": "« Mango Girl » – Pintura original asistida por IA por Gesner Deslandes",
            "artwork_title": "🍋 « Mango Girl » – Cinco años, Camp City, Puerto Príncipe",
            "description": "Una niña de cinco años sentada sobre una alfombra rota, sus pies descalzos tocando el suelo ligeramente sucio de una ciudad de campamento improvisado.\nEn sus pequeñas manos, un mango maduro – su jugo dulce gotea por su barbilla, manchando su pequeño vestido ya roto.\nDetrás de ella, un mosaico de lonas y láminas de metal corrugado alberga a otras familias que viven en la misma dignidad precaria.\nSin embargo, sus ojos no muestran desesperación – solo la simple alegría de comer una fruta bajo el sol haitiano.\nEsta pintura captura la resiliencia infantil frente a la pobreza, la belleza de un momento robado a la adversidad.",
            "artist": "Artista: Gesner Deslandes",
            "company": "GlobalInternet.py",
            "phone": "📞 +509 4738-5663",
            "email": "✉️ deslandes78@gmail.com",
            "website": "🌐 https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/",
            "regenerate_btn": "🎨 Regenerar pintura (nueva versión)",
            "print_btn": "🖨️ Imprimir esta obra para exposición",
            "footer": "© 2026 GlobalInternet.py – Software de exhibición de arte digital mejorado con IA",
            "loading": "🎨 Creando su pintura... Espere (20-30 segundos).",
            "error": "Error al generar la pintura. Verifique su conexión a internet e intente de nuevo.",
            "sidebar_title": "🌐 Idioma",
            "sidebar_instruction": "Seleccione su idioma"
        },
        "ht": {
            "gallery_title": "GlobalInternet.py Galeri D'Art",
            "subtitle": "'Mango Girl' – Tablo orijinal asisté pa IA pa Gesner Deslandes",
            "artwork_title": "🍋 “Mango Girl” – Senk ane, Camp City, Pòtoprens",
            "description": "Yon ti fi senk ane chita sou yon tapi chire, pye atè li touche planche ki gen ti salte nan yon vil kan rezèv.\nNan ti men li, yon mango mi – ji dous li koule sou manton li, sali ti rad li deja chire.\nDèyè li, yon melanj twal ak tòl kouvri lòt fanmi k ap viv nan menm diyite presè.\nMen je li pa montre dezespwa – sèlman kè kontan senp manje yon fwi anba solèy la ann Ayiti.\nTablo sa a montre rezistans timoun devan povrete, bèlte yon moman yo vòlè nan difikilte.",
            "artist": "Atis: Gesner Deslandes",
            "company": "GlobalInternet.py",
            "phone": "📞 +509 4738-5663",
            "email": "✉️ deslandes78@gmail.com",
            "website": "🌐 https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/",
            "regenerate_btn": "🎨 Rekree tablo a (nouvo vèsyon)",
            "print_btn": "🖨️ Enprime travay sa a pou egzibisyon",
            "footer": "© 2026 GlobalInternet.py – Lojisyèl egzibisyon atis dijital avèk IA",
            "loading": "🎨 Kreyasyon tablo a... Tanpri tann (20-30 segonn).",
            "error": "Pa t kapab kreye tablo a. Tcheke koneksyon entènèt ou epi eseye ankò.",
            "sidebar_title": "🌐 Lang",
            "sidebar_instruction": "Chwazi lang ou"
        }
    }
    return texts[lang]

# ---------- CUSTOM CSS (dark gallery, white bold text) ----------
st.markdown(
    """
    <style>
    /* Main background */
    .stApp {
        background: linear-gradient(145deg, #1a1a2e 0%, #0f0f1a 100%);
    }
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e2a3e, #0f1722);
        border-right: 2px solid #ffb347;
    }
    [data-testid="stSidebar"] * {
        color: #f0f0f0 !important;
    }
    /* Gallery container */
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
    /* Image caption (figcaption) – force white with shadow */
    .stImage figcaption {
        color: #ffffff !important;
        font-weight: bold !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5) !important;
        background: rgba(0,0,0,0.4) !important;
        display: inline-block !important;
        padding: 0.2rem 1rem !important;
        border-radius: 30px !important;
        margin-top: 0.5rem !important;
    }
    /* Subtitle (under title) */
    .subtitle-white {
        color: #ffffff !important;
        font-weight: 500;
        text-align: center;
    }
    /* Description card – dark background, strong white text */
    .description-card {
        background: rgba(20, 20, 30, 0.95);
        border-radius: 30px;
        padding: 1.8rem;
        margin-top: 2rem;
        border-left: 10px solid #ffb347;
        font-family: 'Georgia', serif;
        color: #ffffff !important;
        font-weight: 700;
        box-shadow: 0 10px 20px rgba(0,0,0,0.3);
    }
    .artwork-title {
        font-size: 2rem;
        font-weight: bold;
        color: #ffd966;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .artwork-detail {
        font-size: 1.1rem;
        line-height: 1.6;
        text-align: justify;
        color: #ffffff !important;
        font-weight: 500;
    }
    .signature {
        margin-top: 2rem;
        text-align: right;
        font-family: 'Brush Script MT', cursive;
        font-size: 1.5rem;
        color: #ffd966 !important;
        font-weight: bold;
        border-top: 1px solid #ffb347;
        padding-top: 1rem;
    }
    .contact-info {
        font-family: monospace;
        font-size: 0.9rem;
        color: #ffffff !important;
        font-weight: 600;
        text-align: center;
        margin-top: 1rem;
    }
    .print-button, .regenerate-btn {
        text-align: center;
        margin: 1.5rem 0;
    }
    /* Button styling */
    .stButton button {
        background-color: #e94560 !important;
        color: white !important;
        border-radius: 30px !important;
        font-weight: bold !important;
        border: none;
        padding: 0.5rem 1.5rem;
    }
    .stButton button:hover {
        background-color: #ff6b6b !important;
        transform: scale(1.02);
    }
    @media print {
        .stApp, .print-button, .regenerate-btn, header, footer, [data-testid="stToolbar"], [data-testid="stSidebar"] {
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
            background: white !important;
            color: black !important;
            border: 1px solid #ccc;
        }
        .description-card * {
            color: black !important;
        }
        .signature, .contact-info {
            color: black !important;
        }
        .print-only {
            display: block !important;
        }
        .stImage figcaption {
            color: black !important;
            text-shadow: none !important;
            background: none !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- PROMPT FOR AI PAINTING ----------
prompt = (
    "A five-year-old Haitian girl with dark skin, curly black hair, sitting on a torn, faded rug on a slightly dirty floor. "
    "She is eating a ripe mango, juice dripping from her mouth, staining her torn, colorful little dress. "
    "Behind her, a camp city with multiple tarps and makeshift homes made of corrugated metal and wood, other families visible. "
    "The setting is Port-au-Prince, Haiti, under a bright sky. Realistic oil painting style, fine art, detailed, warm colors, "
    "emotional, professional gallery quality."
)

def generate_painting(prompt):
    url = f"https://image.pollinations.ai/prompt/{requests.utils.quote(prompt)}?width=1024&height=1024&nologo=true"
    try:
        response = requests.get(url, timeout=90)
        if response.status_code == 200:
            return Image.open(BytesIO(response.content))
    except:
        pass
    return None

# ---------- SESSION STATE ----------
if "painting_img" not in st.session_state:
    with st.spinner("🎨 Creating your painting... Please wait (may take 20-30 seconds)."):
        st.session_state.painting_img = generate_painting(prompt)

# ---------- LANGUAGE SELECTION (SIDEBAR) ----------
st.sidebar.markdown("## 🌐 Language / Langue")
lang_choice = st.sidebar.selectbox(
    "Select your language",
    ["English", "Français", "Español", "Kreyòl Ayisyen"]
)
lang_map = {
    "English": "en",
    "Français": "fr",
    "Español": "es",
    "Kreyòl Ayisyen": "ht"
}
t = get_translations(lang_map[lang_choice])

# ---------- MAIN UI ----------
st.markdown('<div class="gallery-container">', unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align:center; color:#ffd966;'>{t['gallery_title']}</h1>", unsafe_allow_html=True)
st.markdown(f"<p class='subtitle-white'>{t['subtitle']}</p>", unsafe_allow_html=True)

# Display painting
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown('<div class="painting-frame">', unsafe_allow_html=True)
    if st.session_state.painting_img:
        st.image(st.session_state.painting_img, use_container_width=True, caption="'Mango Girl' – Original Painting")
    else:
        st.error(t['error'])
    st.markdown('</div>', unsafe_allow_html=True)

# Regenerate button
with col2:
    if st.button(t['regenerate_btn'], use_container_width=True, key="regenerate"):
        with st.spinner(t['loading']):
            st.session_state.painting_img = generate_painting(prompt)
            st.rerun()

# ---------- ARTWORK DESCRIPTION (translated) ----------
st.markdown('<div class="description-card">', unsafe_allow_html=True)
st.markdown(f'<div class="artwork-title">{t["artwork_title"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="artwork-detail">{t["description"]}</div>', unsafe_allow_html=True)

# Artist signature and contact – translated
st.markdown(
    f"""
    <div class="signature">
    {t['artist']}<br>
    {t['company']}
    </div>
    <div class="contact-info">
    {t['phone']} &nbsp;&nbsp;|&nbsp;&nbsp; {t['email']}<br>
    {t['website']}
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)

# ---------- PRINT BUTTON ----------
st.markdown('<div class="print-button">', unsafe_allow_html=True)
if st.button(t['print_btn'], use_container_width=True):
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
st.markdown(f'<p style="text-align:center; color:#aaa; margin-top:2rem;">{t["footer"]}</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
