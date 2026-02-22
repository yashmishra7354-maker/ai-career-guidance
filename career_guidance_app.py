import streamlit as st

st.set_page_config(page_title="Career Guidance App", layout="wide")

# ---------- SESSION STATE ----------
if "step" not in st.session_state:
    st.session_state.step = 1

if "profile" not in st.session_state:
    st.session_state.profile = {}

# ---------- STEP 1 : BASIC PROFILE ----------
if st.session_state.step == 1:
    st.title("👤 Create Your Profile")

    name = st.text_input("Full Name")
    age = st.number_input("Age", 10, 60)
    education = st.selectbox("Current Level", ["10th", "12th", "College"])
    stream = st.selectbox("Stream", ["Science", "Commerce", "Arts", "Other"])

    if st.button("Next ➡️"):
        st.session_state.profile.update({
            "name": name,
            "age": age,
            "education": education,
            "stream": stream
        })
        st.session_state.step = 2
        st.rerun()

# ---------- STEP 2 : CAREER GOAL ----------
elif st.session_state.step == 2:
    st.title("🎯 Career Goal")

    goal = st.selectbox(
        "What do you want to pursue?",
        ["Job", "Business", "Higher Studies", "Not Sure"]
    )

    if st.button("Next ➡️"):
        st.session_state.profile["goal"] = goal
        st.session_state.step = 3
        st.rerun()

# ---------- STEP 3 : DYNAMIC QUESTIONS ----------
elif st.session_state.step == 3:
    goal = st.session_state.profile["goal"]
    st.title("🧠 Tell Us More")

    if goal == "Business":
        business_type = st.selectbox("Business Type", ["Online", "Offline", "Family Business"])
        capital = st.selectbox("Capital Available?", ["No", "<50k", "50k+"])
        risk = st.selectbox("Risk Level", ["Low", "Medium", "High"])

        if st.button("Get Guidance"):
            st.session_state.profile.update({
                "business_type": business_type,
                "capital": capital,
                "risk": risk
            })
            st.session_state.step = 4
            st.rerun()

    elif goal == "Job":
        interest = st.selectbox("Interest Area", ["Tech", "Government", "Creative"])
        coding = st.radio("Do you like coding?", ["Yes", "No"])
        study_time = st.selectbox("Daily Study Time", ["1-2 hrs", "3-5 hrs", "5+ hrs"])

        if st.button("Get Guidance"):
            st.session_state.profile.update({
                "interest": interest,
                "coding": coding,
                "study_time": study_time
            })
            st.session_state.step = 4
            st.rerun()

    else:
        interest = st.selectbox("What do you enjoy most?", ["Problem Solving", "Creativity", "Helping Others"])
        if st.button("Get Guidance"):
            st.session_state.profile["interest"] = interest
            st.session_state.step = 4
            st.rerun()

# ---------- STEP 4 : GUIDANCE RESULT ----------
elif st.session_state.step == 4:
    st.markdown(
        "<h1 style='color:purple;'>GET GUIDANCE</h1>",
        unsafe_allow_html=True
    )

    profile = st.session_state.profile
    goal = profile.get("goal")

    # ----- SCORING SYSTEM -----
    score = 0
    if goal == "Business":
        score += 30
        if profile.get("business_type") == "Online":
            score += 20
        if profile.get("capital") == "No":
            score += 10
        if profile.get("risk") == "High":
            score += 20

    elif goal == "Job":
        score += 20
        if profile.get("coding") == "Yes":
            score += 30
        if profile.get("study_time") == "5+ hrs":
            score += 20

    # ----- CAREER STRENGTH ANALYSIS -----
    st.markdown("## 📊 Career Strength Analysis")

    if score >= 70:
        st.success("🔥 Strong fit for this career path")
    elif score >= 40:
        st.warning("⚠️ Can succeed with proper guidance")
    else:
        st.info("🔍 Explore more options before deciding")

    st.write("Your Career Readiness Score:", score)

    # ----- MAIN RECOMMENDATION -----
    if goal == "Business":
        st.success("🚀 Recommendation: Start with digital skills + low‑risk online business.")
        st.write("Suggested Skills: Marketing, Freelancing, AI tools")

    elif goal == "Job":
        if profile.get("coding") == "Yes":
            st.success("💻 Recommendation: Learn Python → AI → Projects")
        else:
            st.success("📚 Recommendation: Government or non‑coding career paths")

    else:
        st.success("🔍 Recommendation: Explore multiple fields before final decision")

    # ----- COURSES SECTION -----
    st.markdown("## 📚 Recommended Courses")

    if goal == "Business":
        st.write("✅ Digital Marketing (Free)")
        st.write("✅ Freelancing Basics")
        st.write("✅ Business Model Basics")

        st.markdown("### 🛣️ 6 Month Roadmap")
        st.write("Month 1–2: Learn skills")
        st.write("Month 3–4: Small projects")
        st.write("Month 5–6: Start earning")

    elif goal == "Job" and profile.get("coding") == "Yes":
        st.write("✅ Python")
        st.write("✅ Data Structures")
        st.write("✅ AI Basics")

        st.markdown("### 🛣️ 6 Month Roadmap")
        st.write("Month 1–2: Python")
        st.write("Month 3–4: Projects")
        st.write("Month 5–6: Internship prep")
    st.write("👤 Profile Data:", profile)

    # ----- SAVE DATA TO CSV (ONLY ONCE) -----
    if "saved" not in st.session_state:
        file_name = "career_data.csv"
        df = pd.DataFrame([profile])

        if os.path.exists(file_name):
            df.to_csv(file_name, mode="a", header=False, index=False)
        else:
            df.to_csv(file_name, index=False)

        st.session_state.saved = True
        st.success("✅ Your data has been saved successfully!")
