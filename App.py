import streamlit as st
import joblib
import pandas as pd


PCI=joblib.load('Canada_PCI.pkl')
price=joblib.load('Housing_Price.pkl')

st.sidebar.title('Pages')
# page=st.sidebar.selectbox('Select Model',['PCI','Housing Price'])#to select multiple value
page=st.sidebar.radio('Select Model',options=['Per Capita Income','Housing Price'])#select one value at a time
if page=='Per Capita Income':
    st.title('Per Capita Income of Canada')
    st.write('This is a simple web app to predict the per capita income of Canada')
    year=st.number_input('Enter your Year')
    prediction=PCI.predict([[year]])
    if st.button('Predict'):
        st.write('The Per Capita Income of Canada in the year',year,'is',prediction[0])
else:
    st.title('House Price Prediction')
    st.write('This is a simple web app to predict price of a house')
    sqft=st.number_input('Enter  area',min_value=100)
    bedroom=st.number_input('Enter no of rooms')
    age=st.slider('Enter the age of house',0,100)
    #slider=st.slider('Area',0,1000)
    prediction=price.predict([[sqft,bedroom,age]])
    prediction=pd.Series(prediction)
    if st.button('Predict'):
        st.success(round(prediction[0],2))
