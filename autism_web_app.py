# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 11:49:11 2024

@author: nikitha
"""

import numpy as np
import pickle 
import streamlit as st

loaded_model=pickle.load(open("C:/Users/nikitha/Downloads/autism/autism_model.pkl",'rb'))

#creating a function for prediction
def autism_prediction(input_data):
    
    #changing the input data to numpy array
    input_data_as_numpy_array=np.asarray(input_data)

    #reshape the array as we are predicting for one instance
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)

    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)

    if(prediction[0]==0):
        return "The person has no autism."
    else:
        return "The person has autism."
    
def main():
    #giving a title
    st.title('Autism Disease Prediction Web App')
   
    #getting the input from user
    Social_Responsiveness_Scale=st.text_input('Enter Social Responsive Value 1-10')
    Age=st.text_input('Enter Age')
    Autism_score=st.text_input('Autism score 1-10')
    speech_disorder=st.text_input('Speech Disorder (Yes=1, 0=No)')
    Learning_disorder=st.text_input('Learning Disorder (Yes=1, 0=No)')
    Genetic_Disorders=st.text_input('Genetic Disorder (Yes=1, 0=No)')
    Depression=st.text_input('Depression (Yes=1, 0=No)')
    intellectual_disability=st.text_input('Intellectual disability (Yes=1, 0=No)')
    Behavioural_Issues=st.text_input('Behavioural Issues (Yes=1, 0=No)')
    Anxiety_disorder=st.text_input('Anxiety disorder (Yes=1, 0=No)')
    Sex=st.text_input('Enter your Gender (Female=0, Male=1)')
    Jaundice=st.text_input('Jaundice (Yes=1, 0=No)')
    Family_mem_with_ASD=st.text_input('Family member having autism (Yes=1, 0=No)')
    
    #code for prediction 
    diagnosis=''
    
    #creating a button for prediction
    if st.button('Asthma Test Result'):
        diagnosis=autism_prediction([Social_Responsiveness_Scale,Age,Autism_score,speech_disorder,Learning_disorder,Genetic_Disorders,Depression,intellectual_disability,Behavioural_Issues,Anxiety_disorder,Sex,Jaundice,Family_mem_with_ASD])
        
    st.success(diagnosis)
    
if __name__ =='__main__':
    main()
    
    