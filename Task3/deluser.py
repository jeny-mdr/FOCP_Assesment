from module_import import read_file, encode_password
from getpass import getpass

def deluser():
    """
    Delete a user based on the provided username.

    Returns:
    str: A message indicating whether the user was deleted or not found.
    """

    #Get the username to delete a particular user
    username=input("Enter username:").lower()
    password=getpass("Enter password:")
    
    #Open the file in write mode to rewrite the contents excluding the line to be deleted
    elements = read_file()
    for element in elements:
        if element[0] == username.lower() and element[2] == encode_password(password):
            with open("passwd.txt", "w") as file:
                user_deleted = False
                for element in elements:
                    if element[0] != username:
                        # Write lines other than the one to be deleted back to the file
                        file.write(elements)
                    else:
                         #Mark that the user has been deleted
                         user_deleted = True
      
            return "User Deleted." if user_deleted else "User not found. Nothing changed."
        else:
            return "Incorrect  Username or Password."


if __name__ == "__main__":
    # Call the deluser function and print the result
    print(deluser())
