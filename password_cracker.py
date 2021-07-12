import hashlib

top_10000_passwords = []


def crack_sha1_hash(hash,use_salts=False):
#Here we pass all the values from 'top-10000-passwords' and store it in the empty list top_10000_passwords
    with open('top-10000-passwords.txt','r') as passwords_file:
      Lines = passwords_file.readlines()
      for line in Lines:
        top_10000_passwords.append(line.strip())

  
    hashed_passwords = {}

  #Now we has each passowrd and store it in the empty dictionary 'hashed_passwords' with the hashed password as key and the original password as value 

    for password in top_10000_passwords:
      encoded_password = password.encode()

      if not use_salts:
        hashed_password = hashlib.sha1(encoded_password).hexdigest()
        hashed_passwords[hashed_password] = password
        continue

  #If use_salts is true, then read each salt from 'known-salts.txt'
      with open('known-salts.txt','r') as salts_file:
        Lines = salts_file.readlines()

        for line in Lines:
          salt = line.strip()
          encoded_salt = salt.encode()
  #Here we prepend and append salts to passowrds accordingly 
          encoded_passwords_with_salts = [
            encoded_salt + encoded_password, encoded_password + encoded_salt
        ]
  #Now we hash the prefixed/suffiexd passwords and add the hashed results to the dictionary 
          for p in encoded_passwords_with_salts:
            hashed_password = hashlib.sha1(p).hexdigest()
            hashed_passwords[hashed_password] = password

  #Now we return the original password if the hash is found in the the hashed_passwords dictionary

    if hash in hashed_passwords:
      return hashed_passwords[hash]

    return 'PASSWORD NOT IN DATABASE'
