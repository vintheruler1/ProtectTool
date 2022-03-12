from os import ctermid, times
from pickletools import read_unicodestring1
from sqlite3 import Timestamp
from tkinter import dnd
from tracemalloc import stop
import nextcord
from nextcord import Interaction
from nextcord.ext import commands
from nextcord import Intents

import traceback
import sys

import timedelta

import asyncio

import datetime
from datetime import datetime

import humanfriendly

from colorama import Fore

from urllib.parse import quote_plus

import ssl
from numpy import True_
import requests
from requests import get

import re
from re import *

intents = nextcord.Intents.default()

intents.members = True
intents.presences = True
intents.messages = True

bot = commands.Bot(command_prefix = commands.when_mentioned_or("!"), intents=intents, case_insensitive=True)

bot.remove_command('help')

serverIDS = []
scamLinks = ['https://formulary-moderators-new.com/', "https://disocrde.gift/FverABbCacD", "https://disocrde.gift/BFerDhAbECvcW", 'https://discord.hypesquad-usa.repl.co/event.html', "https://academy-moderator-forms.com/", "https://su.s/", "https://iron-nitro.com/welcome"]
counter = 0


@bot.command()
async def testing(ctx):
    await ctx.reply("Testing!")
    
@bot.slash_command(name="help", description="View help commands.", guild_ids=serverIDS)
async def help(interaction : Interaction):
    class Dropdown(nextcord.ui.Select):
        def __init__(self):

            # Set the options that will be presented inside the dropdown
            options = [
                nextcord.SelectOption(label='Anti-Phish', description='View commands that can customize preventing scams and phishing links.', emoji='🚫'),
                #nextcord.SelectOption(label='Anti-Raid/Nuke', description='View commands to turn on or off Anti-Raid/Nuke', emoji='💣'),
                #nextcord.SelectOption(label='Moderation', description='View commands that can help moderate your server.', emoji='🔨'),
            ]

            # The placeholder is what will be shown when no option is chosen
            # The min and max values indicate we can only pick one of the three options
            # The options parameter defines the dropdown options. We defined this above
            super().__init__(placeholder='Choose your favourite colour...', min_values=1, max_values=1, options=options)

        async def callback(self, interaction: nextcord.Interaction):
            # Use the interaction object to send a response message containing
            # the user's favourite colour or choice. The self object refers to the
            # Select object, and the values attribute gets a list of the user's 
            # selected options. We only want the first one.
            if interaction.user.name == interaction.user.name:
                if self.values[0] == "Anti-Phish":
                    await interaction.response.send_message(f'anti phish', ephemeral=True)
            else:
                await interaction.response.send_message('This is not for you!', ephemeral=True)
            
            
        class DropdownView(nextcord.ui.View):
            def __init__(self):
                super().__init__()

                # Adds the dropdown to our view object.
                self.add_item(Dropdown())
        view = DropdownView()
    await interaction.response.send_message("help commands")
         
@bot.command()
async def help(ctx):
    class Dropdown(nextcord.ui.Select):
        def __init__(self):

            # Set the options that will be presented inside the dropdown
            options = [
                nextcord.SelectOption(label='Anti-Phish', description='View commands that can customize preventing scams and phishing links.', emoji='🚫'),
                #nextcord.SelectOption(label='Anti-Raid/Nuke', description='View commands to turn on or off Anti-Raid/Nuke', emoji='💣'),
                #nextcord.SelectOption(label='Moderation', description='View commands that can help moderate your server.', emoji='🔨'),
            ]

            # The placeholder is what will be shown when no option is chosen
            # The min and max values indicate we can only pick one of the three options
            # The options parameter defines the dropdown options. We defined this above
            super().__init__(placeholder='Choose your favourite colour...', min_values=1, max_values=1, options=options)

        async def callback(self, interaction: nextcord.Interaction):
            # Use the interaction object to send a response message containing
            # the user's favourite colour or choice. The self object refers to the
            # Select object, and the values attribute gets a list of the user's 

                if self.values[0] == "Anti-Phish":
                    embed = nextcord.Embed(
                        title="Anti-Phish Commands",
                        description="There is no commands for Anti-Phish as the module is auto enabled.",
                        color=0x2f3136
                    )
                    await interaction.response.send_message(embed=embed, ephemeral=True)
                #elif self.values[0] == "Anti-Raid/Nuke":
                    #embed = nextcord.Embed(
                        #title="Anti-Raid/Nuke",
                        #description="Set diff"
                    #)
                    #await interaction.response.send_message(f'anti nuke', ephemeral=True)
                #elif self.values[0] == "Moderation":
                    #await interaction.response.send_message(f'moderation', ephemeral=True)
            
    class DropdownView(nextcord.ui.View):
        def __init__(self):
            super().__init__()

            # Adds the dropdown to our view object.
            self.add_item(Dropdown())
    view = DropdownView()
    await ctx.send("Testing", view=view)
    
@bot.command()
async def query(ctx, *, query):
    class Google(nextcord.ui.View):
        def __init__(self, query: str):
            super().__init__()
            # we need to quote the query string to make a valid url. nextcord will raise an error if it isn't valid.
            query = quote_plus(query)
            url = f'https://www.google.com/search?q={query}'

            # Link buttons cannot be made with the decorator
            # Therefore we have to manually create one.
            # We add the quoted url to the button, and add the button to the view.
            
            self.add_item(nextcord.ui.Button(label='Click Here', url=url))
    await ctx.send(f'Your Google Result for: `{query}`', view=Google(query))
    
