import joblib
import numpy as np
import pandas as pd

scaler_Marital_status = joblib.load("model/scaler_Marital_status.joblib")
scaler_Application_mode = joblib.load("model/scaler_Application_mode.joblib")
scaler_Application_order = joblib.load("model/scaler_Application_order.joblib")
scaler_Course = joblib.load("model/scaler_Course.joblib")
scaler_Daytime_evening_attendance = joblib.load("model/scaler_Daytime_evening_attendance.joblib")
scaler_Previous_qualification = joblib.load("model/scaler_Previous_qualification.joblib")
scaler_Previous_qualification_grade = joblib.load("model/scaler_Previous_qualification_grade.joblib")
scaler_Nationality = joblib.load("model/scaler_Nationality.joblib")
scaler_Mothers_qualification = joblib.load("model/scaler_Mothers_qualification.joblib")
scaler_Fathers_qualification = joblib.load("model/scaler_Fathers_qualification.joblib")
scaler_Fathers_occupation = joblib.load("model/scaler_Fathers_occupation.joblib")
scaler_Mothers_occupation = joblib.load("model/scaler_Mothers_occupation.joblib")
scaler_Admission_grade = joblib.load("model/scaler_Admission_grade.joblib")
scaler_Displaced = joblib.load("model/scaler_Displaced.joblib")
scaler_Educational_special_needs = joblib.load("model/scaler_Educational_special_needs.joblib")
scaler_Debtor = joblib.load("model/scaler_Debtor.joblib")
scaler_Tuition_fees_up_to_date = joblib.load("model/scaler_Tuition_fees_up_to_date.joblib")
scaler_Gender = joblib.load("model/scaler_Gender.joblib")
scaler_Scholarship_holder = joblib.load("model/scaler_Scholarship_holder.joblib")
scaler_Age_at_enrollment = joblib.load("model/scaler_Age_at_enrollment.joblib")
scaler_International = joblib.load("model/scaler_International.joblib")

scaler_Curricular_units_1st_sem_credited = joblib.load("model/scaler_Curricular_units_1st_sem_credited.joblib")
scaler_Curricular_units_1st_sem_enrolled = joblib.load("model/scaler_Curricular_units_1st_sem_enrolled.joblib")
scaler_Curricular_units_1st_sem_evaluations = joblib.load("model/scaler_Curricular_units_1st_sem_evaluations.joblib")
scaler_Curricular_units_1st_sem_approved = joblib.load("model/scaler_Curricular_units_1st_sem_approved.joblib")
scaler_Curricular_units_1st_sem_grade = joblib.load("model/scaler_Curricular_units_1st_sem_grade.joblib")
scaler_Curricular_units_1st_sem_without_evaluations = joblib.load("model/scaler_Curricular_units_1st_sem_without_evaluations.joblib")

scaler_Curricular_units_2nd_sem_credited = joblib.load("model/scaler_Curricular_units_2nd_sem_credited.joblib")
scaler_Curricular_units_2nd_sem_enrolled = joblib.load("model/scaler_Curricular_units_2nd_sem_enrolled.joblib")
scaler_Curricular_units_2nd_sem_evaluations = joblib.load("model/scaler_Curricular_units_2nd_sem_evaluations.joblib")
scaler_Curricular_units_2nd_sem_approved = joblib.load("model/scaler_Curricular_units_2nd_sem_approved.joblib")
scaler_Curricular_units_2nd_sem_grade = joblib.load("model/scaler_Curricular_units_2nd_sem_grade.joblib")
scaler_Curricular_units_2nd_sem_without_evaluations = joblib.load("model/scaler_Curricular_units_2nd_sem_without_evaluations.joblib")

scaler_Unemployment_rate = joblib.load("model/scaler_Unemployment_rate.joblib")
scaler_Inflation_rate = joblib.load("model/scaler_Inflation_rate.joblib")
scaler_GDP = joblib.load("model/scaler_GDP.joblib")

