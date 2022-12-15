#Importation des librairies de discord
import discord
from discord.ext import commands
import aiohttp
import json
import random
from blagues_api import BlaguesAPI
#Importations des librairies pour le systeme de logs des commandes
import logging
from time import gmtime, strftime

#Déclaration des variables essentielles au lancement du bot
#Intents
penbot_intents = discord.Intents.all()
#Création de l'activité du bot (Stream Internet)
activity = discord.Activity(type=discord.ActivityType.streaming, name="Internet", url='https://twitch.tv/penbot')
#Création de l'instance
penbot = commands.Bot(command_prefix="pb$", description="Coded by PenTaist#8589", activity=activity ,intents=penbot_intents)
#Suppression des commandes help et youtube afin de les modifier
penbot.remove_command("help")
penbot.remove_command("youtube")
#Token du bot
token = "TOKEN DU BOT"

#Affichage d'un message dans la console quand le bot est complêtement initialisé
@penbot.event
async def on_ready():
    print("Logged in as", penbot.user)

#Envoie d'un message de bienvenue pour les nouveaux membres dans le salon bla bla
@penbot.event
async def on_member_join(member):
    embed = discord.Embed(title="Bienvenue sur le serveur PenTaist - Community !", color=discord.Color.blue())
    embed.add_field(name="Afin d'accèder à l'intégralité du serveur", value="Veuillez vérifier votre compte dans le salon de vérification puis accepter le règlement dans la salon des règles", inline=False)
    await member.send(embed=embed)
    #Envoie d'un message dans la salon bla bla
    channel = penbot.get_channel(1000413429758185472)
    channel_message = f"Hey {member.mention} ! Bienvenue sur ce magnifique serveur 🥳"
    await channel.send(channel_message)
    
#Ajout des réactions dans les salons annonces et events
@penbot.event
async def on_message(message):
    # Emojis messages annonces
    emoji_annonces1 = '📢'
    emoji_annonces2 = '🤣'
    emoji_annonces3 = '🤑'
    emoji_annonces4 = '🤖'
    emoji_annonces5 = '👨‍💻'
    emoji_annonces6 = '🤘'
    emoji_annonces7 = '👀'
    emoji_annonces8 = '⚽'
    emoji_annonces9 = '🎥'
    emoji_annonces10 = '😻'

    # Réactions messages dans le salon annonces
    if message.channel.id == 1010309001092808774:
        await message.add_reaction(emoji_annonces1)
    if message.channel.id == 1010309001092808774:
        await message.add_reaction(emoji_annonces2)
    if message.channel.id == 1010309001092808774:
        await message.add_reaction(emoji_annonces3)
    if message.channel.id == 1010309001092808774:
        await message.add_reaction(emoji_annonces4)
    if message.channel.id == 1010309001092808774:
        await message.add_reaction(emoji_annonces5)
    if message.channel.id == 1010309001092808774:
        await message.add_reaction(emoji_annonces6)
    if message.channel.id == 1010309001092808774:
        await message.add_reaction(emoji_annonces7)
    if message.channel.id == 1010309001092808774:
        await message.add_reaction(emoji_annonces8)
    if message.channel.id == 1010309001092808774:
        await message.add_reaction(emoji_annonces9)
    if message.channel.id == 1010309001092808774:
        await message.add_reaction(emoji_annonces10)
        
    await penbot.process_commands(message)

#Messages d'erreur en cas de commande incorrecte ou de permissions inssufisantes
@penbot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        arguments_message = "Commande Incorrecte !"
        arguments_embed = discord.Embed(title=arguments_message, color=discord.Color.red())
        await ctx.send(embed=arguments_embed, delete_after=5)
        logging.basicConfig(level=logging.ERROR, filename='logs/errors.log')
        logging.error(' Date : ' + str(strftime('%Y-%m-%d %H:%M:%S', gmtime())))
        logging.error(' User : ' + str(ctx.author))
        logging.error(' Error : INVALID COMMAND')
        logging.critical('----------------------------------------------------')
    if isinstance(error, commands.MissingPermissions):
        permissions_messages = "Tu n'a pas les permissions requises !"
        permissions_embed = discord.Embed(title=permissions_messages, color=discord.Color.red())
        await ctx.send(embed=permissions_embed, delete_after=5)
        logging.basicConfig(level=logging.ERROR, filename='logs/errors.log')
        logging.error(' Date : ' + str(strftime('%Y-%m-%d %H:%M:%S', gmtime())))
        logging.error(' User : ' + str(ctx.author))
        logging.error(' Error : INVALID PERMISSIONS')
        logging.critical('----------------------------------------------------')

