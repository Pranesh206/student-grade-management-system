from student import Student
from database import Database

def main():
    db = Database("students.db")
    while True:
        print("\n--- Student Grade Management ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Name: ")
            grade = input("Grade: ")
            db.add_student(Student(name, grade))
        elif choice == "2":
            db.view_students()
        elif choice == "3":
            id = int(input("Student ID to update: "))
            name = input("New Name: ")
            grade = input("New Grade: ")
            db.update_student(id, Student(name, grade))
        elif choice == "4":
            id = int(input("Student ID to delete: "))
            db.delete_student(id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
