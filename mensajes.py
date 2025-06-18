from telethon.sync import TelegramClient

api_id = '23992982'
api_hash = 'fb9a5cd5947245e8a4db840b1d10c86f'
phone = '+56956302932'

client = TelegramClient('session_name', api_id, api_hash)

client.start(phone)

usuarios = ['jerororo']  # usernames sin @
mensaje = "Hola, este es un mensaje automático."

for usuario in usuarios:
    try:
        client.send_message(usuario, mensaje)
        print(f"Mensaje enviado a {usuario}")
    except Exception as e:
        print(f"Error con {usuario}: {e}")

client.disconnect()