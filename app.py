import streamlit as st
from Pages import Home, Project1, Project2, Project3
from streamlit_navigation_bar import st_navbar

# Set page configuration
st.set_page_config(initial_sidebar_state="collapsed")

# Define pages for navigation
pages = ["Home", "Project1", "Project2", "Project3"]

# Define styles for the navigation bar
styles = {
    "nav": {
        "background-color": "rgb(123, 209, 146)",  # Corrected the color code
    },
    "div": {
        "max-width": "32rem",
    },
    "span": {
        "border-radius": "0.5rem",  # Corrected border-radius value
        "color": "rgb(49, 51, 63)",
        "margin": "0 0.125rem",
        "padding": "0.4375rem 0.625rem",
    },
    "active": {
        "background-color": "rgba(185, 114, 255, 0.25)",  # Fixed the alpha value
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",
    },
}

# Create the navigation bar with pages and styles
page = st_navbar(pages, styles=styles)

# Conditional rendering based on the selected page
if page == "Home":
    Home.Home().app()
elif page == "Project1":
    Project1.Project1().app()
elif page == "Project2":
    Project2.Project2().app()
elif page == "Project3":
    Project3.Project3().app()
else:
    Home.Home().app()
