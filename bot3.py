import discord
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('Qué puedo reciclar?'):
        await message.channel.send("Lo que puedes reciclar en contenedores amarillos (plástico): Botellas de plástico, envases de plástico, latas, bebidas etc.")
        await message.channel.send("Lo que puedes reciclar en contenedores verdes (vidrio): Botellas de vidrio, tarros, vasos, tapas etc")
        await message.channel.send("Lo que puedes reciclar en contenedores azules (papel): Libros, revistas, papel de regalo, sobres, cuadernos etc.")
        await message.channel.send("Lo que puedes reciclar en contenedores rojos (peligrosos): Baterías, pilas, insecticidas etc.")
        with open('images/reciclaje.jpeg', 'rb') as f:#fijar que la imagen se llame igual aca que en la carpeta imagenes
            picture = discord.File(f)
        await message.channel.send(file=picture)

client.run("MTI3MjMyNzA5MTYxMzk5MDkyMg.G-8rDe.2WxG_7EZwVcFmDqTgB30IJ1MLD5MedyLAXD1X4")