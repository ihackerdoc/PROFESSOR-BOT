import instaloader
from pyrogram import Client, filters

# Function to download Instagram post or reel
async def download_instagram(url, target_dir="downloads"):
    L = instaloader.Instaloader()
    post = instaloader.Post.from_shortcode(L.context, url.split("/")[-2])
    L.download_post(post, target=target_dir)

# Pyrogram handler to trigger Instagram download
@app.on_message(filters.command("instadl"))
async def instagram_dl_handler(client, message):
    url = message.text.split(" ")[1]
    await message.reply("Downloading from Instagram...")
    await download_instagram(url)
    await message.reply("Download completed!")
