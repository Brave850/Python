import csv

def write_into_csv(info_list):
    with open('student_open.csv','a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name", "Roll-Number", "Age", "Contact_Number", "E-mail_ID"])


        writer.writerow(info_list)

if __name__ == '__main__':
    condition = True
    student_number = 1

    while(condition):
        student_info = input("Enter the student information for student {}. in the following format (Name Roll_Number Age Contact_Number E-mail_ID): ".format(student_number))


        student_info_list=student_info.split(' ')
        

        print("\nThe Entered information is:-\nName: {}\nRoll Number: {}\nAge: {}\nContact_Number: {}\nE-mail_ID: {}\n"
                                        .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3],student_info_list[4]))

        choice_check =input("In Entered Value is correct (yes/no): ")

        if choice_check == 'yes':
            write_into_csv(student_info_list)

            condition_check = input("Enter (yes/no) if you want to enter the information for another student: ")

            if condition_check == "yes" or condition_check == "YES":
                condition = True
                student_number += 1
            elif condition_check == "no" or condition_check == "NO":
                condition=False
        elif choice_check == 'no':
            print("Please Re-enter the value: ")
