from discord.ext import commands
import discord as di
import crawling

TOKEN = "NzUxMDY2OTM3OTQ1MjI3MzM2.X1DrmA.Hkr_zeq2jK92OuKSLm3GRyER-EQ"
clinet = commands.Bot(command_prefix="/")

def insertL(data, j, k):
    st = ''
    for i in range(j, k):
        st = st + str(data[0][i]) + '　　　' + str(data[1][i]) + '\n'
    return st

@clinet.event
async def on_ready():
    print("Logged in as")
    print(clinet.user.name)
    print(clinet.user.id)
    print('--------------')

@clinet.command(name='채권')
async def display(ctx):
    data = crawling.crwaling()
    embed = di.Embed(colour=di.Colour.dark_gold())
    embed.set_author(name="채권")
    embed.add_field(name='옷감', value=insertL(data, 1, 5), inline=False)
    embed.add_field(name='가죽', value=insertL(data, 6, 10), inline=False)
    embed.add_field(name='목재', value=insertL(data, 11, 15), inline=False)
    embed.add_field(name='철 주괴', value=insertL(data, 16, 20), inline=False)

    await ctx.send(embed=embed)

clinet.run(TOKEN)

