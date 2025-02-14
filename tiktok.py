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

def spawn_ammo():
    # Simula la tecla 'ñ'
    keyboard.press('ñ')
    sleep(0.1)
    keyboard.release('ñ')
    sleep(0.9)
    # Escribe el comando
    command = "player.additem 0001f276 100"
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


# Evento cuando alguien **envía un regalo**
@client.on(GiftEvent)
async def on_gift(event: GiftEvent):
    global monedas
    monedas += event.gift.diamond_count * event.gift.repeat_count  # Contar monedas correctamente
    print(f"Total de monedas acumuladas: {monedas}")
    spawn_enemy()
    # Cada 100 monedas, ejecutar el script y restar 100 al contador
    while monedas >= 50:
        spawn_enemy()
        monedas -= 50
        print("Se ha invocado un enemigo por 100 monedas.")

# Evento cuando alguien envía monedas (gifts)
@client.on(LikeEvent)
async def on_gift(event: LikeEvent):
    global likes_guardados
    like = event.total
    print(f"Total de likes: {like}")

    if(like - likes_guardados >= 250):
        spawn_enemy()
        likes_guardados = like

# Evento cuando alguien **te sigue**
@client.on(FollowEvent)
async def on_follow(event: FollowEvent):
    global lista_users

    if(event.user.nickname in lista_users):
        return
    else:
        lista_users.append(event.user.nickname)
    print(f"{event.user.nickname} ha seguido el canal! Spawneando enemigo...")
    spawn_enemy()
# Iniciar el cliente
if __name__ == "__main__":
    client.run()