import streamlit as st
import numpy as np
import pandas as pd
import os

st.markdown('# Some Analysis from our Explored Data')



col1, col2 = st.columns([5,5],gap="medium")

with col1:
#st.image('https://github.com/MathmoBen/BestTrainDelays/blob/main/streamlit/images/delayplot.png?raw=true', caption='The most common PFPI (Process for Performance Improvement) delays in minutes.')
    st.image(os.path.abspath('images/delayplot.png'), caption='The most common PFPI (Process for Performance Improvement) delays in minutes.')

#st.image('https://github.com/MathmoBen/BestTrainDelays/blob/main/streamlit/images/codesplot.png?raw=true', caption='Chart showing the distribution of the delays across the different types of services operating on the London Overground in recent years.')
with col2:
    st.image(os.path.abspath('images/codesplot.png'), caption='Chart showing the distribution of the delays across the different types of services operating on the London Overground in recent years.')

#st.image('https://github.com/MathmoBen/BestTrainDelays/blob/main/streamlit/images/groupsplot.png?raw=true', caption='Chart showing the distribution of the delays across the six separate lines of the London Overground. EK01=Orbitals, EK02=London-Watford (DC lines), EK03=East London Lines, EK04=West Anglia Inner, EK05=Romford-Upminste, EK99=Miscellaneous')


col3, col4 =  st.columns(2)


with col3:
    st.image(os.path.abspath('images/groupsplot.png'), caption='Chart showing the distribution of the delays across the six separate lines of the London Overground. EK01=Orbitals, EK02=London-Watford (DC lines), EK03=East London Lines, EK04=West Anglia Inner, EK05=Romford-Upminste, EK99=Miscellaneous')

#st.image('https://github.com/MathmoBen/BestTrainDelays/blob/main/streamlit/images/unitplot.png?raw=true', caption='Chart showing the distribution of the delays across the different types of rolling stock operating on the London Overground in recent years.')
with col4:
    st.image(os.path.abspath('images/unitplot.png'), caption='Chart showing the distribution of the delays across the different types of rolling stock operating on the London Overground in recent years.')
