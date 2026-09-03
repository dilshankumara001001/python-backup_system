import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import config

def derive_key(password: str) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=config.SALT,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

def encrypt_file(file_path: str, key: bytes) -> str:
    fernet = Fernet(key)
    with open(file_path, 'rb') as f:
        data = f.read()
    encrypted_data = fernet.encrypt(data)
    base_name = os.path.basename(file_path)
    enc_name = base_name + ".enc"
    enc_path = os.path.join(config.ENCRYPTED_DIR, enc_name)
    counter = 1
    while os.path.exists(enc_path):
        name, ext = os.path.splitext(base_name)
        enc_name = f"{name}_{counter}.enc"
        enc_path = os.path.join(config.ENCRYPTED_DIR, enc_name)
        counter += 1
    with open(enc_path, 'wb') as f:
        f.write(encrypted_data)
    info_file = os.path.join(config.METADATA_DIR, enc_name + ".info")
    with open(info_file, 'w') as f:
        f.write(file_path)
    return enc_path

def decrypt_file(enc_path: str, key: bytes) -> str:
    fernet = Fernet(key)
    with open(enc_path, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    base_name = os.path.basename(enc_path)
    info_file = os.path.join(config.METADATA_DIR, base_name + ".info")
    original_path = None
    if os.path.exists(info_file):
        with open(info_file, 'r') as f:
            original_path = f.read().strip()
    if original_path and os.path.isdir(os.path.dirname(original_path)):
        output_path = original_path
    else:
        output_path = os.path.join(os.getcwd(), base_name.replace(".enc", ""))
    out_dir = os.path.dirname(output_path)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)
    with open(output_path, 'wb') as f:
        f.write(decrypted_data)
    return output_path