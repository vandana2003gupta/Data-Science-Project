import streamlit as st
import pickle
import webbrowser
from streamlit_option_menu import option_menu

# Load models with correct paths
try:
    with open('Diseases/Heart-Disease-Prediction/heart.pkl', 'rb') as file:
        heart_model = pickle.load(file)
    with open('Diseases/Diabetes-Prediction-EDA/diabetes.pkl', 'rb') as file:
        diabetes_model = pickle.load(file)
    with open('Diseases/Parkinson-Disease-EDA-and-Prediction/Parkinsons.pkl', 'rb') as file:
        parkinsons_model = pickle.load(file)
except Exception as e:
    st.error(f"Error loading models: {str(e)}")
    st.stop()

# Sidebar navigation
with st.sidebar:
    selected = option_menu('Proactive Health Guard',
                         ['Welcome', 'Autism', 'Diabetes Prediction',
                          'Heart Disease Prediction', 'Parkinsons Prediction',
                          'Yoga Posture Corrector', 'Feedback'],
                         default_index=0)

# Welcome Page
if selected == 'Welcome':
    #st.image("logo1.png")  # Make sure this image exists in the same directory
    st.title(":red[Health Care Analyzer and Disease Predictor]")
    st.write("""
    :blue[ProActive Health Guard is a revolutionary healthcare initiative employing machine learning, Streamlit, 
    bots, and Python libraries for proactive disease prediction. The project analyzes various diseases to help 
    users detect health risks early.]
    """)

# Autism Placeholder
if selected == 'Autism':
    st.title("Autism Prediction")
    st.write("This section is under development")

# Diabetes Prediction
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    st.write(":blue[Detect whether the person is diabetic based on medical inputs.]")

    col1, col2, col3 = st.columns(3)
    with col1:
        pregnancies = st.text_input('Number of Pregnancies', '0')
    with col2:
        glucose = st.text_input('Glucose Level', '120')
    with col3:
        blood_pressure = st.text_input('Blood Pressure', '70')
    with col1:
        skin_thickness = st.text_input('Skin Thickness', '20')
    with col2:
        insulin = st.text_input('Insulin Level', '80')
    with col3:
        bmi = st.text_input('BMI', '25')
    with col1:
        diabetes_pedigree = st.text_input('Diabetes Pedigree Function', '0.5')
    with col2:
        age = st.text_input('Age', '30')

    if st.button('Diabetes Test Result'):
        try:
            input_data = [
                float(pregnancies), float(glucose), float(blood_pressure),
                float(skin_thickness), float(insulin), float(bmi),
                float(diabetes_pedigree), float(age)
            ]
            result = diabetes_model.predict([input_data])[0]
            st.success("The person is not diabetic." if result == 0 else "The person is diabetic.")
        except Exception as e:
            st.error(f"Error: {str(e)}. Please enter valid numbers.")

# Heart Disease Prediction
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    #.image("heart1.jpeg")  # Add the image in root or correct path
    st.write(":blue[Predict heart disease based on various health metrics.]")

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age', '50')
    with col2:
        sex = st.selectbox('Sex', ['Male', 'Female'])
    with col3:
        cp = st.selectbox('Chest Pain Type', ['0: Typical', '1: Atypical', '2: Non-anginal', '3: Asymptomatic'])
    with col1:
        trestbps = st.text_input('Resting BP', '120')
    with col2:
        chol = st.text_input('Cholesterol', '200')
    with col3:
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['0: No', '1: Yes'])
    with col1:
        restecg = st.selectbox('Resting ECG', ['0: Normal', '1: ST-T Abnormality', '2: LV Hypertrophy'])
    with col2:
        thalach = st.text_input('Max Heart Rate', '150')
    with col3:
        exang = st.selectbox('Exercise Induced Angina', ['0: No', '1: Yes'])
    with col1:
        oldpeak = st.text_input('ST Depression', '0.0')
    with col2:
        slope = st.selectbox('Slope', ['0: Upsloping', '1: Flat', '2: Downsloping'])
    with col3:
        ca = st.text_input('Major Vessels Colored', '0')
    with col1:
        thal = st.selectbox('Thalassemia', ['0: Normal', '1: Fixed Defect', '2: Reversable Defect'])

    if st.button('Heart Disease Test Result'):
        try:
            sex = 1 if sex == 'Male' else 0
            cp = int(cp.split(":")[0])
            fbs = int(fbs.split(":")[0])
            restecg = int(restecg.split(":")[0])
            exang = int(exang.split(":")[0])
            slope = int(slope.split(":")[0])
            thal = int(thal.split(":")[0])

            input_data = [
                float(age), sex, cp, float(trestbps), float(chol), fbs,
                restecg, float(thalach), exang, float(oldpeak),
                slope, float(ca), thal
            ]
            result = heart_model.predict([input_data])[0]
            st.success("The person does not have heart disease." if result == 0 else "The person has heart disease.")
        except Exception as e:
            st.error(f"Input Error: {str(e)}")

