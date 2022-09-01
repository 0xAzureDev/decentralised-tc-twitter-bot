import re

from discord.ext import commands
from discord.ext.commands import Context
from helpers.embed import embed_vote
from helpers.time import get_expiration_date
from helpers.views import VoteView


class General(commands.Cog, name="general"):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
        name="request",
        description="Requests a tweet or retweet from the THORChain Twitter account.",
    )
    async def request(self, context: Context, url: str) -> None:
        """
        Request
        -------

        Requests a tweet or retweet from the THORChain Twitter account.

        :param context: The hybrid command context.
        """

        # Pattern for validating a Twitter link
        pattern = re.compile(
            r"^https?:\/\/twitter\.com\/(?:#!\/)?(\w+)\/status(es)?\/(\d+)")

        # Return if the link is not valid
        if not pattern.match(url):
            return await context.reply('Invalid tweet to retweet')

        # Timestamp the request and get an expiration date for the voting process
        expiration = get_expiration_date()

        # Generates the initial embed for the view
        embed = embed_vote(
            url=url,
            requester=context.author.mention,
            expiration=expiration[0]
        )

        # Creates the view with the author, the tweet, the expiration date and the twitter auth tokens
        view = VoteView(context.author, url, expiration, self.bot.config['twitter'])

        # Reply to the command
        await context.reply(view=view, embed=embed)


async def setup(bot):
    await bot.add_cog(General(bot))
