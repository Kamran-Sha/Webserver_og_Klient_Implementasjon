# client.py
import socket
import argparse

def create_client(server_ip, server_port, filename):
    """
    Oppretter en klient som kobler til en server, sender en HTTP GET-forespørsel,
    og skriver ut serverens respons.

    Arguments:
    - server_ip (str): IP-adressen til serveren som klienten skal koble til.
    - server_port (int): Portnummeret serveren lytter på.
    - filename (str): Navnet på filen som skal forespørres fra serveren.

    Returns:
    - None. Funksjonen skriver serverens respons direkte til konsollen.

    Exceptions:
    - socket.error: Håndterer eventuelle nettverksrelaterte feil som kan oppstå under tilkobling,
      sending, eller mottak av data.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            # Koble til serveren
            client_socket.connect((server_ip, server_port))
            
            # Formuler HTTP GET-forespørselen
            http_request = f"GET /{filename} HTTP/1.1\r\nHost: {server_ip}\r\n\r\n"
            client_socket.sendall(http_request.encode())
    
            # Motta og skriv ut svaret fra serveren
            response = client_socket.recv(4096).decode()
            print("Serverens respons:\n", response)
    except socket.error as e:
        print(f"Nettverksfeil: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="En enkel HTTP-klient.")
    parser.add_argument("-i", "--server_ip", type=str, required=True, help="Serverens IP-adresse.")
    parser.add_argument("-p", "--server_port", type=int, required=True, help="Porten serveren lytter på.")
    parser.add_argument("-f", "--filename", type=str, required=True, help="Filnavnet for HTTP GET-forespørselen.")
    
    args = parser.parse_args()
    
    create_client(args.server_ip, args.server_port, args.filename)
