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
            "subtitle": "'Soccer Boys' – Original AI‑assisted painting by Gesner Deslandes",
            "artwork_title": "⚽ “Soccer Boys” – Two Boys Playing with a Sock Ball in Camp City, Under the Rain",
            "description": "Two bare‑chested Haitian boys, wearing only short pants, play soccer in a muddy camp city under heavy rain. One round black ball made of several rolled‑up socks sits at the feet of the boy on the right. The boy on the left is running toward him. They have created their own small soccer field with two makeshift goals – each made from short sticks or scrap wood. The boys' feet splash in puddles, their laughter echoing through the tarps and corrugated metal homes behind them. The boy on the right has a completely realistic body: two arms, two hands with five fingers, two legs, two feet with toes, and a normal left arm. His face shows concentration. The boy on the left is also fully proportioned. Despite the poverty and rain, their joy is unstoppable. This painting captures creativity, resilience, and pure love for soccer.",
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
            "img_caption": "'Soccer Boys' – Original Painting",
            "history_title": "📚 Painting History",
            "download_history_btn": "💾 Download",
            "clear_history_btn": "🗑️ Clear history",
            "no_history": "No paintings saved yet. Generate some to see them here."
        },
        "fr": {
            "gallery_title": "Galerie d'art GlobalInternet.py",
            "subtitle": "« Soccer Boys » – Peinture originale assistée par IA par Gesner Deslandes",
            "artwork_title": "⚽ « Soccer Boys » – Deux garçons jouant avec un ballon en chaussettes sous la pluie, camp ville",
            "description": "Deux garçons torse nu, portant seulement des shorts, jouent au football dans une ville de campement boueuse sous une forte pluie. Un ballon rond noir fait de plusieurs chaussettes roulées repose aux pieds du garçon de droite. Le garçon de gauche court vers lui. Ils ont créé leur propre petit terrain avec deux buts de fortune – faits de bâtons courts ou de bois de récupération. Les pieds des garçons éclaboussent les flaques, leurs rires résonnent à travers les bâches et tôles ondulées derrière eux. Le garçon de droite a un corps complètement réaliste : deux bras, deux mains avec cinq doigts, deux jambes, deux pieds avec orteils, et un bras gauche normal. Son visage montre de la concentration. Le garçon de gauche est aussi bien proportionné. Malgré la pauvreté et la pluie, leur joie est inarrêtable. Cette peinture capture la créativité, la résilience et l'amour pur du football.",
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
            "img_caption": "« Soccer Boys » – Peinture originale",
            "history_title": "📚 Historique des peintures",
            "download_history_btn": "💾 Télécharger",
            "clear_history_btn": "🗑️ Effacer l'historique",
            "no_history": "Aucune peinture sauvegardée. Générez-en pour les voir ici."
        },
        "es": {
            "gallery_title": "Galería de arte GlobalInternet.py",
            "subtitle": "« Soccer Boys » – Pintura original asistida por IA por Gesner Deslandes",
            "artwork_title": "⚽ “Soccer Boys” – Dos niños jugando con un balón de calcetines bajo la lluvia, ciudad de campamento",
            "description": "Dos niños desnudos de cintura para arriba, con pantalones cortos, juegan al fútbol en una ciudad de campamento llena de barro bajo una fuerte lluvia. Un balón redondo negro hecho de varios calcetines enrollados está a los pies del niño de la derecha. El niño de la izquierda corre hacia él. Han creado su propio pequeño campo con dos porterías improvisadas de palos o madera reciclada. Los pies de los niños salpican charcos, sus risas resuenan entre las lonas y chapas de metal corrugado detrás de ellos. El niño de la derecha tiene un cuerpo completamente realista: dos brazos, dos manos con cinco dedos, dos piernas, dos pies con dedos, y un brazo izquierdo normal. Su rostro muestra concentración. El niño de la izquierda también está bien proporcionado. A pesar de la pobreza y la lluvia, su alegría es imparable. Esta pintura captura creatividad, resiliencia y amor puro por el fútbol.",
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
            "img_caption": "« Soccer Boys » – Pintura original",
            "history_title": "📚 Historial de pinturas",
            "download_history_btn": "💾 Descargar",
            "clear_history_btn": "🗑️ Borrar historial",
            "no_history": "No hay pinturas guardadas. Genere algunas para verlas aquí."
        },
        "ht": {
            "gallery_title": "GlobalInternet.py Galeri D'Art",
            "subtitle": "'Soccer Boys' – Tablo orijinal asisté pa IA pa Gesner Deslandes",
            "artwork_title": "⚽ “Soccer Boys” – De ti gason ap jwe foutbòl ak yon boul chosèt anba lapli, nan kan vil",
            "description": "De ti gason san chemiz, ki mete sèlman bout pantalon, ap jwe foutbòl nan yon vil kan labou anba gwo lapli. Yon boul wonn nwa ki fèt ak plizyè chosèt woule chita sou pye ti gason ki sou bò dwat la. Ti gason sou bò gòch la ap kouri al bò kote l. Yo kreye ti teren pa yo ak de biyo pwovizwa fèt ak ti branch bwa. Pye yo ap vole nan flak dlo, ri yo ap fè eko nan twal ak tòl dèyè yo. Ti gason sou bò dwat la gen yon kò totalman reyalis: de bra, de men ak senk dwèt, de janm, de pye ak zòtèy, ak yon bra gòch nòmal. Figi l montre konsantrasyon. Ti gason sou bò gòch la byen pwopòsyonè tou. Malgre povrete ak lapli, kè kontan yo pa ka rete. Tablo sa a montre kreyativite, rezistans, ak renmen foutbòl.",
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
            "img_caption": "'Soccer Boys' – Tablo Orijinal",
            "history_title": "📚 Istorik tablo yo",
            "download_history_btn": "💾 Telechaje",
            "clear_history_btn": "🗑️ Efase istorik",
            "no_history": "Pa gen tablo ki sove. Kreye kèk pou wè yo isit la."
        }
    }
    return texts[lang]

# ---------- CSS (unchanged) ----------
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

# ---------- ENHANCED PROMPT FOR REALISTIC ARMS AND HANDS ----------
prompt = (
    "Oil painting, fine art, realistic style. Two Haitian boys, age 8-12, bare-chested, wearing only short ripped pants, "
    "playing soccer in a muddy camp city under heavy rain. The scene shows exactly two boys: one on the left, one on the right. "
    "There is only one ball. The ball is a round black ball made of several rolled-up black socks. The ball is positioned at the feet of the boy on the right. "
    "The boy on the right is standing with the ball at his feet, about to kick it. He has a completely realistic, well-proportioned human body. "
    "His arms and hands are perfectly normal: two arms, each with a hand that has five distinct fingers, no deformities, no missing fingers, no extra fingers. "
    "His left arm is normal, fully attached, with a hand and five fingers. His right arm is also normal. His legs and feet are normal. "
    "His face shows concentration, realistic skin texture, and natural expression. The boy on the left is running toward the ball; he also has realistic arms and hands with five fingers each, normal proportions. "
    "Two small makeshift goals made of sticks and scrap wood visible. Behind them: tarps and corrugated metal shacks. Splashing puddles, rain streaks, "
    "warm earthy colors, dramatic lighting. High detail, professional gallery quality, photorealistic human figures. No distorted anatomy, no missing fingers, no extra limbs. "
    "The painting must clearly show the fingers on both boys' hands, and the arms must look natural and anatomically correct."
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
            file_name=f"soccer_boys_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}_{idx}.png",
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
                file_name=f"soccer_boys_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png",
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
