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

def guide(interest, hours):
    if interest == "Coding" and hours >= 3:
        return "AI / Software Engineering"
    elif interest == "Mathematics":
        return "Data Analysis / Research"
    elif interest == "Biology":
        return "Medical / Biotech Field"
    elif interest == "Arts":
        return "Design / Creative Field"
    else:
        return "Exploration Phase – Build basic skills"

if st.button("Get Guidance"):
    if name.strip() == "":
        st.warning("Please enter your name")
    else:
        st.success(f"Hello {name} 👋")
        st.info(guide(interest, hours))
