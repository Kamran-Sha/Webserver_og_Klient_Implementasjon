import threading
import socket
import sys

def handle_client(connectionSocket, addr):
    """
    Håndterer en enkelt klientforbindelse i en separat tråd.

    Description:
    Denne funksjonen leser HTTP-forespørselen fra klienten, forsøker å åpne den forespurte filen,
    sender filens innhold som respons hvis filen eksisterer, eller sender en "404 Not Found" respons
    hvis filen ikke finnes.

    Arguments:
    - connectionSocket: Socketobjektet for klientforbindelsen.
    - addr: Adresseinformasjon for klientforbindelsen.

    Returns:
    None

    Exceptions:
    - IOError: Hvis den forespurte filen ikke finnes, sendes en "404 Not Found" respons til klienten.
    """
    try:
        message = connectionSocket.recv(1024).decode()
        if not message:
            return
        filename = message.split()[1]
        with open(filename[1:], 'rb') as file:
            outputdata = file.read()
            connectionSocket.send(b"HTTP/1.1 200 OK\r\n\r\n" + outputdata)
    except IOError:
        connectionSocket.send(b"HTTP/1.1 404 Not Found\r\n\r\n")
    finally:
        connectionSocket.close()

def start_server(port):
    """
    Starter en flertrådet server som lytter på den angitte porten og håndterer hver innkommende
    forbindelse i en egen tråd.

    Description:
    Denne funksjonen oppretter en server socket, binder den til en angitt port, og lytter etter
    innkommende forbindelser. For hver forbindelse opprettes en ny tråd som håndterer kommunikasjonen
    med den tilkoblede klienten.

    Arguments:
    - port (int): Portnummeret serveren vil lytte på.

    Returns:
    None

    Exceptions:
    - Exception: Generell unntakshåndtering for nettverksfeil og filoperasjoner.
    """
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        serverSocket.bind(('', port))
        serverSocket.listen(5)
        print(f"Serveren er klar for forbindelser på port {port}.")

        while True:
            connectionSocket, addr = serverSocket.accept()
            client_thread = threading.Thread(target=handle_client, args=(connectionSocket, addr))
            client_thread.start()
    except Exception as e:
        print(f"Serverfeil: {e}")
    finally:
        serverSocket.close()

if __name__ == "__main__":
    PORT = 8000
    start_server(PORT)
