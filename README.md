# Fake-Ransomware

This is not actual ransomware, however -- it will irreversibly encrypt all the files on your computer if you are not careful. I just thought it was funny to call it ransomware. Just some recursive file encryption here. Nothing bad!

## Required Packages
```
cryptography
```

### Steps
- update the file paths in `ransom.py`
  - `target_directory` - is the directory you want to encrypt
  - `keys_directory` - is where you want to save/load the keys that are generated and used to encrypt your files
  - `extensions_to_encrypt` - the file extensions you want to target for encryption
- create the keys using `python ransom.py -g`
  - this should write a file to your "keys" directory called `private.key` -- dont lose this or generate a new one after encrypting your files
- encrypt the files using `pythong ransom.py -e`
- check the files have been encrypted
- decrypt the files using `pythong ransom.py -d`
