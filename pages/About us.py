####################################### Libraries ###############################
import streamlit as st
import os
#################################################################################
st.set_page_config(
        page_title="About us",
        page_icon = "https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://www.networkrail.co.uk/",
        layout="wide",
        initial_sidebar_state="expanded"
)

###############################CSS + HMTL Stuff for header #####################

html = """
<div class="tw-relative tw-bg-primary tw-flex tw-items-end tw-h-40 md:tw-h-48 lg:tw-h-56 xl:tw-h-64 2xl:tw-h-72 snipcss-SsN7R">
  <div class="tw-container tw-relative tw-mb-8 md:tw-mb-12">
    <h1 class="tw-text-3xl md:tw-text-5xl lg:tw-text-6xl tw-font-bold tw-text-white">
      About us
    </h1>
  </div>
</div>

 """

css = """
 @import url('https://fonts.googleapis.com/css?family=Noto+Sans:100,100i,200,200i,300,300i,400,400i,500,500i,600,600i,700,700i,800,800i,900,900i&display=swap');
  body {
    font-family:"Noto Sans", sans-serif;
    line-height:1.15;
    font-size:14px;
  }
body {
/* CSS Variables that may have been missed get put on body */
    --tw-ring-inset:  var(--tw-empty,/*!*/ /*!*/);
    --tw-bg-opacity:  1;
    --tw-text-opacity:  1;
}

* {
    box-sizing: border-box;
}

* {
    box-sizing: border-box;
    border-width: 0;
    border-style: solid;
    border-color: currentColor;
}

* {
    --tw-ring-inset: var(--tw-empty,/*!*/ /*!*/);
}

.tw-flex {
    display: flex;
}

.tw-relative {
    position: relative;
}

body {
    margin: 0;
}

body {
    font-family: system-ui,		-apple-system, /* Firefox supports this but not yet `system-ui` */		'Segoe UI',		Roboto,		Helvetica,		Arial,		sans-serif,		'Apple Color Emoji',		'Segoe UI Emoji';
}

body {
    font-family: inherit;
    line-height: inherit;
}

html {
    line-height: 1.15;
    -webkit-text-size-adjust: 100%;
}

html {
    font-family: "Noto Sans", sans-serif;
    line-height: 1.5;
}

html {
    font-size: 14px;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

:root {
    -o-tab-size: 4;
    tab-size: 4;
}

.tw-bg-primary {
    --tw-bg-opacity: 1;
    background-color: rgba(227, 81, 0, var(--tw-bg-opacity));
}

.tw-items-end {
    align-items: flex-end;
}

.tw-h-40 {
    height: 10rem;
}

@media (min-width: 768px){
  .md\:tw-h-48 {
    height: 12rem;
  }
}

@media (min-width: 1024px){
  .lg\:tw-h-56 {
    height: 14rem;
  }
}

@media (min-width: 1366px){
  .xl\:tw-h-64 {
    height: 16rem;
  }
}

@media (min-width: 1440px){
  .\32 xl\:tw-h-72  {
    height: 18rem;
  }
}

*,:before,:after {
    box-sizing: border-box;
}

*,:before,:after {
    box-sizing: border-box;
    border-width: 0;
    border-style: solid;
    border-color: currentColor;
}

.tw-container {
    width: 100%;
    margin-right: auto;
    margin-left: auto;
    padding-right: 1rem;
    padding-left: 1rem;
}

@media (min-width: 576px){
  .tw-container {
    max-width: 576px;
    padding-right: 2rem;
    padding-left: 2rem;
  }
}

@media (min-width: 768px){
  .tw-container {
    max-width: 768px;
    padding-right: 3rem;
    padding-left: 3rem;
  }
}

@media (min-width: 1024px){
  .tw-container {
    max-width: 1024px;
    padding-right: 4rem;
    padding-left: 4rem;
  }
}

@media (min-width: 1366px){
  .tw-container {
    max-width: 1366px;
    padding-right: 4rem;
    padding-left: 4rem;
  }
}

@media (min-width: 1440px){
  .tw-container {
    max-width: 1440px;
    padding-right: 4rem;
    padding-left: 4rem;
  }
}

.tw-mb-8 {
    margin-bottom: 2rem;
}

@media (min-width: 768px){
  .md\:tw-mb-12 {
    margin-bottom: 3rem;
  }
}

h1 {
    margin: 0;
}

h1 {
    font-size: inherit;
    font-weight: inherit;
}

.tw-font-bold {
    font-weight: 700;
}

.tw-text-3xl {
    font-size: 1.875rem;
    line-height: 2.25rem;
}

.tw-text-white {
    --tw-text-opacity: 1;
    color: rgba(255, 255, 255, var(--tw-text-opacity));
}

@media (min-width: 768px){
  .md\:tw-text-5xl {
    font-size: 3rem;
    line-height: 1;
  }
}

@media (min-width: 1024px){
  .lg\:tw-text-6xl {
    font-size: 3.75rem;
    line-height: 1;
  }
 """

st.write(f'{html}', unsafe_allow_html=True)

st.write(f'<style>{css}</style>', unsafe_allow_html=True)
#################################################################################


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
