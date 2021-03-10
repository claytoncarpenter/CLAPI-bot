import discord
from discord.ext import commands, tasks
import database
import visualization

# class timer(commands.Cog):
#     def __init__(self):
#         self.index = 0
#         self.printer.start()

#     @tasks.loop(seconds=5.0)
#     async def printer(self):
#         print(self.index)
#         self.index += 1

# timekeep = timer()

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Logged on as {0}!'.format(client.user))
    # await timekeep.printer()

@client.command()
async def test(ctx):
    visualization.bar_plot(ctx.guild.name)
    await ctx.send(file=discord.File(r'plots\barplot.png'))

@client.command()
async def test2(ctx):
    print('test2')
    pass

@client.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)

@client.event
async def on_message(message):
    print(f'{message.author.name} has posted {message.content} on {message.channel.name}')
    database.insert_message(message.id,message.author.name, message.author.id, message.author.bot, message.content,message.guild.name,message.channel.name,message.created_at)
    await client.process_commands(message)

token_file = open(r"E:\Other\DiscordBot\token.txt", "r")
token = token_file.read()
token_file.close()

client.run(token)

client.add_command(test)


#
# 
#  class MyClient(discord.Client):
#     async def on_ready(self):
#         

#     async def on_message(self, message):
#         print('Message from {0.author}: {0.content}'.format(message))

# client = MyClient()
# client.run('ODE1MzI0MTkwMTM5MDg4OTI2.YDqv0g.HpgmyJpR7VuRJtBNKxCspOylq6k')


#channels = client.get_all_channels
#channel = discord.utils.get(client.guilds, name="For The Horde")
#print(channel)