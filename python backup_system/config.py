import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STORAGE_ROOT = os.path.join(BASE_DIR, "backup_storage")
ENCRYPTED_DIR = os.path.join(STORAGE_ROOT, "encrypted")
METADATA_DIR = os.path.join(STORAGE_ROOT, "metadata")
SALT = b'my_fixed_salt_1234'