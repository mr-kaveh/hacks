#!/usr/bin/env python3.6
'''
    Passing Dictionaries to function
    and iterating through their items
'''
def print_users_info(**meta):
    for key, value in meta.items():
        print(key, ' is ', value)
    print('---------------------------')


if __name__ == '__main__':
    dict = {}
    dict = [{
        "firstname": "Hossein",
        "lastname": "Davoodi",
        "job": "DevOps Engineer",
        "age": "30"
    },
        {
            "firstname": "Ali",
            "lastname": "Davoodi",
            "job": "Auditor",
            "age": "27"
        }]

    for i in range(len(dict)):
        print_users_info(**dict[i])
