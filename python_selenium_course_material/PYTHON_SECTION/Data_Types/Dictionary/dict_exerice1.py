# capitals = {"USA": "Washington", "France": "Paris", "Turkey": "Ankara"}
# print(capitals)
#
# france_capital = capitals["France"]
#
# france_capital2 = capitals.get("France")
#
# print(france_capital)
#
# print(france_capital2)
#
# # get nonexisting key
#
# print(capitals.get("Ethiopia", "NO SUCH KEY IN DICTIONARY"))
#
# print("before add")
# print(capitals)
# capitals["Kenya"] = "Nairobi"
# print("after adding Kenya")
# print(capitals)
#
# capitals.update({"India": "New Delhi"})
# print(capitals)
#
# # Assignment: what if you try to add a key that already exist?
#
# capitals["USA"] = "Nevada"
# # adding an existing key with different value changes the value of the existing key
#
#
# print(capitals)
#
# print(capitals.keys())
# print(capitals.values())

employee = {"name": "John Doe",
            "age": 25,
            "phone": 15101111111,
            "title": "Sr. Software Engineer",
            "skills": ["AWS", "Python", "Java", "Docker"]
            }

e_name = employee["name"]
e_age = employee['age']
e_skills = employee["skills"]
user_skill_count = len(e_skills)


print(f"User has {user_skill_count} skills.")
print("User has {} skills".format(user_skill_count))