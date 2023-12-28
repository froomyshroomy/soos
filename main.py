
import os
import difflib
import sqlite3
#db = sqlite3.connect('poke2auto.db')
#cur = db.cursor()
global count
f = open('pokes.txt', 'r')
file = f.read()
file = file.split('\n')
for i in file:
    if len(i) < 2:
        del file[file.index(i)]
mon_list = []
for i in file:
    if len(i) >= 3:
        mon_list.append(i)
import discord
from discord.ext import commands
from discord.ext import tasks
import asyncio
from keep_alive import keep_alive
import requests
from discord_webhook import DiscordWebhook
cid = 1151929107509162058
token = os.environ['tok'] #Don't paste your token here 
editing = {

}
req = requests.get("https://discord.com/api/path/to/the/endpoint")

print(req)
import time
#mon_url=input('url')
gg = open('caught.txt', 'a')
import random
#cid = 1098872258799357962
client = commands.Bot(command_prefix='&')
client._skip_check = lambda x, y: False
@tasks.loop(seconds=0.2)
async def spammer():
  text_channel = client.get_channel(cid)
 # print(text_channel)
  if text_channel != None:
   # words = ["gaeming","om","ap","harry","nato"]
    #print(x)
    num = random.randint(1,10000000000000000000000000)
    await text_channel.send(num)
    intervals = [6, 6.7, 6.6, 6.5, 6.4, 6.3, 6.2, 6.8, 6.9]
    await asyncio.sleep(random.choice(intervals))

@client.command()
async def catchrate(ctx):

  print(count)

  catch_rate = count/60
  await ctx.send(f'the catch rate is {catch_rate} mons per minute')

@tasks.loop(seconds=14400)
async def sleeper():
  print(count)
  spammer.catchrate()
  time.sleep(seconds = 7200)
  spammer.start()
#pokes = ['pikachu','charixadd','swellow','pidove',input('option')]
spam_process = spammer.start()
hint = ""

hint = ""
@client.event
async def on_message(message):
      
      
      def check(m):
          return m.channel == message.channel and m.author != client.user and "The pokémon is" in m.content

      global hint

   
    #if "The pokémon is" in message.content:
      #await message.delete()
      embeds = message.embeds # return list of embeds
    #print("tes")
      if not message.embeds:
        await client.process_commands(message)
        return
      title = (embeds[0].to_dict()['title'])
    #print(title)
   
      if "pokémon has appeared" in title:
        hint = ""
        
        m = await message.channel.send("<@716390085896962058> h")
        time.sleep(4)
        
        while True:
          response = await client.wait_for('message', check = check, timeout=300) 
          if "The pokémon is" in response.content:
            break
        
      s = response.content.split(" is ")[1].replace(".","")
      #response.delete()
      print(s)
      x = get_mon(s)
      #print(options)
      print(x)
      gg.writelines(x)
      first_options = x
      for i in first_options:
        await message.channel.send(" <@716390085896962058> c "+i)
        time.sleep(4)
        if 'human' in response.content:
          stop(spam_process)
       
         


      
      

        
      
      #print(val)
         

    

def get_mon(val):
  
 
  

  val = val.lower()
  while "\_" in val:
      val = val.replace("\_", "-")
        #print(val)
  length = len(val)
  l = list(val)
  new_chars = []
  
  
  with open('pokes.txt') as f:
       lines = [line.rstrip() for line in f]
  new_names = []
  for i in lines:
    if len(i) == length:
      new_names.append(i)
  #print(new_names)
  final_list = []
  for i in new_names:
    name_list = list(i)
    index = 0
    #print(i)

    flag = False
    for k in l:
      if name_list[index] != k and k != "-":
       # print(name_list[index]+"!="+k)
        flag = True
      index = index+1
    if not flag:
      final_list.append(i)
  #print(final_list)
  return final_list
        



@client.command()
async def stop(ctx):
    spammer.stop()

@client.command()
async def spam(ctx):
  spammer.start()

@client.command()
async def say(ctx, *, args):
 
  
 
  await ctx.send(args)

keep_alive()
try:
  client.run(token,bot=False)
except:
  os.system("kill 1")
   