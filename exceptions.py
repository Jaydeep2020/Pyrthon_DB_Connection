class AppError(Exception):
    """
    Base exception for the application.

    All custom exceptions should inherit from this class so they can be
    caught together when needed.

    Example:
        except AppError as e:
            print(e)
    """
    pass


class StudentNotFoundError(AppError):
    """
    Raised when a student with the given ID does not exist.
    """

    def __init__(self, student_id: int):
        self.student_id = student_id
        super().__init__(f"Student with ID {student_id} was not found.")


class CourseNotFoundError(AppError):
    """
    Raised when a course with the given ID does not exist.
    """

    def __init__(self, course_id: int):
        self.course_id = course_id
        super().__init__(f"Course with ID {course_id} was not found.")


class EnrollmentError(AppError):
    """
    Raised when enrollment-related operations fail.
    """

    def __init__(self, message: str = "Enrollment operation failed."):
        super().__init__(message)