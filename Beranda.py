import streamlit as st

import numpy as np
import pandas as pd
import joblib

columns = ['Marital_status','Application_mode','Application_order','Course','Daytime_evening_attendance','Previous_qualification','Previous_qualification_grade','Nationality','Mothers_qualification','Fathers_qualification','Mothers_occupation','Fathers_occupation','Admission_grade','Displaced','Educational_special_needs','Debtor','Tuition_fees_up_to_date','Gender','Scholarship_holder','Age_at_enrollment','International','Curricular_units_1st_sem_credited','Curricular_units_1st_sem_enrolled','Curricular_units_1st_sem_evaluations','Curricular_units_1st_sem_approved','Curricular_units_1st_sem_grade','Curricular_units_1st_sem_without_evaluations','Curricular_units_2nd_sem_credited','Curricular_units_2nd_sem_enrolled','Curricular_units_2nd_sem_evaluations','Curricular_units_2nd_sem_approved','Curricular_units_2nd_sem_grade','Curricular_units_2nd_sem_without_evaluations','Unemployment_rate','Inflation_rate','GDP']
model = joblib.load('xgbpipe.joblib')

st.markdown("<h1 style='text-align: center;'>Student Dropout Analysis <br>School Education 🏫</h1>", unsafe_allow_html=True)
st.image('./images/background.jpg')
st.markdown("""
            Jaya Jaya Institute is a tertiary educational institution that has been established since 2000. To date, it has produced many graduates with excellent reputations. However, there are also many students who do not complete their education, aka dropouts.
            This high number of dropouts is certainly a big problem for an educational institution. Therefore, Jaya Jaya Institute wants to detect as quickly as possible students who might drop out so that they can be given special guidance.
            
            Based on these problems, this application was created with the aim of predicting whether students fall into the Dropout, Graduate or Enrolled categories.
            """)


st.divider()
st.subheader('Did they dropout? :thinking_face:')

maritalstatus = st.selectbox('Choose marital status : ',[1,2,3,4,5,6])
applicationmode = st.selectbox('Choose application mode : ', [1,2,7,10,15,16,17,18,26,39,42,43,44,51,53,57])
applicationorder = st.slider('Choose application order : ',0,9)
course = st.selectbox('Choose course : ',[13,171,8014,9003, 9070,9085,9119,9130,9147,9238,9254,9500,9556,9570,9773,9853,9991])
attendance = st.selectbox('Choose daytime / eveningn attendance : ',[0,1])
previousqualification = st.selectbox('Choose previous qualification :', [1,2,3,4,5,6,9,10,12,14,15,19,38,39,40,42,43])
previousqualificationgrade = st.slider('Input previous qualification grade : ',0,200)
nationality = st.selectbox('Choose nationality : ', [1,2,6,11,13,14,17,21,22,24,25,26,32,41,62,100,101,103,105,108,109])
mothersqualification = st.selectbox('Choose mothers qualification : ', [1,3,4,5,6,9,10,11,14,18,19,22,26,27,29,30,34,35,36,37,38,39,40,41,42,43,44])
fathersqualification = st.selectbox('Choose father qualification :', [1,2,3,4,5,6,9,10,11,12,13,14,18,19,20,22,25,26,27,29,30,31,33,34,35,36,37,38,39,40,41,42,43,44])
mothersoccupation = st.selectbox('Choose mothers occupation : ',[0,1,2,3,4,5,6,7,8,9,10,90,99,122,123,125,131,132,134,141,143,144,151,152,153,171,173,175,191,192,193,194])
fathersoccupation = st.selectbox('Choose fathers occupation : ', [1,2,3,4,5,6,7,8,9,10,90,99,101,102,103,112,114,121,122,123,124,131,132,134,135,141,143,144,151,152,153,154,161,163,171,172,174,175,181,182,183,192,193,194,195])
admissiongrade = st.number_input('Input admission grade : ', 0.0, 200.0, format="%.2f")
displaced = st.selectbox('Displaced : ',[0,1])
educationalspecialneeds = st.selectbox('Educational special needs : ',[0,1])
debtor = st.selectbox('Debtor',[0,1])
tuitionfees = st.selectbox(' Tuitions fees up to date : ',[0,1])
gender = st.selectbox(' Select gender : ',[0,1])
scholarshipholder = st.selectbox(' Scholarship holder : ',[0,1])
ageatenrollment = st.number_input('Age At enrollment',17,70)
international = st.selectbox(' International : ',[0,1])

Curricular_units_1st_sem_credited = st.number_input('Curricular units 1st sem credited : ',0,50)
Curricular_units_1st_sem_enrolled = st.number_input('Curricular units 1st sem enrolled : ',0,50)
Curricular_units_1st_sem_evaluations = st.number_input('Curricular units 1st sem evaluations : ',0,50)
Curricular_units_1st_sem_approved = st.number_input('Curricular units 1st sem approved : ',0,50)
Curricular_units_1st_sem_grade = st.number_input('Curricular units 1st sem grade : ',0.0,50.0, format="%.2f")
Curricular_units_1st_sem_without_evaluations = st.number_input('Curricular units 1st sem without evaluations : ',0,50)

Curricular_units_2nd_sem_credited = st.number_input('Curricular units 2nd sem credited : ',0,50)
Curricular_units_2nd_sem_enrolled = st.number_input('Curricular units 2nd sem enrolled : ',0,50)
Curricular_units_2nd_sem_evaluations = st.number_input('Curricular units 2nd sem evaluations : ',0,50)
Curricular_units_2nd_sem_approved = st.number_input('Curricular units 2nd sem approved : ',0,50)
Curricular_units_2nd_sem_grade = st.number_input('Curricular units 2nd sem grade : ', 0.0, 50.0, format="%.2f")
Curricular_units_2nd_sem_without_evaluations = st.number_input('Curricular units 2nd sem without evaluations : ',0,50)

unemployment_rate = st.number_input('Input unemployment rate :', 3.0, 17.0, format="%.2f")
inflationrate = st.number_input('Input inflation rate : ', 0.0, 5.0, format="%.2f")
gdp = st.number_input('Input GDP :', -4.0, 3.5, format="%.2f")


row = np.array([maritalstatus, applicationmode, applicationorder, course, attendance,previousqualification,
                previousqualificationgrade, nationality, mothersqualification, fathersqualification,
                mothersoccupation, fathersoccupation, admissiongrade, displaced, educationalspecialneeds,debtor,
                tuitionfees, gender, scholarshipholder, ageatenrollment, international, Curricular_units_1st_sem_credited,
                Curricular_units_1st_sem_enrolled, Curricular_units_1st_sem_evaluations, Curricular_units_1st_sem_approved,
                Curricular_units_1st_sem_grade, Curricular_units_1st_sem_without_evaluations, Curricular_units_2nd_sem_credited,
                Curricular_units_2nd_sem_enrolled, Curricular_units_2nd_sem_evaluations, Curricular_units_2nd_sem_approved,
                Curricular_units_2nd_sem_grade, Curricular_units_2nd_sem_without_evaluations, unemployment_rate, inflationrate, gdp
                ])

X = pd.DataFrame([row], columns = columns)

result_area = st.empty()

if st.button('Predict'):
    prediction = model.predict(X)
    if prediction[0] == 0:
        result_area.error('Status : Dropout!')
    elif prediction[0] == 1:
        result_area.success('Status : Graduate :thumbsup:')
    else:
        result_area.success('Status : Enrolled :thumbsup:')

