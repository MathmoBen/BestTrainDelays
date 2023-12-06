####################################### Libraries ###############################
import streamlit as st
#################################################################################

# set Title
st.title("About us")
st.text("")

# set CSS style to round all images expect the one with the "exclude-me" tag (i.e. linkedin icons)
st.markdown("""
<style>
    img:not(#exclude-me) {border-radius: 50%}
</style>

""", unsafe_allow_html=True)

############################### Lewis info#######################################
# create two cols, one for profile photo and the other with the social networks links
col1, mid, col2 = st.columns([1,2,20],gap="medium")

with col1:
    st.image('images/ltrudeau.jpeg', width=100,caption='Lewis Trudeau')

with col2:
    st.text(" ")
    st.write("""
<img src="https://github.githubassets.com/favicons/favicon.svg" width="20" border-radius="50"> **Github profile**: https://github.com/LewisT1424

<img id='exclude-me' src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" width="20"> **LinkedIn**: https://www.linkedin.com/in/lewis-trudeau-338a62201/

             """, unsafe_allow_html=True)
# add large blank space
st.write("#")
############################### Debora info #######################################
# create two cols, one for profile photo and the other with the social networks links
col1, mid, col2 = st.columns([1,2,20],gap="medium")
with col1:
    st.image('images/dramella.png', width=100,caption='Debora Ramella')

with col2:
    st.text(" ")
    st.markdown("""
 <img class="image backArrow" src="https://github.githubassets.com/favicons/favicon.svg" width="20"> **Github profile**: https://github.com/dramella

 <img id='exclude-me' src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" width="20"> **LinkedIn**: https://www.linkedin.com/in/debora-ramella/

             """, unsafe_allow_html=True)

# add large blank space
st.write("#")
############################### Ben info #######################################
# create two cols, one for profile photo and the other with the social networks links

col1, mid, col2 = st.columns([1,2,20],gap="medium")

with col1:
    st.image('images/ben.jpeg', width=100,caption='Ben Fairbairn')

with col2:
    st.text(" ")
    st.write("""
 <img src="https://github.githubassets.com/favicons/favicon.svg" width="20"> **Github profile**: https://github.com/MathmoBen

 <img id='exclude-me' src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" width="20"> **LinkedIn**: https://www.linkedin.com/in/ben-fairbairn-b73a9030/

             """, unsafe_allow_html=True)

# add large blank space
st.write("#")
############################### Joel info #######################################
# create two cols, one for profile photo and the other with the social networks links

col1, mid, col2 = st.columns([1,2,20],gap="medium")

with col1:
    st.image('images/joel.jpeg', width=100,caption='Joel Okwuchukwu')

with col2:
    st.text(" ")
    st.write("""
 <img src="https://github.githubassets.com/favicons/favicon.svg" width="20"> **Github profile**: https://github.com/YvngJoey101

 <img id='exclude-me' src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" width="20"> **LinkedIn**: https://www.linkedin.com/in/joel-okwuchukwu-808880229/

             """, unsafe_allow_html=True)
