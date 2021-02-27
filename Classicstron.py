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

client.run('ODE1MzI0MTkwMTM5MDg4OTI2.YDqv0g.HpgmyJpR7VuRJtBNKxCspOylq6k')

#
# 
#  class MyClient(discord.Client):
#     async def on_ready(self):
#         print('Logged on as {0}!'.format(self.user))

#     async def on_message(self, message):
#         print('Message from {0.author}: {0.content}'.format(message))

# client = MyClient()
# client.run('ODE1MzI0MTkwMTM5MDg4OTI2.YDqv0g.HpgmyJpR7VuRJtBNKxCspOylq6k')