import discord, random
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
intents.message_content = True

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        await bot.tree.sync()
    
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('/RPS'):
            number = random.randint(1, 3)
            if number == 1:
                botPick = 1
                await message.channel.send('The Bot picked Scissors')
            elif number == 2:
                botPick = 2
                await message.channel.send('The Bot picked Stone')
            elif number == 3:
                botPick = 3
                await message.channel.send('The Bot picked Paper')
            else:
                print('Error in the randomizer')
            if message.content.startswith('/RPS Scissors') or message.content.startswith('/RPS scissors'):
                if botPick == 1:
                    await message.channel.send("It's a draw")
                elif botPick == 2:
                    await message.channel.send('You lost...')
                elif botPick == 3:
                    await message.channel.send('You won!')
                else:
                    print('Error')
            elif message.content.startswith('/RPS Stone') or message.content.startswith('/RPS stone'):
                if botPick == 1:
                    await message.channel.send('You won!')
                elif botPick == 2:
                    await message.channel.send("It's a draw")
                elif botPick == 3:
                    await message.channel.send('You lost...')
                else:
                    print('Error')
            elif message.content.startswith('/RPS Paper') or message.content.startswith('/RPS paper'):
                if botPick == 1:
                    await message.channel.send('You lost...')
                elif botPick == 2:
                    await message.channel.send('You won!')
                elif botPick == 3:
                    await message.channel.send("It's a draw")
                else:
                    print('Error')
            else:
                await message.channel.send('Sry cant use anything with a typo...')
        
        if message.content.startswith('/Cointoss'):
            coinflip = random.randint(1, 2)
            if coinflip == 1:
                await message.channel.send('Its... Heads!')
            elif coinflip == 2:
                await message.channel.send('Its... Tails!')
            else:
                await message.channel.send('Error')
        
        if message.content.startswith('/Diceroll'):
            dice = random.randint(1, 6)
            await message.channel.send("It's a " + str(dice))
        

client = MyClient(intents=intents)

client.run('NothingToSeeHere')
