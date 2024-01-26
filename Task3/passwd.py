from module_import import encode_password
from getpass import getpass

#Function to change password
def passwd():
    """
    Change the password for a particular user.

    Returns:
    str: A message indicating whether the password was changed or not.
    """

    username = input("User: ")
    current_password = getpass("Current Password: ")
    new_password = getpass("New Password: ")
    confirm_password = getpass("Confirm: ")

    #Read the passwd file
    with open("passwd.txt", "r") as file:
        lines = file.readlines()

    #Open the file in write mode to change the password
    with open("passwd.txt", "w") as file:
        password_changed = False
        for line in lines:
            elements = line.strip().split(":")
            stored_username, stored_password = elements[0], elements[2]

            if stored_username == username and encode_password(current_password) == stored_password:
                new_encryption = encode_password(new_password)
                file.write(f"{username}:{elements[1]}:{new_encryption}\n")
                password_changed = True
            else:
                file.write(line)

        return "Password changed."if password_changed else "User not found or incorrect password. Nothing changed."


if __name__ == "__main__":
    # Call the passwd function and print the result
    print(passwd())