#Commande help
@penbot.command()
async def help(ctx):
    embed = discord.Embed(title="Voici la liste de toutes les commandes disponnibles", color=discord.Color.blue())
    embed.add_field(name="Commandes de base :", value="pb$ping : Jouer au ping pong\npb$serverinfos : Affiche les information du serveur", inline=False)
    embed.add_field(name="Commandes de modération :", value="pb$ban MEMBRE RAISON : Bannir un membre\npb$kick MEMBRE RAISON : Expulser un membre\npb$rename MEMBRE NOM : Renommer un membre\npb$roleadd MEMBRE ROLE : Donner un rôle à un membre\npb$roledel MEMBRE ROLE : Retirer un rôle à un membre\npb$rm NOMBRE : Supprimer les messages", inline=False)
    embed.add_field(name="Fun :", value="pb$dog : Envoie une image de chien\npb$cat : Envoie une image de chat\npb$gif MOT : Envoie un gif en rapport avec le mot entré\npb$joke : Je vous fait une blague (pas sur qu'elle sois drôle XD)", inline=False)
    embed.add_field(name="Réseaux :", value="pb$github : GitHub de PenTaist#8589\npb$youtube : Chaine YouTube de PenTaist#8589\npb$website : Site de PenTaist#8589", inline=False)

    await ctx.send(embed=embed)

    #Systeme de logs
    logging.basicConfig(level=logging.INFO, filename='logs/basic_commands.log')
    logging.info(' Date : ' + str(strftime('%Y-%m-%d %H:%M:%S', gmtime())))
    logging.info(' User : ' + str(ctx.author))
    logging.info(' Command : pb$help')
    logging.info('----------------------------------------------------')

#Commande ping
@penbot.command()
async def ping(ctx):
    ping_message = "Pong !"
    ping_embed = discord.Embed(title=ping_message, color=discord.Color.blue())
    await ctx.send(embed=ping_embed, delete_after=5)
    #Systeme de logs
    logging.basicConfig(level=logging.INFO, filename='logs/basic_commands.log')
    logging.info(' Date : ' + str(strftime('%Y-%m-%d %H:%M:%S', gmtime())))
    logging.info(' User : ' + str(ctx.author))
    logging.info(' Command : pb$ping')
    logging.info('----------------------------------------------------')

#Commande serverinfo
@penbot.command()
async def serverinfos(ctx):
    server = ctx.guild
    text_channels = len(server.text_channels)
    voice_channels = len(server.voice_channels)
    description = server.description
    number_of_members = server.member_count
    server_name = server.name
    if server.description == None:
        description = "Le serveur n'a pas encore de description"
    serverinfos_message =f"Le serveur ***{server_name}*** est un serveur de **{number_of_members} membres.**"
    serverinfos_embed = discord.Embed(title=serverinfos_message, color=discord.Color.blue())
    serverinfos_embed.add_field(name="Description du serveur", value=f"{description}", inline=False)
    serverinfos_embed.add_field(name="Salons textuels :", value=f"{text_channels}", inline=True)
    serverinfos_embed.add_field(name="Salons vocaux :", value=f"{voice_channels}", inline=True)
    await ctx.send(embed=serverinfos_embed)
    #Systeme de logs
    logging.basicConfig(level=logging.INFO, filename='logs/basic_commands.log')
    logging.info(' Date : ' + str(strftime('%Y-%m-%d %H:%M:%S', gmtime())))
    logging.info(' User : ' + str(ctx.author))
    logging.info(' Command : pb$serverinfos')
    logging.info('----------------------------------------------------')

