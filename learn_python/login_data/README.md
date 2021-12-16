# login_data
I did the first model to test the cryptographic module, than I made the second script (attempt) that worked with the flaws.
The third script I created can locally store a key, an encrypt username, and an encrypt password and use the key to decrypt it.
Once you login and change your username and password, script wil close it-self.
So you need to re-open it and than changes are made.

But first you need activate key_generator.py to generate file "key.key" and "login_data.txt". "key.key" hold generated key for crypting and decrypting. "login_data.txt" holds crypted username and password.

By default: 
  username: username
and
  password: password
