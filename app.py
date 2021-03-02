import streamlit as st
import datetime
import requests

'''
# TaxiFareModel front
'''

'''
## Please select the parameters below:
'''

#Pickup time

d = st.date_input("Date of pickup", datetime.date(2021, 3, 2))
t = st.time_input('Time of pickup', datetime.time(8, 45))

#Pickup coordinates

pickup_lon = st.number_input('Pickup longitude')
pickup_lat = st.number_input('Pickup latitude')

#Dropoff coordinates

dropoff_lon = st.number_input('Dropoff longitude')
dropoff_lat = st.number_input('Dropoff latitude')

#Passengers

passengers = st.slider('Passenger count', 1, 4, 1)

key = '2012-10-06 2012:10:20.0000001'

url = 'http://taxifare.lewagon.ai/predict_fare/'

'''
## Fare amount:
'''

pickup_datetime = str(d) + " " + str(t) + " UTC"

params = {
        'key': [key],
        'pickup_datetime': [pickup_datetime],
        'pickup_longitude': [float(pickup_lon)],
        'pickup_latitude': [float(pickup_lat)],
        'dropoff_longitude': [float(dropoff_lon)],
        'dropoff_latitude': [float(dropoff_lat)],
        'passenger_count': [int(passengers)]
        }

r = requests.get(url, params=params).json()

st.markdown(round(r['prediction'],2))