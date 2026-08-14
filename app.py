import streamlit as st

# ==============================
# AI STUDENT PERFORMANCE APP
# ==============================

st.set_page_config(
    page_title="AI Student Performance",
    page_icon="🎓",
    layout="centered"
)

# ==============================
# TITLE
# ==============================

st.title("🎓 AI STUDENT PERFORMANCE")
st.subheader("Performance Prediction & Personalized Study Planner")

st.divider()

# ==============================
# STUDENT INFORMATION
# ==============================

st.header("📝 Student Information")

name = st.text_input("Student Name")

attendance = st.number_input(
    "Attendance (%)",
    min_value=0.0,
    max_value=100.0,
    value=75.0
)

study_hours = st.number_input(
    "Daily Study Hours",
    min_value=0.0,
    max_value=24.0,
    value=2.0
)

maths = st.number_input(
    "Mathematics Marks (%)",
    min_value=0.0,
    max_value=100.0,
    value=70.0
)

science = st.number_input(
    "Science Marks (%)",
    min_value=0.0,
    max_value=100.0,
    value=70.0
)

english = st.number_input(
    "English Marks (%)",
    min_value=0.0,
    max_value=100.0,
    value=70.0
)

# ==============================
# PREDICTION
# ==============================

if st.button("🤖 PREDICT PERFORMANCE", use_container_width=True):

    if name.strip() == "":
        st.error("Please enter the student name.")

    else:

        # Average marks
        average_marks = (maths + science + english) / 3

        # Study score
        study_score = min(study_hours * 10, 100)

        # Prediction
        predicted_score = (
            average_marks * 0.65
            + attendance * 0.20
            + study_score * 0.15
        )

        predicted_score = min(
            max(predicted_score, 0),
            100
        )

        # ==============================
        # PERFORMANCE LEVEL
        # ==============================

        if predicted_score >= 85:
            level = "Excellent"
            color = "green"

        elif predicted_score >= 70:
            level = "Good"
            color = "blue"

        elif predicted_score >= 50:
            level = "Average"
            color = "orange"

        else:
            level = "Needs Improvement"
            color = "red"

        # ==============================
        # SUBJECT ANALYSIS
        # ==============================

        subjects = {
            "Mathematics": maths,
            "Science": science,
            "English": english
        }

        weakest_subject = min(
            subjects,
            key=subjects.get
        )

        strongest_subject = max(
            subjects,
            key=subjects.get
        )

        # ==============================
        # RISK LEVEL
        # ==============================

        if predicted_score >= 70:
            risk = "LOW RISK"

        elif predicted_score >= 50:
            risk = "MEDIUM RISK"

        else:
            risk = "HIGH RISK"

        # ==============================
        # DISPLAY RESULTS
        # ==============================

        st.divider()

        st.header("📊 AI PERFORMANCE ANALYSIS")

        st.metric(
            "Predicted Performance",
            f"{predicted_score:.1f}%"
        )

        if color == "green":
            st.success(f"Performance Level: {level}")

        elif color == "blue":
            st.info(f"Performance Level: {level}")

        elif color == "orange":
            st.warning(f"Performance Level: {level}")

        else:
            st.error(f"Performance Level: {level}")

        if risk == "LOW RISK":
            st.success(f"Risk Level: {risk}")

        elif risk == "MEDIUM RISK":
            st.warning(f"Risk Level: {risk}")

        else:
            st.error(f"Risk Level: {risk}")

        col1, col2 = st.columns(2)

        with col1:
            st.write("🔴 **Weakest Subject**")
            st.write(weakest_subject)

        with col2:
            st.write("🟢 **Strongest Subject**")
            st.write(strongest_subject)

        # ==============================
        # STUDY PLAN
        # ==============================

        st.divider()

        st.header("📚 PERSONALIZED STUDY PLAN")

        if weakest_subject == "Mathematics":

            plan = [
                ("Monday", "Mathematics", "2 hours"),
                ("Tuesday", "Science", "1 hour"),
                ("Wednesday", "Mathematics", "2 hours"),
                ("Thursday", "English", "1 hour"),
                ("Friday", "Mathematics", "2 hours"),
                ("Saturday", "Science", "1 hour"),
                ("Sunday", "Revision", "1 hour")
            ]

        elif weakest_subject == "Science":

            plan = [
                ("Monday", "Science", "2 hours"),
                ("Tuesday", "Mathematics", "1 hour"),
                ("Wednesday", "Science", "2 hours"),
                ("Thursday", "English", "1 hour"),
                ("Friday", "Science", "2 hours"),
                ("Saturday", "Mathematics", "1 hour"),
                ("Sunday", "Revision", "1 hour")
            ]

        else:

            plan = [
                ("Monday", "English", "2 hours"),
                ("Tuesday", "Mathematics", "1 hour"),
                ("Wednesday", "English", "2 hours"),
                ("Thursday", "Science", "1 hour"),
                ("Friday", "English", "2 hours"),
                ("Saturday", "Mathematics", "1 hour"),
                ("Sunday", "Revision", "1 hour")
            ]

        for day, subject, hours in plan:
            st.write(f"**{day}** → {subject} — {hours}")

        st.divider()

        st.caption(
            "AI-Based Student Performance Prediction System"
        )