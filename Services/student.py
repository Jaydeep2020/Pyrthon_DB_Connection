from exceptions import StudentNotFoundError
from DB.db_connection import get_cursor

class Student:
    def __init__(self, full_name: str, email: str, phone: str, dob: str, gender: str, address: str):
        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.dob = dob
        self.gender = gender
        self.address = address

    def add_student(self):
        query = """
        INSERT INTO students ("full_name", "email", "phone", "date_of_birth", "gender", "address")
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (self.full_name, self.email, self.phone, self.dob, self.gender, self.address)

        with get_cursor() as cursor:
            cursor.execute(query, values)
            print(f"✅ Student '{self.full_name}' added successfully!")

    @staticmethod
    def get_all_students():
        query = """
        SELECT * FROM students"""
        with get_cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

    @staticmethod
    def delete_student(id):
        query = """
        DELETE FROM students WHERE id = %s"""
        with get_cursor() as cursor:
            cursor.execute(query, (id,))
            if cursor.rowcount == 0:
                raise StudentNotFoundError(id)

    @staticmethod
    def search_student(name):
        query = """
        SELECT * FROM students WHERE full_name LIKE %s
        """
        with get_cursor() as cursor:
            cursor.execute(query, (f"%{name}%",))
            return cursor.fetchall()



