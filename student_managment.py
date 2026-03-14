class student:
    school = input("enter the school name: ")
    passing_grade = 40  # Passing grade threshold

    def __init__(self):
        self.name = input("Enter the name of the student: ")
        self.index_number = input("Enter the index number: ")
        print("**" *20, "\n")

    def course_work(self):
        self.course = dict()
        self.total = 0
        self.count = 0
        while True:
            self.subject = input("Enter the subject: ")
            if self.subject == "done":
                break
            self.mark = int(input("Enter the marks: "))
            self.course[self.subject] = self.mark
            self.count += 1
            self.total += self.mark

        self.number_of_subjects = self.count
        self.total_marks_obtained = self.total
        self.average = (self.total) / self.count

        return self.course
    
    def get_grade(self):
        """Calculate grade based on average marks"""
        if self.average >= 80:
            return 'A'
        elif self.average >= 70:
            return 'B'
        elif self.average >= 60:
            return 'C'
        elif self.average >= 50:
            return 'D'
        elif self.average >= self.passing_grade:
            return 'E'
        else:
            return 'F'  # Failed

    def student_id(self):
        self.student_details = dict()
        self.student_details['Name'] = self.name
        self.student_details['Index Number'] = self.index_number
        return self.student_details


def main():
    """Main program to manage multiple students and ranking"""
    students = []
    
    # Input multiple students
    while True:
        print(f"\n--- STUDENT {len(students) + 1} ---")
        std = student()
        marks = std.course_work()
        details = std.student_id()
        std.get_grade()
        students.append(std)
        
        another = input("\nDo you want to enter another student? (yes/no): ").strip().lower()
        if another != 'yes':
            break
    
    if not students:
        print("No students entered!")
        return
    
    # Rank students by average marks (highest to lowest)
    ranked_students = sorted(students, key=lambda x: x.average, reverse=True)
    
    # Display ranking
    print("\n" + "="*80)
    print(f"STUDENT RANKING FOR {student.school.upper()}")
    print("="*80 + "\n")
    
    for rank, student_obj in enumerate(ranked_students, 1):
        status = "PASSED" if student_obj.average >= student.passing_grade else "FAILED"
        print(f"Rank {rank}: {student_obj.name} (Index: {student_obj.index_number})")
        print(f"  Total Marks: {student_obj.total_marks_obtained}")
        print(f"  Average: {student_obj.average:.2f}")
        print(f"  Grade: {student_obj.get_grade()}")
        print(f"  Status: {status}")
        print("-" * 80)
    
    # Summary statistics
    total_passed = sum(1 for s in students if s.average >= student.passing_grade)
    total_failed = len(students) - total_passed
    
    print(f"\nSUMMARY:")
    print(f"Total Students: {len(students)}")
    print(f"Passed: {total_passed}")
    print(f"Failed: {total_failed}")
    print(f"Average of All Students: {sum(s.average for s in students) / len(students):.2f}")
    print("="*80)


if __name__ == "__main__":
    main()