# Ransomware

This is not actual ransomware, however -- it will irreversibly encrypt all the files on your computer if you are not careful.

## Required Packages
```
pip install pycryptodome
```

### Steps
- create the keys
```
python3 create_keys.py
```
- this should write 2 files to the `keys` directory in this project. `private.pem` and `public.pem` -- dont mess with these once created. 
- 

### Resources
- https://pycryptodome.readthedocs.io/en/latest/src/examples.html