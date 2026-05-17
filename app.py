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
            "subtitle": "'Birth at the Lyceum' – Original AI‑assisted painting by Gesner Deslandes",
            "artwork_title": "👶 “Birth at the Lyceum” – Pregnant Woman Giving Birth at a Refugee School, Port‑au‑Prince",
            "description": "In front of the Lycee Du Cencenquantenaire (Lycee Des Jeunes Filles), a school now serving as a refugee shelter, a pregnant Black Haitian woman lies on the concrete ground at the main entrance, her dress lifted, legs open, trying to give birth. A man on her left (wearing a t‑shirt and blue jeans) and a woman on her right (wearing a colorful dress) kneel beside her, helping her breathe and deliver without medical assistance. Other Black Haitians stand in the background near the building, watching. Some men wear shirts with black jeans; others wear t‑shirts with blue jeans. Women wear normal dresses of various colors. On every balcony of the building, displaced families have hung clothes, shirts, pants, dresses, and sleeping rugs to dry under the bright sun. The building has the name 'Lycee Du Cencenquantenaire' clearly visible. The scene is realistic, emotionally powerful, with warm sunlight casting shadows. No rain, only a sunny day.",
            "artist": "Artist: Gesner Deslandes",
            "company": "GlobalInternet.py",
            "phone": "📞 +509 4738-5663",
            "email": "✉️ deslandes78@gmail.com",
            "website": "🌐 https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/",
            "regenerate_btn": "🎨 Regenerate Painting (new version)",
            "print_btn": "🖨️ Print this artwork for exhibition",
            "download_btn": "💾 Download this painting (PNG)",
            "footer": "© 2026 GlobalInternet.py – AI‑enhanced digital art exhibition software",
            "loading": "🎨 Creating your painting... Please wait (may take 20-30 seconds).",
            "error": "Failed to generate painting. Please check your internet connection and try again.",
            "sidebar_title": "🌐 Language",
            "sidebar_instruction": "Select your language",
            "img_caption": "'Birth at the Lyceum' – Original Painting",
            "history_title": "📚 Painting History",
            "download_history_btn": "💾 Download",
            "clear_history_btn": "🗑️ Clear history",
            "no_history": "No paintings saved yet. Generate some to see them here."
        },
        "fr": {
            "gallery_title": "Galerie d'art GlobalInternet.py",
            "subtitle": "« Naissance au Lycée » – Peinture originale assistée par IA par Gesner Deslandes",
            "artwork_title": "👶 « Naissance au Lycée » – Femme enceinte accouchant dans une école de réfugiés, Port‑au‑Prince",
            "description": "Devant le Lycee Du Cencenquantenaire (Lycee Des Jeunes Filles), une école devenue refuge, une femme enceinte noire haïtienne est allongée sur le sol en béton à l'entrée principale, sa robe relevée, les jambes écartées, tentant d'accoucher. Un homme à sa gauche (portant un t‑shirt et un jean bleu) et une femme à sa droite (portant une robe colorée) l'aident à respirer et à délivrer le bébé sans assistance médicale. D'autres Haïtiens noirs se tiennent en arrière-plan près du bâtiment, regardant. Certains hommes portent des chemises avec jeans noirs, d'autres des t‑shirts avec jeans bleus. Les femmes portent des robes normales de différentes couleurs. À chaque balcon du bâtiment, des familles déplacées ont suspendu vêtements, chemises, pantalons, robes et tapis de sol pour les faire sécher au soleil. Le bâtiment porte le nom 'Lycee Du Cencenquantenaire' visible. La scène est réaliste, puissante, avec une lumière chaude projetant des ombres. Pas de pluie, seulement un jour ensoleillé.",
            "artist": "Artiste : Gesner Deslandes",
            "company": "GlobalInternet.py",
            "phone": "📞 +509 4738-5663",
            "email": "✉️ deslandes78@gmail.com",
            "website": "🌐 https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/",
            "regenerate_btn": "🎨 Regénérer la peinture (nouvelle version)",
            "print_btn": "🖨️ Imprimer cette œuvre pour exposition",
            "download_btn": "💾 Télécharger cette peinture (PNG)",
            "footer": "© 2026 GlobalInternet.py – Logiciel d'exposition d'art numérique assisté par IA",
            "loading": "🎨 Création de votre peinture... Veuillez patienter (20-30 secondes).",
            "error": "Échec de la génération. Vérifiez votre connexion internet et réessayez.",
            "sidebar_title": "🌐 Langue",
            "sidebar_instruction": "Choisissez votre langue",
            "img_caption": "« Naissance au Lycée » – Peinture originale",
            "history_title": "📚 Historique des peintures",
            "download_history_btn": "💾 Télécharger",
            "clear_history_btn": "🗑️ Effacer l'historique",
            "no_history": "Aucune peinture sauvegardée. Générez-en pour les voir ici."
        },
        "es": {
            "gallery_title": "Galería de arte GlobalInternet.py",
            "subtitle": "« Nacimiento en el Liceo » – Pintura original asistida por IA por Gesner Deslandes",
            "artwork_title": "👶 “Nacimiento en el Liceo” – Mujer embarazada dando a luz en una escuela de refugiados, Puerto Príncipe",
            "description": "Frente al Lycee Du Cencenquantenaire (Lycee Des Jeunes Filles), una escuela que ahora sirve como refugio, una mujer embarazada negra haitiana yace en el suelo de cemento en la entrada principal, su vestido levantado, piernas abiertas, tratando de dar a luz. Un hombre a su izquierda (con camiseta y jeans azules) y una mujer a su derecha (con vestido colorido) la ayudan a respirar y a entregar al bebé sin asistencia médica. Otros haitianos negros están en el fondo cerca del edificio, observando. Algunos hombres usan camisas con jeans negros; otros usan camisetas con jeans azules. Las mujeres usan vestidos normales de varios colores. En cada balcón del edificio, familias desplazadas han colgado ropa, camisas, pantalones, vestidos y alfombras para secar bajo el sol. El edificio tiene el nombre 'Lycee Du Cencenquantenaire' visible. La escena es realista, emocionalmente poderosa, con luz cálida que proyecta sombras. Sin lluvia, solo un día soleado.",
            "artist": "Artista: Gesner Deslandes",
            "company": "GlobalInternet.py",
            "phone": "📞 +509 4738-5663",
            "email": "✉️ deslandes78@gmail.com",
            "website": "🌐 https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/",
            "regenerate_btn": "🎨 Regenerar pintura (nueva versión)",
            "print_btn": "🖨️ Imprimir esta obra para exposición",
            "download_btn": "💾 Descargar esta pintura (PNG)",
            "footer": "© 2026 GlobalInternet.py – Software de exhibición de arte digital mejorado con IA",
            "loading": "🎨 Creando su pintura... Espere (20-30 segundos).",
            "error": "Error al generar la pintura. Verifique su conexión a internet e intente de nuevo.",
            "sidebar_title": "🌐 Idioma",
            "sidebar_instruction": "Seleccione su idioma",
            "img_caption": "« Nacimiento en el Liceo » – Pintura original",
            "history_title": "📚 Historial de pinturas",
            "download_history_btn": "💾 Descargar",
            "clear_history_btn": "🗑️ Borrar historial",
            "no_history": "No hay pinturas guardadas. Genere algunas para verlas aquí."
        },
        "ht": {
            "gallery_title": "GlobalInternet.py Galeri D'Art",
            "subtitle": "'Nesans nan Lise a' – Tablo orijinal asisté pa IA pa Gesner Deslandes",
            "artwork_title": "👶 “Nesans nan Lise a” – Fanm ansent ap akouche devan yon lekòl refijye, Pòtoprens",
            "description": "Devan Lycee Du Cencenquantenaire (Lycee Des Jeunes Filles), yon lekòl kounye a se yon abri refijye, yon fanm ansent nwa Ayisyèn kouche sou tè konkrè a devan pòtay prensipal la, rad li leve, janm louvri, ap eseye akouche. Yon gason sou bò gòch li (ki mete t‑chèz ak pantalon ble) ak yon fanm sou bò dwat li (ki mete yon rad kolore) ede l respire ak delivre tibebe a san asistans medikal. Lòt moun nwa Ayisyen yo kanpe nan dèyè bò bilding lan, ap gade. Gen gason ki mete chemiz ak pantalon nwa, gen lòt ki mete t‑chèz ak pantalon ble. Fanm yo mete rad nòmal ak koulè diferan. Sou chak galri bilding lan, fanmi deplase yo pandye rad, chemiz, pantalon, wòb, ak tapi pou seche anba solèy la. Bilding lan gen non 'Lycee Du Cencenquantenaire' klèman vizib. Sèn nan reyalis, fò anpil emosyon, ak limyè cho ki bay lonbraj. Pa gen lapli, sèlman yon jou solèy.",
            "artist": "Atis: Gesner Deslandes",
            "company": "GlobalInternet.py",
            "phone": "📞 +509 4738-5663",
            "email": "✉️ deslandes78@gmail.com",
            "website": "🌐 https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/",
            "regenerate_btn": "🎨 Rekree tablo a (nouvo vèsyon)",
            "print_btn": "🖨️ Enprime travay sa a pou egzibisyon",
            "download_btn": "💾 Telechaje tablo sa a (PNG)",
            "footer": "© 2026 GlobalInternet.py – Lojisyèl egzibisyon atis dijital avèk IA",
            "loading": "🎨 Kreyasyon tablo a... Tanpri tann (20-30 segonn).",
            "error": "Pa t kapab kreye tablo a. Tcheke koneksyon entènèt ou epi eseye ankò.",
            "sidebar_title": "🌐 Lang",
            "sidebar_instruction": "Chwazi lang ou",
            "img_caption": "'Nesans nan Lise a' – Tablo Orijinal",
            "history_title": "📚 Istorik tablo yo",
            "download_history_btn": "💾 Telechaje",
            "clear_history_btn": "🗑️ Efase istorik",
            "no_history": "Pa gen tablo ki sove. Kreye kèk pou wè yo isit la."
        }
    }
    return texts[lang]

