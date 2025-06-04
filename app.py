import streamlit as st
import pickle
import os
from streamlit_option_menu import option_menu
from PIL import Image

# Page config
st.set_page_config(page_title="ProActive Health Guard", layout="wide", page_icon="🧬")

# Theme color
orange = "#FF6F00"
light_orange = "#FFE0B2"
white_bg = "#FFFFFF"

# Custom CSS
st.markdown(f"""
    <style>
        .reportview-container {{
            background-color: {white_bg};
        }}
        .sidebar .sidebar-content {{
            background-color: {light_orange};
        }}
        .css-1d391kg {{
            background-color: {white_bg};
        }}
        h1, h2, h3, h4 {{
            color: {orange};
        }}
        .stButton>button {{
            background-color: {orange};
            color: white;
        }}
        .stAlert {{
            padding: 20px;
            border-radius: 10px;
        }}
    </style>
""", unsafe_allow_html=True)

# Load models with error handling
try:
    diabetes_model = pickle.load(open("Diseases/Diabetes-Prediction-EDA/diabetes.pkl", 'rb'))
    heart_model = pickle.load(open("Diseases/Heart-Disease-Prediction/heart.pkl", 'rb'))
    parkinson_model = pickle.load(open("Diseases/Parkinson-Disease-EDA-and-Prediction/Parkinsons.pkl", 'rb'))
    autism_model = pickle.load(open("Diseases/Autism-EDA/autism.pkl", 'rb'))
except Exception as e:
    st.error(f"Error loading models: {str(e)}")

# Sidebar menu
with st.sidebar:
    selected = option_menu("ProActive Health Guard",
        ["Welcome", "Autism", "Diabetes Prediction", "Heart Disease Prediction",
         "Parkinsons Prediction", "Yoga Posture Detection", "Review"],
        icons=['house', 'person', 'droplet-half', 'heart', 'activity', 'camera-video', 'chat-left-text'],
        default_index=0,
        styles={
            "container": {"background-color": light_orange},
            "icon": {"color": orange, "font-size": "18px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px"},
            "nav-link-selected": {"background-color": orange},
        })