# Parkinson's Prediction
# Parkinson's Prediction
if selected == 'Parkinsons Prediction':
    st.title("🧠 Parkinson's Disease Prediction")
    st.write(":blue[Predict Parkinson's Disease based on voice and health metrics.]")

    col1, col2 = st.columns(2)

    with col1:
        fo = st.text_input("MDVP:Fo(Hz)", '120')
        fhi = st.text_input("MDVP:Fhi(Hz)", '140')
        flo = st.text_input("MDVP:Flo(Hz)", '100')
        jitter_percent = st.text_input("MDVP:Jitter(%)", '0.005')
        jitter_abs = st.text_input("MDVP:Jitter(Abs)", '0.00005')
        rap = st.text_input("MDVP:RAP", '0.003')
        ppq = st.text_input("MDVP:PPQ", '0.004')
        ddp = st.text_input("Jitter:DDP", '0.009')
        shimmer = st.text_input("MDVP:Shimmer", '0.03')
        shimmer_db = st.text_input("MDVP:Shimmer(dB)", '0.3')
        apq3 = st.text_input("Shimmer:APQ3", '0.01')

    with col2:
        apq5 = st.text_input("Shimmer:APQ5", '0.02')
        apq = st.text_input("MDVP:APQ", '0.02')
        dda = st.text_input("Shimmer:DDA", '0.01')
        nhr = st.text_input("NHR", '0.02')
        hnr = st.text_input("HNR", '20')
        rpde = st.text_input("RPDE", '0.4')
        dfa = st.text_input("DFA", '0.7')
        spread1 = st.text_input("spread1", '-6.5')
        spread2 = st.text_input("spread2", '0.1')
        d2 = st.text_input("D2", '2.3')
        ppe = st.text_input("PPE", '0.2')

    if st.button("Parkinson's Test Result"):
        try:
            features = list(map(float, [
                fo, fhi, flo, jitter_percent, jitter_abs,
                rap, ppq, ddp, shimmer, shimmer_db,
                apq3, apq5, apq, dda, nhr, hnr,
                rpde, dfa, spread1, spread2, d2, ppe
            ]))

            result = parkinsons_model.predict([features])[0]

            if result == 1:
                st.error("The person **may have Parkinson's Disease**.")
            else:
                st.success("The person **does not have Parkinson's Disease**.")
        
        except Exception as e:
            st.error(f"Input Error: {str(e)}. Please enter valid numerical values.")



# Yoga Posture Corrector
if selected == "Yoga Posture Corrector":
    st.title("🧘‍♂️ Yoga Posture Corrector")
    st.write("Click the button below to launch the live posture correction app.")
    if st.button("Open Urban Yogi Pose Corrector"):
        webbrowser.open_new_tab("https://urban-yogi-main.vercel.app/")

# Feedback Page
if selected == "Feedback":
    st.title("📝 Feedback Section")
    st.write("Thank you for using our app. Your feedback is valuable!")
    feedback = st.text_area("Write your suggestions below:")
    rating = st.slider("How was your experience?", 0, 10, 5)
    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback!")
