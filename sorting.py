class Student:
    def __init__(self, name, mark1, mark2):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2

    def calculate_total_marks(self):
        return self.mark1 + self.mark2

def add_student(students):
    name = input("Enter student's name: ")
    mark1 = float(input("Enter mark 1: "))
    mark2 = float(input("Enter mark 2: "))
    students.append(Student(name, mark1, mark2))
    print("Student added successfully!")

def calculate_total_marks(students):
    for student in students:
        total_marks = student.calculate_total_marks()
        print(f"{student.name}: Total Marks = {total_marks}")

def selection_sort(students):
    n = len(students)
    for i in range(n - 1):
        mini = i
        for j in range(i + 1, n):
            if students[j].calculate_total_marks() < students[mini].calculate_total_marks():
                mini = j
        students[i], students[min_idx] = students[mini], students[i]

def display_sorted_students(students):
    selection_sort(students)
    print("Sorted List of Students:")
    for student in students:
        print(f"Name: {student.name}, Total Marks: {student.calculate_total_marks()}")

def display_menu():
    print("\nMenu:")
    print("1. Add Student")
    print("2. Calculate Total Marks for all Students")
    print("3. Display Sorted List of Students by Total Marks")
    print("4. Exit")

def main():
    students = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student(students)
        elif choice == "2":
            calculate_total_marks(students)
        elif choice == "3":
            display_sorted_students(students)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Call the main function directly
main()