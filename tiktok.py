import asyncio
import random
from time import sleep
from TikTokLive import TikTokLiveClient
from TikTokLive.events import CommentEvent, LikeEvent, GiftEvent, FollowEvent
from pynput.keyboard import Controller, Key
import json
# Cambia esto por tu usuario de TikTok (sin @)
USERNAME = "nayd3c"
keyboard = Controller()
# Conectar al chat de TikTok
client = TikTokLiveClient(unique_id=USERNAME)
lista_users= []
monedas = 0
enemy_queue = asyncio.Queue()
likes_guardados = 0
acciones = 0
# Función para ejecutar el comando en Fallout 4
def spawn_enemy():
    # Simula la tecla 'ñ'
    keyboard.press('ñ')
    sleep(0.1)
    keyboard.release('ñ')
    sleep(0.9)
    # Escribe el comando
    lista =["000971B9 5", #cucaracha trio
            "000758AD 3", #necrofago trio
            "001A03F7 1", #asaltante sinth muy dificil
            "001A734A 2", # saqueador tanque medio dificil
            "001437F4 1", # yao guai albino muy dificil
            "001423A9 1", # sanguinaria matriarca mortal
            "0017E6F0 1", # supermutante de la guerra legendario mortal---------
            "0017E6D3 2", #mirelurk legendario facil -----------
            "0016CA41 2", #cucaracha legendaria -----
            "0017E6DE 1", # saqueador legendario ----------
            "0012B97C 1", # BEHEMOTH ANCIANO
        ]
    command = "player.placeatme "+random.choice(lista)
    for char in command:
        keyboard.press(char)
        sleep(0.01)
        keyboard.release(char)
    sleep(0.1)
    # Simula la tecla 'enter'
    keyboard.press(Key.enter)
    sleep(0.1)
    keyboard.release(Key.enter)
    sleep(0.1)
    # Simula la tecla 'ñ' nuevamente
    keyboard.press('ñ')
    sleep(0.1)
    keyboard.release('ñ')

def spawn_recursos():
    # Simula la tecla 'ñ'
    keyboard.press('ñ')
    sleep(0.1)
    keyboard.release('ñ')
    sleep(0.9)
    
    # Lista de recursos con sus códigos
    recursos = [
        "0006907a 10", # Aluminio
        "0006907c 10", # Cobre
        "0006907b 10", # Circuitos
        "0006907d 10", # Cristal
        "000731a3 20", # Madera
        "00106d98 10", # Goma
        "00106d99 10", # Hormigón
        "000731a4 20", # Acero
        "000aec5d 10", # Hueso
        "0006907e 10", # Engranajes
        "00059B25 5",  # Pegamento
        "000aec5f 10", # Textiles
        "001bf72e 5",  # Pegamento alternativo
        "00069087 5",  # Fibra Óptica
        "0006907f 10", # Plástico
        "000AEC5E 10", # Cerámica
        "000AEC63 10", # Plomo
        "000AEC5C 10", # Amianto
        "000AEC62 5",  # Oro
        "000AEC64 10", # Piel
        "000AEC60 5",  # Tubo
        "001BF732 5",  # Aceite
        "001BF72D 5",  # Ácido
        "00069082 10", # Muelle
        "00069086 5",  # Material Nuclear
        "001bf72f 5",  # Antiséptico
        "00069085 10", # Vidrio
        "00069081 10", # Tornillo
        "0004D1F2 5",  # Cinta Adhesiva
        "00059b1e 5",  # Trementina
        "000AEC61 5",  # Fibra De Vidrio
        "00059B02 5",  # Dinero De Antes De La Guerra
        "000AEC66 5"   # Plata
    ]
    
    command = ";player.additem " + random.choice(recursos)
    
    for char in command:
        keyboard.press(char)
        sleep(0.01)
        keyboard.release(char)
    
    sleep(0.1)
    
    # Simula la tecla 'enter'
    keyboard.press(Key.enter)
    sleep(0.1)
    keyboard.release(Key.enter)
    sleep(0.1)
    
    # Simula la tecla 'ñ' nuevamente
    keyboard.press('ñ')
    sleep(0.1)
    keyboard.release('ñ')

def spawn_ammo():
    # Simula la tecla 'ñ'
    keyboard.press('ñ')
    sleep(0.1)
    keyboard.release('ñ')
    sleep(0.9)
    # Escribe el comando
    lista =["0001f673 50",# cartucho de escopeta
            "00075FE4 1", # nucleo de fusion
            "0001f66c 1", # 5mm
            "0001f276 50", # 10mm
            "0001f279 50", # 50mm
            "000c1897 50", # celulas de energia
            "0001f278 50", # 5.56mm
            "0001f66a 50", # .45
            "0009221c 50", # .44
            "0001f66b 50", # .308
            "0004ce87 50", # .38
            "00023736 25", # estimulante
            "00023742 25", # radaway
        ]
    command = ";player.additem "+random.choice(lista)
    for char in command:
        keyboard.press(char)
        sleep(0.01)
        keyboard.release(char)
    sleep(0.1)
    # Simula la tecla 'enter'
    keyboard.press(Key.enter)
    sleep(0.1)
    keyboard.release(Key.enter)
    sleep(0.1)
    # Simula la tecla 'ñ' nuevamente
    keyboard.press('ñ')
    sleep(0.1)
    keyboard.release('ñ')

def comprobarEstado():
    while True:
        if(acciones >= 1):
            spawn_enemy()
            if random.randint(0, 100) <= 20:
                    sleep(0.1)
                    spawn_ammo()
            acciones -= 1
        else:
            sleep(5)
            continue

# Evento cuando alguien **envía un regalo**
@client.on(GiftEvent)
async def on_gift(event: GiftEvent):
    global monedas
    global acciones
    monedas += event.gift.diamond_count
    print(f"Total de monedas acumuladas: {monedas}")
    spawn_enemy()
    # Cada 100 monedas, ejecutar el script y restar 100 al contador
    if random.randint(0, 100) <= 20:
        sleep(0.1)
        spawn_ammo()
        print("Se ha invocado un enemigo por 50 monedas.")

# Evento cuando alguien envía monedas (gifts)
@client.on(LikeEvent)
async def on_gift(event: LikeEvent):
    global likes_guardados
    global acciones
    like = event.total
    print(f"Total de likes: {like}")

    if(like - likes_guardados >= 250):
        spawn_enemy()
        if random.randint(0, 100) <= 20:
            sleep(0.1)
            spawn_ammo()
        likes_guardados = like

# Evento cuando alguien **te sigue**
@client.on(FollowEvent)
async def on_follow(event: FollowEvent):
    global lista_users
    global acciones
    if(event.user.nickname in lista_users):
        return
    else:
        lista_users.append(event.user.nickname)
    print(f"{event.user.nickname} ha seguido el canal! Spawneando enemigo...")
    spawn_enemy()
    if random.randint(0, 100) <= 20:
        sleep(0.1)
        spawn_ammo()

if __name__ == "__main__":
    client.run()