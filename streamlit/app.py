import streamlit as st
import numpy as np
import pandas as pd
import numpy as np
import pickle
#from scripts.preprocessing.preprocess import preprocessing_pipe
import datetime


st.set_page_config(page_title= "Ex-stream-ly Cool App",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded"
    )

# model = pickle.load(open("/home/yvngjoey/code/MathmoBen/TrainDelays/Model/model.pkl", 'rb'))
# pipe = pickle.load(open("/home/yvngjoey/code/MathmoBen/TrainDelays/Model/pipe.pkl", 'rb'))


st.markdown("""# Train Delay Estimator
""")


df = pd.read_csv('/home/yvngjoey/code/MathmoBen/BestTrainDelays/streamlit/lookup_for_streamlit.csv')
first_df = df[['Station Name']]


origin = st.selectbox(
     'Select your travel origin ', first_df)

origin_date = st.date_input('origin_date', datetime.date(2023, 6, 19))

origin_time = st.time_input('origin_time', datetime.time(1, 30))


destination = st.selectbox('Select your travel destination ', first_df)

destination_date = st.date_input('destination_date', datetime.date(2023, 6, 19))

destination_time = st.time_input('destination_time', datetime.time(1, 30))


train_service_code = st.selectbox(
    'Pick a train service code',
    ('22214000', '22204000', '21921000', '25234001', '21234001', '21252001',
       '25235001', '22216000', '22206000', '21235001', '22218000', '22215003',
       '21237001', '22215002'))

train_service_group_code = st.selectbox(
    'Pick a previously affected group code',
    ('EK01', 'EK02', 'EK03', 'EK04', 'EK05', 'EK99'))

Applicable_Timetable = st.checkbox('Applicable-Timetable')

Incident_reason = st.selectbox('Previous train incident reason',
             ('A', 'D', 'F', 'I', 'J','M', 'O', 'P', 'Q', 'R','T', 'V', 'X', 'Z'))


st.write('A: Freight Terminal Operations Cause,\
        D : Holding codes, \
        F : Freight Operating Causes, \
        I & J : Infrastructure reasons,\
        M & N : Mechaical/Fleet Engineer causes,\
        O : Network Rail Operating cause, \
        P : Planned delays, \
        Q : Network Rail Non-Operating, \
        R : Station Operations,\
        T : Passenger Operations, \
        V : External events, \
        X : External events linked to the network rail, \
        Y : Reactionary delays, Z : Unexplained events/delays'
)


train_class_unit = st.selectbox('Pick a previously affected train unit class',
             ('313', '317', '315', '321','375', '378', '710'))

event_code = st.checkbox('PERFORMANCE_EVENT_CODE')











# # We take the features we have selected
# # We convert them from easy-to-understand strings into a format the model expects
# # e.g. We have a dataframe that maps the string 'Hoxton' to 0.324, 0.456456

# # We send them to the API
# # The API sends back a number (e.g 5)

# # We do st.write (f'{5} min wait)



#

# hoxton, hoxton, Mon, SA, EK01, 22214000
# ENGLISH_DAY_TYPE, SERVICE_GROUP_CODE_AFFECTED, TRAIN_SERVICE_CODE_AFFECTED


# df1 = pd.read_csv('/home/yvngjoey/code/MathmoBen/TrainDelays/mapping_data/stanox-lookup-lc.csv')
# #st.dataframe(df1)

# total_df = pd.read_csv('/home/yvngjoey/code/MathmoBen/TrainDelays/Notebooks/clean_data_final.csv')
# #st.write(total_df.columns)
# small_df = total_df[total_df['ENGLISH_DAY_TYPE']==option4].drop(columns = ['PFPI_MINUTES'])


# X_processed = pipe.transform(small_df)


# if st.button('Click to predict'):
#     st.text(model.predict(X_processed))


#Sst.dataframe(small_df)


# data = {'TRAIN_SERVICE_CODE_AFFECTED' : [option7]
#         'SERVICE_GROUP_CODE_AFFECTED' : [option6],
#         'ENGLISH_DAY_TYPE' : ['SA', 'WD', 'SU', 'BH', 'BD'],
#         'APP_TIMETABLE_FLAG_AFF' : ['Y', 'N'],
#         'UNIT_CLASS_AFFECTED': [375, 317, 315, 313, 710, 378, 321],
#         'INCIDENT_REASON': ['M', 'A', 'O', 'X', 'T', 'V', 'R', 'Q', 'I', 'Z', 'P', 'J', 'F', 'D'],
# # 'PERFORMANCE_EVENT_CODE' : [M, A],
# 'ORIGIN_STATION' :[],
# 'DESTINATION_STATION', :[],
# 'PLANNED_ORIG_WTT_DATETIME_AFF' :[],
# 'PLANNED_DES_WTT_DATETIME_AFF' : []
# }


# #df = pd.DataFrame(data =data)


# df.loc[:, 'PLANNED_ORIG_WTT_DATETIME_AFF'] = pd.to_datetime(df.PLANNED_ORIG_WTT_DATETIME_AFF)
# df.loc[:, 'ORIG_MONTH'] = df.PLANNED_ORIG_WTT_DATETIME_AFF.dt.month
# df.loc[:, 'ORIG_DAY'] = df.PLANNED_ORIG_WTT_DATETIME_AFF.dt.day
# df.loc[:, 'ORIG_HOUR'] = df.PLANNED_ORIG_WTT_DATETIME_AFF.dt.hour
# df.loc[:, 'ORIG_MINUTE'] = df.PLANNED_ORIG_WTT_DATETIME_AFF.dt.minute
# df.drop(columns='PLANNED_ORIG_WTT_DATETIME_AFF', inplace = True)



# import math
# sin_cos_df = df2[['ORIG_MONTH','ORIG_DAY','ORIG_HOUR','ORIG_MINUTE','DEST_MONTH','DEST_DAY','DEST_HOUR','DEST_MINUTE']]

# def col_transform(col_name):
#     df[f'{col_name}_SIN'] = sin_cos_df[f'{col_name}'].apply(lambda x: math.sin(2 * math.pi * x / 60))
#     df[f'{col_name}_COS'] = sin_cos_df[f'{col_name}'].apply(lambda x: math.cos(2 * math.pi * x / 60))
#     df.drop(columns=[col_name], inplace=True)



# for col in sin_cos_df.columns:
#     col_transform(col)







# st.write(f'{5} min wait')

# st.write('Relevant Description/ Glossary ')

# st.write ('Train service codes- this is the service group within the Schedule 8 performance regime')

# st.write('Service group codes- The codes of the trains that have been delayed in the past')


# st.image('yvngjoey/code/MathmoBen/TrainDelays/trains.png')