#Commandes ban
@penbot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *reason):
    author = ctx.author
    reason = " ".join(reason)
    embed = discord.Embed(title=f"{user} à été ban par {author}", color=discord.Color.green())
    embed.add_field(name="Raison :", value=f"{reason}")
    if ctx.author.top_role <= user.top_role:
        top_role_message = "Impossible de ban cet utilisateur !"
        top_role_embed = discord.Embed(title=top_role_message, color=discord.Color.red())
        await ctx.send(embed=top_role_embed, delete_after=5)
        logging.basicConfig(level=logging.ERROR, filename='logs/errors.log')
        logging.error(' Date : ' + str(strftime('%Y-%m-%d %H:%M:%S', gmtime())))
        logging.error(' User : ' + str(ctx.author))
        logging.error(' Command : pb$ban')
        logging.error(' Error : INVALID PERMISSIONS')
        logging.critical('----------------------------------------------------')
    if reason == "":
        no_reason_embed = discord.Embed(title="Veuillez spécifier la raison !", color=discord.Color.red())
        no_reason_embed.add_field(name="Utilisation", value="pb$ban MEMBRE RAISON")
        await ctx.send(embed=no_reason_embed)
    mp_ban_embed = discord.Embed(title=f"Vous avez été ban de {ctx.guild}", color=discord.Color.red())
    mp_ban_embed.add_field(name="Ban par :", value=f"{author}", inline=False)
    mp_ban_embed.add_field(name="Raison :", value=f"{reason}", inline=False)
    await user.send(embed=mp_ban_embed)
    await ctx.guild.ban(user, reason=reason)
    await ctx.send(embed=embed)
    #Systeme de logs
    logging.basicConfig(level=logging.INFO, filename='logs/mod_commands.log')
    logging.info(' Date : ' + str(strftime('%Y-%m-%d %H:%M:%S', gmtime())))
    logging.info(' User : ' + str(author))
    logging.info(f' Command : pb$ban {user} {reason}')
    logging.info('----------------------------------------------------')

#Commande unban
@penbot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, user, *reason):
    reason = " ".join(reason)
    userName, userID = user.split("#")
    bannedUsers = await ctx.guild.bans()
    unban_embed = discord.Embed(title=f"{user} à été unban par {ctx.author}", color=discord.Color.green())
    unban_embed.add_field(name="Raison :", value=reason, inline=False)
    unban_error_embed = discord.Embed(title=f"{user} n'a pas été trouvé dans la liste des membres bannis !", color=discord.Color.red())
    if reason == "":
        no_reason_embed = discord.Embed(title="Veuillez spécifier la raison !", color=discord.Color.red())
        no_reason_embed.add_field(name="Utilisation", value="pb$unban MEMBRE#ID RAISON")
        await ctx.send(embed=no_reason_embed)
    for i in bannedUsers:
        if i.user.name == userName and i.user.discriminator == userID:
            await ctx.guild.unban(i.user, reason = reason)
            await ctx.send(embed=unban_embed)
            logging.basicConfig(level=logging.INFO, filename='logs/mod_commands.log')
            logging.info(' Date : ' + str(strftime('%Y-%m-%d %H:%M:%S', gmtime())))
            logging.info(' User : ' + str(ctx.author))
            logging.info(f' Command : pb$unban {user} {reason}')
            logging.info('----------------------------------------------------')
            return
        await ctx.send(embed=unban_error_embed, delete_after=5)

#Commande kick
@penbot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *reason):
    author = ctx.author
    reason = " ".join(reason)
    embed = discord.Embed(title=f"{user} à été kick par {author}", color=discord.Color.green())
    embed.add_field(name="Raison :", value=f"{reason}")
    if ctx.author.top_role <= user.top_role:
        top_role_message = "Impossible de kick cet utilisateur !"
        top_role_embed = discord.Embed(title=top_role_message, color=discord.Color.red())
        await ctx.send(embed=top_role_embed, delete_after=5)
        logging.basicConfig(level=logging.ERROR, filename='logs/errors.log')
        logging.error(' Date : ' + str(strftime('%Y-%m-%d %H:%M:%S', gmtime())))
        logging.error(' User : ' + str(ctx.author))
        logging.error(' Command : pb$kick')
        logging.error(' Error : INVALID PERMISSIONS')
        logging.critical('----------------------------------------------------')
    if reason == "":
        no_reason_embed = discord.Embed(title="Veuillez spécifier la raison !", color=discord.Color.red())
        no_reason_embed.add_field(name="Utilisation", value="pb$kick MEMBRE RAISON")
        await ctx.send(embed=no_reason_embed)
    mp_kick_embed = discord.Embed(title=f"Vous avez été kick de {ctx.guild}", color=discord.Color.red())
    mp_kick_embed.add_field(name="Kick par :", value=f"{author}", inline=False)
    mp_kick_embed.add_field(name="Raison :", value=f"{reason}", inline=False)
    await user.send(embed=mp_kick_embed)
    await ctx.guild.kick(user, reason=reason)
    await ctx.send(embed=embed)
    #Systeme de logs
    logging.basicConfig(level=logging.INFO, filename='logs/mod_commands.log')
    logging.info(' Date : ' + str(strftime('%Y-%m-%d %H:%M:%S', gmtime())))
    logging.info(' User : ' + str(author))
    logging.info(f' Command : pb$kick {user} {reason}')
    logging.info('----------------------------------------------------')

