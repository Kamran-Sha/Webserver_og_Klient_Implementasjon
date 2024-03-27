# Prosjekttittel: Webserver og Klient Implementasjon

## Introduksjon

Dette prosjektet er en del av oppgavesettet for DATA2410 Nettverk og skytjenester ved Oslomet. Det inkluderer implementering av en enkel webserver, en webklient, og en flertrådet webserver, alle utviklet i Python.

## Oppstart

Før du dykker inn i å kjøre koden, sørg for at du har Python 3 installert på systemet ditt. Det er alt du trenger for å komme i gang!

## Hvordan kjøre prosjektet

### Enkel Webserver (Oppgave 1)

1. Åpne en terminal.
2. Naviger til mappen som inneholder `server.py`.
3. Kjør kommandoen: `python3 server.py`.
4. Åpne en nettleser og besøk `http://localhost:8000/index.html`.

### Webklient (Oppgave 2)

1. Åpne en annen terminal.
2. Naviger til mappen med `client.py`.
3. Kjør: `python3 client.py -i 127.0.0.1 -p 8000 -f index.html`.

### Flertrådet Webserver (Oppgave 3)

1. Følg trinnene for å kjøre den enkle webserveren, men bruk `multi_threaded_server.py` denne gangen.

## Filbeskrivelser

- `server.py`: Kode for den enkle webserveren.
- `client.py`: Kode for webklienten.
- `multi_threaded_server.py`: Kode for den flertrådete webserveren.

## Viktige Merknader

- Pass på at du bruker riktig portnummer og IP-adresse når du kobler til med klienten.
- Hvis serveren ikke starter, kan det hende at porten allerede er i bruk.

---

Håper du finner dette prosjektet både informativt og spennende.
