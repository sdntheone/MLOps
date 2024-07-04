import streamlit as st
st.title('futureai')

col1,col2=st.columns(2)

with col1:
    st.image('scenery.jpg')
with col2:
    st.write('''A serene landscape unfolds, where rolling hills gently rise and fall, their verdant slopes cloaked in 
    a lush carpet of emerald green. Majestic trees, their branches swaying gracefully in the breeze, 
    frame the horizon with a tapestry of rustling leaves.''' )