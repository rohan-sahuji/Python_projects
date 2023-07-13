# SLicing the Email address of user

def main():
    Email = input('Enter the Email address to be sliced: ')
    (username, domain) = Email.split('@')
    (domain, extension) = domain.split('.')
    print('Username: ', username, '\nDomain: ', domain, '\nExtension: ',extension)

while True:
    main()