import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import datetime

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
            "subtitle": "'Mercenaries: The Night of July 7, 2021' – Original painting by Gesner Deslandes",
            "artwork_title": "🔫 “Mercenaries” – The Night President Jovenel Moïse Was Assassinated",
            "description": "A group of heavily armed mercenaries stands in the middle of the night, their pickup trucks' headlights cutting through the darkness. Each man carries a rifle. This scene is a remembrance of the tragic night of July 7, 2021, when President Jovenel Moïse was assassinated in his home. If we believe in the US justice system, justice was served, but the Haitian population is still paying the price of that night in 2026. This painting is a memorial, a cry for accountability, and a reminder that the truth has never been fully told.",
            "artist": "Artist: Gesner Deslandes",
            "company": "GlobalInternet.py",
            "phone": "📞 +509 4738-5663",
            "email": "✉️ deslandes78@gmail.com",
            "website": "🌐 https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/",
            "regenerate_btn": "🔄 Reload Image",
            "print_btn": "🖨️ Print this artwork for exhibition",
            "download_btn": "💾 Download this painting (PNG)",
            "footer": "© 2026 GlobalInternet.py – Digital art exhibition software",
            "loading": "🎨 Loading your painting...",
            "error": "Failed to load painting. Please check your internet connection and try again.",
            "sidebar_title": "🌐 Language",
            "sidebar_instruction": "Select your language",
            "img_caption": "'Mercenaries – The Night of July 7, 2021' – Original Painting",
            "history_title": "📚 Painting History",
            "download_history_btn": "💾 Download",
            "clear_history_btn": "🗑️ Clear history",
            "no_history": "No paintings saved yet. Generate some to see them here."
        },
        "fr": {
            "gallery_title": "Galerie d'art GlobalInternet.py",
            "subtitle": "« Mercenaires : La Nuit du 7 Juillet 2021 » – Peinture originale par Gesner Deslandes",
            "artwork_title": "🔫 « Mercenaires » – La nuit de l'assassinat du président Jovenel Moïse",
            "description": "Un groupe de mercenaires lourdement armés se tient au milieu de la nuit, les phares de leurs pick‑ups perçant l'obscurité. Chaque homme porte un fusil. Cette scène est un souvenir de la nuit tragique du 7 juillet 2021, lorsque le président Jovenel Moïse a été assassiné chez lui. Si nous croyons au système judiciaire américain, la justice a été rendue, mais la population haïtienne paie encore le prix de cette nuit en 2026. Cette peinture est un mémorial, un cri pour la responsabilité et un rappel que la vérité n'a jamais été entièrement révélée.",
            "artist": "Artiste : Gesner Deslandes",
            "company": "GlobalInternet.py",
            "phone": "📞 +509 4738-5663",
            "email": "✉️ deslandes78@gmail.com",
            "website": "🌐 https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/",
            "regenerate_btn": "🔄 Recharger l'image",
            "print_btn": "🖨️ Imprimer cette œuvre pour exposition",
            "download_btn": "💾 Télécharger cette peinture (PNG)",
            "footer": "© 2026 GlobalInternet.py – Logiciel d'exposition d'art numérique",
            "loading": "🎨 Chargement de votre peinture...",
            "error": "Échec du chargement. Vérifiez votre connexion internet.",
            "sidebar_title": "🌐 Langue",
            "sidebar_instruction": "Choisissez votre langue",
            "img_caption": "« Mercenaires – La Nuit du 7 Juillet 2021 » – Peinture originale",
            "history_title": "📚 Historique des peintures",
            "download_history_btn": "💾 Télécharger",
            "clear_history_btn": "🗑️ Effacer l'historique",
            "no_history": "Aucune peinture sauvegardée."
        },
        "es": {
            "gallery_title": "Galería de arte GlobalInternet.py",
            "subtitle": "« Mercenarios: La Noche del 7 de Julio de 2021 » – Pintura original por Gesner Deslandes",
            "artwork_title": "🔫 “Mercenarios” – La noche del asesinato del presidente Jovenel Moïse",
            "description": "Un grupo de mercenarios fuertemente armados está en medio de la noche, los faros de sus camionetas cortan la oscuridad. Cada hombre lleva un rifle. Esta escena es un recuerdo de la trágica noche del 7 de julio de 2021, cuando el presidente Jovenel Moïse fue asesinado en su casa. Si creemos en el sistema judicial estadounidense, se hizo justicia, pero la población haitiana todavía está pagando el precio de esa noche en 2026. Esta pintura es un memorial, un grito de rendición de cuentas y un recordatorio de que la verdad nunca se ha contado por completo.",
            "artist": "Artista: Gesner Deslandes",
            "company": "GlobalInternet.py",
            "phone": "📞 +509 4738-5663",
            "email": "✉️ deslandes78@gmail.com",
            "website": "🌐 https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/",
            "regenerate_btn": "🔄 Recargar imagen",
            "print_btn": "🖨️ Imprimir esta obra para exposición",
            "download_btn": "💾 Descargar esta pintura (PNG)",
            "footer": "© 2026 GlobalInternet.py – Software de exhibición de arte digital",
            "loading": "🎨 Cargando su pintura...",
            "error": "Error al cargar. Verifique su conexión a internet.",
            "sidebar_title": "🌐 Idioma",
            "sidebar_instruction": "Seleccione su idioma",
            "img_caption": "« Mercenarios – La Noche del 7 de Julio de 2021 » – Pintura original",
            "history_title": "📚 Historial de pinturas",
            "download_history_btn": "💾 Descargar",
            "clear_history_btn": "🗑️ Borrar historial",
            "no_history": "No hay pinturas guardadas."
        },
        "ht": {
            "gallery_title": "GlobalInternet.py Galeri D'Art",
            "subtitle": "'Mèsenè: Lannwit 7 Jiyè 2021' – Tablo orijinal pa Gesner Deslandes",
            "artwork_title": "🔫 “Mèsenè” – Lannwit asasina Prezidan Jovenel Moïse",
            "description": "Yon gwoup mèsenè byen ame kanpe nan mitan lannwit, limyè machin yo klere fènwa a. Chak gason gen yon fizi nan men yo. Sèn sa a se yon chonjaj lannwit trajik 7 jiyè 2021, lè yo te asasine Prezidan Jovenel Moïse lakay li. Si nou kwè nan sistèm jistis ameriken an, jistis te rive, men popilasyon ayisyen an ap toujou peye pri lannwit sa a an 2026. Tablo sa a se yon memoryal, yon rèl pou responsabilite, ak yon rapèl ke verite a pa janm te rakonte nèt ale.",
            "artist": "Atis: Gesner Deslandes",
            "company": "GlobalInternet.py",
            "phone": "📞 +509 4738-5663",
            "email": "✉️ deslandes78@gmail.com",
            "website": "🌐 https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/",
            "regenerate_btn": "🔄 Rechaje imaj la",
            "print_btn": "🖨️ Enprime travay sa a pou egzibisyon",
            "download_btn": "💾 Telechaje tablo sa a (PNG)",
            "footer": "© 2026 GlobalInternet.py – Lojisyèl egzibisyon atis dijital",
            "loading": "🎨 Ap chaje tablo a...",
            "error": "Pa t kapab chaje tablo a. Tcheke koneksyon entènèt ou.",
            "sidebar_title": "🌐 Lang",
            "sidebar_instruction": "Chwazi lang ou",
            "img_caption": "'Mèsenè – Lannwit 7 Jiyè 2021' – Tablo Orijinal",
            "history_title": "📚 Istorik tablo yo",
            "download_history_btn": "💾 Telechaje",
            "clear_history_btn": "🗑️ Efase istorik",
            "no_history": "Pa gen tablo ki sove."
        }
    }
    return texts[lang]

