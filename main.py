import os
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We zijn ingelogt als {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!rooster'):
      await message.channel.send('https://sa-davinci.xedule.nl')
    if message.content.startswith('Homo') or message.content.startswith('homo'):
      await message.channel.send('*__**Je bent zelf een homo**__*')  
    if message.content.startswith('!pablo'):
      await message.channel.send('https://www.youtube.com/watch?v=tJpSVqmG27I')
    if message.content.startswith('!codeaura'):
      await message.channel.send('Thank me later voor code')
      await message.channel.send('https://github.com/CodeAura')
    if message.content.startswith('!sus'):
      await message.channel.send('https://youtu.be/Regpv0xU3ZQ')
    if message.content.startswith('!shishalounge'):
      await message.channel.send('Niet zo poffen g')
    if message.content.startswith('!noob'):
      await message.channel.send('https://youtu.be/uKWcIaJtS6Q')
    if message.content.startswith('!speedrun'):
      await message.channel.send("Gotta go FASTTTTTTTTTTTTTTTTTTTTTTT")
      await message.channel.send('https://youtu.be/Jb9Ebe_rA8M')
    if message.content.startswith('!help'):
      await message.channel.send(embed = embed)
    if message.content.startswith('Thuisbezorgd'):
      await message.channel.send('wat wil je bestellen abi je eigen poep ofz')
    if message.content.startswith('!crypto'):
      await message.channel.send('**Zakenman hiero. Wacht ik help wel...**')
      await message.channel.send('https://coinmarketcap.com')
      await message.channel.send('Als je winst maak maak het over naar NLINGB92232837298183 thanks')
    if message.content.startswith('balls'):
      await message.channel.send('ballz in yo jawz')
    if message.content.startswith('jo'):
      await message.content.send("https://thumbs.gfycat.com/AppropriateClassicCommongonolek-size_restricted.gif")
    if message.content.startswith('!codeaura'):
      await message.content.send("Thank me later voor code!")
      await message.content.send("https://github.com/CodeAura")

embed=discord.Embed(title="Gimmy Neutron Commands!", description="You still need help big noob", color=0xff0000)
embed.set_thumbnail(url="https://media.discordapp.net/attachments/483325612899958796/940237457968992276/cc3ad6d1-5204-407d-a077-c39940fcf610.png?width=864&height=669")
embed.add_field(name="!crypto", value="`Shows Marketing`", inline=True)
embed.add_field(name="!speedrun", value="`Speedrunning man`", inline=True)
embed.add_field(name="!sus", value="`Among us ඞ`", inline=True)
embed.add_field(name="!noob", value="`You a big noob`", inline=True)
embed.add_field(name="!codeaura", value="`check me github hier`", inline=True)
embed.add_field(name="!pablo", value="`Pablo tutututu`", inline=True)
embed.add_field(name="!rooster", value="`Check het rooster hier!`", inline=True)
embed.set_footer(text="Gimmy Neutron | Mikee#1009")


client.run(os.getenv('TOKEN'))