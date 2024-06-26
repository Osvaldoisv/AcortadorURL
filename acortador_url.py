import pyshorteners
import streamlit as st

def shorten_url(url):
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)
    return shortened_url

# creamos app web con streamlit
st.set_page_config(page_title="URL Shortener", page_icon="/", layout="centered")
st.image("images/www.png", use_column_width=True)
st.title("URL Shortener")
url = st.text_input("Enter the URL")
if st.button("Generate new UWL"):
    st.write("URL shortened: ", shorten_url(url))

# For running, type in console:
    # streamlit run acortador_url

# for stop (in VSCode):
    # Ctrl + C (in console)