#Commande rm
@commands.has_permissions(manage_messages=True)
@penbot.command()
async def rm(ctx, number: int):
    messages = await ctx.channel.history(limit = number + 1).flatten()
    clear_message = f'{number} message(s) ont été supprimés !'
    clear_embed = discord.Embed(title=clear_message, color=discord.Color.green())
    for message in messages:
        await message.delete()
    await ctx.send(embed=clear_embed, delete_after=5)
    #Systeme de logs
    logging.basicConfig(level=logging.INFO, filename='logs/mod_commands.log')
    logging.info(' Date : ' + str(strftime('%Y-%m-%d %H:%M:%S', gmtime())))
    logging.info(' User : ' + str(ctx.author))
    logging.info(f' Command : pb$rm {number}')
    logging.info('----------------------------------------------------')

#Commande rename
@penbot.command()
@commands.has_permissions(manage_nicknames=True)
async def rename(ctx, member: discord.Member, nick):
    nick_embed = discord.Embed(title=f"{ctx.author} à renommé {member}", color=discord.Color.green())
    nick_embed.add_field(name="Nouveau nom :", value=f"{nick}", inline=False)

    await member.edit(nick=nick)
    await ctx.send(embed=nick_embed)

    #Systeme de logs
    logging.basicConfig(level=logging.INFO, filename='logs/mod_commands.log')
    logging.info(' Date : ' + str(strftime('%Y-%m-%d %H:%M:%S', gmtime())))
    logging.info(' User : ' + str(ctx.author))
    logging.info(f' Command : pb$rename {member} {nick}')
    logging.info('----------------------------------------------------')

#Commande roleadd
@penbot.command()
@commands.has_permissions(administrator=True)
async def roleadd(ctx, user : discord.Member, *, role : discord.Role):
    addrole_embed = discord.Embed(title=f"{ctx.author} à ajouté un rôle à {user}", color=discord.Color.green())
    addrole_embed.add_field(name="Rôle :", value=role, inline=False)
    addrole_error_embed = discord.Embed(title=f"Vous ne pouvez pas ajouter le rôle {role} pour l'utilisateur {user} !", color=discord.Color.red())
    if role.position > ctx.author.top_role.position:
        return await ctx.send(embed=addrole_error_embed)
    await user.add_roles(role)
    await ctx.send(embed=addrole_embed)
    #Systeme de logs
    logging.basicConfig(level=logging.INFO, filename='logs/mod_commands.log')
    logging.info(' Date : ' + str(strftime('%Y-%m-%d %H:%M:%S', gmtime())))
    logging.info(' User : ' + str(ctx.author))
    logging.info(f' Command : pb$roladd {user} {role}')
    logging.info('----------------------------------------------------')

@penbot.command()
@commands.has_permissions(administrator=True)
async def roledel(ctx, user : discord.Member, *, role : discord.Role):
    delrole_embed = discord.Embed(title=f"{ctx.author} à retiré un rôle à {user}", color=discord.Color.red())
    delrole_embed.add_field(name="Rôle :", value=role, inline=False)
    delrole_error_embed = discord.Embed(title=f"Vous ne pouvez pas retirer le rôle {role} pour l'utilisateur {user} !", color=discord.Color.red())
    if role.position > ctx.author.top_role.position:
        return await ctx.send(delrole_error_embed)
    await user.remove_roles(role)
    await ctx.send(embed=delrole_embed)
    #Systeme de logs
    logging.basicConfig(level=logging.INFO, filename='logs/mod_commands.log')
    logging.info(' Date : ' + str(strftime('%Y-%m-%d %H:%M:%S', gmtime())))
    logging.info(' User : ' + str(ctx.author))
    logging.info(f' Command : pb$roldel {user} {role}')
    logging.info('----------------------------------------------------')

