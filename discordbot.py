import discord
from discord.ext import commands
import random
import threading

#Setting Variables
annoyQwapy = 'https://i.imgur.com/pB218JW.png <@267038519057317889>'
annoyingWords = ['<:Qwapy:746174714367705120>', ':Qwapy:', '<@267038519057317889>', '@Qwapy']
command_prefix = 'q.'
Token = "None of Your Buisness"
client = commands.Bot(command_prefix = 'q.')
currentTime = 59
leaderID = [267038519057317889, 310946266911735808]



#Normal commands vvvvvvv

@client.command()
async def Annoy(ctx): #annoys qwapy daily
    if str(ctx.message.author.id) in users:
        if int(users[users.index(str(ctx.message.author.id)) + 3]) +60 > currentTime:
            await ctx.send("You must wait "+ str(int(users[users.index(str(ctx.message.author.id)) + 3]) + 60 - currentTime) +" minute(s) to do this command again!")
        else:
            await ctx.send(annoyQwapy)
            users[users.index(str(ctx.message.author.id)) + 3] = str(currentTime)
            updateCount(ctx.message.author.id)
            strVal, ranVal = updateMoney(ctx.message.author.id)
            await ctx.send(strVal + " You got " + str(ranVal) +" QBucks!")
    else:
        await ctx.send("You have yet to annoy <@267038519057317889> / create an account. Type :Qwapy: to start!")



@client.command()
async def Count(ctx): #outputs annoy count
    if str(ctx.message.author.id) not in users:
        await ctx.send("You have yet to annoy <@267038519057317889>. Type :Qwapy: to start!")
    else:
        await ctx.send("You have annoyed Qwapy "+ users[users.index(str(ctx.message.author.id)) + 1] + " times!")



@client.command()
async def Bal(ctx): #outputs wealth
    if str(ctx.message.author.id) not in users:
        await ctx.send("You have yet to annoy <@267038519057317889>. Type :Qwapy: to start!")
    else:
        await ctx.send("You have "+users[users.index(str(ctx.message.author.id)) + 2] +" QBucks")


   
@client.command()
async def Flip(ctx, amount : int):
    if str(ctx.message.author.id) not in users:
        await ctx.send("You have yet to annoy <@267038519057317889>. Type :Qwapy: to start!")
    else:
        if (int(users[users.index(str(ctx.message.author.id)) + 2]) < amount):
            await ctx.send("You do not have enough QBucks for that much!")
        else:
            users[users.index(str(ctx.message.author.id)) + 2] = str(int(users[users.index(str(ctx.message.author.id)) + 2]) - amount)
            ranFlip = random.randint(1,2)
            if ranFlip == 1:
                await ctx.send("You lost! You now have "+ users[users.index(str(ctx.message.author.id)) + 2] + " QBucks")
            else:
                users[users.index(str(ctx.message.author.id)) + 2] = str(int(users[users.index(str(ctx.message.author.id)) + 2]) + (amount*2))
                await ctx.send("You won! You now have "+ users[users.index(str(ctx.message.author.id)) + 2] + " QBucks")
            setFile()



@client.command()
async def Userbal(ctx, userID : int):
    if str(userID) not in users or userID < 10000000000000:
        await ctx.send("They have yet to annoy <@267038519057317889>. Type :Qwapy: to start!")
    else:
        await ctx.send("They have "+users[users.index(str(userID)) + 2] +" QBucks")



@client.command()
async def Commands(ctx): #gives list of bot commands
    embed = discord.Embed(
        title = 'Commands:',
        description = '''Use the prefix 'q.' followed by the command''',
        colour = discord.Colour.blue()
    )

    embed.set_footer(text='Made by Qwapy')
    embed.set_thumbnail(url='https://i.imgur.com/pB218JW.png')
    embed.set_author(name='Qwapy Bot', icon_url='https://i.imgur.com/pB218JW.png')
    embed.add_field(name='Admin', value ='Displays all admin commands', inline = False)
    embed.add_field(name='Annoy', value ='An hourly command to annoy <@267038519057317889>', inline = False)
    embed.add_field(name='Bal', value ='Displays your current balance', inline = False)
    embed.add_field(name='Commands', value ='Displays all commands', inline = False)
    embed.add_field(name='Count', value ='''Displays the amount of times you've annoyed <@267038519057317889>''', inline = False)
    embed.add_field(name='Flip <amount>', value ='''Gambles <amount> QBuck(s) for a 50/50 chance to win''', inline = False)
    embed.add_field(name='Store', value ='Displays all Store commands to redeem your QBucks', inline = False)
    embed.add_field(name='Userbal <userID>', value ='''Displays the <userID>'s balance.''', inline = False)

    await ctx.send(embed=embed)




#Store commands below vvvvv

@client.command()
async def Store(ctx):
    embed = discord.Embed(
        title = 'Store Commands:',
        description = '''Use the prefix 'q.' followed by the command''',
        colour = discord.Colour.blue()
    )

    embed.set_footer(text='Made by Qwapy')
    embed.set_thumbnail(url='https://i.imgur.com/pB218JW.png')
    embed.set_author(name='Qwapy Bot', icon_url='https://i.imgur.com/pB218JW.png')

    await ctx.send(embed=embed)



#Admin commands below vvvvv


