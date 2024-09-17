import time
import os
import sys
import random
import subprocess

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def effetto_digitazione(testo, velocita=0.03):
    for char in testo:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(velocita)
    print()

def caricamento_proibito(durata=5):
    fasi = [
        "Inizializzazione protocolli di sicurezza...",
        "Bypassando firewall...",
        "Crittografia quantistica in corso...",
        "Mascheramento tracce digitali...",
        "Accesso ai database riservati...",
        "Decodifica chiavi di accesso...",
        "Elusione sistemi di rilevamento...",
        "Attivazione tunnel criptato...",
        "Sincronizzazione con nodi nascosti...",
        "Verifica autorizzazioni di livello Omega..."
    ]
    
    start = time.time()
    while time.time() - start < durata:
        clear_screen()
        effetto_digitazione("ACCESSO AL SERVER MEG_APEX IN CORSO", 0.05)
        print("\n")
        for _ in range(3):
            fase = random.choice(fasi)
            effetto_digitazione(f"[*] {fase}", 0.02)
        
        progresso = min(100, int((time.time() - start) / durata * 100))
        barra = f"[{'#' * progresso}{' ' * (100 - progresso)}] {progresso}%"
        print("\n" + barra)
        
        time.sleep(0.2)
    
    clear_screen()
    effetto_digitazione("ACCESSO COMPLETATO", 0.1)
    time.sleep(1)

def mostra_file(nome_file, contenuto):
    clear_screen()
    effetto_digitazione(f"=== {nome_file} ===\n")
    effetto_digitazione(contenuto)
    input("\nPremi Invio per tornare all'archivio...")

def archivio():
    files = {
        "Livello_0.txt": "Il Livello 0, noto come 'The Lobby', è il punto di ingresso più comune nelle Backrooms. Caratterizzato da moquette umida, pareti gialle monotone e un ronzio costante di luci fluorescenti.\n\nNota: L'agente Sarah (ID: SARAH_159) ha segnalato anomalie nella struttura temporale di questo livello.",
        "Livello_1.txt": "Il Livello 1, 'Habitat Sicuro', è un vasto magazzino con corridoi labirintici. Più scuro e più grande del Livello 0, con occasionali incontri con altre entità.\n\nCredenziali di emergenza per l'agente Mark: Username: MARK_423, Password: S@feH@ven1",
        "Livello_2.txt": "Il Livello 2, 'Pipe Dreams', è un intricato sistema di tubi e macchinari industriali. L'ambiente è ostile, con temperature elevate e rumori inquietanti.\n\nATTENZIONE: L'accesso a questo livello richiede autorizzazione di Livello 2 o superiore.",
        "Livello_3.txt": "Il Livello 3, 'Electrical Station', è un complesso di uffici abbandonati con cavi elettrici esposti e macchinari pericolosi. L'illuminazione è intermittente e si sentono strani rumori elettrici.\n\nNota tecnica: Il server di backup usa le credenziali - Username: TECH_789, Password: El3ctr1c@l3",
        "Rapporto_Agente_L2.txt": "RAPPORTO AGENTE MEG - LIVELLO 2\n\nAgente: Alex Mercer\nCodice Identificativo: AM-276\nLivello di Autorizzazione: 2\n\nRapporto Missione:\nDurante l'ultima esplorazione del Livello 2, ho notato un aumento significativo dell'attività delle entità ostili. I rumori provenienti dai tubi sembrano comunicare tra loro. Consiglio massima cautela per le future missioni.\n\nNOTA IMPORTANTE: In caso di emergenza, utilizzare le seguenti credenziali per accedere al server di sicurezza di Livello 2:\n\nUsername: ALEX_276\nPassword: P1p3Dr3@ms\n\nQUESTE CREDENZIALI SONO STRETTAMENTE CONFIDENZIALI. NON CONDIVIDERE.",
        "Protocollo_Sicurezza.txt": "PROTOCOLLO DI SICUREZZA MEG\n\n1. Tutti gli agenti devono cambiare le proprie credenziali ogni 30 giorni.\n2. L'accesso ai livelli superiori richiede autorizzazione specifica.\n3. In caso di compromissione, utilizzare le credenziali di emergenza: Username: EMERGENCY_999, Password: L0ckD0wn!"
    }

    while True:
        clear_screen()
        effetto_digitazione("=== ARCHIVIO MEG_APEX - LIVELLO 1 ===")
        effetto_digitazione("File disponibili:")
        for i, file in enumerate(files.keys(), 1):
            print(f"{i}. {file}")
        print("0. Esci dall'archivio")
        print("9. Tenta accesso al Livello 2")

        scelta = input("\nSeleziona un'opzione (0-9): ")
        if scelta == "0":
            break
        elif scelta in [str(i) for i in range(1, 7)]:
            file_selezionato = list(files.keys())[int(scelta) - 1]
            mostra_file(file_selezionato, files[file_selezionato])
        elif scelta == "9":
            tenta_accesso_livello_2()
        else:
            effetto_digitazione("Scelta non valida. Riprova.")
            time.sleep(1)

def tenta_accesso_livello_2():
    clear_screen()
    effetto_digitazione("TENTATIVO DI ACCESSO AL LIVELLO 2")
    effetto_digitazione("Inserire le credenziali di sicurezza:")
    username = input("Username: ")
    password = input("Password: ")

    credenziali_valide = [
        ("ALEX_276", "P1p3Dr3@ms"),
        ("MARK_423", "S@feH@ven1"),
        ("TECH_789", "El3ctr1c@l3"),
        ("EMERGENCY_999", "L0ckD0wn!")
    ]

    if (username, password) in credenziali_valide:
        effetto_digitazione("Credenziali corrette. Accesso al Livello 2 consentito.")
        time.sleep(1)
        try:
            subprocess.run(["python", "TwoApex.py"], check=True)
        except subprocess.CalledProcessError:
            effetto_digitazione("Errore nell'avvio del server di Livello 2. Contattare l'amministratore.")
        except FileNotFoundError:
            effetto_digitazione("File TwoApex.py non trovato. Assicurarsi che sia nella stessa directory.")
    else:
        effetto_digitazione("Credenziali errate. Accesso negato.")
    
    input("Premi Invio per continuare...")

def main():
    clear_screen()
    effetto_digitazione("Iniziando procedura di accesso al server MEG_APEX...", 0.05)
    effetto_digitazione("ATTENZIONE: Accesso non autorizzato è punibile secondo il Protocollo Omega", 0.05)
    time.sleep(1)
    caricamento_proibito()
    effetto_digitazione("Accesso consentito. Benvenuto, Agente.")
    effetto_digitazione("Caricamento del modulo di indagine sull'incidente...")
    time.sleep(1)
    effetto_digitazione("Sei entrato nel primo livello di sicurezza del server MEG_APEX.")
    effetto_digitazione("Qui troverai informazioni di base sui primi livelli delle Backrooms.")
    time.sleep(2)
    
    archivio()
    effetto_digitazione("Disconnessione dal primo livello di sicurezza...")
    effetto_digitazione("ATTENZIONE: Qualsiasi forma di intrusione non autorizzata avrà gravi conseguenze.")
    input("Premi Invio per terminare la sessione...")

if __name__ == "__main__":
    main()
