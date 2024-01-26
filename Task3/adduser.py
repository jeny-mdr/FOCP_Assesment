from module_import import read_file,encode_password
from getpass import getpass

PASSWORD_FILE = "passwd.txt"
# Function to add new user
def adduser():
    """
    Function to add a new user to the system.
    
    Returns:
    str: A message indicating the success or failure of user creation.
    """

    while True:
        user_name = input("Enter new username: ")            #Get the required information to add new user
        existing_users = [user[0] for user in read_file()]
        if user_name.lower() in existing_users:
            print("Cannot add. Most likely username already exists.")
        else:
            real_name = input("Enter real name: ")
            password = getpass("Enter password: ")           # Encrypt the password 
            encrypted_password = encode_password(password)   
            with open(PASSWORD_FILE, "w") as file:           # Append user information to the PASSWORD_FILE
                file.write(f"{user_name}:{real_name}:{encrypted_password}\n")

            return (f"User Created.\n{user_name}:{real_name}:{encrypted_password}\n")
            break  
      
           
if __name__ == "__main__":
    #Call the function to add new user
    print(adduser())
   
   