# Welcome Page
if selected == "Welcome":
    st.title("👩‍⚕️ ProActive Health Guard")
    st.markdown(f"""
        <div style="background-color:{light_orange};padding:20px;border-radius:10px">
            <h3 style="color:{orange};">Empowering You with AI</h3>
            <p>ProActive Health Guard is a revolutionary healthcare initiative leveraging 
            <b>machine learning, Streamlit, bots, and Python</b> to offer early disease detection and yoga posture correction, 
            enabling a healthier tomorrow.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.image("Urban-Yogi-Main/UY-1.png", caption="Health Monitoring System", use_column_width=True)

# Autism Prediction
if selected == "Autism":
    st.header("🧠 Autism Prediction")
    with st.form("autism_form"):
        cols = st.columns(2)
        age = cols[0].number_input("Age", min_value=1, max_value=100, value=18)
        gender = cols[1].selectbox("Gender", ["Male", "Female", "Other"])
        a1 = st.slider("Q1: Difficulty with social situations", 0, 1)
        a2 = st.slider("Q2: Fixation on routines", 0, 1)
        a3 = st.slider("Q3: Sensory sensitivity", 0, 1)
        submitted = st.form_submit_button("Predict Autism")
    
    if submitted:
        try:
            features = [int(age), 1 if gender == "Male" else 0, a1, a2, a3]
            prediction = autism_model.predict([features])
            if prediction[0] == 1:
                st.error("Result: Autistic - Please consult a specialist")
            else:
                st.success("Result: Not Autistic")
        except Exception as e:
            st.error(f"Prediction error: {str(e)}")

# Diabetes Prediction
if selected == "Diabetes Prediction":
    st.header("🩸 Diabetes Prediction")
    with st.form("diabetes_form"):
        cols = st.columns(4)
        Pregnancies = cols[0].number_input("Pregnancies", min_value=0, max_value=20, value=0)
        Glucose = cols[1].number_input("Glucose", min_value=0, max_value=200, value=100)
        BloodPressure = cols[2].number_input("Blood Pressure", min_value=0, max_value=150, value=70)
        SkinThickness = cols[3].number_input("Skin Thickness", min_value=0, max_value=100, value=20)
        Insulin = cols[0].number_input("Insulin", min_value=0, max_value=1000, value=80)
        BMI = cols[1].number_input("BMI", min_value=0.0, max_value=70.0, value=25.0, step=0.1)
        DiabetesPedigreeFunction = cols[2].number_input("Pedigree Function", min_value=0.0, max_value=3.0, value=0.5, step=0.01)
        Age = cols[3].number_input("Age", min_value=1, max_value=120, value=30)
        submitted = st.form_submit_button("Diabetes Test Result")
    
    if submitted:
        try:
            values = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, 
                     BMI, DiabetesPedigreeFunction, Age]
            prediction = diabetes_model.predict([values])
            if prediction[0] == 1:
                st.error("Result: Diabetic - Please consult a doctor")
            else:
                st.success("Result: Not Diabetic")
        except Exception as e:
            st.error(f"Prediction error: {str(e)}")

# Heart Disease Prediction
if selected == "Heart Disease Prediction":
    st.header("❤️ Heart Disease Prediction")
    with st.form("heart_form"):
        cols = st.columns(4)
        age = cols[0].number_input("Age", min_value=1, max_value=120, value=50)
        sex = cols[1].selectbox("Sex", ["Male", "Female"])
        cp = cols[2].number_input("Chest Pain type (0-3)", min_value=0, max_value=3, value=0)
        trestbps = cols[3].number_input("Resting BP", min_value=50, max_value=250, value=120)
        chol = cols[0].number_input("Cholesterol", min_value=100, max_value=600, value=200)
        fbs = cols[1].number_input("FBS > 120", min_value=0, max_value=1, value=0)
        restecg = cols[2].number_input("Rest ECG", min_value=0, max_value=2, value=0)
        thalach = cols[3].number_input("Max Heart Rate", min_value=50, max_value=220, value=150)
        exang = cols[0].number_input("Exercise Angina", min_value=0, max_value=1, value=0)
        oldpeak = cols[1].number_input("Oldpeak", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
        slope = cols[2].number_input("Slope", min_value=0, max_value=2, value=1)
        ca = cols[3].number_input("Vessels", min_value=0, max_value=4, value=0)
        thal = cols[0].number_input("Thal", min_value=0, max_value=3, value=1)
        submitted = st.form_submit_button("Heart Disease Test Result")
    
    if submitted:
        try:
            sex_num = 1 if sex == "Male" else 0
            features = [age, sex_num, cp, trestbps, chol, fbs, restecg, 
                       thalach, exang, oldpeak, slope, ca, thal]
            prediction = heart_model.predict([features])
            if prediction[0] == 1:
                st.error("Result: Heart Disease Detected - Please consult a cardiologist")
            else:
                st.success("Result: No Heart Disease Detected")
        except Exception as e:
            st.error(f"Prediction error: {str(e)}")

# Parkinsons Prediction
if selected == "Parkinsons Prediction":
    st.header("🧬 Parkinson's Disease Prediction")
    with st.form("parkinsons_form"):
        cols = st.columns(4)
        mdvp_fo = cols[0].number_input("MDVP:Fo(Hz)", min_value=50.0, max_value=300.0, value=150.0, step=0.1)
        mdvp_fhi = cols[1].number_input("MDVP:Fhi(Hz)", min_value=50.0, max_value=300.0, value=170.0, step=0.1)
        mdvp_flo = cols[2].number_input("MDVP:Flo(Hz)", min_value=50.0, max_value=300.0, value=100.0, step=0.1)
        mdvp_jitter = cols[3].number_input("MDVP:Jitter(%)", min_value=0.0, max_value=1.0, value=0.005, step=0.001, format="%.3f")
        mdvp_shimmer = cols[0].number_input("MDVP:Shimmer", min_value=0.0, max_value=1.0, value=0.02, step=0.001, format="%.3f")
        nhr = cols[1].number_input("NHR", min_value=0.0, max_value=1.0, value=0.01, step=0.001, format="%.3f")
        hnr = cols[2].number_input("HNR", min_value=0.0, max_value=40.0, value=20.0, step=0.1)
        rpde = cols[3].number_input("RPDE", min_value=0.0, max_value=1.0, value=0.5, step=0.001, format="%.3f")
        dfa = cols[0].number_input("DFA", min_value=0.0, max_value=1.0, value=0.7, step=0.001, format="%.3f")
        spread1 = cols[1].number_input("spread1", min_value=-10.0, max_value=0.0, value=-5.0, step=0.1)
        spread2 = cols[2].number_input("spread2", min_value=0.0, max_value=1.0, value=0.2, step=0.01)
        d2 = cols[3].number_input("D2", min_value=0.0, max_value=10.0, value=2.0, step=0.1)
        ppe = cols[0].number_input("PPE", min_value=0.0, max_value=1.0, value=0.2, step=0.01)
        submitted = st.form_submit_button("Parkinson's Test Result")
    
    if submitted:
        try:
            features = [mdvp_fo, mdvp_fhi, mdvp_flo, mdvp_jitter, mdvp_shimmer,
                      nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe]
            prediction = parkinson_model.predict([features])
            if prediction[0] == 1:
                st.error("Result: Parkinson's Detected - Please consult a neurologist")
            else:
                st.success("Result: No Parkinson's Detected")
        except Exception as e:
            st.error(f"Prediction error: {str(e)}")

# Yoga Posture Detection
if selected == "Yoga Posture Detection":
    st.header("🧘 Urban-Yogi: Yoga Posture Detection")
    
    # Option 1: Simple implementation with image upload
    st.subheader("Upload an image for posture analysis")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        st.write("Analyzing posture...")
        
        # Placeholder for actual yoga detection logic
        # In a real implementation, you would:
        # 1. Process the image with your yoga detection model
        # 2. Return feedback on the posture
        st.warning("Posture analysis functionality would be implemented here with proper model integration")
        
        # Example feedback
        st.success("""
        Posture Analysis Results:
        - Alignment: Good
        - Balance: Needs improvement
        - Suggested correction: Straighten your back
        """)
    
    # Option 2: Link to separate app (if you prefer to keep them separate)
    st.markdown("---")
    st.markdown("""
    ### For advanced real-time posture detection
    [Click here to access the full Urban-Yogi Detector](https://urban-yogi-yoga-detection.streamlit.app/)
    """)

# Review Section
if selected == "Review":
    st.header("📝 User Review & Feedback")
    with st.form("review_form"):
        name = st.text_input("Name (optional)")
        email = st.text_input("Email (optional)")
        feedback = st.text_area("Your feedback or suggestions")
        rating = st.slider("Rating (1-10)", 1, 10, 8)
        submitted = st.form_submit_button("Submit Review")
    
    if submitted:
        st.success("🎉 Thank you for your feedback!")
        st.balloons()
        
        # In a real app, you would store this data
        st.write(f"""
        Received feedback from: {name if name else 'Anonymous'}
        Rating: {rating}/10
        Feedback: {feedback}
        """)