import time
import random
import os
import subprocess

def pulisci_schermo():
    os.system('cls' if os.name == 'nt' else 'clear')

def testo_corrotto(testo):
    corrotto = ""
    for carattere in testo:
        if random.random() < 0.1:
            corrotto += chr(random.randint(33, 126))
        else:
            corrotto += carattere
    return corrotto

def effetto_glitch(testo):
    glitch = ""
    for carattere in testo:
        if random.random() < 0.1:
            glitch += random.choice(['█', '▓', '▒', '░', '╳', '╪', '┼', '┴', '┬', '├', '┤'])
        else:
            glitch += carattere
    return glitch

def crea_database_creature():
    creature = [
        "Hound", "Skin-Stealers", "Smilers", "Clumps", "Faceling",
        "The Beast of Level 5", "Dullers", "Crawlers", "Deathmoths", "Bursters",
        "Facerooms", "Skin-Takers", "Clowns", "Stalkers", "Wretches",
        "Bacteria", "Insanities", "Partygoers", "Windows", "Sirens",
        "Frogmen", "Hunters", "Watchers", "Mannequins", "Shadows",
        "Deathmaws", "Howlers", "Skin-Dogs", "Bone Thieves", "Leeches",
        "Jellyfishes", "Screamers", "Puppeteers", "Whisperers", "Void Demons",
        "Flesh Walls", "Memory Eaters", "Dream Stealers", "Time Shifters", "Reality Benders"
    ]

    os.makedirs("database_creature", exist_ok=True)
    for i, creatura in enumerate(creature, 1):
        with open(f"database_creature/creatura_{i:02d}.txt", "w") as f:
            f.write(f"Nome: {creatura}\n")
            f.write(f"Livello di pericolo: {random.randint(1, 10)}\n")
            f.write(f"Descrizione: Una misteriosa entità delle backrooms...\n")
            f.write(f"Avvistamenti: Livello {random.randint(0, 999)}\n")

def animazione_caricamento():
    simboli = ['|', '/', '-', '\\']
    messaggi = [
        "Caricamento terzo livello...",
        "Inizializzazione ambiente corrotto...",
        "Aggiramento protocolli di sicurezza...",
        "Accesso ai dati riservati...",
        "Creazione database creature..."
    ]
    
    for _ in range(20):
        for simbolo in simboli:
            pulisci_schermo()
            for messaggio in messaggi:
                print(effetto_glitch(testo_corrotto(f"[{simbolo}] {messaggio}")))
            time.sleep(0.2)

    pulisci_schermo()
    messaggi_finali = [
        "Terzo livello compromesso!",
        "Accesso concesso a tutti i sottosistemi.",
        "Database creature creato con successo.",
        "Attenzione: Rilevate molteplici violazioni di sicurezza!",
        "Avvio protocolli di emergenza..."
    ]
    
    for messaggio in messaggi_finali:
        print(effetto_glitch(testo_corrotto(messaggio)))
    time.sleep(2)

def menu_principale():
    while True:
        pulisci_schermo()
        print(effetto_glitch(testo_corrotto("=== TERZO LIVELLO ===\n")))
        print(effetto_glitch(testo_corrotto("1. Visualizza database creature")))
        print(effetto_glitch(testo_corrotto("2. Accedi al quarto livello")))
        print(effetto_glitch(testo_corrotto("3. Esci")))
        
        scelta = input(effetto_glitch(testo_corrotto("\nScegli un'opzione: ")))
        
        if scelta == "1":
            visualizza_database()
        elif scelta == "2":
            accedi_quarto_livello()
        elif scelta == "3":
            break
        else:
            print(effetto_glitch(testo_corrotto("Opzione non valida. Riprova.")))
            time.sleep(1)

def visualizza_database():
    pulisci_schermo()
    print(effetto_glitch(testo_corrotto("=== DATABASE CREATURE ===\n")))
    for file in os.listdir("database_creature"):
        with open(os.path.join("database_creature", file), "r") as f:
            contenuto = f.read()
            print(effetto_glitch(testo_corrotto(contenuto)))
            print()
    input(effetto_glitch(testo_corrotto("Premi Enter per tornare al menu principale...")))

def accedi_quarto_livello():
    pulisci_schermo()
    print(effetto_glitch(testo_corrotto("Avvio accesso al quarto livello...")))
    time.sleep(1)
    subprocess.run(["python", "FourApex.py"])

if __name__ == "__main__":
    crea_database_creature()
    animazione_caricamento()
    menu_principale()
