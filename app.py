import os
import streamlit as st
from utils.models import *
from dotenv import find_dotenv, load_dotenv





load_dotenv(find_dotenv())


def main():
    st.set_page_config(page_title = "Voice Storyteller",
                       page_icon= "🔊")
    

    st.title("🪄 AI Magic: Turn Any Image into an Audio Story")

    uploaded_file = st.file_uploader("Choose an image...", type = 'jpg')

    if uploaded_file is not None:
        print(uploaded_file)
        bytes_data = uploaded_file.getvalue()
        with open(uploaded_file.name, 'wb') as file:
            file.write(bytes_data)
        st.image(uploaded_file, caption = 'Uploaded Image.',
                 use_column_width=True,
                 width = 150)
        
        # button to handle story creation
        col1, col2, col3, col4, col5 = st.columns(5)
        if col3.button('Generate Story'):
            progress_bar = st.progress(0, text = "Loading the model...")
            scenario = img_to_text(uploaded_file.name)
            progress_bar.progress(33, text = "Generating a story") 
            story = text_to_speech(scenario)
            progress_bar.progress(66, text="Creating audio")
            speech_to_audio(story)
            progress_bar.progress(100)

            with st.expander("scenario"):
                st.write(scenario)
            with st.expander("story"):
                st.write(story)
            
            st.audio("audio.flac")


if __name__ == '__main__':
    main()