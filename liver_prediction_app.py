import numpy as np
import pickle
import streamlit as st
from sklearn.preprocessing import MinMaxScaler
import time
from PIL import Image




#load saved model
load_model=pickle.load(open('Trained_model.pkl','rb'))


#creating function for prediction
def liver_prediction(input):

    #changing input to numpy array
    data=np.asarray(input)
    # reshaping of data
    reshape_data=data.reshape(1,-1)
    # normalise data
    mms=MinMaxScaler()
    nor_data=mms.fit_transform(reshape_data)
    print(nor_data)
    #prediction using mmodel
    prediction=load_model.predict(nor_data)
    print(prediction)

    if (prediction==0):
       return "You are healthy"
    else:
       return "you have liver disease "
    
#streamlit function with name as main

def main():
   
    #giving title
    st.title('Application For Liver Disease Prediction')
    st.text(""" 
             Machine Learning app""")
    img=Image.open("liver.jpg")
    st.image(img)
    
    #getting input from user
    Age= st.text_input('Enter your Age')

    st.write("___")
    
    Gender = st.radio('Gender',('Male','Female'))
    if Gender=="Male":
        Gender = 1
    else:
        Gender = 0
    st.write("___")    
    Total_Bilirubin= st.text_input('Enter Total bilirubin level') 
    st.write("___")
    
    Direct_Bilirubin= st.text_input('Enter Direct bilirubin level')
    st.write("___")
    Alkaline_Phosphotase= st.text_input('Enter Alkaline phosphotase level')
    st.write("___")
    Alamine_Aminotransferase= st.text_input('Enter alamine level')
    st.write("___")
    Aspartate_Aminotransferase= st.text_input('Enter aspartate aminotransferase level')
    st.write("___")
    Total_Protiens= st.text_input('Enter total protein value')
    st.write("___")
    Albumin = st.text_input('Enter albumin levels')
    st.write("___")
    Albumin_and_Globulin_Ratio= st.text_input('Enter albumin and globulin ratio value')
    st.write("___")
    
    # code for prediction 
    diagnosis = ''
    
    # creating button for prediction
    if st.button('Test Results'):
        diagnosis = liver_prediction([Age,Gender,Total_Bilirubin,Direct_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase,Total_Protiens,Albumin,Albumin_and_Globulin_Ratio])
        with st.spinner('waiting..'):
            time.sleep(3)
    st.success(diagnosis)

    st.sidebar.header("Main Menu")
    st.sidebar.button('Home')
    st.sidebar.button('About')
    st.sidebar.button('Contact')
    st.sidebar.header("Make your liver healthy by eating some fruits")
    vid=open("livervid.mp4", 'rb')
    video = vid.read()
    st.sidebar.video(video)

    
if __name__=='__main__':
    main()
