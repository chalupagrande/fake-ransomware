#!/usr/bin/env python
import os

# define function to decrypt all the files in a folder
def decrypt_files_in_dir_recursively(fernet, dir):
  directories = os.listdir(dir)
  for filename in directories:
    full_path = os.path.join(dir, filename)
    if os.path.isdir(full_path):
      decrypt_files_in_dir_recursively(fernet, full_path)
    else:
      try:
        # opening the original file to decrypt
        file = open(full_path, 'rb')
        original = file.read()

        # decrypting the file
        decrypted = fernet.decrypt(original)

        decrypted_file = open(full_path, 'wb')
        decrypted_file.write(decrypted)
        decrypted_file.close()
      except:
        print(filename, "not encrypted, skipping...")
