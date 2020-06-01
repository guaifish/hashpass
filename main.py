import base64
import hashlib


def generate_password(raw_password, salt, length=16):
    raw_password += salt
    raw_password = raw_password.encode('utf8')
    s = hashlib.sha256(raw_password).digest()
    full_password = base64.b64encode(s)
    return full_password.decode('utf8')[:length]