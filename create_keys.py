from Crypto.PublicKey import RSA


def export_private_key(key, filename, passphrase):
    with open(filename, "wb") as file:
        file.write(key.exportKey("PEM", passphrase))
        file.close()


def export_public_key(key, filename):
    with open(filename, "wb") as file:
        file.write(key.publickey().exportKey("PEM"))
        file.close()


def import_private_key(filename, passphrase):
    with open(filename, "rb") as file:
        private_key = RSA.importKey(file.read(), passphrase)

    return private_key


def import_public_key(filename):
    with open(filename, "rb") as file:
        public_key = RSA.importKey(file.read())

    return public_key


key = RSA.generate(2048)

export_private_key(key, "./keys/private.pem", "password")
export_public_key(key, "./keys/public.pem")
