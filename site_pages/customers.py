import streamlit as st
import time

import engine

st.subheader('Add new Customer')

name = st.text_input(label='Enter Name', )
st.divider()

if name != '':
    submit = st.button('Submit', type='primary')
    if submit:
        answer = engine.new_customer(name)

        if answer == 'Customer Added':
            st.subheader(answer)
            time.sleep(3)
            st.switch_page('site_pages/home.py')

