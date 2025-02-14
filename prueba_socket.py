from time import sleep


def send_fallout_command(command):
    # Ruta al archivo de comandos
    file_path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Fallout 4\\CommandQueue.txt"
    
    # Escribir el comando en el archivo
    with open(file_path, 'w') as file:
        file.write(command)
    print(f"Comando enviado a Fallout 4: {command}")

# Ejemplo de uso: Enviar un comando para spawnear un enemigo



if __name__ == "__main__":
   sleep(10)
   print("spawn")
   send_fallout_command("player.placeatme 00020749 1")  # Spawnea un Raider