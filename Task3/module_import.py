import codecs

# Funtion to encode password
def encode_password(password):
    """
    Encode a password using the ROT13 algorithm.

    Parameters:
    - password (str): The password to be encoded.

    Returns:
    str: The encoded password.
    """
    
    return codecs.encode(password, 'rot_13')


#Function to read file
def read_file():
   """
   Reads a password file and returns a list of user credentials.

   Returns:
   list:List with sub lists that consist of user credentials. 
   """

   with open("passwd.txt", "r") as file:
       return [line.strip().split(':') for line in file]