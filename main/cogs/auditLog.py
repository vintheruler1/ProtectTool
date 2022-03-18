from nextcord import Interaction, slash_command
from nextcord.ext.commands import Bot, Cog
from nextcord.ext import commands
import nextcord
import datetime
import json
import asyncio
import time

class AuditLog(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot
        
    @commands.command()
    async def auditlog(self, ctx, channel= None):
        with open("./databases/auditLogChannel.json", "r") as f:
            auditLogJson = json.load(f)
        if channel is None:
            await ctx.send("Please provide a channel!")
        else:
            auditLogJson[str(ctx.guild.id)] = {}
            auditLogJson[str(ctx.guild.id)]['channel'] = channel
            with open("./databases/auditLogChannel.json", "w") as f:
                json.dump(auditLogJson, f, indent=4, sort_keys=True, ensure_ascii=False)

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        with open("./databases/auditLogChannel.json", "r") as f:
            auditLogJson = json.load(f)
        auditLogChan = auditLogJson[str(before.guild.id)]['channel']
        newLog = int(auditLogChan)
        if auditLogChan is None or auditLogChan == "" or auditLogChan == "\n" or auditLogChan == None:
            return
        else:
            channel = self.bot.get_channel(newLog)
            if before.display_name != after.display_name:
                embed = nextcord.Embed(
                    title="Member Update",
                    description=f"Nickname changed by {after.mention}.",
                    color=after.color,
                    timestamp=datetime.datetime.now()
                )
                fields = [("Before", before.display_name , False),
                        ("After", after.display_name, False)]
                
                for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)

                await channel.send(embed=embed)
                
    @commands.Cog.listener()
    async def on_message_delete(self, message:nextcord.Message):
        with open("./databases/auditLogChannel.json", "r") as f:
            auditLogJson = json.load(f)
        auditLogChan = auditLogJson[str(message.guild.id)]['channel']
        newLog = int(auditLogChan)
        if auditLogChan is None or auditLogChan == "" or auditLogChan == "\n" or auditLogChan == None:
            return
        else:
            channel = self.bot.get_channel(newLog)
            embed = nextcord.Embed(
                title="Message Deleted",
                description=f"Message sent by {message.author.mention} was deleted in <#{message.channel.id}>"
            )
            fields = [("Message: ", f"{message.content}", False)]
            for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)
            await channel.send(embed=embed)
            
    #@commands.Cog.listener()
    #async def on_bulk_message_delete(self, messages:list):
    #    var = len(list)-1
     #   with open("./databases/auditLogChannel.json", "r") as f:
      #      auditLogJson = json.load(f)
       # auditLogChan = auditLogJson[str(var.guild.id)]['channel']
#        newLog = int(auditLogChan)
#        if auditLogChan is None or auditLogChan == "" or auditLogChan == "\n" or auditLogChan == None:
 #           return
  #      else:
   #         
    #        channel = self.bot.get_channel(newLog)
     #       embed = nextcord.Embed(
      #          title="Bulk Message Delete",
       #         description=f"Bulk message delete in <#{var.channel.id}>"
        #    )
         #   fields = [("Messages Deleted", f": {len(messages)}", False)]
          #  for name, value, inline in fields:
           #         embed.add_field(name=name, value=value, inline=inline)
#            print('hi')
 #           await time.sleep(10)
  #          print('bye')
   #         await channel.send(embed=embed)
            
    @commands.Cog.listener()
    async def on_message_edit(self, before:nextcord.Message, after:nextcord.Message):
        with open("./databases/auditLogChannel.json", "r") as f:
            auditLogJson = json.load(f)
        auditLogChan = auditLogJson[str(after.guild.id)]['channel']
        newLog = int(auditLogChan)
        if auditLogChan is None or auditLogChan == "" or auditLogChan == "\n" or auditLogChan == None:
            return
        else:
            channel = self.bot.get_channel(newLog)
            embed = nextcord.Embed(
                title="Message Edited",
                description=f"Message edited by {after.author.mention} in <#{after.channel.id}>\n\n"
            )
            fields = [("Before: ", f"{before.content}", False), ("After: ", f"{after.content}", False)]
            for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)
            embed.add_field(name="** **", value=f"[Jump to Message]({after.jump_url})", inline=False)
            await channel.send(embed=embed)
    
    #@commands.Cog.listener()
    #async def on_member_join(self, member:nextcord.Member):
        
def setup(bot: Bot) -> None:
    bot.add_cog(AuditLog(bot))
    
    
#@slash_command(name="ping", description="A simple ping command.", guild_ids=[...])
#    async def ping(self, inter: Interaction) -> None:
#        await inter.send(f"Pong! {self.bot.latency * 1000:.2f}ms")