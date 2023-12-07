####################################### Libraries ###############################

import streamlit as st
import numpy as np
import pandas as pd
import os
###################################Page Configuration ##########################

st.set_page_config(
        page_title="Data Analysis",
        page_icon = "https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://www.networkrail.co.uk/",
        layout="wide",
        initial_sidebar_state="expanded"
        )
##########################HTML and CSS stuff for header ##########################

background_style ="""
.stApp {
    background-color: white;
    color: black;
}
    """

html = """
<div class="tw-relative tw-bg-primary tw-flex tw-items-end tw-h-40 md:tw-h-48 lg:tw-h-56 xl:tw-h-64 2xl:tw-h-72 snipcss-SsN7R">
  <div class="tw-container tw-relative tw-mb-8 md:tw-mb-12">
    <h1 class="tw-text-3xl md:tw-text-5xl lg:tw-text-6xl tw-font-bold tw-text-white">
      Data Analysis
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
st.markdown(f'<style>{background_style}</style>', unsafe_allow_html=True)


################################################################################


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
