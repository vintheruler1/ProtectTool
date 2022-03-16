from os import ctermid, times
from pickletools import read_unicodestring1
from sqlite3 import Timestamp
from tracemalloc import stop
import nextcord
from nextcord import Embed, Interaction, slash_command
from nextcord.ext import commands
from nextcord.ext.commands import Greedy
from nextcord import Intents
from nextcord.utils import utcnow
from nextcord.ext.commands import Bot, Cog

import traceback
import sys
from pandas import describe_option

import timedelta

import asyncio

import datetime
from datetime import *

import subprocess

import humanfriendly

from colorama import Fore

from urllib.parse import quote_plus, uses_relative

import ssl
from numpy import True_
import requests
from requests import get

import re
from re import *

import psutil
import platform

intents = nextcord.Intents.default()

intents.members = True
intents.presences = True
intents.messages = True

bot = commands.Bot(command_prefix = commands.when_mentioned_or("!"), intents=intents, case_insensitive=True)

bot.remove_command('help')

serverIDS = []
with open('./databases/scams.txt', 'r') as f:
    read = f.read().splitlines()
    
with open('./databases/stats.txt', 'r') as f:
    reading = f.read().splitlines()
    
counter = 0

def embed(title, description):
    embed=nextcord.Embed(title=f"{title}", description=f"{description}", color=0x2f3136, timestamp=datetime.now())
    return embed

@bot.command(aliases=['stats'])
async def info(ctx):
        ram_usage = psutil.virtual_memory().percent
        cpu_usage = round(psutil.cpu_percent())
        operating_system = platform.system()
        embed=nextcord.Embed(title="Information", 
                             description=
                             f"""
                             Bot Name: **{bot.user.name}**
                             Bot Id: `{bot.user.id}`
                             
                            I am in: `{len(bot.guilds)}` guilds/servers.
                            Watching over: `{len(bot.users)}` users.
                            
                            Version: **v0.1 BETA Release**
                             
                             Ping: `{round(bot.latency * 1000)}`ms
                             
                             ```yaml
RAM Usage: {ram_usage}%/100%
CPU Usage: {cpu_usage}%/100%
Platform System: {operating_system} or {sys.platform}
Platform Release: {platform.release()}
                             ```
                             
                             ```yaml
Python Version: {platform.python_version()}
Nextcord Version: {nextcord.__version__}
                             ```
                             Made and Maintained by: **AutureSystems, \nGelbieBots, and Vintheruler1#7617**
                             """,
                             color=0x2f3136)
        await ctx.send(embed=embed)

@bot.slash_command(name="reportfake", description="Report a fake link!", guild_ids=serverIDS)
@commands.cooldown(1, 5, commands.BucketType.user)
async def reportfake(interaction : Interaction, link:str):
    chan = bot.get_channel(953427059865161738)
    embed = nextcord.Embed(
        title="Fake Link Reported",
        description=f"{interaction.user} (`{interaction.user.id}`) has reported a fake link.\nLink: `{link}`\n\nIf this link is fake, please contact a developer that can edit the database.",
        color=0x2f3136, 
        timestamp=datetime.now()
    )
    await chan.send(embed=embed)
    await interaction.response.send_message("I have reported the link to a moderator. Thank you.", ephemeral=True)
    
@bot.command(aliases=["setdelay", "slowdown", "typingspeed"], description="Set the slowmode for the following channel in **seconds**")
@commands.has_permissions(manage_channels=True)
@commands.bot_has_permissions(manage_channels=True)
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.guild_only()
async def slowmode(ctx, seconds: int):
        await ctx.channel.edit(slowmode_delay=seconds)
        var = embed("Set slowmode to {} seconds.".format(seconds), "I have successfully set the slowmode to {} seconds in <#{}>.".format(seconds, ctx.channel.id))
        await ctx.send(embed=var)
    
@bot.command(pass_context=True, aliases=["clear"], description="Delete an amount of messages in the following channel.")
@commands.has_permissions(administrator=True)
@commands.bot_has_permissions(administrator=True)
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.guild_only()
async def purge(ctx, limit: int):
        await ctx.message.delete()
        await ctx.channel.purge(limit=limit)
        embed = nextcord.Embed(
            title="Purged Messages!",
            description=f"{ctx.author.mention} has purged {limit} messages!", color=0x2f3136, timestamp=datetime.now()
        )
        await ctx.send(embed=embed)
    