# ---------- CUSTOM CSS (unchanged) ----------
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
        .print-only { display: block !important; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- VERY DETAILED PROMPT FOR THE NEW PAINTING ----------
prompt = (
    "Oil painting, fine art, realistic style, photorealistic. The scene is set in Port‑au‑Prince, Haiti, on a bright sunny day (no rain). "
    "In the background stands a large multi‑story concrete school building named 'Lycee Du Cencenquantenaire' (also known as Lycee Des Jeunes Filles). "
    "The name 'Lycee Du Cencenquantenaire' is clearly written on the building. The building has several balconies on each floor. "
    "On every balcony, displaced families have hung clothes to dry: shirts, t‑shirts, pants, dresses, and sleeping rugs. "
    "In the foreground, at the main entrance yard, a pregnant Black Haitian woman lies on the concrete ground. "
    "She is wearing a dress, her legs are open, her belly is very large, and she is actively trying to give birth. "
    "Beside her, only two people are helping: a Black Haitian man on her left (wearing a t‑shirt and blue jeans), and a Black Haitian woman on her right (wearing a colorful dress). "
    "They are kneeling and assisting her to breathe and deliver the baby without any medical equipment. "
    "No other people are in the immediate foreground. "
    "In the background (near the building and on the sides), several other Black Haitians are standing and watching. "
    "Among those background figures, some men wear shirts with black jeans, others wear t‑shirts with blue jeans. "
    "The women in the background wear normal dresses of various colors. "
    "All people have realistic skin tones (Black), natural faces, complete arms and hands with five fingers. "
    "The ground is concrete, warm sunlight casts soft shadows. The mood is tense but hopeful, capturing the harsh reality of life in a displaced camp. "
    "High detail, professional gallery quality, emotionally powerful."
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

def pil_to_bytes(img, format="PNG"):
    buf = BytesIO()
    img.save(buf, format=format)
    return buf.getvalue()

# ---------- SESSION STATE ----------
if "painting_img" not in st.session_state:
    with st.spinner("🎨 Creating your painting... Please wait (may take 20-30 seconds)."):
        st.session_state.painting_img = generate_painting(prompt)
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
            file_name=f"birth_lyceum_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}_{idx}.png",
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
                st.session_state.painting_img = generate_painting(prompt)
                st.rerun()
    with col_btn2:
        if st.session_state.painting_img is not None:
            img_bytes = pil_to_bytes(st.session_state.painting_img)
            st.download_button(
                label=t['download_btn'],
                data=img_bytes,
                file_name=f"birth_lyceum_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png",
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
