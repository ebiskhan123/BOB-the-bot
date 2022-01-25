'''
Central location for utility functions
'''
import discord

def get_embed(title,desc,color):
    return discord.Embed(title=title,description=desc,color=color)