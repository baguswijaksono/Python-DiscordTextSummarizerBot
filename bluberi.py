from ast import arg
from email import message
from inspect import ArgSpec
from urllib.request import urlopen
import requests
from discord.ext import commands
import json
from signal import default_int_handler
from requests import delete, options
import discord
import os
import re

bot = commands.Bot(command_prefix='.') 
bot.remove_command('help')

@bot.command(name="sumarize")
async def msg(ctx, *args):
  message=' '
  for word in args:
    message+=word+' '
    w=message.replace('"','')
  r = requests.post(
    "https://api.deepai.org/api/summarization",
    data={
        'text': w,
    },
    headers={'api-key': '478cd374-ce66-4fcd-a1f9-b96527f62085'})
  x=(r.json())
  y=x['output']
  z=str(ctx.message.author.name)
  print(w)
  if (y==""):
    username=str(ctx.message.author.name)
    embed=discord.Embed(
    colour= discord.Colour.red()
            )
    embed.add_field(name="Failed to sumerize your text.",value="Sorry "+username+" It seems like you not entering the right text/paragraph.", inline=True)
    await ctx.send(embed=embed)

  else:
    embed=discord.Embed(
    title="Summarization Result: ",
    colour= discord.Colour.blue()
          )
    embed.add_field(name="Hi "+z+", Here sumary from text you send to me :). ",value=y, inline=True)
    await ctx.send(embed=embed)
  

@bot.command(name='about')
async def embed(ctx):
    embed=discord.Embed(
    title="Blueberry Discord Summarization Bot",
        description="Programmed With Python Programming Language 3.9.7",
        colour= discord.Colour.blue()
            )
    embed.set_footer(text="invite this bot using the link below https://bit.ly/bluberirusak")
    embed.set_image(url="https://cdn.discordapp.com/attachments/938105309283647499/938418384637394974/0_-_Copy.png")
    embed.set_author(name="Bagus Muhammad Wijaksono")
    await ctx.send(embed=embed)

@bot.command(name='help')
async def embad(ctx):
    embed=discord.Embed(
            title="General Command list.",
            colour= discord.Colour.blue()
            )
    embed.add_field(name='!help',value="Showing general command list", inline=False)
    embed.add_field(name='!Manual',value="Displays about how to use this bot.", inline=True)
    embed.add_field(name='!info',value="Display basic information about this stupid bot", inline=False)
    embed.add_field(name='Additional information:',value="the bot will automatically leave the voice channel when the music is finished playing and there are no more users on the voice channel.", inline=True)
    await ctx.send(embed=embed)
  
@bot.command(name='info')
async def embad(ctx):
    embed=discord.Embed(
        title="General Command list.",
            colour= discord.Colour.blue()
            )
    embed.add_field(name='information:',value="This bot will Reduces the size of a document/text by only keeping the most relevant sentences from it. This model aims to reduce the size to 20 percent of the original.", inline=True)
    await ctx.send(embed=embed)

@bot.command(name='manual')
async def embad(ctx):
    embed=discord.Embed(
            colour= discord.Colour.blue()
            )
    embed.add_field(name='How to use Blueberry Rusak Summarization Bot.',value="You can use this bot Using command $.sumarize <drop your text here> then wait until the bost send the sumarize of the txt that you send.", inline=False)
    embed.set_image(url="https://media.discordapp.net/attachments/940985050126745620/981434826429186048/Screenshot_from_2022-06-01_12-49-06.png")
    await ctx.send(embed=embed)
@bot.command(name='test_gagal')
async def embad(ctx):
    username=str(ctx.message.author.name)
    embed=discord.Embed(
    colour= discord.Colour.red()
                    )
    embed.add_field(name="Failed to play music.",value="Sorry "+username+" I didn't find the song you looking for, maybe because the keywords you entered are lifetream format or playlist.", inline=True)
    await ctx.send(embed=embed)


bot.run("OTM4NTQ4MDA1NjA5NTM3NjA2.GmYCNw.G1cvH937vS1UU3Hrbttmda8a1VCJ2Sv12VfolU")






