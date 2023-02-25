# Generates passwrod
def generate_password(size=12):
    from random import randint

    password = ''
    for c in range(size):
        password += chr(randint(32, 125))
    print(password)


while True:
    action = int(input("""What you want to do?
    1 - Generate a password
    2 - Validate a password
    3 - Quit program
    
    Your answer: """))

    if action == 1:
        generate_password()
    elif action == 2:
        print('=-' * 20)
        print(f"{'Working in progress':^40}")
        print('=-' * 20)
    else:
        break`
