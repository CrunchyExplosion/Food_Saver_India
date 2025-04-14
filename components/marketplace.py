import streamlit as st
import pandas as pd

def show_marketplace():
    st.subheader("Smart Redistribution Marketplace")
    
    if not st.session_state.inventory.empty:
        # Display marketplace listings
        st.dataframe(
            st.session_state.inventory[['Item', 'Quantity', 'Location', 'Days_Left']],
            use_container_width=True
        )
        
        # Marketplace Map
        st.subheader("Available Stock Locations")
        location_coords = {
            "Delhi": (28.6139, 77.2090),
            "Mumbai": (19.0760, 72.8777),
            "Bengaluru": (12.9716, 77.5946),
            "Chennai": (13.0827, 80.2707),
            "Kolkata": (22.5726, 88.3639)
        }
        
        inventory = st.session_state.inventory.copy()
        inventory[['lat', 'lon']] = inventory['Location'].apply(
            lambda x: pd.Series(location_coords[x]))
        
        st.map(inventory)
    else:
        st.info("No inventory items available for marketplace")