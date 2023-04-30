import socket
import random

# definisanje hosta i porta
HOST = 'localhost'
PORT = 12345

# kreiranje socket objekta
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# vezivanje socket objekta za HOST i PORT
server_socket.bind((HOST, PORT))

# postavljanje maksimalnog broja klijenata za povezivanje
server_socket.listen(1)

# generisanje slučajnog broja od 1 do 10
broj = random.randint(1, 10)

# prihvatanje povezivanja od klijenta
conn, addr = server_socket.accept()

# slanje poruke klijentu da unese broj
conn.send(b"Unesite broj od 1 do 10: ")

# prijem broja od klijenta
data = conn.recv(1024)
broj_klijenta = int(data.decode())

# provera da li je klijent pogodio broj
if broj_klijenta == broj:
    poruka = "Pogodili ste broj!"
else:
    poruka = "Niste pogodili broj. Traženi broj je bio: " + str(broj)

# slanje poruke klijentu o ishodu igre
conn.send(poruka.encode())

# zatvaranje konekcije
conn.close()