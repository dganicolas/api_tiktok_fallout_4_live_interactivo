import time
import pyf4se  # Librería para interactuar con F4SE

# Función para enviar comandos al Fallout 4
def send_fallout_command(command):
    pyf4se.send_mod_event("F4SECommand", command)
    print(f"Comando enviado: {command}")

# Ejemplo: Spawn de un enemigo
send_fallout_command("player.placeatme 0001DB4C 1")  # Deathclaw

# Esperar un poco para ver el resultado
time.sleep(2)
