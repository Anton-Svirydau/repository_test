# tuple

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

user_roles = ("admin", "editor", "viewer")
# role_1, role_2, role_3 = user_roles
role_1, role_2, _ = user_roles

print(role_1)
print(role_2)
# print(role_3)
