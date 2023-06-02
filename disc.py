import instaloader
import discord
import re
import os

def get_instagram_post_info(post_url):
    # Create an instance of Instaloader class
    L = instaloader.Instaloader()

    # Login using the credentials (If you want to access private pages)
    #L.login(USER, PASSWORD)

    # Load post by its URL
    post = instaloader.Post.from_shortcode(L.context, post_url.split("/")[-2])

    # Download the post
    L.download_post(post, target="YOURFOLDER")

    # Get the caption of the post
    caption = post.caption

    if caption is not None:
        return caption

def extract_post_id(link):
    parts = link.split('/')
    return parts[-2]


client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    # Access the data of the new message
    message_content = message.content

    # Check if the message contains an Instagram link
    match = re.search(
        r'(?:https?:\/\/)?(?:www\.)?(?:instagram\.com|instagr\.am)\/(?:[a-zA-Z0-9_\.]+\/)?(?:p|tv|reel)\/[a-zA-Z0-9_\-]+\/?',
        message_content)
    if match:
        instagram_url = match.group(0)
        if not instagram_url.endswith("/"):  # check if text doesn't end with "/"
            instagram_url += "/"  # add "/" at the end of the text

        newText = get_instagram_post_info(instagram_url)
        print(newText)

# Replace 'your_bot_token_here' with your Discord bot token
client.run('your_bot_token_here')
