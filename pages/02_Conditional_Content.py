import streamlit as st
from helpers import sidebar; sidebar()

st.title('Conditional Content')

st.write('This page is always available, but the features and content depend on the user login and subscription status')
c1, c2, c3 = st.columns(3)
free_slider_value = c1.slider('This is a free slider', 0, 10, 5)

logged_in_slider_value = c2.slider('Premium slider for logged in users', 0, 20, 10)
if not st.session_state.user_logged_in and logged_in_slider_value!=10:
    c2.warning('You need to be logged in to use this slider')
    logged_in_slider_value = 10

subscribed_slider_value = c3.slider('Premium slider for subscribed users', 0, 30, 15)
if not st.session_state.user_subscribed and subscribed_slider_value!=15:
    c3.warning('You need to be subscribed to use this slider')
    subscribed_slider_value = 15

st.write('The free slider value is', free_slider_value)
st.write('The logged in slider value is', logged_in_slider_value)
st.write('The subscribed slider value is', subscribed_slider_value)


