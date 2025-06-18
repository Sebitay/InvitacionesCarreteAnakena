def leer_nombres_csv(archivo_csv):
    """Lee nombres desde un archivo CSV simple"""
    nombres = []
    try:
        with open(archivo_csv, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                nombre = linea.strip()
                if nombre and nombre.lower() != 'nombre':  # Saltar cabecera
                    nombres.append(nombre)
        return nombres
    except Exception as e:
        print(f"Error leyendo CSV: {e}")
        return []
    

import time
import random
from telethon.sync import TelegramClient
from telethon.errors import FloodWaitError, UsernameNotOccupiedError, UsernameInvalidError

api_id = '23992982'
api_hash = 'fb9a5cd5947245e8a4db840b1d10c86f'
phone = '+56956302932'

invitados = leer_nombres_csv('invitados.csv')
invitados = ["Jerohem Yañez,@jerororo"]

mensaje = "{nombre}, es de nuestro agrado invitarte a la siguiente edicion del esperado Carrete Anakena\n\n Escriba 'CONFIRMAR' para confirmar su asistencia"

with TelegramClient('new_session', api_id, api_hash) as client:
    client.start(phone=phone)

    for invitado in invitados:
        nombre, telegram = invitado.split(',')
        username = telegram.strip().replace('@', '')
        image = f"images/invitacion_{nombre.replace(' ', '_')}.png"
        mensaje_personalizado = mensaje.format(nombre=nombre)

        try:
            entity = client.get_entity(username)
            client.send_file(entity, image, caption=mensaje_personalizado)
            print(f"✅ Mensaje enviado a {nombre}")

            # Delay aleatorio entre 7 y 15 segundos
            time.sleep(random.uniform(7, 15))

        except FloodWaitError as e:
            print(f"⏳ FloodWait: esperando {e.seconds} segundos...")
            time.sleep(e.seconds)

        except (UsernameNotOccupiedError, UsernameInvalidError):
            print(f"❌ Usuario no válido o no existe: {username}")

        except Exception as e:
            print(f"⚠️ Error al enviar a {nombre} (@{username}): {e}")
