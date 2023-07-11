import streamlit as st
from helpers import sidebar; sidebar()

if st.session_state.user_logged_in and st.session_state.user_subscribed:
    st.title('You are in the LoggedIn+Subcribed Content Page')
    st.write('Congrats! You are logged in and subscribed')
    st.snow()
else:
    if not st.session_state.user_logged_in:
        st.warning('You need to login to see this content')
    if not st.session_state.user_subscribed:
        st.warning('You need to subscribe to see this content')