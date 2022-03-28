student_list = []


def create_student():
    name = input("Please enter the new student's name: ")
    student_data = {
        'name': name,
        'marks': []
    }

    return student_data


def add_mark(student, mark):
    student['marks'].append(mark)


def calculate_average_mark(student):
    number = len(student['marks'])
    if number == 0:
        return 0

    total = sum(student['marks'])
    return total / number


def student_detail(student):
    print("{}, average mark: {}".format(student['name'],
                                        calculate_average_mark(student)))


def print_student_list(students):
    for i, student in enumerate(students):
        print("ID: {}".format(i))
        student_detail(student)


def menu():
    selection = input("Enter 'p' to print the student list,\n"
                      "'s' to add a new student, \n"
                      "'a' to add a mark to a student,\n"
                      "or 'q' to quit. \n"
                      "Enter your selection: \n")
    while selection != 'q':
        if selection == 'p':
            print(print_student_list(student_list))
        elif selection == 's':
            student_list.append(create_student())
        elif selection == 'a':
            student_id = int(input("Enter the student ID to add a mark to: "))
            student = student_list[student_id]
            new_mark = int(input("Enter the new mark to be added: "))
            add_mark(student, new_mark)
        selection = input("Enter 'p' to print the student list,"
                          "'s' to add a new student, "
                          "'a' to add a mark to a student,"
                          "or 'q' to quit. "
                          "Enter your selection: ")
        
        
menu()