def data_preprocessing(data):
    """PPreprocessing data

    Args:
        data (Pandas DataFrame): Dataframe that contain all the data to make prediction 
        
    return:
        Pandas DataFrame: Dataframe that contain all the preprocessed data
    """
    data = data.copy()
    df = pd.DataFrame()
    
    df["Marital_status"] = scaler_Marital_status.transform(np.asarray(df["Marital_status"]).reshape(-1,1))[0]
    df["Application_mode"] = scaler_Application_mode.transform(np.asarray(df["Application_mode"]).reshape(-1,1))[0]
    df["Application_order"] = scaler_Application_order.transform(np.asarray(df["Application_order"]).reshape(-1,1))[0]
    df["Course"] = scaler_Course.transform(np.asarray(df["Course"]).reshape(-1,1))[0]
    df["Daytime_evening_attendance"] = scaler_Daytime_evening_attendance.transform(np.asarray(df["Daytime_evening_attendance"]).reshape(-1,1))[0]
    df["Previous_qualification"] = scaler_Previous_qualification.transform(np.asarray(df["Previous_qualification"]).reshape(-1,1))[0]
    df["Previous_qualification_grade"] = scaler_Previous_qualification_grade.transform(np.asarray(df["Previous_qualification_grade"]).reshape(-1,1))[0]
    df["Nationality"] = scaler_Nationality.transform(np.asarray(df["Nationality"]).reshape(-1,1))[0]
    df["Mothers_qualification"] = scaler_Mothers_qualification.transform(np.asarray(df["Mothers_qualification"]).reshape(-1,1))[0]
    df["Fathers_qualification"] = scaler_Fathers_qualification.transform(np.asarray(df["Fathers_qualification"]).reshape(-1,1))[0]
    df["Fathers_occupation"] = scaler_Fathers_occupation.transform(np.asarray(df["Fathers_occupation"]).reshape(-1,1))[0]
    df["Mothers_occupation"] = scaler_Mothers_occupation.transform(np.asarray(df["Mothers_occupation"]).reshape(-1,1))[0]
    df["Admission_grade"] = scaler_Admission_grade.transform(np.asarray(df["Admission_grade"]).reshape(-1,1))[0]
    df["Displaced"] = scaler_Displaced.transform(np.asarray(df["Displaced"]).reshape(-1,1))[0]
    df["Educational_special_needs"] = scaler_Educational_special_needs.transform(np.asarray(df["Educational_special_needs"]).reshape(-1,1))[0]
    df["Debtor"] = scaler_Debtor.transform(np.asarray(df["Debtor"]).reshape(-1,1))[0]
    df["Tuition_fees_up_to_date"] = scaler_Tuition_fees_up_to_date.transform(np.asarray(df["Tuition_fees_up_to_date"]).reshape(-1,1))[0]
    df["Gender"] = scaler_Gender.transform(np.asarray(df["Gender"]).reshape(-1,1))[0]
    df["Scholarship_holder"] = scaler_Scholarship_holder.transform(np.asarray(df["Scholarship_holder"]).reshape(-1,1))[0]
    df["Age_at_enrollment"] = scaler_Age_at_enrollment.transform(np.asarray(df["Age_at_enrollment"]).reshape(-1,1))[0]
    df["International"] = scaler_International.transform(np.asarray(df["International"]).reshape(-1,1))[0]

    df["Curricular_units_1st_sem_credited"] = scaler_Curricular_units_1st_sem_credited.transform(np.asarray(df["Curricular_units_1st_sem_credited"]).reshape(-1,1))[0]
    df["Curricular_units_1st_sem_enrolled"] = scaler_Curricular_units_1st_sem_enrolled.transform(np.asarray(df["Curricular_units_1st_sem_enrolled"]).reshape(-1,1))[0]
    df["Curricular_units_1st_sem_evaluations"] = scaler_Curricular_units_1st_sem_evaluations.transform(np.asarray(df["Curricular_units_1st_sem_evaluations"]).reshape(-1,1))[0]
    df["Curricular_units_1st_sem_approved"] = scaler_Curricular_units_1st_sem_approved.transform(np.asarray(df["Curricular_units_1st_sem_approved"]).reshape(-1,1))[0]
    df["Curricular_units_1st_sem_grade"] = scaler_Curricular_units_1st_sem_grade.transform(np.asarray(df["Curricular_units_1st_sem_grade"]).reshape(-1,1))[0]
    df["Curricular_units_1st_sem_without_evaluations"] = scaler_Curricular_units_1st_sem_without_evaluations.transform(np.asarray(df["Curricular_units_1st_sem_without_evaluations"]).reshape(-1,1))[0]

    df["Curricular_units_2nd_sem_credited"] = scaler_Curricular_units_2nd_sem_credited.transform(np.asarray(df["Curricular_units_2nd_sem_credited"]).reshape(-1,1))[0]
    df["Curricular_units_2nd_sem_enrolled"] = scaler_Curricular_units_2nd_sem_enrolled.transform(np.asarray(df["Curricular_units_2nd_sem_enrolled"]).reshape(-1,1))[0]
    df["Curricular_units_2nd_sem_evaluations"] = scaler_Curricular_units_2nd_sem_evaluations.transform(np.asarray(df["Curricular_units_2nd_sem_evaluations"]).reshape(-1,1))[0]
    df["Curricular_units_2nd_sem_approved"] = scaler_Curricular_units_2nd_sem_approved.transform(np.asarray(df["Curricular_units_2nd_sem_approved"]).reshape(-1,1))[0]
    df["Curricular_units_2nd_sem_grade"] = scaler_Curricular_units_2nd_sem_grade.transform(np.asarray(df["Curricular_units_2nd_sem_grade"]).reshape(-1,1))[0]
    df["Curricular_units_2nd_sem_without_evaluations"] = scaler_Curricular_units_2nd_sem_without_evaluations.transform(np.asarray(df["Curricular_units_2nd_sem_without_evaluations"]).reshape(-1,1))[0]

    df["Unemployment_rate"] = scaler_Unemployment_rate.transform(np.asarray(df["Unemployment_rate"]).reshape(-1,1))[0]
    df["Inflation_rate"] = scaler_Inflation_rate.transform(np.asarray(df["Inflation_rate"]).reshape(-1,1))[0]
    df["GDP"] = scaler_GDP.transform(np.asarray(df["GDP"]).reshape(-1,1))[0]
    
    return df