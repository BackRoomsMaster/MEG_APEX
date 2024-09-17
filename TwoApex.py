import time
import os
import random
import sys

def pulisci_schermo():
    os.system('cls' if os.name == 'nt' else 'clear')

def schermata_caricamento():
    print("Inizializzazione del Secondo livello...")
    for i in range(101):
        print(f"Caricamento: {i}%", end='\r')
        time.sleep(0.05)
    pulisci_schermo()

def schermate_avvertimento():
    avvertimenti = [
        "ATTENZIONE: L'accesso non autorizzato è severamente vietato.",
        "CAUTELA: Le informazioni che stai per accedere sono classificate.",
        "ALLERTA: Procedi con cautela. La realtà potrebbe essere alterata.",
        "AVVISO: La tua percezione della realtà potrebbe essere compromessa.",
        "PERICOLO: Informazioni sul Livello 6 delle Backrooms in arrivo."
    ]
    
    for avvertimento in avvertimenti:
        pulisci_schermo()
        print("\n" * 10)
        print(avvertimento.center(80))
        time.sleep(2)

def crea_database():
    return [
        {"id": 1, "titolo": "Panoramica Livello 6", "contenuto": "Il Livello 6 è un vasto ambiente simile a una fabbrica oscura con macchinari pericolosi."},
        {"id": 2, "titolo": "Condizioni di Illuminazione", "contenuto": "Luci fioche e tremolanti illuminano a malapena i corridoi e le stanze infinite."},
        {"id": 3, "titolo": "Entità", "contenuto": "Fai attenzione alle entità ostili note come 'Gli Operai della Fabbrica', evitale a tutti i costi."},
        {"id": 4, "titolo": "Consigli di Sopravvivenza", "contenuto": "Rimani in silenzio, evita i macchinari e conserva le risorse per sopravvivere nel Livello 6."},
        {"id": 5, "titolo": "Punti di Uscita", "contenuto": "Rare uscite possono portare ai Livelli 5, 7 o 8. Usa estrema cautela quando tenti di uscire."},
        {"id": 6, "titolo": "Pericoli Ambientali", "contenuto": "Fumi tossici, pavimenti instabili e macchinari malfunzionanti rappresentano minacce costanti."},
        {"id": 7, "titolo": "Distorsione Temporale", "contenuto": "Il tempo scorre in modo diverso nel Livello 6, rendendo difficile tenere traccia dei giorni o delle ore."},
        {"id": 8, "titolo": "Anomalie Sonore", "contenuto": "Strani rumori meccanici e urla distanti sono comuni, ma le loro fonti sono sconosciute."},
        {"id": 9, "titolo": "Scarsità di Risorse", "contenuto": "Cibo e acqua sono estremamente rari. I sopravvissuti devono essere ingegnosi per trovare sostentamento."},
        {"id": 10, "titolo": "Effetti Psicologici", "contenuto": "Una permanenza prolungata nel Livello 6 può portare a grave paranoia, allucinazioni e crollo mentale."}
    ]

def mostra_terminale(database):
    while True:
        pulisci_schermo()
        print("Secondo livello - Database Livello 6 delle Backrooms")
        print("=" * 50)
        print("1. Elenca tutti i file")
        print("2. Visualizza contenuto del file")
        print("3. Rivivi il ricordo dell'esploratore")
        print("4. Esci")
        scelta = input("Inserisci la tua scelta (1-4): ")

        if scelta == '1':
            for file in database:
                print(f"{file['id']}. {file['titolo']}")
            input("\nPremi Invio per continuare...")
        elif scelta == '2':
            id_file = int(input("Inserisci l'ID del file: "))
            file = next((f for f in database if f['id'] == id_file), None)
            if file:
                print(f"\nTitolo: {file['titolo']}")
                print(f"Contenuto: {file['contenuto']}")
            else:
                print("File non trovato.")
            input("\nPremi Invio per continuare...")
        elif scelta == '3':
            if gioco_ricordo(database):
                return True
        elif scelta == '4':
            print("Uscita dal Secondo livello...")
            sys.exit()
        else:
            print("Scelta non valida. Riprova.")
            time.sleep(1)
    return False

