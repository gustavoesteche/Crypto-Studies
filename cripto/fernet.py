# Common criptography used in python language 

from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)
f = Fernet(key)

message = "oi gatinha vamos sair"
e_message = f.encrypt(message.encode('utf-8'))

print("mensagem encriptada " + e_message.decode('utf-8'))

print(len(e_message.decode('utf-8'))) # padding de ate 100 char 

d_message = f.decrypt(e_message)
print("mensagem decriptada " + d_message.decode('utf-8') )

# how does fernet works ? 
# 