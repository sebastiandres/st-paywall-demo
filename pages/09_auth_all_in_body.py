import streamlit as st
from st_paywall.auth import authenticate , get_user_email

with st.echo("below"):
    authenticate()
    user_email = get_user_email()
    st.write(f"User email: {user_email}")
