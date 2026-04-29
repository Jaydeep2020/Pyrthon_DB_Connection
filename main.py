from Services.student import Student
from Services.courses import Course
from Services.enrollment import Enrollment
from exceptions import (StudentNotFoundError, CourseNotFoundError, EnrollmentError)
import streamlit as st


st.set_page_config(
    page_title="Student Course Management System",
    layout="wide"
)

st.title("🎓 Student Course Management System")

menu = st.sidebar.selectbox(
    "Select Option",
    [
        "Add Student",
        "View Students",
        "Search Student",
        "Delete Student",
        "Add Course",
        "View Courses",
        "Search Course",
        "Delete Course",
        "Enroll Student",
        "View Enrollments"
    ]
)

try:
    # ---------------- ADD STUDENT ----------------
    if menu == "Add Student":
        st.header("Add Student")

        full_name = st.text_input("Full Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone")
        dob = st.date_input("Date of Birth")
        gender = st.selectbox(
            "Gender",
            ["Male", "Female", "Other"]
        )
        address = st.text_area("Address")

        if st.button("Add Student"):
            if not full_name or not email:
                st.warning("Full Name and Email are required")
            else:
                s = Student(full_name, email, phone, dob, gender, address)
                s.add_student()
                st.success("✅ Student added successfully")
                del s

    # ---------------- VIEW STUDENTS ----------------
    elif menu == "View Students":
        st.header("All Students")

        students = Student.get_all_students()

        if students:
            st.table(students)
        else:
            st.info("No students found")

    # ---------------- SEARCH STUDENT ---------------
    elif menu == "Search Student":
        st.header("Search Student")

        student_name = st.text_input("Student Name")

        if st.button("Search Student"):
            student = Student.search_student(student_name)
            st.table(student)


    # ---------------- DELETE STUDENT ----------------
    elif menu == "Delete Student":
        st.header("Delete Student")

        student_id = st.number_input(
            "Student ID",
            min_value=1,
            step=1
        )

        if st.button("Delete Student"):
            Student.delete_student(student_id)
            st.success("✅ Student deleted successfully")

    # ---------------- ADD COURSE ----------------
    elif menu == "Add Course":
        st.header("Add Course")

        course_name = st.text_input("Course Name")
        course_code = st.text_input("Course Code")
        duration = st.number_input(
            "Duration (Months)",
            min_value=1,
            step=1
        )
        fees = st.number_input(
            "Fees",
            min_value=0.0
        )
        description = st.text_area("Description")

        if st.button("Add Course"):
            if not course_name or not course_code:
                st.warning("Course Name and Course Code are required")
            else:
                c = Course(course_name, course_code, duration, fees, description)
                c.add_course()
                st.success("✅ Course added successfully")
                del c

    # ---------------- VIEW COURSES ----------------
    elif menu == "View Courses":
        st.header("All Courses")

        courses = Course.get_all_courses()

        if courses:
            st.table(courses)
        else:
            st.info("No courses found")

    # ---------------- SEARCH STUDENT ---------------
    elif menu == "Search Course":
        st.header("Search Course")

        course_name = st.text_input("Course Name")

        if st.button("Search Course"):
            course = Course.search_course(course_name)
            st.table(course)

    # ---------------- DELETE COURSE ----------------
    elif menu == "Delete Course":
        st.header("Delete Course")

        course_id = st.number_input(
            "Course ID",
            min_value=1,
            step=1
        )

        if st.button("Delete Course"):
            Course.delete_course(course_id)
            st.success("✅ Course deleted successfully")

    # ---------------- ENROLL STUDENT ----------------
    elif menu == "Enroll Student":
        st.header("Enroll Student Into Course")

        student_id = st.number_input(
            "Student ID",
            min_value=1,
            step=1
        )

        course_id = st.number_input(
            "Course ID",
            min_value=1,
            step=1
        )

        if st.button("Enroll"):
            Enrollment.enroll_student(
                student_id,
                course_id
            )
            st.success("✅ Student enrolled successfully")

    # ---------------- VIEW ENROLLMENTS ----------------
    elif menu == "View Enrollments":
        st.header("All Enrollments")

        enrollments = Enrollment.get_all_enrollments()

        if enrollments:
            st.table(enrollments)
        else:
            st.info("No enrollments found")

# ---------------- ERROR HANDLING ----------------

except StudentNotFoundError as e:
    st.error(str(e))

except CourseNotFoundError as e:
    st.error(str(e))

except EnrollmentError as e:
    st.error(str(e))

except Exception as e:
    st.error(f"Unexpected Error: {str(e)}")