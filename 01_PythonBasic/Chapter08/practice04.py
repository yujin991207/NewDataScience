#4
import sys

usernames = sys.argv[1:]

def greet_users(usernames):
    for name in usernames:
        print(f'Hello! {name[0].upper()}{name[1:]}')

        #print(f'Hello, {usernames[0].upper()}! ')

greet_users(usernames)




