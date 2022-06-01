import pickle
import pandas as pd
import numpy as np
import streamlit as st

# data = pd.read_csv("./diabetes_binary_5050split_health_indicators_BRFSS2015.csv")

# I want to leave that attributes: HighBP, BMI,  Age, Education,  Income and of course the class attribute

# # these 11 attributes almost no effect on the modelling algorithms, so I dropped them
# data.drop(['CholCheck'], axis=1, inplace=True)
# data.drop(['Smoker'], axis=1, inplace=True)
# data.drop(['Stroke'], axis=1, inplace=True)
# data.drop(['HeartDiseaseorAttack'], axis=1, inplace=True)
# data.drop(['PhysActivity'], axis=1, inplace=True)
# data.drop(['Fruits'], axis=1, inplace=True)
# data.drop(['Veggies'], axis=1, inplace=True)
# data.drop(['Sex'], axis=1, inplace=True)
# data.drop(['HvyAlcoholConsump'], axis=1, inplace=True)
# data.drop(['AnyHealthcare'], axis=1, inplace=True)
# data.drop(['NoDocbcCost'], axis=1, inplace=True)
#
# # these 4 attributes are kinda effective, but I am choosing to drop them to increase user experience and usability.
# data.drop(['DiffWalk'], axis=1, inplace=True)
# data.drop(['HighChol'], axis=1, inplace=True)
# data.drop(['MentHlth'], axis=1, inplace=True)
# data.drop(['PhysHlth'], axis=1, inplace=True)
#
# # experimental
# # this attribute is so effective at models performance, but it is an attribute that already says the health status
# # of a person so i does not make sense to use it. it is like cheating. I dropped it as well.
# data.drop(['GenHlth'], axis=1, inplace=True)

#
# cols = list(data.columns)
# cols.remove("Diabetes_binary")
# sampled, target = SMOTE().fit_resample(data[cols], data["Diabetes_binary"])
# X_train, X_test, Y_train, Y_test = train_test_split(sampled[cols],
#                                                     target,
#                                                     test_size=0.1,
#                                                     shuffle=True)
#
# print("Train Feature Size : ", len(X_train))
# print("Train Label Size : ", len(Y_train))
# print("Test Feature Size : ", len(X_test))
# print("Test Label Size : ", len(Y_test))

# load the model
# load the model
# with open("model.pkl", "rb") as f:
#     pickled_model = pickle.load(f)

f = open("model.pkl", "rb")
pickled_model = pickle.load(f)
f.close()


st.set_page_config(layout="wide")


# Remove whitespace from the top of the page and sidebar
st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 0rem;
                    padding-bottom: 10rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
               .css-1d391kg {
                    padding-top: 3.5rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)


def show_predict_page():
    st.title("Diabetes Prediction")
    st.header("""We need some information to predict the diabetes""")
    st.markdown("***")
    col1, col2, col3 = st.columns(3)
    col1.subheader("Information of the Person")
    bmi = int(col1.text_input('Body Mass Index (BMI)', '21'))
    col2.subheader("-")
    age = int(col2.text_input('Age', '35'))
    income = int(col1.slider('Income Level', 1, 8, 3))
    highBP = col1.radio(
        "Do you have high blood pressure?",
        ('Yes', 'No'))

    if highBP == 'Yes':
        highBPasInt = 1
    else:
        highBPasInt = 0

    education = int(col2.slider('Education Level', 1, 6, 4))
    button_calculate = col1.button("Predict the Diabetes")
    if button_calculate:
        col1.write(f"You entered: BMI: {bmi}, Age: {age},\n\n "
                   f"Income Level: {income}, "
                   f"Education: {education}, HighBP: {highBP}")

        my_array = np.array([[highBPasInt, bmi, age, education, income]])
        df = pd.DataFrame(my_array, columns=['HighBP', 'BMI', 'Age', 'Education', 'Income'])
        result = pickled_model.predict(df)
        # col1.write(result)
        if result == 1:
            col1.write("**Probably have Diabetes**")
        else:
            col1.write("**Probably does not have Diabetes**")
        st.write("This estimations are %72 accurate and based on some other humans data.\n\n "
                 "This estimation does not specifies the truth. We recommend everyone to go to a hospital and "
                 "make a full check-up at regular intervals.")

    col3.write("Income Levels:\n")
    col3.write("1: Less than $10,000\n")
    col3.write("2: Less than $15,000\n")
    col3.write("3: Less than $20,000\n")
    col3.write("4: Less than $25,000\n")
    col3.write("5: Less than $35,000\n")
    col3.write("6: Less than $50,000\n")
    col3.write("7: Less than $75,000\n")
    col3.write("8: More than $75,000")
    col3.markdown("***")
    col3.write("Education Levels:\n\n"
               "1 = Never attended school or only kindergarten \n\n"
               "2 = Grades 1 through 8 (Elementary) \n\n"
               "3 = Grades 9 through 11 (Some high school) \n\n"
               "4 = Grade 12 or GED (High school graduate) \n\n"
               "5 = College 1 year to 3 years (Some college or technical school) \n\n"
               "6 = College 4 years or more (College graduate)")
    st.markdown("***")

#
# predicted = pickled_model.predict(X_test)
#
# print("pickled model")
# print("Train Accuracy : {:.2f} %".format(accuracy_score(pickled_model.predict(X_train), Y_train) * 100))
# print("Test Accuracy : {:.2f} %".format(accuracy_score(pickled_model.predict(X_test), Y_test) * 100))
#
# cm = confusion_matrix(Y_test, predicted)
# classes = ["0", "1"]
# disp = ConfusionMatrixDisplay(confusion_matrix=cm,
#                               display_labels=classes)
# fig, ax = plt.subplots(figsize=(10, 10))
# plt.title("Confusion Matrix")
# disp = disp.plot(ax=ax)
# plt.show()
#
# print(classification_report(predicted, Y_test))
# print("ACCURACY:", accuracy_score(Y_test, predicted))
# print("RECALL:", recall_score(Y_test, predicted, average="binary"))
# print("end")
# results = pickled_model.score(X_test, Y_test)
# print(results)

# attributes:
# INCOME2
# Variable is already ordinal with 1 being less than $10,000 all the
# way up to 8 being $75,000 or more
#
# 1 Less than $10,000
# Notes: If "no," code 02
# 18,449 4.21 5.12
# 2 Less than $15,000 ($10,000 to less than $15,000)
# Notes: If "no," code 03; if "yes," ask 01
# 19,599 4.47 4.51
# 3 Less than $20,000 ($15,000 to less than $20,000)
# Notes: If "no," code 04; if "yes," ask 02
# 26,797 6.12 6.55
# 4 Less than $25,000 ($20,000 to less than $25,000)
# Notes: If "no," ask 05; if "yes," ask 03
# 32,377 7.39 7.65
# 5 Less than $35,000 ($25,000 to less than $35,000)
# Notes: If "no," ask 06
# 39,235 8.95 8.77
# 6 Less than $50,000 ($35,000 to less than $50,000)
# Notes: If "no," ask 07
# 52,052 11.88 11.35
# 7 Less than $75,000 ($50,000 to less than $75,000)
# Notes: If "no," code 08
# 58,130 13.27 12.63
# 8 $75,000 or more

# Education level scale 1-6 1 = Never attended school or only kindergarten 2 = Grades 1 through
# 8 (Elementary) 3 = Grades 9 through 11 (Some high school) 4 = Grade 12 or GED (High school graduate) 5 = College 1
# year to 3 years (Some college or technical school) 6 = College 4 years or more (College graduate)
