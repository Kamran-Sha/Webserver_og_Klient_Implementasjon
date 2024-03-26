# Velkommen til Prosjektet Mitt for DATA2410!

Hei der! 👋 Dette prosjektet har vært en del av den spennende reisen gjennom faget DATA2410 Nettverk og skytjenester. Her har jeg tatt på meg utfordringen med å kode en enkel webserver, en smart liten webklient, og til slutt, en flertrådet webserver som kan håndtere flere forespørsler samtidig. Alt dette ved bruk av Python.

## Kom i Gang

For å dykke rett inn i dette prosjektet, trenger du Python 3. Det er alt! Ingen fancy eksterne biblioteker eller lang oppsettsprosess her, bare god gammeldags programmeringsglede.

## Hvordan Få Ting til å Rulle

### For den Enkle Webserveren (Oppgave 1)

1. Åpne terminalen din og sørg for at du er i samme mappe som `server.py`.
2. Kjør `python3 server.py` for å vekke webserveren til live.
3. Pop åpen en nettleser og besøk `http://localhost:8000/filnavn.html` for å be serveren pent om en fil.

### For Webklienten (Oppgave 2)

1. I en ny terminalvindu, naviger til mappen med `client.py`.
2. Skriv inn `python3 client.py -i 127.0.0.1 -p 8000 -f filnavn.html` for å sende en forespørsel til serveren.
3. Ta en titt i terminalen for å se hva serveren svarer.

### For den Flertrådete Webserveren (Oppgave 3)

1. Følg de samme trinnene som for den enkle serveren, men bruk `multi_threaded_server.py` denne gangen.
2. Nå kan serveren din håndtere flere besøkende på en gang, uten å svette.

## Ting å Huske På

- Husk å matche portnummer og IP-adresse når du kobler til med klienten.
- Dersom serveren nekter å starte, kan det hende at porten allerede er opptatt.
- Får du en "404 Not Found"-melding? Dobbeltsjekk at filen faktisk er der du tror den er.

---

Håper dette gir et godt overblikk og setter deg i stand til å leke med prosjektet mitt. Lykke til, og takk for at du tok tiden til å utforske det jeg har bygget! 🚀