#!/usr/bin/env python3
import os
import config
from src.menu import main_menu

def initialize_folders():
    os.makedirs(config.STORAGE_ROOT, exist_ok=True)
    os.makedirs(config.ENCRYPTED_DIR, exist_ok=True)
    os.makedirs(config.METADATA_DIR, exist_ok=True)
    print("✅ System Ready! Folders auto-created at:", config.STORAGE_ROOT)

if __name__ == "__main__":
    initialize_folders()
    main_menu()