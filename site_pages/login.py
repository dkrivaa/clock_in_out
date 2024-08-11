import streamlit as st


login = st.text_input('Enter Password', type='password', placeholder='Enter Password')

if login != '':
    if login == st.secrets['PASSWORD']:
        st.switch_page('site_pages/home.py')

    else:
        st.warning('Incorrect Password')

