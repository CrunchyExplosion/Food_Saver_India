import streamlit as st
from components import dashboard, inventory, marketplace, analytics
import pandas as pd

# Configure page
st.set_page_config(page_title="FoodSaver India", layout="wide", page_icon="🍎")

# Custom CSS for navigation
st.markdown("""
<style>
    .nav-container {
        display: flex;
        justify-content: space-around;
        margin: 1rem 0;
        border-bottom: 2px solid #4CAF50;
        padding-bottom: 0.5rem;
    }
    .nav-button {
        padding: 0.5rem 1rem;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.3s ease;
        background: none;
        font-size: 1.1rem;
    }
    .nav-button:hover {
        background: #4CAF50;
        color: white !important;
        transform: scale(1.05);
    }
    .nav-button.active {
        background: #4CAF50;
        color: white !important;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Initialize session state for navigation
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "Dashboard"
    
    # Main title
    st.title("🍎 FoodSaver India")
    st.markdown("## Reducing Food Waste Across India's Supply Chain using AI and web technologies")

    # Navigation bar with emoji thumbnails
    nav_cols = st.columns([1,1,1,1])
    pages = [
        ("📊 Dashboard", "Dashboard"),
        ("📦 Inventory", "Inventory Management"),
        ("🛒 Marketplace", "Smart Marketplace"),
        ("📈 Analytics", "Analytics")
    ]
    
    with st.container():
        cols = st.columns(4)
        for i, (emoji, page_name) in enumerate(pages):
            with cols[i]:
                if st.button(
                    emoji,
                    key=f"nav_{page_name}",
                    use_container_width=True,
                    help=page_name
                ):
                    st.session_state.current_page = page_name

    # Add custom class to active button using JavaScript
    st.markdown(f"""
    <script>
        document.querySelectorAll('button[data-testid="stButton"]').forEach(button => {{
            if (button.textContent.includes("{st.session_state.current_page.split()[0]}")) {{
                button.classList.add('active');
            }}
        }})
    </script>
    """, unsafe_allow_html=True)

    # Initialize session state for inventory
    if 'inventory' not in st.session_state:
        st.session_state.inventory = pd.DataFrame(columns=[
            'Item', 'Quantity', 'Expiry_Date', 'Location', 'Temperature', 'Humidity'
        ])

    # Page routing
    if st.session_state.current_page == "Dashboard":
        dashboard.show_dashboard()
    elif st.session_state.current_page == "Inventory Management":
        inventory.manage_inventory()
    elif st.session_state.current_page == "Smart Marketplace":
        marketplace.show_marketplace()
    elif st.session_state.current_page == "Analytics":
        analytics.show_analytics()

    # Footer
    st.markdown("""
    <div style='
        background-color: #4CAF50;
        padding: 15px;
        border-radius: 10px;
        margin-top: 3rem;
        text-align: center;
        color: white;
        font-size: 1.8rem;
    '>
        © 2025 FoodSaver India. All rights reserved. || Mentor : Dr. Sunita Varjani
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
