import datetime
now = datetime.datetime.now()
# print(now.year, now. month, now. day) 


# birthday = '12/12/1980'

# print(birthday.split("/"))


def get_students_of_age(student_list, low, high):
    
    result = []

    for student in student_list:
        # student -> (Mary, 12/12/1980)
        # ['mary', '12/12/1980']
        name = student[0]

        birthday = student[1]

        birthdaysplit = birthday.split("/")
        birthyear = birthdaysplit[2] #birthdaysplit[-1]

        age = now.year - int(birthyear)

        if (age>=low) and (age<=high):
            result.append(name)


    return result  



# a = 'Mary'
# b = 'Ben'
# c = 'Charles'

# result = [a,c]
# print(result)

# result[0]= b
# print(result)