#!/usr/bin/env python

import os
from cryptography.fernet import Fernet
import sys, getopt

target_directory = "the/directory/you/want/to/encrypt"
keys_directory = "the/directory/where/you/want/to/store/keys"
key_path = os.path.join(keys_directory, "private.key")
extensions_to_encrypt = [".txt", ".doc", ".jpg", ".jpeg", ".png"]


# generates the fernet key and saves it to filename
def generate_and_save_fernet_key(filename):
    with open(filename, "wb") as file:
        key = Fernet.generate_key()
        file.write(key)
        file.close()


# imports the fernet key from filename
def import_fernet_key(filename):
    with open(filename, "rb") as file:
        private_key = open(key_path, "rb")

    return private_key


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
                file = open(full_path, "rb")
                original = file.read()

                # decrypting the file
                decrypted = fernet.decrypt(original)

                decrypted_file = open(full_path, "wb")
                decrypted_file.write(decrypted)
                decrypted_file.close()
            except:
                print(filename, "not encrypted, skipping...")


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
                file = open(full_path, "rb")
                original = file.read()
                # encrypting the file
                encrypted = fernet.encrypt(original)
                # opening the file in write mode and
                # writing the encrypted data
                encrypted_file = open(full_path, "wb")
                encrypted_file.write(encrypted)
                encrypted_file.close()


def main(argv):
    try:
        opts, args = getopt.getopt(
            argv,
            "hdeg",
        )

        for opt, arg in opts:
            if opt in ["-d"]:
                print("Decrypting...")
                fernet_key = import_fernet_key(key_path).read()
                fernet = Fernet(fernet_key)
                decrypt_files_in_dir_recursively(fernet, target_directory)
            elif opt in ["-g"]:
                print("Generating key...")
                generate_and_save_fernet_key(key_path)
            elif opt in ["-e"]:
                print("Encrypting...")
                # encrypt the files
                fernet_key = import_fernet_key(key_path).read()
                fernet = Fernet(fernet_key)
                encrypt_files_in_dir_recursively(
                    fernet, target_directory, extensions_to_encrypt
                )
            elif opt in ["-h"]:
                print(
                    "Usage \n\t -d\t:Decrypt \n\t -e\t:Encrypt \n\t -g\t:Generate key"
                )
    except getopt.GetoptError as error:
        print("Error: ", error)
        print("Usage \n\t -d\t:Decrypt \n\t -e\t:Encrypt \n\t -g\t:Generate key")
        sys.exit(2)


# RUN MAIN FUNCTION
if __name__ == "__main__":
    main(sys.argv[1:])
