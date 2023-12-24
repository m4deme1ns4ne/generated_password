import string
import secrets
import pyperclip

def generated_password(l: int) -> str:
    '''
    This function create to secure password
    '''
    alphabet_with_nums = string.ascii_letters + string.digits
    while True:
        password = ''.join(secrets.choice(alphabet_with_nums) for _ in range(l))
        if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 3):
            break
    return password

if __name__ == '__main__':

    while True:
        try:
            len_password = int(input('Input len password (no less than 5): '))
            if len_password < 5:
                raise TypeError
            break
        except ValueError:
            print('You can print only numbers', 'Try it again', sep='\n')
        except TypeError:
            print('You can write numbers no larger than 5', 'Try it again', sep='\n')
            
    my_password = generated_password(len_password)
    print(f'Your secure password: {my_password}')
    pyperclip.copy(my_password)