@bot.command()
async def invite(ctx):
    class Invite(nextcord.ui.View):
        def __init__(self):
            super().__init__()
            url = f"https://discord.com/api/oauth2/authorize?client_id=950528649046675467&permissions=8&scope=bot%20applications.commands"
            self.add_item(nextcord.ui.Button(label='Invite Link', url=url))
    embed = nextcord.Embed(
        title="Invite Me",
        description="Click the button below to invite me to your server! Thanks for choosing GelbieProtect!"
    )
    view = Invite()
    await ctx.send(embed=embed, view=view)



@bot.event
async def on_message(message):
    #print(message.created_at)
    #print(datetime.fromisoformat('{}+00:00'.format(datetime.utcnow())))
    #print(message.created_at) - datetime.fromisoformat('{}+00:00'.format(datetime.utcnow()))
    
    
    #def _check(m):
        #var = datetime.fromisoformat('{}+00:00'.format(datetime.utcnow()))
        #var2 = message.created_at
        #diff = (var2 - var)
        #seconds = diff.total_seconds()
       # return (m.author == message.author
      #          and len(m.mentions)
     #           and seconds < 30)
        
    #if not message.author.bot:
        #if message.author.guild_permissions.administrator:
        #    return
        #else:
           # try:
#                if len(list(filter(lambda m: _check(m), bot.cached_messages))) >= 5:
#                    await message.channel.send("Please do not mention more than 5 people!")
#            except Exception as e:
#                pass
    try:
        match = re.match("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", message.content).group(0)
        if match:
            resp = requests.get(match)
            resssp = resp.url
            if resssp == match:
                    print("not equal to?")
                    return
            elif resssp != match:
                    embed = nextcord.Embed(
                        title="<a:weewoo:951883123170365490> Link Shortened!",
                        description=f"The link has been shortened! The real link that is unshortened is: `{resssp}` \n\n[Jump to Message]({message.jump_url})\n\n Proceed with caution at your own risk.",
                        color=0x2f3136,
                        timestamp=datetime.utcnow()
                    )
                    await message.channel.send(embed=embed)
                
        try:
                    match = re.match("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", message.content).group(0)
                    response = requests.get(f'{match}', verify=True)
                    print('gotten')
        except Exception as e:
                    print('e')
                    await message.channel.send("This is not SSL Certified!!!!")
        else:
                    print("SSL Certified")
                    pass
            
            #shortnerChecker = get_real_url_from_shortlink("https://eee.py") 
            #sslCertificate = ssl_certificate('https://amongussussssss.py')

            #https://discord.com/channels/267624335836053506/343944376055103488/951634087884492881
    except Exception as e:
        pass
    msg = message.content.split()
    for scam in scamLinks:
        if scam in msg:
            try:
                class Confirm(nextcord.ui.View):
                    def __init__(self):
                        super().__init__()
                        self.value = None

                    # When the confirm button is pressed, set the inner value to `True` and
                    # stop the View from listening to more input.
                    # We also send the user an ephemeral message that we're confirming their choice.
                    @nextcord.ui.button(label='Report Fake Link', style=nextcord.ButtonStyle.red, disabled=False)
                    async def report(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
                        button.disabled=True
                        channel = bot.get_channel(951913409123848242)
                        await channel.send(f"**------------------------------------------**\n\n<@&951610263055003678> \nA scam link has been reported as fake.\nUser who sent scam: {message.author}\n\nThe URL is: `{message.content}` and the reporter is `{interaction.user}, {interaction.user.id}`.\n\nIf this is fake, please contact a developer and they will remove the link ASAP.")
                        await interaction.response.send_message("The link has been reported to an Administrator. Thank you for reporting this.", ephemeral=True)
                        self.value = True
                        self.stop()
                        scamEmbed = nextcord.Embed(
                            title="<a:weewoo:951883123170365490> Scam Found",
                            description="A scam link has been identified and has been deleted for your saftey.\n\nIf you think that this is a fake link, please click the **Red** Button below.\n\nScam sent by: `{}, {}`\n\nThis link was reported by {}.".format(message.author, message.author.id, interaction.user.name),
                            timestamp=datetime.utcnow(),
                            color=0x2f3136
                        )
                        await interaction.message.edit(embed=scamEmbed, view=self)
                        
                        
                        
                await message.delete()
                view = Confirm()
                scamEmbed = nextcord.Embed(
                    title="<a:weewoo:951883123170365490> Scam Found",
                    description="A scam link has been identified and has been deleted for your saftey.\n\nIf you think that this is a fake link, please click the **Red** Button below.\n\nScam sent by: `{}, {}`".format(message.author, message.author.id),
                    color=0x2f3136
                )
                await message.channel.send(embed=scamEmbed, view=view)
                pass
                return
            except Exception as e:
                print(e)
                pass
    
    await bot.process_commands(message)



@bot.event
async def on_connect():
    print("Bot connected")
    for guild in bot.guilds:
        serverIDS.append(guild.id)
    await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.listening, name="to potential scam links. | /help | Blocked over 200 scam links."), status=nextcord.Status.idle)
    bot.add_startup_application_commands()
    await bot.rollout_application_commands()

inital_extensions = []


if __name__ == '__main__':
    for extension in inital_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(Fore.YELLOW + f'Failed to load extension {extension}', file=sys.stderr)
            traceback.print_exc()



bot.run("OTUwNTI4NjQ5MDQ2Njc1NDY3.YiaOyQ.NOQ3BRIOSEoeEs3IlAnlrGCEqaA")
