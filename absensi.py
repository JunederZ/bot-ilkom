import traceback
import datetime
import asyncio

import discord
from discord.ext import commands

import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discordTest.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

class modalData(discord.ui.Modal):

    def __init__(self, *, title = "Vote Refunder", custom_id = 'transactionRequestDataModal:data') -> None:
        super().__init__(title=title, custom_id=custom_id)

    matkul = discord.ui.TextInput(
        label='Mata Kuliah',
        placeholder='Masukan mata kuliah yang diabsensi.',
        min_length=3,
        max_length=20,
        style=discord.TextStyle.short,
        required=True
    )

    pertemuan = discord.ui.TextInput(
        label='Pertemuan ke - _',
        placeholder='Masukan dalam bentuk ANGKA',
        min_length=1,
        max_length=4,
        required=True,
        style=discord.TextStyle.short
    )

    minggu = discord.ui.TextInput(
        label='Minggu ke - _',
        placeholder='Masukan dalam bentuk ANGKA',
        max_length=40,
        required=True,
        style=discord.TextStyle.short
    )
    

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            f"matkul : {self.matkul.value}\n"
            f"Minggu : {self.minggu.value}\n"
            f"Pertemuan : {self.pertemuan.value}"
     
        )

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('Oops! Something went wrong.', ephemeral=True)
        
        traceback.print_tb(error.__traceback__)

@bot.event
async def on_ready():
    print("")
    print(f"Successfully Login in as {bot.user}")


@bot.event
async def on_interaction(interaction: discord.Interaction):
    try:
        if not interaction.data["custom_id"]: return
    except KeyError:
        return

    if interaction.data["custom_id"] == "absensi:reqdata":
        await interaction.response.defer(thinking=True)
        embed = discord.Embed(
            description='__**Silahkan isi data absensi dengan menggunakan tombol 📝**__\n‌',
            color=discord.Colour.from_rgb(204, 0, 255),
            timestamp=datetime.datetime.now().astimezone()
        )
        embed.add_field(inline=False, name='Petunjuk', value='Harap mengisi datanya dengan benar agak tidak terjadi kesalahan')
        embed.set_author(name='Absensi System', icon_url='https://cdn.discordapp.com/attachments/932526421228814336/1008722570889146469/shopping_cart_checkout_FILL0_wght400_GRAD0_opsz48.png')
        await interaction.edit_original_response(embed=embed, view=modalData())
        return

class inputDataButton(discord.ui.View):
    def __init__(self: discord.ui.View):
        super().__init__(timeout=None)

    @discord.ui.button(label='Isi Data', emoji="📝", style=discord.ButtonStyle.green, custom_id='absensi:reqdata')
    async def sad(self, interaction: discord.Interaction, button: discord.ui.Button):
        return

@bot.command()
async def test(ctx: commands.Context):
    await ctx.send("sad", view=inputDataButton())
    return
    
async def main():
    async with bot:
        await bot.start("TOKEN")       

asyncio.run(main())
