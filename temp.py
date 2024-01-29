import numpy as np
import pickle
import streamlit as st
from twilio.rest import Client

# loading the saved model
loaded_model = pickle.load(open('E:/Capstone Project/New folder/dt1.sav', 'rb'))

# Twilio credentials
account_sid = 'AC92b4c5e80eb832845a03464f67afbb8e'
auth_token = '41a0ab4741669c59bc72cbdc9543c6a9'
client = Client(account_sid, auth_token)
twilio_phone_number = '+17733581082'  # Twilio phone number

# creating a function for Prediction
def Heart_stroke_prediction(input_data,phone):
    input_data1 = [float(value) for value in input_data]

    # changing the input_data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data1[:11])

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if prediction[0] == 1:
        send_alert_message(phone)
        return 'High chances of heart stroke'
    else:
        return 'Low chances of heart Stroke'

def send_alert_message(phone_number):
    # Your Twilio phone number and the patient's phone number
    message = client.messages.create(
        body='High chances of Heart Stroke. Please consult a doctor.',
        from_=twilio_phone_number,
        to=phone_number
    )
    st.write(f"Alert message sent to {phone_number}: {message.body}")

def main():
    # giving a title
    st.title('Heart Stroke Prediction')

    # getting the input data from the user
    
    Age = st.text_input('Enter Age')
    Gender = st.text_input('Enter Gender(0-Female , 1-Male)')
    ChestPain = st.text_input('EnterChestPain on scale of 4 (1,2,3,4)')
    BloodPressure = st.text_input('Enter BloodPressure')
    cholestrol = st.text_input('Enter Cholestrol')
    fasting_blood_sugar = st.text_input('fasting_blood_sugar')
    resting_ecg = st.text_input('Enter resting_ecg(0,1)')
    Max_heart_rate= st.text_input('Enter Max Heart Rate')
    exerciseAngina = st.text_input('Enter exercise angina')
    oldpeak = st.text_input('oldpeak')
    OneSlope = st.text_input('Enter 1 Slope')
    Phone = st.text_input('Enter Patient Phone Number')

    # code for Prediction
    diagnosis_placeholder = st.empty()  # Placeholder to update the result

    # creating a button for Prediction
    if st.button('Heart Stroke Test Result'):
        diagnosis = Heart_stroke_prediction([Age,Gender,ChestPain, BloodPressure, cholestrol, fasting_blood_sugar, resting_ecg,
                                             Max_heart_rate, exerciseAngina, oldpeak,OneSlope],Phone)
        diagnosis_placeholder.success(diagnosis)

if __name__ == '__main__':
    main()
