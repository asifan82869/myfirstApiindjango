import requests
'''
def get_token():
    url = "http://127.0.0.1:8000/api/auth/"
    response = requests.post(url, data = {'username': 'asif', 'password': 'asif1234'})
    return response.json()
'''
def get_data():
    #token = get_token()
    url = "http://127.0.0.1:8000/api/user_list/"
    #header = {'Authorization': 'Token {}'.format(token) }
    response = requests.get(url)
    data = response.json()
    print(type(data))
    for x in data:
        print(x)
'''
def check_id(id):
    token = get_token()
    already = 0
    url = "http://127.0.0.1:8000/api/user_list/"
    header = {'Authorization': 'Token {}'.format(token) }
    response = requests.get(url, headers=header)
    data = response.json()
    for x in data:
        for y in x.values():
            if(y == id):
                already = 1
                break
    return already

def create_user(id,name,age,rank):
    token = get_token()
    url = "http://127.0.0.1:8000/api/user_list/"
    header = {'Authorization': 'Token {}'.format(token) }
    already = check_id(id)
    if(already == 0):
        data = {
        "employee_id": id,
        "name": name,
        "age": age,
        "ranking": rank
        }
        response = requests.post(url, data=data, headers=header)
        get_data()
    else:
        print('Employee id alredy exits.')


def edit_user(id):
    token = get_token()
    url = "http://127.0.0.1:8000/api/user_list/{}/".format(id)
    header = {'Authorization': 'Token {}'.format(token)}
    data = {
        "name": "omakr K",
        }
    response = requests.put(url, data=data, headers=header)
    get_data()
        
#id = input("Enter user id: ")
#name = input("Emter user name: ")
#age = int(input("Enter user age: "))
#rank = float(input("Enter user ranks: "))

#edit_user(3)

def delete_user(id):
    token = get_token()
    url = "http://127.0.0.1:8000/api/user_list/{}/".format(id)
    header = {'Authorization': 'Token {}'.format(token)}
    response = requests.delete(url, headers=header)
    get_data()

delete_user(6)
'''
