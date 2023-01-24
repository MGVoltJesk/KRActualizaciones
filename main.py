#Importar discord
import discord
from bs4 import BeautifulSoup
import requests
import io
import aiohttp

#Declarar intents
intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_connect():
  print("Bot conectado")

@client.event
async def on_ready():

    #Obtener URL de actualizaciones 1
    url1 = "https://kresup1.tiiny.site/" 
    page1 = requests.get(url1)
    soup1 = BeautifulSoup(page1.content, "html.parser")
    text1 = soup1.get_text()

    #Obtener URL de actualizaciones 2
    url2 = "https://kresup2.tiiny.site/"
    page2 = requests.get(url2)
    soup2 = BeautifulSoup(page2.content, "html.parser")
    text2 = soup2.get_text()

    # Encontrar el canal por su nombre
    channel = discord.utils.get(client.get_all_channels(), name="actualizaciones")
    
    # Enviar el mensaje
    await channel.send(text1)
    await channel.send(text2)

    channel = client.get_channel("ID_HERE") # ID del canal
    url = "https://assets.krunker.io/img/backgrounds/junkyrd_0.png" # URL de imagen
    async with aiohttp.ClientSession() as session: # Crea la sesion
      async with session.get(url) as resp: # Obtiene la imagen de la url
        img = await resp.read() # Lee la imagen de la respuesta
        with io.BytesIO(img) as file: # Convierte a file-like object
            await channel.send(file=discord.File(file, "testimage.png"))
# Usar el token del bot

    channel = client.get_channel("ID_HERE") #ID del canal
    masked_link_embed = discord.Embed( #Crear embed
    title='Ver historial de cambios', #Titulo del embed
    description='[Historial](https://actualizacioneskrunkeres.tiiny.site/)', #Link de la URL y lo camufla como "Historial"
    color=discord.Colour.gold() #Color del embed
  )
    await channel.send(embed=masked_link_embed) #Enviar embed
    pass 

client.run("TOKEN")