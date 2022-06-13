from pages.about_diabetes import show_about_diabetes_page
from pages.home_page import show_home_page
from pages.predict_page import show_predict_page
import streamlit as st

# Create a page dropdown
page = st.selectbox("Choose your page", ["Home Page", "Predict Page", "More About Diabetes"])
if page == "Home Page":
    # Display details of page 1
    show_home_page()
elif page == "Predict Page":
    # Display details of page 2
    show_predict_page()
elif page == "More About Diabetes":
    # Display details of page 3
    show_about_diabetes_page()