# ---------- CUSTOM CSS ----------
st.markdown(
    """
    <style>
    .stApp { background: linear-gradient(145deg, #1a1a2e 0%, #0f0f1a 100%); }
    [data-testid="stSidebar"] { background: linear-gradient(180deg, #1e2a3e, #0f1722); border-right: 2px solid #ffb347; }
    [data-testid="stSidebar"] * { color: #f0f0f0 !important; }
    .gallery-container { max-width: 1200px; margin: 0 auto; padding: 2rem; }
    .painting-frame { background: #f5e6d3; padding: 1.5rem; border-radius: 40px; box-shadow: 0 30px 40px rgba(0,0,0,0.4); border: 1px solid #d4a373; text-align: center; }
    .stCaption, .stImage figcaption { color: #ffffff !important; font-weight: bold !important; font-size: 1.1rem !important; text-align: center !important; margin-top: 0.5rem !important; }
    .description-card { background: rgba(20,20,30,0.95); border-radius: 30px; padding: 1.8rem; margin-top: 2rem; border-left: 10px solid #ffb347; font-family: 'Georgia', serif; color: #ffffff !important; font-weight: 700; box-shadow: 0 10px 20px rgba(0,0,0,0.3); }
    .artwork-title { font-size: 2rem; font-weight: bold; color: #ffd966; text-align: center; margin-bottom: 0.5rem; }
    .artwork-detail { font-size: 1.1rem; line-height: 1.6; text-align: justify; color: #ffffff !important; font-weight: 500; }
    .signature { margin-top: 2rem; text-align: right; font-family: 'Brush Script MT', cursive; font-size: 1.5rem; color: #ffd966 !important; font-weight: bold; border-top: 1px solid #ffb347; padding-top: 1rem; }
    .contact-info { font-family: monospace; font-size: 0.9rem; color: #ffffff !important; font-weight: 600; text-align: center; margin-top: 1rem; }
    .print-button, .regenerate-btn, .download-button { text-align: center; margin: 1rem 0; }
    .stButton button { background-color: #e94560 !important; color: white !important; border-radius: 30px !important; font-weight: bold !important; border: none; padding: 0.5rem 1.5rem; }
    .stButton button:hover { background-color: #ff6b6b !important; transform: scale(1.02); }
    .history-item { margin-bottom: 1rem; text-align: center; background: rgba(0,0,0,0.3); padding: 0.5rem; border-radius: 15px; }
    @media print {
        .stApp, .print-button, .regenerate-btn, .download-button, header, footer, [data-testid="stToolbar"], [data-testid="stSidebar"] { display: none !important; }
        .gallery-container { margin: 0; padding: 0; }
        .painting-frame { box-shadow: none; padding: 0; }
        .description-card { background: white !important; color: black !important; border: 1px solid #ccc; }
        .description-card * { color: black !important; }
        .signature, .contact-info { color: black !important; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- CORRECT RAW IMAGE URL ----------
# 使用正确的原始图片链接，替换了之前的错误链接
image_url = "https://raw.githubusercontent.com/Deslandes1/Painting-1-by-Gesner-Deslandes/main/Gemini_Generated_Image_fwpr4ofwpr4ofwpr.png"

def load_image_from_url(url):
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            return Image.open(BytesIO(response.content))
    except:
        pass
    return None

def pil_to_bytes(img, format="PNG"):
    buf = BytesIO()
    img.save(buf, format=format)
    return buf.getvalue()

# ---------- SESSION STATE ----------
if "painting_img" not in st.session_state:
    with st.spinner("🎨 Loading your painting..."):
        st.session_state.painting_img = load_image_from_url(image_url)
        st.session_state.painting_history = []

if "painting_history" not in st.session_state:
    st.session_state.painting_history = []

# ---------- LANGUAGE SELECTION ----------
st.sidebar.markdown("## 🌐 Language / Langue")
lang_choice = st.sidebar.selectbox(
    "Select your language",
    ["English", "Français", "Español", "Kreyòl Ayisyen"]
)
lang_map = {"English": "en", "Français": "fr", "Español": "es", "Kreyòl Ayisyen": "ht"}
t = get_translations(lang_map[lang_choice])

# ---------- SIDEBAR HISTORY ----------
st.sidebar.markdown(f"## {t['history_title']}")
if st.sidebar.button(t['clear_history_btn']):
    st.session_state.painting_history = []
    st.rerun()

if not st.session_state.painting_history:
    st.sidebar.info(t['no_history'])
else:
    for idx, img in enumerate(reversed(st.session_state.painting_history)):
        st.sidebar.image(img, use_container_width=True, caption=f"Version {len(st.session_state.painting_history)-idx}")
        img_bytes = pil_to_bytes(img)
        st.sidebar.download_button(
            label=f"{t['download_history_btn']} #{len(st.session_state.painting_history)-idx}",
            data=img_bytes,
            file_name=f"mercenaries_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}_{idx}.png",
            mime="image/png",
            key=f"hist_dl_{idx}"
        )
        st.sidebar.markdown("---")

# ---------- MAIN UI ----------
st.markdown('<div class="gallery-container">', unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align:center; color:#ffd966;'>{t['gallery_title']}</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center; color:#ddd;'>{t['subtitle']}</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown('<div class="painting-frame">', unsafe_allow_html=True)
    if st.session_state.painting_img:
        st.image(st.session_state.painting_img, use_container_width=True, caption=t['img_caption'])
    else:
        st.error(t['error'])
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button(t['regenerate_btn'], use_container_width=True, key="regenerate"):
            if st.session_state.painting_img is not None:
                st.session_state.painting_history.append(st.session_state.painting_img.copy())
            with st.spinner(t['loading']):
                st.session_state.painting_img = load_image_from_url(image_url)
                st.rerun()
    with col_btn2:
        if st.session_state.painting_img is not None:
            img_bytes = pil_to_bytes(st.session_state.painting_img)
            st.download_button(
                label=t['download_btn'],
                data=img_bytes,
                file_name=f"mercenaries_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png",
                mime="image/png",
                use_container_width=True,
                key="download_current"
            )

# ---------- ARTWORK DESCRIPTION ----------
st.markdown('<div class="description-card">', unsafe_allow_html=True)
st.markdown(f'<div class="artwork-title">{t["artwork_title"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="artwork-detail">{t["description"]}</div>', unsafe_allow_html=True)

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
    st.markdown("<script>window.print();</script>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown(f'<p style="text-align:center; color:#aaa; margin-top:2rem;">{t["footer"]}</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
