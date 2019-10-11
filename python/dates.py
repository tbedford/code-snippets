students = [ {'name': 'fred', 'age': 29}, {'name': 'jim', 'age': 34}, {'name': 'alice', 'age': 12} ]

students = sorted(students, key=lambda x: x['age'])
#print(students)


students = [ {'name': 'fred', 'dob': '1961-08-12'}, {'name': 'jim', 'dob': '1972-01-12'}, {'name': 'alice', 'dob': '1949-01-01'}, {'name': 'bob', 'dob': '1931-12-25'} ]

students = sorted(students, key=lambda x: x['dob'])
print(students)

