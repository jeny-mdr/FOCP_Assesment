from module_import import encode_password, read_file
from getpass import getpass
PASSWORD_FILE = "passwd.txt"

#Function for the existing users to log into the system
def login():
    """
    Provides the access to the system after authentication.

    Returns:
    str: A message indicating whether access is granted or denied.
    """
    #Get the required input to verify the credentials
    username = input("User: ")
    password = getpass("Password: ")
    elements = read_file()
    for element in elements:
        if element[0] == username.lower() and element[2] == encode_password(password):
            return "Access granted."
            
    return "Access denied."


if __name__ == "__main__":
    # Call the login function and print the result
    print(login())