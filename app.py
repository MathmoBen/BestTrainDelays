import streamlit as st
import numpy as np
import pandas as pd
import numpy as np
import pickle
#from scripts.preprocessing.preprocess import preprocessing_pipe
import datetime
import os
import flaml

st.set_page_config(page_title= "Ex-stream-ly Cool App",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded"
     )


# CSS  = '''
# <style>

# h1 {color:red;}.stApp {

# background-image: url(https://www.railadvent.co.uk/2017/12/night-overground-train-services-have-begun-in-london.html);
# background-size: cover;

# }
# </style>
# '''






# model = pickle.load(open(os.path.abspath("Models/XGBoost_MSE_on_test_with_log_transf_1_27.sav"), 'rb'))
model = pickle.load(open(os.path.abspath("Models/XGBoost_RMSE_on_test_with_log_transf_rmse_1_64.sav"), 'rb'))
pipe = pickle.load(open(os.path.abspath("Models/pipe_dump.pkl"), 'rb'))

st.markdown("""# Train Delay Estimator
""")


df = pd.read_csv(os.path.abspath('lookup_for_streamlit.csv'))
first_df = df[['Station Name']]

col1, col2, col3, col4 = st.columns(4)

with col1:
    origin = st.selectbox(
     'Select your travel origin', first_df)

with col2:
    origin_date = st.date_input('Origin date', datetime.date.today())

with col3:
    origin_time = st.time_input('Origin time', datetime.time(15, 00))

col4, col5, col6 = st.columns(3)
with col4:
    destination = st.selectbox('Select your travel destination ', first_df)

with col5:
    destination_date = st.date_input('Destination date', datetime.date.today())

with col6:
    destination_time = st.time_input('Destination time', datetime.time(15, 30))



col7, col8 = st.columns(2)

with col7:
    train_service_code = st.selectbox(
    'Pick a train service code',
    ('22214000 -- Richmond - Camden Road - Stratford', '22204000 -- Willesden - Kensington - Clapham Jct',
    '21921000 -- Gospel Oak - Barking', '25234001 -- London Liverpool St - Cheshunt/Enfield Town (Peak)',
    '21234001 -- London Liverpool St - Cheshunt/Enfield Town (Off Peak)', '21252001 -- London Overground (West Anglia) ECS',
    '25235001 -- London Liverpool St - Chingford Services (Peak)', '22216000 -- London Euston - Watford Junction (D.C Lines)',
    '22206000 -- Queens Rd Peckham - Clapham Jct SLL', '21235001 -- London Euston - Watford Junction (D.C Lines)',
    '22218000 -- ELL : (Tfl Infrastructure only-)', '22215003 -- ELL : New X Gate-C Palace/W Croydon',
    '21237001 -- Romford - Upminster', '22215002 -- ELL (ECS Movements)'))

with col8:
    train_service_group_code = st.selectbox(
    'Select a train service group code',
    ('EK01 -- Orbitals',
     'EK02 -- London-Watford (DC lines)',
     'EK03 -- East London Lines',
     'EK04 -- West Anglia Inner',
     'EK05 -- Romford-Upminster',
     'EK99 -- Miscellaneous '))


col9, col11 = st.columns(2)


with col9:
    Incident_reason = st.selectbox('Train incident reasons',
             ('A - Freight Terminal Operations Cause',
              'D - Holding codes',
              'F - Freight Operating Causes',
              'I - Infrastructure reasons',
              'J - Infrastructure reasons',
              'M - Mechaical/Fleet Engineer causes',
              'O - Network Rail Operating cause',
              'Q - Network Rail Non-Operating',
              'R - Station Operations',
              'T - Passenger Operations',
              'V - External events',
              'X - External events linked to the network rail',
              'Z - Unexplained events/delays'))



with col11:
    train_class_unit = st.selectbox('Select a train unit class',
             ('313', '317', '315', '321','375', '378', '710'))


Applicable_Timetable = st.checkbox('Is train on official performance records?')

event_code = st.checkbox('Is the delay automatically logged?')


for i in range(5):
    st.text("")

if Applicable_Timetable:
    app_time = 'Y'
else:
    app_time = 'N'

if event_code:
    code = 'A'
else:
    code ='M'


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
                         'UNIT_CLASS_AFFECTED' : [train_class_unit], 'PERFORMANCE_EVENT_CODE' : [code], 'ENGLISH_DAY_TYPE':[dayofweek]  }
)



# st.dataframe(data)
if st.button('Predict'):
    processed = pipe.transform(data)
    # st.write(processed)

    result = model.predict(processed)
    st.write(f'This train is estimated to be delayed by {round(float(result[0]), 1)} minutes')
# # We take the features we have selected
# # We convert them from easy-to-understand strings into a format the model expects
# # e.g. We have a dataframe that maps the string 'Hoxton' to 0.324, 0.456456

# # We send them to the API
# # The API sends back a number (e.g 5)

# # We do st.write (f'{5} min wait)


# background-color: #e5e5f7;
# opacity: 0.8;
# background: repeating-linear-gradient( 45deg, #fab87d, #fab87d 10.5px, #e5e5f7 10.5px, #e5e5f7 52.5px );
# # #

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
