#Programas necessários:
# git
# Heroku

#heroku buildbacks:
# heroku/python
# https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git
# https://github.com/xrisk/heroku-opus.git

#Para subir a aplicação pro heroku:
# 1º - Te ruma conta no Heroku e os softwares necessários instalados
# 2º - Criar o projeto no heroku e salvar o nome (site -https://dashboard.heroku.com/apps )
# 3º - Ir nos settongs do projeto e adicionar os buildpacks mostrados anteriormente
# 4º - No terminal, digitar os seguintes comandos:
#       git init
#       heroku git:remote -a nome 
#       git add .
#       git commit -am "Nome qualquer!"
#       git push heroku master
#  Após digitar esses comandos, a aplicação vai subir, então devemos aguardar.
# 5º - Iniciar a aplicação pelo site do Heroku (aba resources)


import discord
import asyncio
#import os
from discord.ext import commands, tasks
from discord.utils import get
#import random
#import time
import requests
from itertools import cycle
#import youtube_dl
import funcoes


client = commands.Bot('!')

status = cycle(['Mensagem1', 'Mensagem2']) #Mensagens que vão rodar no status do BOT

@tasks.loop(seconds=10) #Tarefa que vai a cada 10 segundos atualizar o status do BOT
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_ready(): #Função executada quando o BOT é inicializado
    change_status.start() #Inicia tarefa de atualizar status
    intents = discord.Intents(messages=True, guilds=True)
    intents.members = True
    print('O BOT está pronto!.')

@client.command() #Comando para o BOT 
async def salve(ctx):
     print("Mandando uma mensagem de salve no chat!")
     await ctx.send(f'Opa salve salve!') #Ele responde com essa informação

@client.command() #Comando para o BOT 
async def falar(ctx, mensagem):
     print("Mandando uma mensagem no chat!")
     print(mensagem)
     await ctx.send(mensagem,tts=True) #Ele responde com essa informação e irá falar

audios = ["salve_Sarah.mp3","4_7_anoes.mp3","cala_ryan.mp3","camisa_rosa.mp3","mamute_siberiano.mp3","opa_baum.mp3","pai_toc.mp3"]

@client.command()
async def audio(ctx, info:int):

    pessoa = ctx.message.author #Descobre quem envivou essa mensagem
    canal = pessoa.voice.channel.name #Pega o canal de voz que essa pessoa está
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=canal) #Seleciona o canal que a pessoa está
    print(ctx.guild.voice_channels)
    print(type(voiceChannel))
    await voiceChannel.connect()#Conecta no canal

    voice = discord.utils.get(client.voice_clients, guild=ctx.guild) #Reproduz um audio
    voice.play(discord.FFmpegPCMAudio("audios_alunos/{}".format(audios[info])))

    while voice.is_playing(): #Aguarda esse audio acabar
        await asyncio.sleep(0.4)
    await voice.disconnect() #Desconecta do canal



@client.event
async def on_voice_state_update(member, before, after): #Entra no canal e fala algo
    
    if  member.voice and not member.bot and (before.channel != after.channel):

        #if str(member) == "Vinicius Piovezan#1668": #Caso queira que isso aconteça com uam pessoa específica, usar esse IF

        print(before.channel, after.channel)
        canal = member.voice.channel.name
        voiceChannel = discord.utils.get(member.guild.channels, name=canal) #Seleciona o canal que a pessoa está
        await voiceChannel.connect()#Conecta no canal
        voice = discord.utils.get(client.voice_clients, guild=member.guild) #Reproduz um audio
        voice.play(discord.FFmpegPCMAudio("audios_alunos/{}".format(audios[5])))

        while voice.is_playing(): #Aguarda esse audio acabar
            await asyncio.sleep(1)
        await voice.disconnect() #Desconecta do canal

@client.command()
async def info(ctx, *, member: discord.Member):
    print(ctx)
    await ctx.send(f'Entrou as: {member.joined_at}\nnick: {member.nick}\nGuild: {member.guild}\nStatus: {member.status}\navatar: {member.avatar_url}\nRelação: {member.relationship}')

@client.command()
async def imagem(ctx, member: discord.Member, texto):
    print("Escrevendo na foto do {}".format(member))
    url_imagem = member.avatar_url
    response = requests.get(url_imagem)
    file = open("pessoa.png", "wb")
    file.write(response.content)
    file.close()
    funcoes.imagem(texto)
    await ctx.send(file=discord.File('pessoa_e.png'))

@client.command()
async def tirinha(ctx, member: discord.Member, texto):
    print("Escrevendo na foto do {}".format(member))
    url_imagem = member.avatar_url
    response = requests.get(url_imagem)
    file = open("pessoa.png", "wb")
    file.write(response.content)
    file.close()
    funcoes.tirinha(texto)
    await ctx.send(file=discord.File('pessoa_b.png'))

@client.event
async def on_message(message):
   if 'https://' in message.content:
      await message.delete()
      await message.channel.send(f"{message.author.mention} OOOO MANO, NÃO É PARA MANDAR LINK BIXO!!")
   else:
      await client.process_commands(message)

@client.command('cargo')
@commands.has_permissions(administrator=True) #Permissões necessárias para executar esse comando
async def role(ctx, user : discord.Member, *, role : discord.Role):
  if role.position > ctx.author.top_role.position: #Caso a pessoa seja de um cargo a baixo do que ela está tentando fornecer, o BOT não permite
    return await ctx.send('**:x: |Esse cargo é superior ao seu!!**') 
  if role in user.roles:
      await user.remove_roles(role) #removes the role if user already has
      await ctx.send(f"Removendo {role} do {user.mention}")
  else:
      await user.add_roles(role) #adds role if not already has it
      await ctx.send(f"Adicioando {role} para {user.mention}") 


client.run('KEY')

