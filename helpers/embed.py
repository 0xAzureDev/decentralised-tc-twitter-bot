import discord

from helpers.consensus import pretty_consensus
from helpers.time import get_expiration_date


def embed_vote(
    url: str,
    requester: str,
    title: str = 'Should this tweet be retweeted by the official @THORChain account?',
    description: str = '⬆️ Click on the hyperlink to display the tweet!',
    color: int = 0x1CE6CC,
    quota: str = '⦁ Minimum of 30 votes\n⦁ ⅔ Majority Consensus',
    consensus: str = pretty_consensus(0, 0),
    expiration: str = get_expiration_date()[0],
    status: str = '🟡 Voting period',
) -> object:
    """
    Embed Vote
    ----------

    Generates an embed for the voting view.

    :param url: The url of the tweet to be retweeted.
    :param requester: The user who submitted the tweet.
    :param title: The title of the embed.
    :param description: The description of the embed.
    :param color: The color of the embed.
    :param quota: The minimum requirement for the proposal to pass.
    :param consensus: The consensus of the proposal.
    :param expiration: The expiration date of the proposal.
    :param status: The status of the proposal.
    """

    embed = discord.Embed()

    embed.title = title
    embed.description = description
    embed.color = color
    embed.url = url

    embed.add_field(name="Requester", value=requester, inline=False)
    embed.add_field(name="Quota Requirement", value=quota, inline=False)
    embed.add_field(name="Consensus", value=consensus, inline=True)
    embed.add_field(name="Expiration", value=expiration, inline=True)
    embed.add_field(name="Status", value=status, inline=True)

    return embed
