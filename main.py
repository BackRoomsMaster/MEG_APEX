import time
import os
import sys
import subprocess

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def effetto_digitazione(testo, velocita=0.03):
    for char in testo:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(velocita)
    print()

def menu_principale():
    while True:
        clear_screen()
        effetto_digitazione("=== TERMINALE MEG_APEX ===")
        effetto_digitazione("1. Accedi al Server MEG_APEX")
        effetto_digitazione("2. Esci")
        scelta = input("Inserisci la tua scelta: ")

        if scelta == "1":
            accedi_server()
        elif scelta == "2":
            effetto_digitazione("Uscita dal Terminale MEG_APEX...")
            break
        else:
            effetto_digitazione("Scelta non valida. Riprova.")
            time.sleep(1)

def accedi_server():
    clear_screen()
    effetto_digitazione("Iniziando procedura di accesso al server MEG_APEX...", 0.05)
    effetto_digitazione("ATTENZIONE: Accesso non autorizzato è punibile secondo il Protocollo Omega", 0.05)
    time.sleep(1)
    
    # Avvia OneApex.py
    try:
        subprocess.run(["python", "OneApex.py"], check=True)
    except subprocess.CalledProcessError:
        effetto_digitazione("Errore nell'avvio del server MEG_APEX. Contattare l'amministratore.")
    except FileNotFoundError:
        effetto_digitazione("File OneApex.py non trovato. Assicurarsi che sia nella stessa directory.")
    
    input("Premi Invio per tornare al menu principale...")

if __name__ == "__main__":
    clear_screen()
    effetto_digitazione("Inizializzazione del Terminale MEG_APEX...", 0.05)
    time.sleep(1)
    menu_principale()
