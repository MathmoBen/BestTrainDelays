####################################### Libraries ###############################

import streamlit as st
#################################################################################
st.title("About us")
st.text("")


##################### Lewis
col1, mid, col2 = st.columns([1,2,20])

with col1:
    st.image('images/ltrudeau.jpeg', width=100,caption='Lewis Trudeau')

with col2:
    st.write("""
* **Github profile**: https://github.com/LewisT1424
* **LinkedIn**: https://www.linkedin.com/in/lewis-trudeau-338a62201/

             """)

##################### Debora
col1, mid, col2 = st.columns([1,2,20])
with col1:
    st.image('images/dramella.png', width=100,caption='Debora Ramella')

with col2:
    st.write("""
* **Github profile**: https://github.com/dramella
* **LinkedIn**: https://www.linkedin.com/in/debora-ramella/

             """)

##################### Ben
col1, mid, col2 = st.columns([1,2,20])

with col1:
    st.image('images/ben.jpeg', width=100,caption='Ben Fairbairn')

with col2:
    st.write("""
* **Github profile**: https://github.com/MathmoBen
* **LinkedIn**: https://www.linkedin.com/in/ben-fairbairn-b73a9030/

             """)

##################### Joel
col1, mid, col2 = st.columns([1,2,20])

with col1:
    st.image('images/joel.jpeg', width=100,caption='Joel Okwuchukwu')

with col2:
    st.write("""
* **Github profile**: https://github.com/YvngJoey101
* **LinkedIn**: https://www.linkedin.com/in/joel-okwuchukwu-808880229/

             """)
