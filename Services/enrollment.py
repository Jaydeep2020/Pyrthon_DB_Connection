from DB.db_connection import get_cursor
# from exceptions import EnrollmentError

class Enrollment:
    @staticmethod
    def enroll_student(student_id, course_id):
        query = """
        INSERT INTO enrollments (student_id, course_id)
        VALUES (%s, %s)
        """
        values = (student_id, course_id)
        # try:
        with get_cursor() as cursor:
            cursor.execute(query, values)
        # except Exception:
        #     raise EnrollmentError("Enrollment failed or already exists")

    @staticmethod
    def get_all_enrollments():
        query = """
        SELECT e.id, s.full_name, c.course_name, e.enrollment_date, e.status
        FROM enrollments e
        JOIN students s ON e.student_id = s.id
        JOIN courses c ON e.course_id = c.id
        ORDER BY e.id
        """
        with get_cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

# Enrollment.enroll_student(1, 2)