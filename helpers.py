import streamlit as st

def sidebar():
    st.sidebar.title('Configurable status')
    # Initialize
    if 'user_logged_in' not in st.session_state:
        st.session_state.user_logged_in = False
    if 'user_subscribed' not in st.session_state:
        st.session_state.user_subscribed = False
    # Update if clicked
    user_logged_in = st.sidebar.checkbox('Login status', value=False)
    st.session_state.user_logged_in = user_logged_in
    user_subscribed = st.sidebar.checkbox('Subscription status', value=False)
    st.session_state.user_subscribed = user_subscribed
    return