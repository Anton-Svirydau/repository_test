# tuple, dict, args, **kwargs, json
import json
""""""

'''
user_roles = ("admin", "editor", "viewer")
print(user_roles, len(user_roles))
print("admin" in user_roles)
print("writer" in user_roles)
print(user_roles[1])

for role in user_roles:
    print(role)


# not_tuple = ("admin")
# print(type(not_tuple))

my_tuple = ("admin",)
print(type(my_tuple))
'''

'''
user_roles = ("admin", "editor", "viewer")
# role_1, role_2, role_3 = user_roles
role_1, role_2, _ = user_roles

print(role_1)
print(role_2)
# print(role_3)
'''

'''
person = {}

person["name"] = "John"
person["age"] = "30"
person["city"] = "New York"

print(person)
'''
"""
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# print(person)
# person["job"] = "Engineer"
# print(person)
# print(person["name"])

# print(person.get("name"))
# print(person.get("name", "Jack"))
# print(person.get("country"))
# print(person.get("country", "USA"))
'''
for item in person.items():
    key, value = item
    print(item)
    print(key)
    print(value)
    print(type(item))

for key, value in person.items():
    print(key)
    print(value)
'''

for key in person.keys():
    print(key)

for value in person.values():
    print(value)
"""

'''
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
other_person = {
    "city": "New York",
    "age": 30,
    "name": "John"
}
other_other_person = {
    "city": "New York",
    "age": 30,
    "name": "John",
    "country": "Canada"
}

print(person == other_person)
print(person == other_other_person)
'''

'''
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
additional_person_info = {
    "job": "Engineer",
    "married": True,
    "city": "London"
}

# person.update(additional_person_info)
person = person | additional_person_info

print(person)
'''

'''
"""
average_marks = []
best_students = []

for student in students:
    average_mark = 0
    if student["grades"] is None:
        average_marks.append(average_mark)
    else:
        average_mark = 0
        for i in student["grades"]:
            average_mark += i
        average_mark = average_mark / len(student["grades"])
        average_marks.append(average_mark)

max_mark = max(average_marks)

for a in range(len(average_marks)):
    if average_marks[a] == max_mark:
        best_students.append(students[a])

print(best_students)
"""

students_1 = [
    {"name": "John", "surname": "Doe", "grades": [5, 5, 4, 4]},
    {"name": "Jane", "surname": "Doe", "grades": [4, 3, 4, 3, 5]},
    {"name": "Bill", "surname": "Gates", "grades": [5, 5, 5, 3]},
    {"name": "Steve", "surname": "Jobs", "grades": [3, 5, 4, 3, 3, 5]},
    {"name": "Guido", "surname": "Van Rossum", "grades": [5, 3, 5, 4, 5, 5, 3, 5]},
    {"name": "Elon", "surname": "Musk", "grades": None}
]


def get_best_students(*, students: list[dict]) -> list[dict]:
    best_students = []
    best_average_grade = 0
    for student in students:
        grades = student["grades"]
        if grades is None:
            average_grade = 0
        else:
            average_grade = sum(grades) / len(grades)
        if average_grade > best_average_grade:
            best_average_grade = average_grade
            best_students = [student]
        elif average_grade == best_average_grade:
            best_students.append(student)
    return best_students


print(get_best_students(students=students_1))
'''

'''
def add_all(*args):
    print(args)
    print(type(args))


add_all(1, 2, 3)


def add_all_1(*args):
    summary = 0
    for num in args:
        summary += num
    return summary


print(add_all_1(1, 2, 3, 4, 5))

values = [1, 2, 3, 4, 5]
other_values = [6, 7, 8, 9, 10]

print(add_all_1(*values, *other_values))
'''

'''
def introduce(**kwargs):
    print(kwargs)
    print(type(kwargs))


introduce(name="John", age=30, city="New York")


def introduce_1(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)


introduce_1(name="John", age=30, city="New York")

person = {
    "city": "New York",
    "age": 30,
    "name": "John"
}

introduce_1(**person)
'''

'''
def func_with_all_arguments(x: int, y: int, *args, value: int = 6, **kwargs):
    print(x, y)
    print(args)
    print(value)
    print(kwargs)


person = {
    "city": "New York",
    "age": 30,
    "name": "John"
}

func_with_all_arguments(1, 2, 3, 4, 5, **person)
'''

'''
def modify_dict(old_dict: dict, **kwargs) -> tuple[dict, bool]:
    is_modified = False

    for key, value in kwargs.items():
        if old_dict.get(key) != value:
            old_dict[key] = value
            is_modified = True

    return old_dict, is_modified


product = {"id": 1, "name": "Laptop", "price": 999.99}

structure_0 = modify_dict(old_dict=product, name="Laptop")

print(structure_0)
print(type(structure_0))

prod, was_modify = modify_dict(old_dict=product, in_stock=True)

print(prod)
print(was_modify)
'''

'''
book = {
    "title": "1984",
    "author": "George Orwell",
    "isbn": "978-0451524935",
    "uuid": "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11",
    "count": 30,
    "genres": ["dystopia"]
}

json_string = json.dumps(book)

print(type(json_string))
print(json_string)

# read_book = json.loads(json_string)
'''
