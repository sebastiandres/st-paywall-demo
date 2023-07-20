import streamlit as st
from st_paywall.google_auth import login_button, get_user_email, logout_button 

with st.echo("below"):
    with st.sidebar:
        login_button()
        logout_button()
    # Now do something
    email = get_user_email()
    st.write(f"Logged in as {email}")
