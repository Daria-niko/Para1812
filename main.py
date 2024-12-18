from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)  # Ключ будет выведен в консоль, скопируйте его
