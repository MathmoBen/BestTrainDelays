####################################### Libraries ###############################
import streamlit as st
import os
#################################################################################
st.set_page_config(
        page_title="About us",
        page_icon = "https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://www.networkrail.co.uk/"
)


# def add_bg_from_local(image_file):
#     with open(image_file, "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read())
#     st.markdown(
#     f"""
#     <style>
#     .stApp {{
#         background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
#         background-size: cover
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True
#     )
# add_bg_from_local(os.path.join(os.getcwd(), 'pages', 'Overground-Logo.jpg'))




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
    st.image(os.path.abspath('images/ltrudeau.jpeg'), width=105)

with col2:
    st.markdown("**Lewis Trudeau**")
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
    st.image(os.path.abspath('images/dramella.png'), width=105)

with col2:
    st.markdown("**Debora Ramella**")
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
    st.image(os.path.abspath('images/ben.jpeg'), width=105)

with col2:
    st.markdown("**Ben Fairbairn**")
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
    st.image(os.path.abspath('images/joel.jpeg'), width=105)

with col2:
    st.markdown("**Joel Okwuchukwu**")
    st.write("""
 <img src="https://github.githubassets.com/favicons/favicon.svg" width="20"> **Github profile**: https://github.com/YvngJoey101

 <img id='exclude-me' src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" width="20"> **LinkedIn**: https://www.linkedin.com/in/joel-okwuchukwu-808880229/

             """, unsafe_allow_html=True)
