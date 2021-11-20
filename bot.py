import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '#')

@client.event
async def on_ready():
    print('bot is ready.')

@client.event
async def on_message(message):

    if  message.author == client.user:
        return

    if message.content == 'hello':
     await message.channel.send('welcome to niyas server')
     
    elif message.content =='what is your name':
        await message.channel.send('my name is helper')
        
    elif message.content == 'rules':
        await message.channel.send('1.Do not organize, participate in, or encourage harassment of others.\n')
        await message.channel.send('2.Do not organize, promote, or coordinate servers around hate speech.\n')
        await message.channel.send('3.Do not make threats of violence or threaten to harm others.\n')
        await message.channel.send('4.Do not evade user blocks or server bans.\n')
        await message.channel.send('5.Do not send others viruses or malware,\n')
        await message.channel.send('6.You may not share content that glorifies or promotes suicide or self-harm\n')
        await message.channel.send('7.You may not share images of sadistic gore or animal cruelty.\n')
        await message.channel.send('8. you should not promote, encourage or engage in any illegal behavior. \n')
        await message.channel.send('9.You may not spam Discord\n')
    elif message.content == 'games':
        await message.channel.send('1.super mario./n')
        await message.channel.send('2.stick merge./n')
        await message.channel.send('3.stick man hook./n')
        await message.channel.send('4.3d arena racing./n')
        await message.channel.send('5.moto x3m ./n')
    elif message.content == 'super mario':
        await message.channel.send(' https://supermario-game.com/')
    elif message.content == 'stick merge':
        await message.channel.send(' https://poki.com/en/g/stick-merge')
    elif message.content == 'stick man hook':
        await message.channel.send('https://poki.com/en/g/stickman-hook')
    elif message.content == '3d arena racing':
        await message.channel.send('  https://poki.com/en/g/3d-arena-racing')
    elif message.content == 'moto x3m':
        await message.channel.send('https://poki.com/en/g/moto-x3m')
    elif message.content ==  'how are you':
        await message.channel.send('i am fine')
        
    elif message.content == ' help':
        await message.channel.send('contact to customer care./n')

    else:
     await message.channel.send('i cant ans u r question')
    
     
@client.event
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send(F'{user} reacted with {reaction.emoji}')
    
@client.event
async def on_message_edit (before, after):
    await before.channel.send(
        f'{before.author} edit a message.\n'
        f'Before: {before.content}\n'
        f'After: {after.content}'
  )

client.run('OTAwMjY2OTYzMjY2MzEwMTY0.YW-08g.lfyUQb1oJ7mMg0S1F7xjcAoTtS0')
