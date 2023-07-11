import streamlit as st
from helpers import sidebar; sidebar()

if st.session_state.user_logged_in:
    
    st.title('Logged In Content Page')
    st.write('Congrats! You are logged in')
    st.balloons()
else:
    st.warning('You need to login to see this content')
