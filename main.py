import streamlit as st
import pandas as pd


pg = st.navigation(
   [st.Page('site_pages/login.py', title='Login', default=True),
    st.Page('site_pages/home.py', title='Home'),
    st.Page('site_pages/customers.py', title='Customers'),]
)

pg.run()

