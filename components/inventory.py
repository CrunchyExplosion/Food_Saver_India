import streamlit as st
import pandas as pd
import datetime

def calculate_expiry_status(expiry_date):
    today = datetime.date.today()
    delta = expiry_date - today
    return delta.days

def manage_inventory():
    st.subheader("Real-Time Inventory Update ⏱️")
    
    # Initialize inventory in session state
    if "inventory" not in st.session_state:
        st.session_state.inventory = pd.DataFrame(columns=["Item", "Quantity", "Expiry_Date", "Location", "Temperature", "Humidity"])
    
    # Add/Edit Inventory
    with st.expander("Manage Inventory Items 🛠️"):
        edit_col, delete_col = st.columns(2)
        
        with edit_col:
            st.markdown("### Add/Edit Item")
            with st.form("inventory_form"):
                item = st.text_input("Item Name")
                quantity = st.number_input("Quantity (kg)", min_value=1)
                expiry = st.date_input("Expiry Date", datetime.date.today())
                loc = st.selectbox("Location", ["Delhi", "Mumbai", "Bengaluru", "Chennai", "Kolkata"])
                temp = st.slider("Storage Temperature (°C)", -10, 40, 25)
                humidity = st.slider("Humidity (%)", 0, 100, 60)
                
                if st.form_submit_button("Save Item"):
                    new_entry = pd.DataFrame({
                        "Item": [item],
                        "Quantity": [quantity],
                        "Expiry_Date": [expiry],
                        "Location": [loc],
                        "Temperature": [temp],
                        "Humidity": [humidity]
                    })
                    
                    # Update if item exists, else add new
                    if item in st.session_state.inventory["Item"].values:
                        st.session_state.inventory.loc[st.session_state.inventory["Item"] == item, ["Quantity", "Expiry_Date", "Location", "Temperature", "Humidity"]] = [quantity, expiry, loc, temp, humidity]
                    else:
                        st.session_state.inventory = pd.concat([st.session_state.inventory, new_entry], ignore_index=True)
                    
                    st.success(f"Item '{item}' added/updated successfully!")
        
        with delete_col:
            st.markdown("### Delete Item")
            if not st.session_state.inventory.empty:
                item_to_delete = st.selectbox("Select item to delete", 
                    st.session_state.inventory["Item"].unique())
                if st.button("Delete Item"):
                    st.session_state.inventory = st.session_state.inventory[
                        st.session_state.inventory["Item"] != item_to_delete
                    ]
                    st.success(f"Item '{item_to_delete}' deleted successfully!")
    

    
    # Inventory Table
    st.subheader("Current Inventory")
    if not st.session_state.inventory.empty:
        inventory = st.session_state.inventory.copy()
        inventory['Days_Left'] = inventory['Expiry_Date'].apply(calculate_expiry_status)
        
        # Edit existing items
        edited_df = st.data_editor(
            inventory,
            column_config={
                "Days_Left": st.column_config.ProgressColumn(
                    "Days Left",
                    help="Days until expiry",
                    format="%d days",
                    min_value=0,
                    max_value=100,
                )
            },
            use_container_width=True
        )

    # Inventory Map
    st.subheader("Inventory Locations")
    if not st.session_state.inventory.empty:
        location_coords = {
            "Delhi": (28.6139, 77.2090),
            "Mumbai": (19.0760, 72.8777),
            "Bengaluru": (12.9716, 77.5946),
            "Chennai": (13.0827, 80.2707),
            "Kolkata": (22.5726, 88.3639)
        }
        
        inventory = st.session_state.inventory.copy()
        inventory[['lat', 'lon']] = inventory['Location'].apply(lambda x: pd.Series(location_coords[x]))
        
        st.map(inventory)
        
        # Update session state with edited data
        st.session_state.inventory = edited_df.drop(columns=['lat', 'lon'], errors='ignore')
    else:
        st.info("No inventory items added yet")