def gioco_ricordo(database):
    pulisci_schermo()
    print("ATTENZIONE: Stai per rivivere il ricordo di un esploratore morto nel Livello 6.")
    print("Le tue scelte dovranno basarsi sulle informazioni contenute nel database.")
    input("\nPremi Invio per iniziare...")

    scelte = [
        {
            "testo": "Ti trovi in un vasto ambiente industriale con macchinari pericolosi. L'aria è densa di fumi tossici. Cosa fai?",
            "opzioni": ["Cerchi una maschera antigas", "Trattieni il respiro e corri", "Stracci la tua maglietta e la usi come filtro"],
            "corretta": 2,
            "spiegazione": "I fumi tossici sono un pericolo costante nel Livello 6. Usare la maglietta come filtro improvvisato è la soluzione migliore in assenza di equipaggiamento specifico."
        },
        {
            "testo": "Senti dei passi pesanti avvicinarsi. Potrebbero essere 'Gli Operai della Fabbrica'. Come procedi?",
            "opzioni": ["Ti nascondi dietro un macchinario", "Cerchi di comunicare con loro", "Rimani immobile nel buio"],
            "corretta": 2,
            "spiegazione": "Gli Operai della Fabbrica sono entità ostili da evitare a tutti i costi. Rimanere immobili nel buio sfrutta le condizioni di scarsa illuminazione del livello."
        },
        {
            "testo": "Trovi una rara scorta di cibo e acqua. Come gestisci queste risorse?",
            "opzioni": ["Consumi tutto subito", "Porti con te solo l'acqua", "Razioni attentamente entrambi"],
            "corretta": 2,
            "spiegazione": "Le risorse sono estremamente scarse nel Livello 6. Razionare attentamente è fondamentale per la sopravvivenza a lungo termine."
        },
        {
            "testo": "Noti che il tuo orologio si comporta in modo strano. Come interpreti questo fenomeno?",
            "opzioni": ["L'orologio è rotto", "C'è una distorsione temporale", "Ignori il problema"],
            "corretta": 1,
            "spiegazione": "Il Livello 6 è noto per le sue distorsioni temporali, che rendono difficile tracciare il passaggio del tempo."
        },
        {
            "testo": "Dopo ore di esplorazione, senti di perdere il contatto con la realtà. Cosa fai?",
            "opzioni": ["Continui a esplorare freneticamente", "Ti fermi e mediti", "Cerchi di parlare con te stesso ad alta voce"],
            "corretta": 1,
            "spiegazione": "La permanenza prolungata nel Livello 6 può causare effetti psicologici gravi. Fermarsi e meditare può aiutare a mantenere la lucidità mentale."
        }
    ]

    for scelta in scelte:
        pulisci_schermo()
        print(scelta["testo"])
        for i, opzione in enumerate(scelta["opzioni"], 1):
            print(f"{i}. {opzione}")
        
        risposta = input("\nInserisci il numero della tua scelta: ")
        if risposta.isdigit() and 1 <= int(risposta) <= 3:
            if int(risposta) == scelta["corretta"]:
                print("\nScelta corretta.")
                print(scelta["spiegazione"])
            else:
                print("\nScelta errata.")
                print(scelta["spiegazione"])
                print("Il ricordo si interrompe. Accesso al terzo livello negato.")
                return False
        else:
            print("\nScelta non valida. Il ricordo si interrompe.")
            print("Accesso al terzo livello negato.")
            return False
        
        input("\nPremi Invio per continuare...")

    print("\nHai rivissuto con successo il ricordo dell'esploratore, dimostrando una profonda comprensione del Livello 6.")
    print("Accesso al terzo livello consentito.")
    return True

def main():
    schermata_caricamento()
    schermate_avvertimento()
    database = crea_database()
    if mostra_terminale(database):
        print("\nPreparazione per l'accesso al terzo livello...")
        time.sleep(2)
        os.system('python ThreeApex.py')
    else:
        print("\nImpossibile accedere al terzo livello. Terminazione del programma.")
        sys.exit()

if __name__ == "__main__":
    main()
