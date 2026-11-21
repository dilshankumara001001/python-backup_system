  # 🔐 Secure File Backup System

A secure, modular file backup tool that encrypts your sensitive data using AES-256 encryption. Built with Python, this CLI application allows you to safely store and restore files with password protection.

## ✨ Key Features
- **Strong Encryption**: Uses Fernet (AES-256) with PBKDF2 key derivation.
- **Auto Setup**: Automatically creates `backup_storage/` folders on first run.
- **Easy Restore**: Restores files to their exact original location.
- **CLI Interface**: Simple menu-driven operations.
- **Duplicate Protection**: Automatically renames duplicate encrypted files.

## 🛠️ Tech Stack
- Python 3.6+
- cryptography library
- Modular Architecture (src/ folder separation)

## ⚙️ Quick Start
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