@bot.command(aliases=["repeat", "copy", "mimick"], description="Make the bot say a message.")
@commands.cooldown(1, 5, commands.BucketType.user)
async def say(ctx, *, message):
    embed = nextcord.Embed(
        description=f"{message}",
        color=0x2f3136,
        timestamp=datetime.now()
    )
    embed.set_footer(text="Sent by {}".format(ctx.author))
    await ctx.send(embed=embed)
    
@bot.command(aliases=["mute", "stfu", "shutup"], description="Timeout (mute) someone. Use: minutes, hours (Not required), days (Not required)")
@commands.has_permissions(mute_members=True)
@commands.bot_has_permissions(mute_members=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def timeout(ctx, member: nextcord.Member, minutes : int, hours: int = None, days: int = None):
    if hours == None:
        hours = 0
    if days == None:
        days = 0
        
    await member.edit(
            timeout=datetime.utcnow() + timedelta(minutes=minutes, hours=hours, days=days)
            )
    title = f"Timed out {member}"
    description = f"I have timed out {member.mention} for {minutes} minute(s), {hours} hour(s), {days} day(s)."
    embed=nextcord.Embed(title=f"{title}", description=f"{description}", color=0x2f3136, timestamp=datetime.now())
    await ctx.send(embed=embed)

@bot.command(description="Unban a user.")
@commands.has_permissions(ban_members=True)
@commands.bot_has_permissions(ban_members=True)
@commands.guild_only()
@commands.cooldown(1, 5, commands.BucketType.user)
async def unban(ctx, user: nextcord.User, *, reason):
    await ctx.guild.unban(user=user, reason=reason)
    title = f"Unbanned {user}"
    description = f"I have successfully unbanned {user.mention} for the reason of: {reason}"
    embed=nextcord.Embed(title=f"{title}", description=f"{description}", color=0x2f3136, timestamp=datetime.now())
    await ctx.send(embed=embed) 

@bot.command(description="Kick a user.")
@commands.has_permissions(kick_members=True)
@commands.bot_has_permissions(kick_members=True)
@commands.guild_only()
@commands.cooldown(1, 5, commands.BucketType.user)
async def kick(ctx, member: nextcord.Member, reason=None):
    await ctx.guild.kick(user=member, reason=reason)
    title = f"Kicked {member}"
    description = f"I have kicked {member.mention} for the reason of: {reason}"
    embed=nextcord.Embed(title=f"{title}", description=f"{description}", color=0x2f3136, timestamp=datetime.now())
    await ctx.send(embed=embed)

@bot.command(description="Testing command")
async def testing(ctx):
    if ctx.author.id == ctx.guild.owner_id:
        await ctx.reply("Ya da owner")
    else:
        await ctx.reply("Ya not da owner")
        
@bot.command(description="Mass Ban users! Max 120 members.")
@commands.has_permissions(ban_members= True)
@commands.bot_has_permissions(ban_members= True)
@commands.guild_only()
@commands.cooldown(1, 5, commands.BucketType.user)
async def massban(ctx, *users: nextcord.User):
    if len(users) > 120:
        await ctx.send("I cannot ban more than 120 members at a time!")
    else:
        async with ctx.channel.typing():
            for user in users:
                #https://discord.com/channels/881118111967883295/952729587404664902/952737951073304646
                await ctx.guild.ban(user=user, reason='Massban')
        embed = nextcord.Embed(
            title="Massbanned {} users".format(len(users)),
            description="I have sucessfully massbanned {} users!".format(len(users)), timestamp=datetime.now()
        )
        await ctx.send("I have sucessfully banned {} users!".format(len(users)))
        
@bot.slash_command(name="help", description="View help commands.", guild_ids=serverIDS)
async def help(interaction : Interaction):
    await interaction.response.send_message("Coming soon")
         
@bot.command(description="View commands.")
@commands.cooldown(1, 5, commands.BucketType.user)
async def help(ctx):
    embed = nextcord.Embed(
        title="ProtectTool Help",
        description="Help commands for ProtectTool!", timestamp=datetime.now()
    )
    for command in bot.walk_commands():
        description = command.description
        if not description or description is None or description == "":
            description = "No Description Provided"
        embed.add_field(name=f"!{command.name} {command.signature if command.signature is not None else '' }", value=description) #, value=description
        embed.set_footer(text=f"Slash commands are coming at the end of March! On April 1st, you will not be able to use the ! prefix, but you will have to use the / prefix using the Discord interaction")
    
    await ctx.send(embed=embed)
            
@bot.command(description="Get a google URL for your query.")
@commands.cooldown(1, 5, commands.BucketType.user)
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
    
@bot.command(description="Invite me!")
@commands.cooldown(1, 5, commands.BucketType.user)
async def invite(ctx):
    class Invite(nextcord.ui.View):
        def __init__(self):
            super().__init__()
            url = f"https://discord.com/api/oauth2/authorize?client_id=950528649046675467&permissions=8&scope=bot%20applications.commands"
            self.add_item(nextcord.ui.Button(label='Invite Link', url=url))
    embed = nextcord.Embed(
        title="Invite Me",
        description="Click the button below to invite me to your server! Thanks for choosing ProtectTool!", timestamp=datetime.now()
    )
    view = Invite()
    await ctx.send(embed=embed, view=view)

@bot.command(description="Lock the current channel you are in. Use `--server` to lock the whole server.")
@commands.has_permissions(manage_channels = True)
@commands.bot_has_permissions(manage_channels = True)
@commands.guild_only()
@commands.cooldown(1, 5, commands.BucketType.user)
async def lock(ctx, channel : nextcord.TextChannel=None, setting=None):
    if setting == '--server':
        class Confirm(nextcord.ui.View):
                    def __init__(self):
                        super().__init__()
                        self.value = None
                    
                    # When the confirm button is pressed, set the inner value to `True` and
                    # stop the View from listening to more input.
                    # We also send the user an ephemeral message that we're confirming their choice.
                    
                    
                    @nextcord.ui.button(label='Confirm', style=nextcord.ButtonStyle.green, disabled=False)
                    async def confirm(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
                        if ctx.author.id == interaction.user.id:
                            button.disabled=True
                            await interaction.response.send_message("Locking down server!", ephemeral=True)
                            self.value = True
                            self.stop()
                            embed = nextcord.Embed(
                                title="Locked down Server!",
                                description=f"`{interaction.user}, {interaction.user.id}` has locked down the server!", timestamp=datetime.now(),
                                color=0x2f3136
                            )
                            await interaction.message.edit(embed=embed, view=self)
                            
                            for channel in ctx.guild.channels:
                                await channel.set_permissions(ctx.guild.default_role, reason=f"{ctx.author.name} locked {channel.name} with --server", send_messages=False)
                            await ctx.send("I have locked down the server.", delete_after=10)
                                
                        else:
                            await interaction.response.send_message("This is not for you!", ephemeral=True)
                            
        view = Confirm()
        await ctx.send("Please confirm to lockdown the server!", view=view)
    if channel is None:
        channel = ctx.message.channel
        await channel.set_permissions(ctx.guild.default_role, reason=f"{ctx.author.name} locked {channel.name}", send_messages=False)
        await ctx.reply(f"I have locked <#{channel.id}>!")

@bot.command(description="Unlock the current channel you are in. Use `--server` to unlock all the channels in the server.")
@commands.has_permissions(manage_channels = True)
@commands.bot_has_permissions(manage_channels = True)
@commands.guild_only()
@commands.cooldown(1, 5, commands.BucketType.user)
async def unlock(ctx, channel : nextcord.TextChannel=None, setting=None):
    if setting == '--server':
        
        for channel in ctx.guild.channels:
            await channel.set_permissions(ctx.guild.default_role, reason=f"{ctx.author.name} unlocked {channel.name} with --server", send_messages=True)
        embed = nextcord.Embed(
            title="Unlocked Server",
            description=f"I have successfully unlocked the server!", timestamp=datetime.now()
        )    
        await ctx.reply(embed=embed)
        return
    if channel is None:
        channel = ctx.message.channel
    await channel.set_permissions(ctx.guild.default_role, reason=f"{ctx.author.name} locked {channel.name}", send_messages=True)
    embed = nextcord.Embed(
            title="Unlocked Channel",
            description=f"I have successfully Unlocked {channel}!", timestamp=datetime.now()
    )   
    await ctx.reply(embed=embed)

@bot.command(description="Ban a user.")
@commands.has_permissions(ban_members = True)
@commands.bot_has_permissions(ban_members = True)
@commands.guild_only()
@commands.cooldown(1, 5, commands.BucketType.user)
async def ban(ctx, user: nextcord.User, *, reason=None):
    await ctx.guild.ban(user = user, reason=reason)
    embed=nextcord.Embed(title="Banned User", description=f"I have successfully banned `{user}` for the reason of: `{reason}`", color=0x2f3136, timestamp=datetime.now())
    await ctx.send(embed=embed)

@bot.event
async def on_message(message):
    msg = message.content.split()
    if message.author.id != bot.user.id:
        for word in msg:
            newVar = word
            for line in read:
                        otherVar = "https://" + line
                        otherVar2 = "http://" + line
                        otherVar3 = line
                        otherVar4 = line + "/"
                        if otherVar in newVar or otherVar2 in newVar or otherVar3 in newVar:
                            await message.delete()
                            scamEmbed = nextcord.Embed(
                                title="<a:weewoo:951883123170365490> Scam Found",
                                description="A scam link has been identified and has been deleted for your saftey.\n\nIf you think that this is a fake link, please click the **Red** Button below.\n\nScam sent by: `{}, {}`".format(message.author, message.author.id),
                                color=0x2f3136
                                , timestamp=datetime.now()
                            )
                            scamEmbed.set_footer(text="Was the link a fake URL? Use /reportfake to report the fake URL!")
                            await message.channel.send(embed=scamEmbed)
                            pass
                            return
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
        #           and seconds > 30)
            
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
                        return
                elif resssp != match:
                        embed = nextcord.Embed(
                            title="<a:weewoo:951883123170365490> Link Shortened!",
                            description=f"The link has been shortened! The real link that is unshortened is: `{resssp}` \n\n[Jump to Message]({message.jump_url})\n\n Proceed with caution at your own risk.",
                            color=0x2f3136, timestamp=datetime.now()
                        )
                        await message.channel.send(embed=embed)
                    
            try:
                        match = re.match("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", message.content).group(0)
                        response = requests.get(f'{match}', verify=True)
                        print('gotten')
            except Exception as e:
                        print('e')
                        await message.channel.send("The most recently posted link is not SSL Certified.")
            else:
                        print("SSL Certified")
                        pass
                
                #shortnerChecker = get_real_url_from_shortlink("https://eee.py") 
                #sslCertificate = ssl_certificate('https://amongussussssss.py')

                #https://discord.com/channels/267624335836053506/343944376055103488/951634087884492881
        except Exception as e:
            pass
    else:
        return
    await bot.process_commands(message)


@bot.command(description="OWNER ONLY")
@commands.is_owner()
async def changeActivity(ctx, *, activityMessage):
    await bot.change_presence(status=nextcord.Status.dnd, activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=f'{activityMessage}'))
    await ctx.send("Done")
    
@bot.command(description="OWNER ONLY")
@commands.is_owner()
async def close(ctx):
   await ctx.send("Closing...")
   await bot.close()

@bot.command(description="OWNER ONLY")
@commands.is_owner()
async def restart(ctx):
    await ctx.send("Restarting...")
    print("{} has restarted the bot!".format(ctx.author))
    await _restart_bot()

async def _restart_bot():
    await bot.close()
    subprocess.call([sys.executable, "launcher.py"])

@bot.event
async def on_connect():
    print("Bot connected")
    for guild in bot.guilds:
        serverIDS.append(guild.id)
    await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="over your server. | !help | Blocked over 200 scam links, raids, and nukings."), status=nextcord.Status.dnd)
    bot.add_startup_application_commands()
    await bot.rollout_application_commands()

extensions = [
    "cogs.join",
    "cogs.ping"
]

try:
    for extension in extensions:
        bot.load_extension(extension)
except Exception as e:
    print("Failed to load Cog. ERROR:\n", e)


bot.run("OTUwNTI4NjQ5MDQ2Njc1NDY3.YiaOyQ.NOQ3BRIOSEoeEs3IlAnlrGCEqaA")
