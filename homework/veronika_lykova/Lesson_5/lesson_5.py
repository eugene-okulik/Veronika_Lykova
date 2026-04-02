# Task 1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print (name, last_name, city, phone, country)

# Task 2
string1 = 'результат операции: 42'
find_number_position1 = string1.index(':') + 2
number1 = int(string1[find_number_position1:]) + 10
print(number1)

string2 = 'результат операции: 514'
find_number_position2 = string2.index(':') + 2
number2 = int(string2[find_number_position2:]) + 10
print(number2)


string3 = 'результат работы программы: 9'
find_number_position3 = string3.index(':') + 2
number3 = int(string3[find_number_position3:]) + 10
print(number3)

#Task 3
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
print(', '.join(students) + 'study these subjects: ' + ', '.join(subjects))
