import discord

# Configuración de intents
intents = discord.Intents.default()
intents.message_content = True

# Crear un bot con los intents configurados
client = discord.Client(intents=intents)

# Diccionario de comandos
commands = {
    '$hello': "Hi! :P",
    '$bye': "Adios! :D",
    '$help': (
        "**Comandos disponibles:**\n"
        "$hello - Saluda al usuario.\n"
        "$bye - Despídete con una carita feliz.\n"
        "$help - Muestra esta ayuda."
    ),
}

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    # Ignorar mensajes del propio bot
    if message.author == client.user:
        return

    # Procesar el mensaje
    command_response = commands.get(message.content)

    if command_response:
        await message.channel.send(command_response)
    else:
        # Mensaje de error para comandos no reconocidos
        if message.content.startswith('$'):
            await message.channel.send("Comando no reconocido. Usa `$help` para ver los comandos disponibles.")
        else:
            # Reenviar el mensaje si no es un comando
            await message.channel.send(message.content)

@client.event
async def on_error(event, *args, **kwargs):
    # Manejo básico de errores
    print(f'Ocurrió un error en el evento {event}: {args[0]}')

client.run("TOKEN")
