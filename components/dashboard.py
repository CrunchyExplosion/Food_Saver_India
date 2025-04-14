import streamlit as st
import time
import os
from PIL import Image

def show_dashboard():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Inventory Items", len(st.session_state.inventory))
    with col2:
        st.metric("Active Alerts", sum(1 for item in st.session_state.inventory.itertuples() 
                  if item.Days_Left <= 10))
    
    # Image Carousel
    st.subheader("Food Preservation Techniques")
    image_folder = "assets/"
    images = [f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg' , '.webp'))]
    
    if 'carousel_index' not in st.session_state:
        st.session_state.carousel_index = 0
    
    cols = st.columns([1, 4, 1])
    with cols[0]:
        if st.button("←"):
            st.session_state.carousel_index = (st.session_state.carousel_index - 1) % len(images)
    with cols[2]:
        if st.button("→"):
            st.session_state.carousel_index = (st.session_state.carousel_index + 1) % len(images)
    
    with cols[1]:
        current_image = Image.open(os.path.join(image_folder, images[st.session_state.carousel_index]))
        st.image(current_image, use_container_width=True)
    
    # Auto-advance every 3 seconds
    time.sleep(3)
    st.session_state.carousel_index = (st.session_state.carousel_index + 1) % len(images)
    st.rerun()