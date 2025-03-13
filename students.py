# List of students as dictionaries
students = [
    {"first_name": "John", "last_name": "Doe", "index_number": 12345, "nationality": "Polish", "starting_date": "2025-03-13", "courses": ["Mathematics", "Physics", "Computer Science"]},
    {"first_name": "Alice", "last_name": "Smith", "index_number": 67890, "nationality": "British", "starting_date": "2025-03-14", "courses": ["Biology", "Chemistry", "History"]},
    {"first_name": "Carlos", "last_name": "Garcia", "index_number": 11223, "nationality": "Spanish", "starting_date": "2025-03-15", "courses": ["Art", "Philosophy", "Music"]}
]

# Loop to display each student's name and index number
for student in students:
    print(f"Name: {student['first_name']} {student['last_name']}, Index Number: {student['index_number']}")

