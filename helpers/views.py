import re

import discord

from helpers.consensus import percentage_consensus, pretty_consensus
from helpers.embed import embed_vote
from helpers.retweet import submit_retweet
from helpers.time import is_expired


class VoteView(discord.ui.View):

    UPVOTE = 'upvote'
    DOWNVOTE = 'downvote'

    def __init__(self, author, url, expiration, twitter):
        super().__init__()

        self.author = author  # requester of the retweet
        # expiration string of the voting proposal
        self.expiration_string = expiration[0]
        # expiration date of the voting proposal
        self.expiration_date = expiration[1]
        self.url = url  # url to the tweet to retweet
        self.twitter = twitter  # twitter auth

        self.up = 0
        self.down = 0
        self.quota = {
            "total_votes": 30,
            "consensus": 66.66
        }
        self.status = '🟡 Voting period'
        self.voters = {}

    @discord.ui.button(label="Upvote", custom_id=UPVOTE, style=discord.ButtonStyle.green, emoji="⬆️")
    async def upvote_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.__handle_interaction(interaction, self.UPVOTE)

    @discord.ui.button(label="Downvote", custom_id=DOWNVOTE, style=discord.ButtonStyle.red, emoji="⬇️")
    async def downvote_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.__handle_interaction(interaction, self.DOWNVOTE)

    async def __handle_interaction(self, interaction, action):
        # If it's expired, do not process the vote else, process the vote
        if is_expired(self.expiration_date):
            self.__disable_buttons()
            self.status = '🔴 Proposal expired!'
        else:
            self.__upvote(interaction.user) if action == self.UPVOTE else self.__downvote(
                interaction.user)

        embed = embed_vote(
            url=self.url,
            requester=self.author.mention,
            consensus=pretty_consensus(self.up, self.down),
            expiration=self.expiration_string,
            status=self.status
        )

        await interaction.response.edit_message(view=self, embed=embed)

    def __upvote(self, user):
        if user in self.voters.keys():
            if self.voters[user] == self.DOWNVOTE:
                self.down -= 1
                self.up += 1
                self.voters[user] = self.UPVOTE
        else:
            self.voters[user] = self.UPVOTE
            self.up += 1

        # Quota requirements met
        if self.up + self.down >= self.quota['total_votes'] and percentage_consensus(self.up, self.down) >= self.quota['consensus']:
            tweet_id = re.search('/status/(\d+)', self.url).group(1)
            submit_retweet(tweet_id, self.twitter)

            # Disable buttons
            self.__disable_buttons()

            self.status = '🟢 Retweet complete!'

    def __downvote(self, user):
        if user in self.voters.keys():
            if self.voters[user] == self.UPVOTE:
                self.up -= 1
                self.down += 1
                self.voters[user] = self.DOWNVOTE
        else:
            self.voters[user] = self.DOWNVOTE
            self.down += 1

        # Quota requirements met
        if self.up + self.down >= self.quota['total_votes'] and percentage_consensus(self.up, self.down) < self.quota['consensus']:
            # Disable buttons
            self.__disable_buttons()

            self.status = '🔴 Requirements not met!'

    def __disable_buttons(self):
        # Disable upvote button
        btn = [x for x in self.children if x.custom_id == self.UPVOTE][0]
        btn.disabled = True

        # Disable downvote button
        btn = [x for x in self.children if x.custom_id == self.DOWNVOTE][0]
        btn.disabled = True
