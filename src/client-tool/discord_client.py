#Needs to be compiled into pyinstaller package as well
import discord;from sys import argv
try:
    user_or_channel = argv[1]
    idd = argv[2]
except Exception:
    exit()
blob = str(argv)
blob = blob.replace(",", "").replace('"', "").replace("'", "").replace("[", "").replace("]", "")
message = blob.replace(f"{blob.split()[0]} {blob.split()[1]} {blob.split()[2]} ", "")
client=discord.Client() 
@client.event 
async def on_ready():
    if user_or_channel == "--user":
        user = client.get_user(int(idd))
        await user.send(message)
        exit()
    if user_or_channel == "--channel":
        channel = client.get_channel(int(idd))
        await channel.send(message)
        exit()
try:client.run('SDFG1MTc3NzU0NjQzNTk1Mjg0.XdJNNQ.u98lYK7MHLUH4FaU3yduXE_nDO4')
except Exception as E:
    #print(str(E))
    exit()
