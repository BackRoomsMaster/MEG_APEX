import time
import random
import os

CLASSIFIED_FOLDER = "classified"

SECURITY_QUESTIONS = {
    "Qual è il nome in codice del Livello 0?": "lobby",
    "Quanti livelli sono stati ufficialmente documentati dal MEG?": "9",
    "Quale entità è conosciuta come 'il re' delle Backrooms?": "the beast",
    "Qual è il colore predominante nel Livello 1?": "giallo",
    "Quale oggetto è fondamentale per sopravvivere nel Livello 6?": "torcia",
    "Qual è il nome della base principale del MEG nel Livello 11?": "alpha",
    "Quale livello è noto come 'Il Vuoto'?": "7",
    "Quale sostanza è pericolosa da bere nel Livello 0?": "almond water",
    "Qual è il metodo più sicuro per spostarsi tra i livelli?": "noclip"
}

def glitched_loading():
    loading_chars = ['|', '/', '-', '\\']
    glitch_chars = ['@', '#', '$', '%', '&', '*', '!', '?']
    
    for _ in range(20):
        glitch = ''.join(random.choice(glitch_chars) for _ in range(random.randint(1, 5)))
        print(f"\rLoading {random.choice(loading_chars)} {glitch}", end='', flush=True)
        time.sleep(0.2)
        
        if random.random() < 0.3:
            print(f"\r{''.join(random.choice(glitch_chars) for _ in range(50))}", end='', flush=True)
            time.sleep(0.1)
    
    print("\nCARICAMENTO COMPLETATO... MA QUALCOSA NON VA...")
    time.sleep(2)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def read_file(file_name):
    file_path = os.path.join(CLASSIFIED_FOLDER, file_name)
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return f"Errore: Il file '{file_name}' non esiste."
    except Exception as e:
        return f"Errore nella lettura del file: {str(e)}"

def list_files():
    if not os.path.exists(CLASSIFIED_FOLDER):
        return []
    return [f for f in os.listdir(CLASSIFIED_FOLDER) if f.endswith('.txt')]

def security_questions():
    questions = list(SECURITY_QUESTIONS.items())
    random.shuffle(questions)
    correct_answers = 0
    
    for question, correct_answer in questions:
        user_answer = input(f"{question}: ").strip().lower()
        if user_answer == correct_answer.lower():
            correct_answers += 1
    
    return correct_answers == len(questions)

def corrupted_text(text):
    glitch_chars = ['@', '#', '$', '%', '&', '*', '!', '?']
    corrupted = ''
    for char in text:
        if random.random() < 0.1:
            corrupted += random.choice(glitch_chars)
        else:
            corrupted += char
    return corrupted

def animated_print(text, delay=0.03, corruption_chance=0.2):
    for char in text:
        if random.random() < corruption_chance:
            print(random.choice(['@', '#', '$', '%', '&', '*', '!', '?']), end='', flush=True)
        else:
            print(char, end='', flush=True)
        time.sleep(delay)
    print()

def supervisor_chat():
    messages = [
        ("Supervisore", "Agente, mi ricevi? Sei riuscito ad accedere al Livello 7?"),
        ("Tu", "Sì, signore. Sono appena entrato. È... diverso da come me l'aspettavo."),
        ("Supervisore", "Bene. Qual è la tua prima impressione?"),
        ("Tu", "È buio qui. C'è un odore strano nell'aria. Sento... rumori."),
        ("Supervisore", "Mantieni la calma. Descrivi i rumori."),
        ("Tu", "Sembrano... passi. No, aspetta. Non sono passi. È più come un... strisciare."),
        ("Supervisore", "Agente, ascoltami attentamente. Devi muoverti. Ora."),
        ("Tu", "Cosa? Perché? Cosa sta succ-"),
        ("Supervisore", "CORRI! È una trappola!"),
        ("Tu", "Oh dio, li vedo! Sono... AAAARGH!"),
        ("Supervisore", "Agente? AGENTE! Rispondi!"),
        ("Sistema", "Connessione persa.")
    ]
    
    for sender, message in messages:
        animated_print(f"{sender}: {corrupted_text(message)}")
        time.sleep(random.uniform(1.5, 3.5))
        if sender == "Tu":
            input("Premi Invio per continuare...")
    
    animated_print("\nFine della trasmissione.", delay=0.1, corruption_chance=0.5)

def terminal():
    clear_screen()
    print("=== TERMINALE DI ACCESSO ALL'ARCHIVIO CLASSIFICATO ===")
    print("Benvenuto nel sistema di archiviazione del Livello 6: Apex")
    
    while True:
        print("\nOpzioni disponibili:")
        print("1. Elencare i file")
        print("2. Leggere un file")
        print("3. Accedere al Livello 7")
        print("4. Uscire")
        
        choice = input("\nScegli un'opzione (1-4): ").strip()
        
        if choice == "1":
            files = list_files()
            if files:
                print("\nFile disponibili nell'archivio classificato:")
                for file in files:
                    print(f"- {file}")
            else:
                print("\nNessun file trovato nell'archivio classificato.")
        elif choice == "2":
            file_name = input("Inserisci il nome del file da leggere: ")
            if file_name in list_files():
                print(f"\nContenuto di {file_name}:")
                print(read_file(file_name))
            else:
                print(f"\nErrore: Il file '{file_name}' non esiste nell'archivio classificato.")
        elif choice == "3":
            print("\nAccesso al Livello 7 richiesto. Rispondi alle domande di sicurezza.")
            if security_questions():
                print("\nAccesso concesso. Inizializzazione della comunicazione con il supervisore...")
                time.sleep(2)
                supervisor_chat()
                break
            else:
                print("\nAccesso negato. Risposte errate alle domande di sicurezza.")
        elif choice == "4":
            print("\nDisconnessione dal terminale in corso...")
            break
        else:
            print("\nScelta non valida. Riprova.")

def main():
    glitched_loading()
    terminal()

if __name__ == "__main__":
    main()
