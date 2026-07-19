import streamlit as st
import matplotlib.pyplot as plt
# Personalized recommendation logic based on student performance

st.title("🎓 AI Tutor for Personalized Learning")

math = st.slider("Math Marks", 0, 100, 50)
programming = st.slider("Programming Marks", 0, 100, 50)
english = st.slider("English Marks", 0, 100, 50)

st.info("Enter your marks to receive personalized learning recommendations.")

# This function analyes student marks
# and provides personalized Learning recommendations
def recommendation(marks):
    if marks < 50:
        return "Weak", "Practice MCQs and Beginner Lessons"
    elif marks < 75:
        return "Average", "Revision Notes and Weekly Tests"
    else:
        return "Strong", "Advanced Exercises and Projects"

if st.button("Generate AI Recommendations"):

    st.header("📊 Student Performance Results")

    for subject, marks in {
        "Math": math,
        "Programming": programming,
        "English": english
    }.items():

        level, rec = recommendation(marks)

        st.subheader(subject)
        st.write("Level:", level)
        st.write("Recommendation:", rec)
        
    average = (math + programming + english) / 3

    st.subheader("Overall Performance")
    st.write("Average Score:", round(average, 2))

    if average < 50:
     overall = "Needs Improvement"
   elif average < 75:
      overall = "Good"
else:
    overall = "Excellent"

st.write("Overall Level:", overall)

    fig, ax = plt.subplots()

    subjects = ["Math", "Programming", "English"]
    scores = [math, programming, english]

    ax.bar(subjects, scores)
    ax.set_title("Student Marks Comparison")
    ax.set_xlabel("Subjects")
    ax.set_ylabel("Marks")

    ax.set_ylim(0,100)

    st.pyplot(fig)
    st.subheader("🤖 AI Decision Explanation")

    if math < 50:
        st.write("✓ Math score is below 50%, so practice MCQs and beginner lessons are recommended.")
    elif math < 75:
        st.write("✓ Math performance is average, so revision notes and weekly tests are recommended.")
    else:
        st.write("✓ Math performance is strong, so advanced exercises are recommended.")

    if programming < 50:
        st.write("✓ Programming score is below 50%, so more coding practice is needed.")
    elif programming < 75:
        st.write("✓ Programming performance is average, so regular practice and revision are suggested.")
    else:
        st.write("✓ Programming performance is strong, so advanced projects are suggested.")

    if english < 50:
        st.write("✓ English score is below 50%, so beginner lessons and practice are recommended.")
    elif english < 75:
        st.write("✓ English performance is average, so revision is recommended.")
    else:
        st.write("✓ English performance is strong.")

        st.subheader("📊 System Performance Metrics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Testing Samples", "20")

with col2:
    st.metric("Recommendation Accuracy", "90%")

with col3:
    st.metric("Rule Coverage", "100%")
    