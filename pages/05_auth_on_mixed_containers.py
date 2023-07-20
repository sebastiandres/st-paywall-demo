import streamlit as st
from st_paywall.google_auth import login_button, get_user_email, logout_button 

with st.echo("below"):
    # Code:
    # Login button on main body
    login_button()
    # Logout on a column
    c1, c2, c3 = st.columns(3)
    c1.button("Click me")
    c2.button("Click me 2")
    with c3:
        logout_button()
    # Get user email
    email = get_user_email()
    st.write(f"Logged in as {email}")