@client.command()
async def Admin(ctx):
    if ctx.message.author.id not in leaderID:
        await ctx.send("You do not have the permissions for this command, consult <@267038519057317889>")
    else:
        embed = discord.Embed(
            title = 'Admin Commands:',
            description = '''Use the prefix 'q.' followed by the command ''',
            colour = discord.Colour.blue()
        )

        embed.set_footer(text='Made by Qwapy')
        embed.set_thumbnail(url='https://i.imgur.com/pB218JW.png')
        embed.set_author(name='Qwapy Bot', icon_url='https://i.imgur.com/pB218JW.png')
        embed.add_field(name='Admin', value ='Displays all Admin commands', inline = False)
        embed.add_field(name='Clear <amount>', value ='Clears <amount> messages', inline = False)
        embed.add_field(name='Clearall', value ='Clears all messages (hopefully)', inline = False)
        embed.add_field(name='Give <userID> <amount>', value ='Gives the <userID> <amount> QBucks', inline = False)
        embed.add_field(name='Stop', value ='Stops the bot', inline = False)

        await ctx.send(embed=embed)



@client.command()
async def Clear(ctx, amount: int):
    if ctx.message.author.id in leaderID:
        await ctx.channel.purge(limit=amount)
    else:
        await ctx.send("You do not have the permissions for this command, consult <@267038519057317889>")

@client.command()
async def Clearall(ctx,):
    await ctx.channel.purge(limit = 100000)


@client.command()
async def Give(ctx, userID : str, amount : int):
    if ctx.message.author.id == 267038519057317889:
        if userID not in users or userId < 100000000000000:
            await ctx.send("This person has yet to create an account")
        else:
            await ctx.send(users[users.index(str(userID)) + 2])
            users[users.index(str(userID)) + 2] = str(int(users[users.index(str(userID)) + 2]) + amount)
            await ctx.send(users[users.index(str(userID)) + 2])
    else:
        await ctx.send("You do not have the perms!")


@client.command()
async def Stop(ctx): #stops bot
    if ctx.message.author.id == 267038519057317889:
        await ctx.send('Cya') 
        exit()
    else:
        await ctx.send("You do not have the permissions for this command, consult <@267038519057317889>")




#Error commands below vvvvvvv

@Flip.error
async def flipError(ctx):
    await ctx.send("""Invalid input please try again. Type "q.Flip <amount>" to make sure it works!""")
        
@Userbal.error
async def userbalError(ctx):
    await ctx.send("""Invalid input please try again. Type "q.Userbal <userID>" to make sure it works!""")

@Clear.error
async def clearError(ctx):
    await ctx.send("""Invalid input please try again. Type "q.clear <amount>" to make sure it works!""")





#Event commands below vvvvvv

@client.event
async def on_ready(): #called on startup
    print("Bot Online")
    channel = client.get_channel(746399272282357870)
    await channel.send('Bot Online')
    await client.change_presence(activity=discord.Game(':Qwapy:'))



@client.event
async def on_command_error(ctx,error):
    pass



@client.event
async def on_message(message):
    #update how many times has annoying stuff
    for currentAnnoy in range(len(annoyingWords)):
        if annoyingWords[currentAnnoy] in message.content:
            updateCount(message.author.id)
            break;

    #checks for commands (and puts in non-case sensitive modes)
    if message.author.id != client.user.id and message.channel.id == 746399272282357870:
        message.content = message.content.lower()
        message.content = ''.join([message.content[:2], message.content[2].upper(), message.content[3:]])
        await client.process_commands(message)



#Normal commands belw vvvvvvvvv
def updateCount(userID): #updates count
    if str(userID) not in users: #creates new user
        users.append(str(userID)) #UserId
        users.append(str(1)) #times you've annoyed Qwapy
        users.append(str(0)) #money amount
        users.append(str(-1)) #time
        setFile()
    else: 
        users[users.index(str(userID)) + 1] = str(int(users[users.index(str(userID)) + 1]) + 1)
        setFile()



def updateMoney(userID): #random amount of money given
    strval = ''
    ranVal = random.randint(0,100)
    if ranVal <= 50 and ranVal >= 0:
        ranval = random.randint(0,150)
        strVal = 'You got a 1/2 chance!'
    elif ranVal > 50 and ranVal <=70:
        ranVal = random.randint(150,300)
        strVal = 'You got a 1/4 chance!'
    elif ranVal > 70 and ranVal<=95:
        ranVal = random.randint(300,600)
        strVal = 'You got a 1/5 chance!'
    elif ranVal>95 and ranVal!=100:
        ranVal = random.randint(600,1000)
        strVal = 'You got a 1/20 chance!'
    elif ranVal ==100:
        ranVal = random.randint(1000,2000)
        strVal = 'You got a 1/100 chance!'
        
    #sets money
    users[users.index(str(userID)) + 2] = str(int(users[users.index(str(userID)) + 2]) + ranVal)
    setFile()
    return strVal,ranVal



def getTime():#gets current day every 60 seconds
    global currentTime
    currentTime += 1
    threading.Timer(60, getTime).start()
    saveFileTime()



def getFileTime(): #gets time from file
    timeCount = open("Time.txt","r")
    for line in timeCount:
        returnVal = int(line.rstrip('\n'))
    return returnVal



def saveFileTime(): #saves time to file
    timeCount = open("Time.txt","w")
    timeCount.write(str(currentTime))
    timeCount.close()



def readFile(): #gets user data from file
    returnUsers = []
    annoyCount = open("Scores.txt","r")
    for line in annoyCount:
        returnUsers.append(str(line.rstrip('\n')))
    annoyCount.close()
    print(returnUsers)
    return returnUsers



def setFile(): #sets user data into file
    annoyCount = open("Scores.txt","w") #writing the leaderboards
    for currentPos in range(len(users)):
        annoyCount.write(str(users[currentPos])+"\n")
    annoyCount.close()




#Running program vvvv

currentTime = getFileTime()
getTime()
users = readFile()
client.run(Token)


