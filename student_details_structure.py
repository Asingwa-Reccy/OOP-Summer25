# Student's dataset variables
first_name = "Reccy"
last_name = "Asingwa"
index_number = 12345
nationality = "kenyan"
starting_date = "2025-03-13"
courses = ["Mathematics", "Physics", "Computer Science"]
def display_student_info(first_name, last_name, index_number, nationality, starting_date, courses):
    print("Student Information:")
    print(f"Name: {first_name} {last_name}")
    print(f"Index Number: {index_number}")
    print(f"Nationality: {nationality}")
    print(f"Starting Date: {starting_date}")
    print(f"Courses: {', '.join(courses)}")

# Call the function with your variables
display_student_info(first_name, last_name, index_number, nationality, starting_date, courses)
