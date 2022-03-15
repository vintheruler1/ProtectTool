from nextcord import Interaction, slash_command
from nextcord.ext.commands import Bot, Cog
from nextcord.ext import commands
import nextcord
from datetime import datetime

class Join(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild:nextcord.Guild):
        channel = self.bot.get_channel(953425150592839740)
        embed = nextcord.Embed(
            title="I have joined a new server!",
            description=f"__**Name:**__ **{guild.name}**\n**__ID:__** `{guild.id}`\n**__Owner:__** {guild.owner} (<@{guild.owner_id}>)\n\n__I am now in `{(len(self.bot.guilds))}` __servers!__",
            color=0x2f3136, 
            timestamp=datetime.now()
        )
        await channel.send(embed=embed)

        
def setup(bot: Bot) -> None:
    bot.add_cog(Join(bot))