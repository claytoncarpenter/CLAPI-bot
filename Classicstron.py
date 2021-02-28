import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is Ready!')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server')

@client.command()
async def test(ctx, arg):
    await ctx.send(arg)

@client.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)

@client.event
async def on_message(message):
    print(f'{message.author} has posted {message.content} on {message.channel}')
    message_record = f'\n{message.author}|{message.mentions}|{message.content}|{message.channel}|{message.created_at}'
    with open('document.csv','a') as fd:
        fd.write(message_record)

token_file = open(r"E:\Other\DiscordBot\token.txt", "r")
token = token_file.read()
token_file.close()

client.run(token)

#
# 
#  class MyClient(discord.Client):
#     async def on_ready(self):
#         print('Logged on as {0}!'.format(self.user))

#     async def on_message(self, message):
#         print('Message from {0.author}: {0.content}'.format(message))

# client = MyClient()
# client.run('ODE1MzI0MTkwMTM5MDg4OTI2.YDqv0g.HpgmyJpR7VuRJtBNKxCspOylq6k')