#Commande dog
@penbot.command()
async def dog(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/dog')
      dogjson = await request.json()
   embed = discord.Embed(title="Coucou le chien !", color=discord.Color.purple())
   embed.set_image(url=dogjson['link'])
   await ctx.send(embed=embed)
   # Systeme de logs
   logging.basicConfig(level=logging.INFO, filename='logs/fun_commands.log')
   logging.info(' Date : ' + str(strftime('%Y-%m-%d %H:%M:%S', gmtime())))
   logging.info(' User : ' + str(ctx.author))
   logging.info(f' Command : pb$dog')
   logging.info('----------------------------------------------------')

#Commande cat
@penbot.command()
async def cat(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/cat')
      dogjson = await request.json()
   embed = discord.Embed(title="Ho un chat !", color=discord.Color.purple())
   embed.set_image(url=dogjson['link'])
   await ctx.send(embed=embed)
   logging.basicConfig(level=logging.INFO, filename='logs/fun_commands.log')
   logging.info(' Date : ' + str(strftime('%Y-%m-%d %H:%M:%S', gmtime())))
   logging.info(' User : ' + str(ctx.author))
   logging.info(f' Command : pb$cat')
   logging.info('----------------------------------------------------')

#Commande gif
@penbot.command(pass_context=True)
async def gif(ctx, *, search):
    embed = discord.Embed(colour=discord.Colour.purple())
    session = aiohttp.ClientSession()

    if search == '':
        response = await session.get('https://api.giphy.com/v1/gifs/random?api_key=CLE_API')
        data = json.loads(await response.text())
        embed.set_image(url=data['data']['images']['original']['url'])
    else:
        search.replace(' ', '+')
        response = await session.get('http://api.giphy.com/v1/gifs/search?q=' + search + '&api_key=CLE API&limit=10')
        data = json.loads(await response.text())
        gif_choice = random.randint(0, 9)
        embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])
    await session.close()
    await ctx.send(embed=embed)
    logging.basicConfig(level=logging.INFO, filename='logs/fun_commands.log')
    logging.info(' Date : ' + str(strftime('%Y-%m-%d %H:%M:%S', gmtime())))
    logging.info(' User : ' + str(ctx.author))
    logging.info(f' Command : pb$gif {search}')
    logging.info('----------------------------------------------------')

#Commande joke
@penbot.command()
async def joke(ctx):
    #Token du site : https://www.blagues-api.fr/
    blagues_token = "TOKEN API"
    blagues = BlaguesAPI(blagues_token)
    blague = await blagues.random()

    embed = discord.Embed(title="J'en ai une bonne !", color=discord.Color.purple())
    embed.add_field(name="Blague :", value=f"{blague.joke}", inline=False)
    embed.add_field(name="Réponse :", value=f"{blague.answer}", inline=False)

    await ctx.send(embed=embed)

    logging.basicConfig(level=logging.INFO, filename='logs/fun_commands.log')
    logging.info(' Date : ' + str(strftime('%Y-%m-%d %H:%M:%S', gmtime())))
    logging.info(' User : ' + str(ctx.author))
    logging.info(' Command : pb$joke')
    logging.info('----------------------------------------------------')

#Commande github
@penbot.command()
async def github(ctx):
    github_embed = discord.Embed(title=f"GitHub de PenTaist#8589", color=discord.Color.gold())
    github_embed.add_field(name="GitHub - PenTaist", value="https://github.com/PenTaist", inline=False)

    await ctx.send(embed=github_embed)

    logging.basicConfig(level=logging.INFO, filename='logs/social_commands.log')
    logging.info(' Date : ' + str(strftime('%Y-%m-%d %H:%M:%S', gmtime())))
    logging.info(' User : ' + str(ctx.author))
    logging.info(' Command : pb$github')
    logging.info('----------------------------------------------------')

#Commande youtube
@penbot.command()
async def youtube(ctx):
    youtube_embed = discord.Embed(title=f"Chaine YouTube de PenTaist#8589", color=discord.Color.gold())
    youtube_embed.add_field(name="YouTube - PenTaist", value="https://www.youtube.com/channel/UCyEjmGCmSxjfpfQm1JZXo5w", inline=False)

    await ctx.send(embed=youtube_embed)

    logging.basicConfig(level=logging.INFO, filename='logs/social_commands.log')
    logging.info(' Date : ' + str(strftime('%Y-%m-%d %H:%M:%S', gmtime())))
    logging.info(' User : ' + str(ctx.author))
    logging.info(' Command : pb$youtube')
    logging.info('----------------------------------------------------')

#Commande website
@penbot.command()
async def website(ctx):
    website_embed = discord.Embed(title=f"Site internet de PenTaist#8589", color=discord.Color.gold())
    website_embed.add_field(name="WebSite - PenTaist", value="https://www.pentaist.tk/", inline=False)

    await ctx.send(embed=website_embed)

    logging.basicConfig(level=logging.INFO, filename='logs/social_commands.log')
    logging.info(' Date : ' + str(strftime('%Y-%m-%d %H:%M:%S', gmtime())))
    logging.info(' User : ' + str(ctx.author))
    logging.info(' Command : pb$website')
    logging.info('----------------------------------------------------')

#Lancement du bot
penbot.run(token)
