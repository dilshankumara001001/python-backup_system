import os
import getpass
from src.crypto_utils import derive_key, encrypt_file, decrypt_file
import config

def backup_file():
    file_path = input("Enter the full path of the file to backup: ").strip()
    if not os.path.exists(file_path):
        print("❌ File not found.")
        return
    password = getpass.getpass("Enter encryption password: ")
    key = derive_key(password)
    try:
        enc_path = encrypt_file(file_path, key)
        print(f"✅ Backup successful! Encrypted file saved at: {enc_path}")
    except Exception as e:
        print(f"❌ Backup failed: {e}")

def list_backups():
    enc_files = [f for f in os.listdir(config.ENCRYPTED_DIR) if f.endswith(".enc")]
    if not enc_files:
        print("📭 No backups found.")
        return
    print("\n📂 Available backups:")
    for i, f in enumerate(enc_files, 1):
        info_path = os.path.join(config.METADATA_DIR, f + ".info")
        orig = "Unknown"
        if os.path.exists(info_path):
            with open(info_path, 'r') as inf:
                orig = inf.read().strip()
        print(f"  {i}. {f}  (Original: {orig})")
    print()

def restore_file():
    enc_files = [f for f in os.listdir(config.ENCRYPTED_DIR) if f.endswith(".enc")]
    if not enc_files:
        print("📭 No backups to restore.")
        return
    print("\n📂 Select a backup to restore:")
    for i, f in enumerate(enc_files, 1):
        print(f"  {i}. {f}")
    choice = input("Enter number (or 0 to cancel): ").strip()
    if not choice.isdigit():
        print("❌ Invalid input.")
        return
    idx = int(choice)
    if idx == 0:
        return
    if idx < 1 or idx > len(enc_files):
        print("❌ Invalid selection.")
        return
    enc_file = enc_files[idx - 1]
    enc_path = os.path.join(config.ENCRYPTED_DIR, enc_file)
    password = getpass.getpass("Enter decryption password: ")
    key = derive_key(password)
    try:
        restored_path = decrypt_file(enc_path, key)
        print(f"✅ Restore successful! File restored to: {restored_path}")
    except Exception as e:
        print(f"❌ Restore failed: {e}")