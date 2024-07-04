import streamlit as st
st.title('futureai')

col1,col2=st.columns(2)

with col1:
    st.image('mor.jpg')
with col2:
    st.write('''A serene landscape unfolds, where rolling hills gently rise and fall, their verdant slopes cloaked in 
    a lush carpet of emerald green. Majestic trees, their branches swaying gracefully in the breeze, 
    frame the horizon with a tapestry of rustling leaves.''' )

st.header('course offered')
st.subheader('python')
st.subheader('ml')
st.subheader('deep learning')
st.subheader('data analysis and machine learning')
st.subheader('DSA')
# st.subheader('mysql')
st.sidebar.title('Menu')
st.sidebar.markdown("""
- Home
- About
- Contact
- Career
- Login
""")

st.sidebar.selectbox('Select One',['teacher','student'])
st.sidebar.button('select')
st.title("Hello Teacher")