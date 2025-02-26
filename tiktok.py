import asyncio
import random
from time import sleep
from TikTokLive import TikTokLiveClient
from TikTokLive.events import LikeEvent, GiftEvent, FollowEvent
from pynput.keyboard import Controller, Key
import pyperclip

# Configuración
USERNAME = "nayd3c"
keyboard = Controller()
client = TikTokLiveClient(unique_id=USERNAME)
lista_users = []
monedas = 0
likes_guardados = 0
acciones_queue = asyncio.Queue()

def spawn_enemy():
    lista = [
        #empezar 06 muka world
        #empezar 01 automatronj
        #empezar 03 far habor
        "060201E5 1",#cave cricket
        "000758AD 3",#necrofago salvaje
        "001A03F7 1",#asaltante synth cambiar por legendario o poner mas 
        "001A734A 2",#saqueador berserk
        "001437F4 1",#yaou guai albino
        "001423A9 1",#matriarca sanguinaria
        "0017E6F0 1",#señor supremo supermutante legendario 
        "0017E6D3 2",# mirelurk legendario
        "0016CA41 2",#mutaracha legendaria
        "0017E6DE 1",#mirelurk resplandeciente legendario
        "0012B97C 1",#behemoth antiguo
        "002499DA 1",#sanguinario mitico legendario
        "0604BC84 1",#Novatron eliminator
        "0100E6AD 1",#Assaultron gorgon
        "01007077 1",#Assaultron succubus
        "0601F5FD 1",#Space sentry obliterator
        "0100E6BF 1",#Sentry bot reaper
        "0100E6C5 1",#Quantum Robobrain
        "0100E6C4 1",#robobrain
        "0601234D 1",#Nukalurk hunter
        "0601234E 1",#Nukalurk king
        "03009584 1",#Glowing angler
        "03009586 1",#Venomous angler
        "03040C2D 1",#Albino hermit crab
        "0302793D 1",#Gulper devourer
        "0600D325 1",#SANGUINARIO quantum
        "03014455 1",# Enraged fog crawler
        "030140F2 1",#Legendary feral wolf
        "0303D2B2 1",#Legendary glowing wolf
        "0017E6D8 1",#Albino mirelurk hunter (legendary)
    ]
    
    command = "player.placeatme " + random.choice(lista)
    return command

def spawn_ammo():
    lista = [
        "0001f673 50",
        "00075FE4 1",
        "0001f66c 1",
        "0001f276 50",
        "0001f279 50",
        "000c1897 50",
        "0001f278 50",
        "0001f66a 50",
        "0009221c 50",
        "0001f66b 50",
        "0004ce87 50",
        "00023736 25",
        "00023742 25",
        "0006907a 10",
        "0006907c 10",
        "0006907b 10",
        "0006907d 10",
        "000731a3 20",
        "00106d98 10",
        "00106d99 10",
        "000731a4 20",
        "000aec5d 10",
        "0006907e 10",
        "00059B25 5",
        "000aec5f 10",
        "001bf72e 5",
        "00069087 5",
        "0006907f 10",
        "000AEC5E 10", 
    ]
    
    command = ";player.additem " + random.choice(lista)
    return command

def escribir_comando():
    sleep1 =0.07
    keyboard.press('ñ')
    sleep(sleep1)
    keyboard.release('ñ')
    command = spawn_enemy()
    if(random.randint(0, 100) <= 15):
        command += spawn_ammo()
    sleep(sleep1)
    pyperclip.copy(command)
    keyboard.press(Key.ctrl)
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release(Key.ctrl)
    keyboard.press(Key.enter)
    sleep(sleep1)
    keyboard.release(Key.enter)
    sleep(sleep1)
    keyboard.press('ñ')
    sleep(sleep1)
    keyboard.release('ñ')
    sleep(sleep1)

@client.on(GiftEvent)
async def on_gift(event: GiftEvent):
    global monedas
    monedas += event.gift.diamond_count
    print(f"Total de monedas acumuladas: {monedas}")
    escribir_comando()

@client.on(LikeEvent)
async def on_like(event: LikeEvent):
    global likes_guardados
    like = event.total
    print(f"Total de likes: {like}")
    
    if like - likes_guardados >= 75:
        escribir_comando()
        likes_guardados = like

@client.on(FollowEvent)
async def on_follow(event: FollowEvent):
    global lista_users
    if event.user.nickname in lista_users:
        return
    lista_users.append(event.user.nickname)
    
    print(f"{event.user.nickname} ha seguido el canal! Spawneando enemigo...")
    escribir_comando()


if __name__ == "__main__":
    client.run()
