import streamlit as st
from st_paywall.google_auth import login_button, get_user_email, logout_button 

with st.echo("below"):
    login_button()
    email = get_user_email()
    logout_button()
    st.write(f"Logged in as {email}")