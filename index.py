# name = "Sardor"
# age = 25 

# def greet():
#     print(f"Hello, my name is {name} and I am {age} years old.")

# greet()


# print("Hello World")

name = "Sardor"
age = 16
skills = ["Python", "JS", "React", "TS", "GO", "Frontend", "Mobile Development"]

user = {
    "name" : name,
    "age": age,
    "is_backend": False,
    "skills" : skills
}

# print(user)

users = [
    {"name": "Sardor", "age": 16, "skills": ["Go", "TS", "Python"]},
    {"name": "Alice", "age": 20, "skills": ["CSS", "HTML"]},
    {"name": "Bob", "age": 18, "skills": ["PHP", "JS"]},
]

def check_access(user):    
    if user["age"] < 18: 
        message = "Доступ запрещен"
    else: 
        message = "Добро пожаловать"
    if "Python" in user["skills"]: 
        message += " Можно изучать Django"
    
    return {
        "name": user["name"],
        "access": message
    }
# for u in users:        
#     result = check_access(u)
    # print(result)
        
def get_users_with_access(users):
    results = []
    for u in users: 
        result = check_access(u)
        results.append(result)
        
    return results
    
access_users = get_users_with_access(users)

def users_api():
    users_json = get_users_with_access(users)
    
    return {
        "status": "success",
        "count": len(users_json),
        "data": users_json
    }

print(users_api(users))    