from exceptions import CourseNotFoundError
from DB.db_connection import get_cursor

class Courses:
    def __init__(self, name: str, code: str, duration: int, fees: float, description: str):
        self.name = name
        self.code = code
        self.duration = duration
        self.fees = fees
        self.description = description

    def add_course(self):
        insert_query = """
        INSERT INTO courses ("course_name", "course_code", "duration_months", "fees", "description")
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (self.name, self.code, self.duration, self.fees, self.description)

        with get_cursor() as cursor:
            cursor.execute(insert_query, values)
            print(f"✅ Course '{self.name}' added successfully!")

    @staticmethod
    def get_all_courses():
        query = """
        SELECT id, course_name, course_code, duration_months, fees, description FROM courses"""
        with get_cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

    @staticmethod
    def delete_course(id):
        query = """DELETE FROM courses WHERE id = %s"""
        with get_cursor() as cursor:
            cursor.execute(query, (id,))
            if cursor.rowcount == 0:
                raise CourseNotFoundError(id)








# c = Courses("AI/ML", "AI002", 6, 24000, "Learning ai ml concepts")
# c.add_course()

# courses = Courses.get_all_courses()
# print(courses)

# Courses.delete_course(1)

