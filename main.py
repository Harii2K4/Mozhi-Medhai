import streamlit as st
from withtextrecog import recognize_speech_multi_language
from text_speech import text_speech
from azure_translation import translation
import time
import os

def main():
    st.set_page_config(page_title="Multilingual Speech Assistant", page_icon="🌐", layout="wide")

    st.title("🎙️ Multilingual Speech Assistant 🗣️")
    st.markdown("---")

    # Initialize session state variables
    if 'recognized_text' not in st.session_state:
        st.session_state.recognized_text = ""
    if 'source_language' not in st.session_state:
        st.session_state.source_language = ""
    if 'translated_text' not in st.session_state:
        st.session_state.translated_text = ""

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📥 Speech Input")
        
        # Add dropdown for input language selection
        input_language = st.selectbox(
            "Select input language",
            ["Auto-detect", "English", "Tamil"],
            key="input_language"
        )
        
        # Assign language code based on selection
        if input_language == "Tamil":
            language_code = "ta-IN"
        elif input_language == "English":
            language_code = "en-IN"
        else:
            language_code = None
        
        if st.button("🎤 Start Speech Recognition", key="speech_recognition"):
            with st.spinner("🎧 Listening..."):
                recognized_text, source_language = get_valid_speech(language_code)
                if recognized_text is not None:
                    st.session_state.recognized_text = recognized_text
                    st.session_state.source_language = source_language

        if st.session_state.recognized_text:
            st.info(f"🗣️ Recognized Text: {st.session_state.recognized_text}")
            st.success(f"🌍 Source Language: {st.session_state.source_language}")

    with col2:
        st.subheader("📤 Translation and Speech Output")
        if st.session_state.recognized_text:
            if st.button("🔄 Translate", key="translate"):
                with st.spinner("📚 Translating..."):
                    st.session_state.translated_text = translation(st.session_state.recognized_text,input_language)

            if st.session_state.translated_text:
                st.info(f"🇮🇳 Translated Text (Tamil): {st.session_state.translated_text}")

                if st.button("🔊 Convert to Speech", key="text_to_speech"):
                    with st.spinner("🎵 Converting to speech..."):
                        output_file = text_speech(st.session_state.translated_text)
                    if output_file and os.path.exists(output_file):
                        st.success("🎉 Speech conversion complete!")
                        st.audio(output_file)

    st.markdown("---")
    st.subheader("📝 Instructions")
    st.markdown("""
    1. Select the input language from the dropdown (Auto-detect, English, or Tamil).
    2. Click on 'Start Speech Recognition' to begin speaking.
    3. Once your speech is recognized, you'll see the text and detected language.
    4. Click 'Translate to Tamil' to get the Tamil translation.
    5. Finally, click 'Convert to Speech' to hear the Tamil translation.
    6. Say 'bye' to exit the program.
    """)
    
    st.markdown("---")
    st.subheader("📝 வழிமுறைகள்")
    st.markdown("""
    1. உள்ளீட்டு மொழியை (தானாக கண்டறிதல், ஆங்கிலம், அல்லது தமிழ்) கீழேயுள்ள மெனுவில் இருந்து தேர்வு செய்யவும்.
    2. 'தொடங்கு உரை அறிவிப்பு' என்பதைக் கிளிக் செய்து பேசத் தொடங்கவும்.
    3. உங்கள் பேச்சு அடையாளம் காணப்பட்டவுடன், உரை மற்றும் கண்டறியப்பட்ட மொழி காண்பிக்கும்.
    4. 'தமிழுக்கு மொழிபெயர்ப்பு' என்பதைக் கிளிக் செய்து தமிழ் மொழிபெயர்ப்பைப் பெறவும்.
    5. கடைசியாக, 'உரை பேச மாற்று' என்பதைக் கிளிக் செய்து தமிழ் மொழிபெயர்ப்பை கேட்கவும்.
    6. 'பை' என்று சொல்கின்ற முறைமையை முடிக்கவும்.
    """)


    # Exit condition
    if "bye" in st.session_state.recognized_text.lower():
        st.warning("👋 Exiting the program. Goodbye!")
        time.sleep(2)
        st.stop()

def get_valid_speech(language_code):
    max_attempts = 3
    for attempt in range(max_attempts):
        recognized_text, source_language = recognize_speech_multi_language(language_code)
        if recognized_text is not None:
            return recognized_text, source_language
        st.error(f"❌ Speech recognition failed. Attempt {attempt + 1}/{max_attempts}. Please try again.")
        time.sleep(1)
    return None, None

if __name__ == "__main__":
    main()