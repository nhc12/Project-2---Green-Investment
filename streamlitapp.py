# Import libraries and their dependencies 
import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt
from pathlib import Path
from PIL import Image

import os
import requests


# Create Header
st.write('''# Renewable Enegergy Portfolio: An Outperformer?''')
st.write('''## Introduction''')
st.write('Using signals from our Algorithmic Trading model, we attempt to determine if our 5-stock equal-weight renewable energy portfolio is likely to outperform the benchmark S&P500 index.' 
         ' Finally, we conclude by using Machine Learning models from Sci-kit Learn and Tensor Flow, with price action as an indicator, that our renewable energy portfolio is likely to outperform the S&P500.')

# First image
image1 = Image.open('./Visualizations/farm.jpg')
st.image(image1) 

# Set up sidebar
st.sidebar.header('FSLR,SEDG, CSIQ, AQN, DQ Portfolio')
image2 = Image.open('./Visualizations/ui_logo.jpg')
st.sidebar.image(image2)        
st.sidebar.write('Group 12: Amany El Gouhary, Katharine Zenta, '
                 'Nicolas Hernandez, Al Bakomito')

# Algorithmic Trading Outputs 
st.write ('''## Algorithmic Trading & Bollinger Bands''') 
st.write('Portfolio Total: US$106960')
image3= Image.open('./Visualizations/Algo1.jpg')
st.image(image3)

st.write('Portfolio Total: US$100616')
image4= Image.open('./Visualizations/Algo2.jpg')
st.image(image4)

st.write('Portfolio Total: US$100361')
image5= Image.open('./Visualizations/Algo3.jpg')
st.image(image5)

st.write('Portfolio Total: US$104078')
image6= Image.open('./Visualizations/Algo4.jpg')
st.image(image6)

st.write('Portfolio Total: US$2816781')
image7= Image.open('./Visualizations/Algo5.jpg')
st.image(image7)

# Machine Learning Outputs 
st.write('''## Machine Learning Outputs''')
st.write('''### LSTM One-level Sequential Model, 10 Day Window''')
st.write('Portfolio & SPY Closing Price: US$100k Initial Investment')
image8= Image.open('./Visualizations/ML1.jpg')
st.image(image8)

st.write('Validation & Prediction Period')
image9= Image.open('./Visualizations/ML2.jpg')
st.image(image9)

st.write('Validation & Prediction Period: Zoomed in')
image10= Image.open('./Visualizations/ML3.jpg')
st.image(image10)