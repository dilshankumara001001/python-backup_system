import sys
from src.file_ops import backup_file, list_backups, restore_file

def main_menu():
    while True:
        print("\n" + "=" * 50)
        print("🔐 SECURE FILE BACKUP SYSTEM")
        print("=" * 50)
        print("1. Backup a File")
        print("2. List Backups")
        print("3. Restore a File")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()
        if choice == "1":
            backup_file()
        elif choice == "2":
            list_backups()
        elif choice == "3":
            restore_file()
        elif choice == "4":
            print("👋 Goodbye!")
            sys.exit(0)
        else:
            print("❌ Invalid choice. Please enter 1-4.")