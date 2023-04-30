import socket

# definisanje hosta i porta
HOST = 'localhost'
PORT = 12345

# kreiranje socket objekta
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# povezivanje sa serverom
client_socket.connect((HOST, PORT))

# prijem poruke od servera
poruka = client_socket.recv(1024)
print(poruka.decode())

# unos broja od korisnika
broj_korisnika = input()

# slanje broja serveru
client_socket.send(broj_korisnika.encode())

# prijem poruke od servera o ishodu igre
poruka = client_socket.recv(1024)
print(poruka.decode())

# zatvaranje konekcije
client_socket.close()