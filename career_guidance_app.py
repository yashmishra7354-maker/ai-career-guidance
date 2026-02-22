import streamlit as st

st.set_page_config(page_title="AI Career Guidance", layout="centered")

st.title("🎓 AI-Based Career Guidance System")
st.caption("AI as a Mentor, Not a Judge")

name = st.text_input("Your Name")

interest = st.selectbox(
    "Your Interest",
    ["Coding", "Mathematics", "Biology", "Arts", "Exploring"]
)

hours = st.slider("Daily Study Hours", 0, 10, 2)

if st.button("Get Guidance"):
    st.success(f"Hello {name} 👋")

    if interest == "Coding":
        st.write("👉 Suggested Path: Programming → DSA → AI/ML")
    elif interest == "Mathematics":
        st.write("👉 Suggested Path: Statistics → Data Analysis → Research")
    elif interest == "Biology":
        st.write("👉 Suggested Path: Bioinformatics → AI in Healthcare")
    elif interest == "Arts":
        st.write("👉 Suggested Path: UI/UX → Creative Tech")
    else:
        st.write("👉 Explore different fields to find your passion")
