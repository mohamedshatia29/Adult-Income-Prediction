import streamlit as st
import pickle
import pandas as pd
import numpy as np


st.set_page_config(
    page_title="Income Prediction App",
    page_icon="💰",
    layout="wide"
)



@st.cache_resource
def load_model():
    with open('xgboost_model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model


model = load_model()




st.title("💰 Income Prediction App")
st.markdown("### Predict income based on census data")
st.markdown("---")




col1, col2 = st.columns(2)



with col1:
    st.subheader("📊 Personal Information")
    age = st.number_input("Age", min_value=17, max_value=90, value=30)
    
    workclass = st.selectbox("Work Class", [
        "Private", "Self-emp-not-inc", "Self-emp-inc", "Federal-gov",
        "Local-gov", "State-gov"
    ])
    
    education = st.selectbox("Education", [
        'HS-grad', 'Masters', 'Bachelors', 'Some-college', 'Doctorate',
       'Prof-school', 'Assoc-voc', 'Assoc-acdm', '7th-8th', '12th',
       '10th', '11th', '9th', '5th-6th', '1st-4th'
    ])
    
    marital_status = st.selectbox("Marital Status", [
       'Married', 'Single'
    ])
    
    race = st.selectbox("Race", [
        "White", "Black","Other"
    ])
    
    sex = st.selectbox("Sex", ["Male", "Female"])



with col2:
    st.subheader("💼 Work Information")
    
    occupation = st.selectbox("Occupation", [
       'Exec-managerial', 'Prof-specialty', 'Tech-support',
       'Adm-clerical', 'Sales', 'Craft-repair', 'Protective-serv',
       'Other-service', 'Machine-op-inspct', 'Farming-fishing',
       'Transport-moving', 'Handlers-cleaners', 'Armed-Forces',
       'Priv-house-serv'
    ])
    
    relationship = st.selectbox("Relationship", [
        'Husband', 'Not-in-family', 'Unmarried', 'Wife', 'Other-relative',
       'Own-child'
    ])

    net_capital = st.selectbox("Capital Net" , 
                               ["High" , "Low"]

    )
    
    native_country = st.selectbox( "Native Country" , 
                                  ["United-States" , "Non-United-States	"]
    
    )

    hours_per_week = st.number_input("Hours per Week", min_value=1, max_value=100, value=40)
            
    

st.markdown("---")



if st.button("🔮 Predict Income", type="primary", use_container_width=True):


    input_data = pd.DataFrame({
        'age': [age],
        'workclass': [workclass],
        'education': [education],
        'marital_status': [marital_status],
        'occupation': [occupation],
        'relationship': [relationship],
        'race': [race],
        'sex': [sex],
        'net_capital': [net_capital],
        'hours_per_week': [hours_per_week],
        'native_country': [native_country]
    })
    


    prediction = model.predict(input_data)[0]
    prediction_proba = model.predict_proba(input_data)[0]
    


    st.markdown("---")
    st.subheader("📈 Prediction Results")
    
    result_col1, result_col2, result_col3 = st.columns(3)
    
    with result_col1:
        if prediction == '>50K':
            st.success("### Income: >$50K")
        else:
            st.info("### Income: ≤$50K")
    
    with result_col2:
        st.metric("Probability ≤$50K", f"{prediction_proba[0]:.2%}")
    
    with result_col3:
        st.metric("Probability >$50K", f"{prediction_proba[1]:.2%}")
    



