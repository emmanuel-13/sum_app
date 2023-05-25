import streamlit as st
import joblib
import pandas as pd
import pyttsx4


def speak(speaker):
    word = pyttsx4.init()
    word.say(speaker)
    word.runAndWait()

def main():
    html = "<div style='background-color: blue'> <h2 style='text-align: center'> Fitting Prediciton App </h2></div>"
    st.write(html, unsafe_allow_html=True)

    model = joblib.load('person_attribute')

    sex = st.selectbox("Sex", ("Male", "Female"))
    if sex == "Male":
        s1 = 1
    else:
        s1 = 0

    age = st.slider("select your age", 5,18)

    fat = st.selectbox("Are you fat",("Yes", "No"))
    if fat == "Male":
        f1 = 1
    else:
        f1 = 0

    b = st.button("predict")

    if b:
        data = model.predict([[s1,f1,age]])
        st.balloons()
        c  = st.success(f'the predicted outcome is {data[0]}')
        # st.table({'Sex': sex, 'Age': age, 'Fat': fat})


if __name__ == "__main__":
    main()