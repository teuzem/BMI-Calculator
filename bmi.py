import streamlit as st
st.title("BMI Calculator")

weight = st.number_input("Enter your weight in Kg")
status = st.radio("Select your height format:",('cms', 'meters', 'feet'))


try:
    if status == 'cms':
        height = st.number_input('Enter your height in cm')
        bmi = weight/((height)**2)

    elif status == 'meters':
        height = st.number_input('Enter your height in meters')
        bmi = weight/((height)**2)

    elif status == 'feet':
        height = st.number_input('Enter your height in feet')
        bmi = weight/((height/3.28)**2)
except:
    print("Zero division error")

if (st.button('Calculate BMI')):
    st.write(f'Your BMI index is {round(bmi)}')

    if bmi < 18.5:
        st.warning('You are underweight')
    elif (bmi >= 18.5 and bmi < 24.9):
        st.success('You are healthy')
    elif (bmi >= 24.9 and bmi < 29.9):
        st.error('You are overweight')
    elif(bmi > 30):
        st.warning('You are extremly overweight')





    


