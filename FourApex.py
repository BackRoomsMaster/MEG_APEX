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

def richiedi_credenziali():
    pulisci_schermo()
    print(effetto_glitch(testo_corrotto("=== ACCESSO AL QUARTO LIVELLO ===\n")))
    print(effetto_glitch(testo_corrotto("Inserire le credenziali di accesso:")))
    
    start_time = time.time()
    while time.time() - start_time < 10:
        username = input(effetto_glitch(testo_corrotto("Username: ")))
        password = input(effetto_glitch(testo_corrotto("Password: ")))
        print(effetto_glitch(testo_corrotto("Verifica credenziali in corso...")))
        time.sleep(1)
        print(effetto_glitch(testo_corrotto("Accesso negato. Riprovare.")))
    
    glitch_schermata()

def glitch_schermata():
    pulisci_schermo()
    for _ in range(10):
        print(effetto_glitch(testo_corrotto("ERRORE DI SISTEMA")))
        time.sleep(0.2)
        pulisci_schermo()
        time.sleep(0.1)
    
    print(effetto_glitch(testo_corrotto("Inizializzazione bypass di sicurezza...")))
    time.sleep(2)
    
    animazione_caricamento()

def animazione_caricamento():
    simboli = ['|', '/', '-', '\\']
    for _ in range(20):
        for simbolo in simboli:
            pulisci_schermo()
            print(effetto_glitch(testo_corrotto(f"[{simbolo}] Caricamento quarto livello...")))
            time.sleep(0.1)
    
    pulisci_schermo()
    print(effetto_glitch(testo_corrotto("ACCESSO AL QUARTO LIVELLO CONCESSO")))
    print(effetto_glitch(testo_corrotto("Benvenuto nell'abisso...")))
    time.sleep(2)
    mostra_frasi_disturbanti()

def mostra_frasi_disturbanti():
    frasi = [
        "Il vuoto ti osserva...",
        "Non c'è via di fuga dall'infinito...",
        "Le pareti sussurrano segreti dimenticati...",
        "Il tempo non ha significato qui...",
        "Sei solo un'eco nell'abisso...",
        "La realtà si sgretola intorno a te...",
        "Il nulla ti abbraccia...",
        "Ogni passo ti porta più lontano da casa...",
        "Le ombre danzano con intenzioni sinistre...",
        "Il silenzio urla verità indicibili..."
    ]
    
    pulisci_schermo()
    print(effetto_glitch(testo_corrotto("=== RIVELAZIONI DEL VUOTO ===\n")))
    
    for frase in frasi:
        print(effetto_glitch(testo_corrotto(frase)))
        time.sleep(random.uniform(1.5, 3.0))
        pulisci_schermo()
    
    accedi_quinto_livello()

def accedi_quinto_livello():
    pulisci_schermo()
    print(effetto_glitch(testo_corrotto("Inizializzazione accesso al quinto livello...")))
    time.sleep(2)
    print(effetto_glitch(testo_corrotto("ATTENZIONE: Violazione critica dei protocolli di sicurezza")))
    time.sleep(1)
    print(effetto_glitch(testo_corrotto("Avvio FiveApex.py...")))
    time.sleep(2)
    subprocess.run(["python", "FiveApex.py"])

if __name__ == "__main__":
    richiedi_credenziali()
