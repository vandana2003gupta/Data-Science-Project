import streamlit as st
import pickle
import webbrowser
from streamlit_option_menu import option_menu
import base64

# Page Configuration
st.set_page_config(page_title="Health Care Analyzer", layout="wide")

# Background Setup
def set_bg_from_local(image_file):
    with open(image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Custom CSS for better visibility of inputs
st.markdown("""
    <style>
    .stTextInput > div > div > input, 
    .stSelectbox > div > div>div,
    .stTextArea textarea {
        background-color: rgba(255, 255, 255, 0.9);
        color: black;
        border: 1px solid #FFA07A;
        border-radius: 10px;
        padding: 0.4rem;
    }

    .stButton button {
        border-radius: 10px;
        background-color: #ff944d;
        color: white;
    }

    .stButton button:hover {
        background-color: #ff6600;
        
    }

    h1 {{
        text-align: center;
        color: black;
    }}

    </style>
""", unsafe_allow_html=True)

# Load Models
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

# Sidebar
with st.sidebar:
    selected = option_menu('Diseases',
                         ['Welcome', 'Autism', 'Diabetes Prediction',
                          'Heart Disease Prediction', 'Parkinsons Prediction',
                          'Yoga Posture Corrector', 'Feedback'],
                         default_index=0)

# Welcome Page
if selected == 'Welcome':
    set_bg_from_local('bg.jpeg')
    st.markdown("<h1>Health Disease Detection</h1>", unsafe_allow_html=True)
    st.write("""This application detects diseases like Diabetes, Heart and Parkinson's 
    using Machine Learning, providing early health risk detection with ML models
    """)
    st.image("Img1.webp", use_container_width=True)

# Autism Page
elif selected == 'Autism':
    set_bg_from_local('bg.jpeg')
    st.markdown("<h1>Autism Detection</h1>", unsafe_allow_html=True)
    st.write("Note - Autism section is under development.")
    st.image("Img2.jpg", use_container_width=True)

# Diabetes Prediction
elif selected == 'Diabetes Prediction':
    set_bg_from_local('bg.jpeg')
    st.markdown("<h1>Diabetes Detection using ML</h1>", unsafe_allow_html=True)
    st.write("Detect whether you are diabetic or not based on medical inputs")

    col1, col2, col3 = st.columns(3)
    with col1: pregnancies = st.text_input('Number of Pregnancies', '0')
    with col2: glucose = st.text_input('Glucose Level', '120')
    with col3: blood_pressure = st.text_input('Blood Pressure', '70')
    with col1: skin_thickness = st.text_input('Skin Thickness', '20')
    with col2: insulin = st.text_input('Insulin Level', '80')
    with col3: bmi = st.text_input('BMI', '25')
    with col1: diabetes_pedigree = st.text_input('Diabetes Pedigree Function', '0.5')
    with col2: age = st.text_input('Age', '30')

    if st.button('Diabetes Test Result'):
        try:
            input_data = [float(pregnancies), float(glucose), float(blood_pressure),
                          float(skin_thickness), float(insulin), float(bmi),
                          float(diabetes_pedigree), float(age)]
            result = diabetes_model.predict([input_data])[0]
            st.success("The person is not diabetic." if result == 0 else "The person is diabetic.")
        except Exception as e:
            st.error(f"Error: {str(e)}. Please enter valid numbers")
    st.image("Diseases/Diabetes-Prediction-EDA/img3.jpg", use_container_width=True)

# Heart Disease Prediction
elif selected == 'Heart Disease Prediction':
    set_bg_from_local('bg.jpeg')
    st.markdown("<h1>Heart Disease Prediction using ML</h1>", unsafe_allow_html=True)
    st.write("Detect whether you have heart disease or not, based on health parameters")

    col1, col2, col3 = st.columns(3)
    with col1: age = st.text_input('Age', '50')
    with col2: sex = st.selectbox('Sex', ['Male', 'Female'])
    with col3: cp = st.selectbox('Chest Pain Type', ['0: Typical', '1: Atypical', '2: Non-anginal', '3: Asymptomatic'])
    with col1: trestbps = st.text_input('Resting BP', '120')
    with col2: chol = st.text_input('Cholesterol', '200')
    with col3: fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['0: No', '1: Yes'])
    with col1: restecg = st.selectbox('Resting ECG', ['0: Normal', '1: ST-T Abnormality', '2: LV Hypertrophy'])
    with col2: thalach = st.text_input('Max Heart Rate', '150')
    with col3: exang = st.selectbox('Exercise Induced Angina', ['0: No', '1: Yes'])
    with col1: oldpeak = st.text_input('ST Depression', '0.0')
    with col2: slope = st.selectbox('Slope', ['0: Upsloping', '1: Flat', '2: Downsloping'])
    with col3: ca = st.text_input('Major Vessels Colored', '0')
    with col1: thal = st.selectbox('Thalassemia', ['0: Normal', '1: Fixed Defect', '2: Reversable Defect'])

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
    st.image("Diseases/Heart-Disease-Prediction/img4.png", use_container_width=True)

# Parkinson’s Disease
elif selected == 'Parkinsons Prediction':
    set_bg_from_local('bg.jpeg')
    st.markdown("<h1>Parkinson's Disease Prediction</h1>", unsafe_allow_html=True)
    st.write("Detect whether you have Parkinson's Disease or not, based on provided metrics.")

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
            st.error("Parkinson's Disease detected." if result == 1 else "No Parkinson's Disease.")
        except Exception as e:
            st.error(f"Input Error: {str(e)}")
    st.image("Diseases/Parkinson-Disease-EDA-and-Prediction/img.webp", use_container_width=True)

# Yoga Posture
elif selected == 'Yoga Posture Corrector':
    set_bg_from_local('bg.jpeg')
    st.markdown("<h1>🧘‍♂️ Yoga Posture Corrector</h1>", unsafe_allow_html=True)
    st.write("Click below to open Urban Yogi live posture correction tool.")
    if st.button("Open Urban Yogi Pose Corrector"):
        webbrowser.open_new_tab("https://urban-yogi-main.vercel.app/")
    st.image("Urban-Yogi-Main/img6.png", use_container_width=True)

# Feedback
elif selected == 'Feedback':
    set_bg_from_local('bg.jpeg')
    st.markdown("<h1>📝 Feedback Section</h1>", unsafe_allow_html=True)
    st.write("We value your feedback!")
    feedback = st.text_area("Write your suggestions below:")
    rating = st.slider("How was your experience?", 0, 10, 5)
    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback!")
