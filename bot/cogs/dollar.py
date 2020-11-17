#dollar.py
import discord
from discord.ext import commands

import requests
from lxml import html

#paths for dollar html
path1 = '//span[@class="pull-right"]/text()'

#urls
url_dollar_blue = 'https://www.dolarhoy.com/cotizaciondolarblue'
url_dollar_official = 'https://www.dolarhoy.com/cotizaciondolaroficial'
url_dollar_beto = 'https://www.dolarhoy.com/cotizacion-dolar-turista'
url_dollar_bag = 'https://www.dolarhoy.com/cotizaciondolarbolsa'
url_dollar_liq = 'https://www.dolarhoy.com/cotizaciondolarcontadoconliqui'

#dollar_img
img_dollar_beto = 'https://i.ibb.co/WgGPx1Y/dolar-Beto-Low.jpg'
img_dollar = 'https://i.ibb.co/ggZK5yM/Benjamin-Franklin-U-S-100-bill.jpg'

#dollar_dict
dollar_blue_dict= {'url': url_dollar_blue, 'img': img_dollar, 'path': path1,
                    'title': 'Dolar blue', 'color': discord.Color.blue(),
                    'description': 'Cotizacion del dolar blue',
                    'field1': 'Compra', 'field2': 'Venta'}

dollar_offi_dict= {'url': url_dollar_official, 'img': img_dollar, 'path': path1,
                    'title': 'Dolar oficial', 'color': discord.Color.blue(),
                    'description': 'Cotizacion del dolar oficial',
                    'field1': 'Compra', 'field2': 'Venta'}

dollar_beto_dict= {'url': url_dollar_beto, 'img': img_dollar_beto, 'path': path1,
                    'title': 'Dolar Beto', 'color': discord.Color.blue(),
                    'description': 'Cotizacion del dolar turista',
                    'field1': 'Compra'}

dollar_bag_dict= {'url': url_dollar_bag, 'img': img_dollar, 'path': path1,
                    'title': 'Dolar bolsa', 'color': discord.Color.blue(),
                    'description': 'Cotizacion del dolar bolsa',
                    'field1': 'Compra', 'field2': 'Venta'}

dollar_liq_dict= {'url': url_dollar_liq, 'img': img_dollar, 'path': path1,
                    'title': 'Dolar contado con liq', 'color': discord.Color.blue(),
                    'description': 'Cotizacion del dolar contado con liq',
                    'field1': 'Compra', 'field2': 'Venta'}


#functions
def get_tree_from_HTML(source):
    """gets the tree data from a HTML file, receives a url as input"""
    url= source
    page= requests.get(url)
    tree= html.fromstring(page.content)

    return tree

def get_data_from_tree(tree, path):
    """extracts the data from a tree, receives a tree and path string as input"""
    data_array= tree.xpath(path)

    return data_array

def build_dollar_embed(dictionary):
    """Builds a embed using a dictionary"""
    embed= discord.Embed(
        title= dictionary['title'],
        description= dictionary['description'],
        colour= dictionary['color']
    )
    embed.set_thumbnail(url= dictionary['img'])

    # scrap dollar data from website
    tree = get_tree_from_HTML(dictionary['url'])
    data = get_data_from_tree(tree, dictionary['path'])
    try:
        if dictionary['field1']:
            embed.add_field(name= dictionary['field1'], value= data[0], inline=False)
    except KeyError:
        pass
    try:
        if dictionary['field2']:
            embed.add_field(name= dictionary['field2'], value= data[1], inline=True)
    except KeyError:
        pass

    return embed    

#Dollar cog
class Dollar(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Quick go buy dollars!!!')

    @commands.command()
    async def dollar(self, ctx, dollar_type):
        """uses the dollar_type argument(string) and decides wich dollar embed print"""
        dictionary = { }
        if dollar_type  == 'blue':
            dictionary = dollar_blue_dict
        elif dollar_type == 'official':
            dictionary = dollar_offi_dict
        elif dollar_type == 'beto':
            dictionary = dollar_beto_dict
        elif dollar_type == 'liq':
            dictionary = dollar_liq_dict
        elif dollar_type == 'bag':
            dictionary = dollar_bag_dict

        embed = build_dollar_embed(dictionary)
        await ctx.send(embed = embed)


def setup(bot):
    bot.add_cog(Dollar(bot))
