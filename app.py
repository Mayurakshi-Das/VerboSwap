from gtts import gTTS
import streamlit as st
from translator import translate_text

st.set_page_config(page_title="PolyglotPal - Translator", page_icon="🌐")

# Styling
st.markdown(
    """
    <style>
        .stApp {
            background-color: #f4f4f4;
            color: #1a1a1a;
        }
        .css-18e3th9 {
            padding: 2rem 1rem 1rem 1rem;
        }
        .stTextArea textarea {
            font-size: 16px;
            color: #000000;  /* Text color: Black */
            background-color: #FFFFFF;  /* Background color: White */
        }
        h1, h2, h3, h4, h5, h6 {
            color: #1a1a1a !important;
        }
        .stSelectbox label, .stTextArea label {
            color: #1a1a1a !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# App title and subtitle
st.title("🌐 Verboswap – A Real-Time Translator")
st.markdown(
    "<h4 style='color: gray;'>Learn something  NEW ✨</h4>",
    unsafe_allow_html=True
)

# Language options
languages = {
    '🇮🇳 Hindi': 'hi',
    '🇫🇷 French': 'fr',
    '🇪🇸 Spanish': 'es',
    '🇩🇪 German': 'de',
    '🇯🇵 Japanese': 'ja',
    '🇨🇳 Chinese (Simplified)': 'zh-cn',
    '🇷🇺 Russian': 'ru',
    '🇸🇦 Arabic': 'ar',
    '🇰🇷 Korean': 'ko',
    '🇺🇸 English': 'en'
}

# Set defaults if not already in session state
if "source_lang" not in st.session_state:
    st.session_state.source_lang = '🇺🇸 English'
if "target_lang" not in st.session_state:
    st.session_state.target_lang = '🇮🇳 Hindi'

# Swap handler
if "swap_triggered" not in st.session_state:
    st.session_state.swap_triggered = False

cols = st.columns([2, 1, 2])
with cols[0]:
    source_lang = st.selectbox(
        "Source Language",
        list(languages.keys()),
        index=list(languages.keys()).index(st.session_state.source_lang),
        key="source_lang_widget"
    )
with cols[1]:
    if st.button("🔄 Swap"):
        # Swap values in session_state
        st.session_state.source_lang, st.session_state.target_lang = (
            st.session_state.target_lang,
            st.session_state.source_lang,
        )
        st.rerun()
with cols[2]:
    target_lang = st.selectbox(
        "Target Language",
        list(languages.keys()),
        index=list(languages.keys()).index(st.session_state.target_lang),
        key="target_lang_widget"
    )

# Update session_state based on selection
st.session_state.source_lang = source_lang
st.session_state.target_lang = target_lang

source_code = languages[st.session_state.source_lang]
target_code = languages[st.session_state.target_lang]

# Text input
text_input = st.text_area("Enter text to translate:", height=150)

# Translate button
translate_button = st.button("🔁 Translate Now")

if translate_button and text_input.strip():
    output = translate_text(text_input, source_language=source_code, dest_language=target_code)

    if "Error" in output:
        st.error(output)
    else:
        st.markdown("#### ✅ Translated Output:")
        st.write(output)

        tts = gTTS(text=output, lang=target_code)
        tts.save("translated_output.mp3")
        st.audio("translated_output.mp3", format="audio/mp3")

else:
    if not translate_button:
        st.info("⏳ Click the 'Translate Now' button to see the result.")
    else:
        st.info("⏳ Start typing to see translation.")

