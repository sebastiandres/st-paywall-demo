import streamlit as st
from st_paywall.google_auth import login_button, get_user_email, logout_button 

with st.echo("below"):
    # Define the columns
    c1, c2, c3 = st.columns(3)
    c1.button("Click me")
    c2.button("Click me 2")
    with c3:
        login_button()
        logout_button()
    email = get_user_email()
    st.write(f"Logged in as {email}")