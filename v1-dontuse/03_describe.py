# Description: Describe what this code does and how it works. Do not go into full detail, just a brief description so that someone else can understand what it does without having to read the code.

import os
import requests
import dotenv
from discord import Client, Embed

client = Client()
dotenv.load_dotenv()

prefix = "!"


class Commands:
    async def ping(message):
        await message.channel.send(f"Latency: {round(client.latency * 1000)}ms")

    async def quote(message):
        await message.channel.trigger_typing()
        quote_res = requests.get("http://api.quotable.io/random")
        quote_data = quote_res.json()

        image_res = requests.get(
            f"https://en.wikipedia.org/w/api.php?action=query&prop=pageimages&format=json&pithumbsize=500&titles={quote_data['author']}")
        image_data = image_res.json()

        embed = Embed()
        embed.description = f"*{quote_data['content']}*"
        embed.set_author(
            name=quote_data['author'],
            url=f"https://en.wikipedia.org/wiki/{quote_data['author'].replace(' ', '_')}",
            icon_url=image_data['query']['pages'][list(image_data['query']['pages'].keys())[
                0]]['thumbnail']['source'].replace(' ', '_')
        )
        embed.color = 0x0099ff

        await message.channel.send(embed=embed)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}, ID: {client.user.id}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(prefix):
        command = message.content[len(prefix):].split(" ")[0]
        if command in dir(Commands):
            return await getattr(Commands, command)(message)

        await message.channel.send(f"Unknown command: {command}")


client.run(os.getenv("TOKEN"))
