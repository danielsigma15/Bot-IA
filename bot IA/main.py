import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(f"Guarda la imagen en ./{attachment.filename}")
            clase = get_class (model_path="keras_model.h5", labels_path="labels.txt", image_path=file_name)
            
            try:
                clase = get_class (model_path="keras_model.h5", labels_path="labels.txt", image_path=f"./{file_name}")
                if clase[0] == "Class 1":
                    await ctx.send(f"El halcon es una ave muy rapida ,cuando ocupan una posicición para atacar a su presa {clase[1]*100}%")
                    await ctx.send("Los halcones comen animeles poco menos de su tamaño ...")
                    await ctx.send("Suelen avitar en las montañas en EEUU")
                
                elif clase[0] == "Class 2":
                    await ctx.send(f"El Gallito de las Rocas, una ave muy hermosa y a la vez muy colorida,en especial por su llamativo color anaranjado {clase[1]*100}%")
                    await ctx.send("Nomas habita en la selva del Perú ...")
                    await ctx.send("Esta ave llega a comer frutos secos e insectos")                
            
                elif clase[0] == "Class 3":
                    await ctx.send(f"El Shima unas de las aves más tiernas del mundo y muy hermoso por su tamallo tan pequeño y su color blanco {clase[1]*100}%")
                    await ctx.send("Esta ave come mariposas exoticas, cuando mas colorida sea la mariposa mejor")
                    await ctx.send("Habita en Japón en la provincia de hokkaido")
            except:
                await ctx.sent("Ha ocurrido un error en la clasificación, revise de nuevo")

    else:
        await ctx.send("Olvidaste subir la imagen :(")

bot.run("tu token")
