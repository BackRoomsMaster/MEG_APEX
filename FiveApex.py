import random
import hashlib
import time
import sys
import string
import subprocess

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_password(input_password, correct_hash):
    return hash_password(input_password) == correct_hash

def animate_cracking(attempts, password_length):
    bar_length = 40
    filled_length = int(bar_length * (len(password_length) / 16))
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    sys.stdout.write(f'\rTentativi: {attempts} | Lunghezza attuale: {password_length} [{bar}]')
    sys.stdout.flush()

def generate_password(length, chars=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(length))

def crack_password(correct_hash):
    attempts = 0
    password_length = 1
    chars = string.ascii_lowercase + string.digits + string.punctuation

    while True:
        attempts += 1
        if attempts % 1000 == 0:
            animate_cracking(attempts, '?' * password_length)

        password = generate_password(password_length, chars)
        if check_password(password, correct_hash):
            print(f"\nPassword trovata dopo {attempts} tentativi!")
            return password

        if attempts % 1000000 == 0:
            password_length += 1
            if password_length > 16:
                password_length = 1
                chars = string.ascii_letters + string.digits + string.punctuation

def launch_sixth_level():
    print("\nAccesso al sesto livello in corso...")
    try:
        subprocess.run(["python", "SixApex.py"], check=True)
    except subprocess.CalledProcessError:
        print("Errore critico nell'avvio del sesto livello.")
        sys.exit(1)
    except FileNotFoundError:
        print("Errore fatale: Impossibile trovare il file SixApex.py.")
        sys.exit(1)

def main():
    print("Benvenuto al quinto livello di sicurezza")
    print("Per accedere al sesto livello, devi superare questa sfida di sicurezza.")
    print("Iniziando l'attacco di forza bruta...")

    correct_password = generate_password(random.randint(8, 16))
    correct_hash = hash_password(correct_password)

    start_time = time.time()
    found_password = crack_password(correct_hash)
    end_time = time.time()

    print(f"La password corretta è: {found_password}")
    print(f"Tempo impiegato: {end_time - start_time:.2f} secondi")
    print("Accesso al sesto livello concesso.")

    print("\nAvanzamento automatico al sesto livello...")
    time.sleep(2) 
    launch_sixth_level()

if __name__ == "__main__":
    main()
