appVersion = 1.0
appStatus = 'Alpha'

# TOKEN GEHEIM!!!
token = ''

# HeyStyx Discord Bot
# For information, see: github.com/nsde/heystyx/
# Created in 2020 with <3 by:
# Felix Orosz (github@nsde) and Benedikt (github@beban09)
# Huge thanks to 'The Morpheus Tutorials' and 'https://leovoel.github.io/embed-visualizer/'

import json
import discord as dc
import requests as rq
import wikipedia as wiki
from random import randint as rdi

cmdPrefix = '§'
wiki.set_lang('de')
lang = 'de'

class MyClient(dc.Client):
    #Einloggen
    async def on_ready(self):
        print('Eingeloggt.')
        await client.change_presence(activity=dc.Activity(type=dc.ActivityType.listening, name="eure Befehle!"))



    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith(cmdPrefix + 'wiki '):
            print(message.content)
            cmd = message.content
            cmdEnd = cmd[6:]
            wikiSearch = wiki.search(cmdEnd)
            wikiSearch = str(wikiSearch)
            wikiSearch = wikiSearch.replace("'",'"') # lol
            wikiSearch = wikiSearch.replace('[','')
            wikiSearch = wikiSearch.replace(']','')

            try:
                outp_Content = ':mag_right: Ähnliche Themen für den Suchbegriff: ' + wikiSearch + ' :mag_right: \n\n' + wiki.summary(cmdEnd, sentences = 1000)
            except:
                outp_Content = (':x: Tut mir leid, da ist wohl was schief gelaufen. Versuche es nochmal!')

            try:
                await message.channel.send(outp_Content)

            except:
                try:
                    await message.channel.send(outp_Content[:1900] + '**...\n :exclamation: Der Artikel musste aus technischen Gründen gekürzt werden!**')

                except:
                    await message.channel.send(':x: Der Begriff "'+ cmdEnd + '" konnte leider nicht gefunden werden. Möglicherweise ist "' + lang + '" die falsche Sprache?')


        if message.content.startswith(cmdPrefix + 'wiki.lang'):
            cmd = message.content
            lang = cmd[11:]
            wiki.set_lang(cmdEnd) # leider funktioniert try-except hier nicht richtg :(
            await message.channel.send(':white_check_mark: Sprache geändert zu "' + lang + '".')
            


                # embed = dc.Embed(colour=dc.Colour(0x52b0ff), description=f'{outp_Content}')
                # embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/270px-Wikipedia-logo-v2.svg.png')
                # embed.set_author(name='Wikipedia Search')
                # embed.set_footer(text='HeyStyx Bot', icon_url='https://betaneostyx.files.wordpress.com/2020/07/dcstyxbot-1.png')
                # message.channel.send(embed=embed)

        if message.content.startswith(cmdPrefix + 'cmd'):
            cmd = message.content
            cmdEnd = cmd[5:]
            
            try:
                outpCMD = exec(cmdEnd)
                await message.channel.send(outpCMD)

            except:
                await message.channel.send('Ungültiger Befehl. Versuche es noch einmal.')



# Client Run
client = MyClient()
client.run(token)
