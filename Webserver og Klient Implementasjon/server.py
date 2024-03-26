# Importerer socket-modulen for nettverkskommunikasjon og sys for å avslutte programmet
from socket import *
import sys

# Setter opp en server socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Konfigurerer og starter server socket
"""
Beskrivelse:
Denne seksjonen av koden initialiserer serveren, binder den til en gitt port, og setter den til å lytte etter innkommende forbindelser.

Argumenter:
- AF_INET: Angir at nettverket bruker IPv4.
- SOCK_STREAM: Angir at socket er av typen TCP, som er forbindelsesorientert.

Variabler:
- serverPort (int): Portnummeret som serveren vil lytte på.
- serverSocket (socket): Socketobjektet som representerer serveren.

Unntakshåndtering:
Ingen spesifikk unntakshåndtering i denne seksjonen.
"""
serverPort = 8000
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive on port', serverPort)

while True:
    # Venter på og aksepterer en ny forbindelse
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    """
    Beskrivelse:
    I denne delen av koden aksepteres en innkommende forbindelse. For hver ny forbindelse, forsøker serveren å lese en HTTP-forespørsel, behandle forespørselen ved å finne den ønskede filen, og sende tilbake filens innhold eller en 404-feilmelding hvis filen ikke finnes.

    Argumenter:
    - connectionSocket (socket): En ny socket som er opprettet for hver klientforbindelse.
    - addr (tuple): Inneholder IP-adressen og portnummeret til klienten.

    Returnerer:
    Ingen returverdi, men sender data tilbake til klienten over nettverket.

    Unntakshåndtering:
    - IOError: Håndterer situasjoner der filen som forespørres ikke eksisterer. Serveren sender en "404 Not Found" respons tilbake til klienten.
    """
    try:
        message = connectionSocket.recv(1024).decode()
        if not message:
            continue
        filename = message.split()[1]
        with open(filename[1:], 'r') as file:
            outputdata = file.read()
            # Sender HTTP-respons header fulgt av filinnholdet
            connectionSocket.send("HTTP/1.1 200 OK\n\n".encode() + outputdata.encode())
    except IOError:
        # Sender en "404 Not Found" respons hvis filen ikke finnes
        connectionSocket.send("HTTP/1.1 404 Not Found\n\nFile not found".encode())
    finally:
        # Lukker klientforbindelsen
        connectionSocket.close()

# Lukker serverens hovedsocket og avslutter programmet
serverSocket.close()
sys.exit()
