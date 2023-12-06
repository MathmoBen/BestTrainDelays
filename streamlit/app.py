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

event_code = st.checkbox('Is the delay automatically logged?')

if Applicable_Timetable:
    app_time = 'Y'
else:
    app_time = 'N'

if event_code:
    code = 'A'
else:
    code ='M'

st.write(destination)

lat_OR = df[df['Station Name'] == origin]['Latitude']
lon_OR = df[df['Station Name'] == origin]['Longitude']
lat_DES = df[df['Station Name'] == destination]['Latitude']
lon_DES = df[df['Station Name'] == destination]['Longitude']

ori_month = origin_date.month
ori_day = origin_date.day
ori_hour = origin_time.hour
ori_minute = origin_time.minute

des_month = destination_date.month
des_day = destination_date.day
des_hour = destination_time.hour
des_minute = destination_time.minute

import math

orig_month_sin = math.sin(2 * math.pi * ori_month / 12)
orig_month_cos = math.cos(2 * math.pi * ori_month / 12)
orig_day_sin = math.sin(2 * math.pi * ori_day / 31)
orig_day_cos = math.cos(2 * math.pi * ori_day / 31)
orig_hour_sin = math.sin(2 * math.pi * ori_hour / 24)
orig_hour_cos = math.cos(2 * math.pi * ori_hour / 24)
orig_minute_sin = math.sin(2 * math.pi * ori_minute / 60)
orig_minute_cos = math.cos(2 * math.pi * ori_minute / 60)

dest_month_sin = math.sin(2 * math.pi * des_month / 12)
dest_month_cos = math.cos(2 * math.pi * des_month / 12)
dest_day_sin = math.sin(2 * math.pi * des_day / 31)
dest_day_cos = math.cos(2 * math.pi * des_day / 31)
dest_hour_sin = math.sin(2 * math.pi * des_hour / 24)
dest_hour_cos = math.cos(2 * math.pi * des_hour / 24)
dest_minute_sin = math.sin(2 * math.pi * des_minute / 60)
dest_minute_cos = math.cos(2 * math.pi * des_minute / 60)

st.write(origin_date.month)
if origin_date.month == 12 and origin_date.day == 26:
    dayofweek = 'BD'
elif origin_date.weekday() == 6:
    dayofweek = 'SU'
elif origin_date.weekday() == 5:
    dayofweek = 'SA'
else:
    dayofweek = 'WD'

data = pd.DataFrame(data = { 'Lat_OR': [float(lat_OR)],
                            'Lon_OR': [float(lon_OR)],'ORIG_MONTH_SIN':[orig_month_sin],'ORIG_MONTH_COS':[orig_month_cos],
                            'ORIG_DAY_SIN':[orig_day_sin],'ORIG_DAY_COS':[orig_day_cos],
                            'ORIG_HOUR_SIN':[orig_hour_sin],'ORIG_HOUR_COS':[orig_hour_cos],
                            'ORIG_MINUTE_SIN':[orig_minute_sin],'ORIG_MINUTE_COS':[orig_minute_cos],
                            'DEST_MONTH_SIN':[dest_month_sin],'DEST_MONTH_COS':[dest_month_cos],
                            'DEST_DAY_SIN':[dest_day_sin],'DEST_DAY_COS':[dest_day_cos],
                            'DEST_HOUR_SIN':[dest_hour_sin],'DEST_HOUR_COS':[dest_hour_cos],
                            'DEST_MINUTE_SIN':[dest_minute_sin],'DEST_MINUTE_COS':[dest_minute_cos],
                     'Lat_DES': [float(lat_DES)],
                            'Lon_DES': [float(lon_DES)],
                    'TRAIN_SERVICE_CODE_AFFECTED' : [train_service_code],\
                     'SERVICE_GROUP_CODE_AFFECTED' : [train_service_group_code], 'APP_TIMETABLE_FLAG_AFF' :[app_time],
                     'INCIDENT_REASON' : [Incident_reason],\
                         'UNIT_CLASS_AFFECTED' : [train_class_unit], 'PERFORMANCE_EVENT_CODE' : [code]  }
)

st.dataframe(data)
st.write(data.shape)






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










# st.write(f'{5} min wait')

# st.write('Relevant Description/ Glossary ')

# st.write ('Train service codes- this is the service group within the Schedule 8 performance regime')

# st.write('Service group codes- The codes of the trains that have been delayed in the past')


# st.image('yvngjoey/code/MathmoBen/TrainDelays/trains.png')
