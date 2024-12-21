import discord
import os
import random
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def suma(ctx, num1:int,num2:int):
    await ctx.send(f"La suma de {num1} y {num2} es {num1+num2}")

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def limpiar(ctx):
    await ctx.channel.purge()
    await ctx.send("Mensajes eliminados", delete_after = 3)

@bot.command()
async def mem(ctx):
    with open('images/meme1.png', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def memr(ctx):
    img_name = os.listdir('images')
    with open(f'images/{random.choice(img_name)}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def poke(ctx,arg):
    try:
        pokemon = arg.split(" ",1)[0].lower()
        result = requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon)
        if result.text == "Not Found":
            await ctx.send("Pokemon no encontrado")
        else:
            image_url = result.json()["sprites"]["front_default"]
            print(image_url)
            await ctx.send(image_url)

    except Exception as e:
        print("Error:", e)
@poke.error
async def error_type(ctx,error):
    if isinstance(error,commands.errors.MissingRequiredArgument):
        await ctx.send("Tienes que darme un pokemon")

@bot.command()
async def wwII(ctx):
    await ctx.send(f"""
    Hola, soy un bot {bot.user}!
    """)# esta linea saluda
    await ctx.send(f'Te voy hablar un poco sobre la wwII o tambien conocida como la segunda guerra mundial')
    await ctx.send(f'es un suceso historico reconocido por librar un sangriento conflicto a nivel mundial, muchos paises sufrieron las concecuencias de esto')
    # Enviar una pregunta al usuario
    await ctx.send("Quieres datos de la segunda guerra mundial? Responde con 'sí' o 'no'.")
# Esperar la respuesta del usuario
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['sí', 'si', 'no']
    response = await bot.wait_for('message', check=check)
    if response:
        if response.content in ['sí', 'si']:
            await ctx.send("1. el dia d fue una gran operacion militar de los aliados sobre las costas de francia mas especificamente sobre las playas de normandia, el objetivo era abrir un nuevo frente para liberar precion sobre el frente sovietico, esta operacion se retraso un dia por el mal clima.")
            await ctx.send("2. hitler triciono a su alido la uurr por sus ambisiones y esto causo su caida mas adelante")   
        else:
            await ctx.send("Está bien, si alguna vez necesitas datos interesantes, no dudes en preguntar.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")
    await ctx.send("Quieres saber porque cayo francia en un mes en la wwII, responde si o no")
    response1 = await bot.wait_for('message', check=check)
    if response1:
        if response1.content in ['sí', 'si']:
            await ctx.send("basicamente fue por: mala gestion del ejercito dejando puntos debiles como el bosque de las ardenas, poca resisitencia por parte de sus aliados ingleses belgas y holandeses, como resultado de ello cayo la capital paris en un mes") 
        else:
            await ctx.send("Está bien, si alguna vez necesitas datos interesantes, no dudes en preguntar.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")

bot.run("")
