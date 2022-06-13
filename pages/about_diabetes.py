import streamlit as st
from PIL import Image


def show_about_diabetes_page():
    st.title("More About Diabetes")
    st.header("""Health Care & Diabetes""")
    st.markdown("***")
    col1, col2 = st.columns([2, 1])
    col1.header("What is Diabetes")
    col1.write("Diabetes is a lifelong condition that causes a person's blood sugar level to become too high.")

    col1.write("There are 2 main types of diabetes:")
    col1.write("-type 1 diabetes – where the body's immune system attacks and destroys the cells that produce insulin")
    col1.write("-type 2 diabetes – where the body does not produce enough insulin, or the body's cells do not react to insulin")
    col1.write("Type 2 diabetes is far more common than type 1. In the UK, around 90% of all adults with diabetes have type 2.")

    col1.write("During pregnancy, some women have such high levels of blood glucose that their body is unable to produce enough insulin to absorb it all. This is known as gestational diabetes.")
    image1 = Image.open('images/ComplicationsOfDiabetes.jpg')
    image2 = Image.open('images/types of diabetes.JPG')
    col2.image(image1)
    col2.image(image2)
    col1.header("When to see a doctor")
    col1.write("Visit your GP as soon as possible if you experience the main symptoms of diabetes, which include:")
    col1.write("-feeling very thirsty")
    col1.write("-peeing more frequently than usual, particularly at night")
    col1.write("-feeling very tired")
    col1.write("-weight loss and loss of muscle bulk")
    col1.write("-itching around the penis or vagina, or frequent episodes of thrush")
    col1.write("-cuts or wounds that heal slowly")
    col1.write("-blurred vision")
    col1.write("Type 1 diabetes can develop quickly over weeks or even days.")
    col1.write("Many people have type 2 diabetes for years without realising because the early symptoms tend to be general.")

    col1.header("Causes of diabetes")
    col1.write("The amount of sugar in the blood is controlled by a hormone called insulin, which is produced by the pancreas (a gland behind the stomach).")
    col1.write("When food is digested and enters your bloodstream, insulin moves glucose out of the blood and into cells, where it's broken down to produce energy.")
    col1.write("However, if you have diabetes, your body is unable to break down glucose into energy. This is because there's either not enough insulin to move the glucose, or the insulin produced does not work properly.")
    col1.write("There are no lifestyle changes you can make to lower your risk of type 1 diabetes.")
    col1.write("You can help manage type 2 diabetes through healthy eating, regular exercise and achieving a healthy body weight.")
