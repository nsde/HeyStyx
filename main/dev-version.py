appVersion = 1.0
appStatus = 'Alpha'

# !!! TOKEN IS IN THE FILE "token.txt" !!!
# HeyStyx Discord Bot
# For information, see: github.com/nsde/heystyx/
# Created in 2020 with <3 by:
# Felix Orosz (github@nsde) and Benedikt (github@beban09)
# Huge thanks to 'The Morpheus Tutorials' and 'https://leovoel.github.io/embed-visualizer/'

import json
import discord as dc # pip install discord
import requests as rq # pip install requests
import wikipedia as wiki # pip install wikipedia
from time import asctime, sleep, localtime, time
from random import randint as rdi

cmdPrefix = '§'
wiki.set_lang('de')
lang = 'de'

# read token
tokenpath = __file__.replace('main.py','token.txt')
with open (tokenpath,'r') as tokenFile:
    token = tokenFile.readlines()
    token = token[0]
    print(token)

class MyClient(dc.Client):

    # log-in
    async def on_ready(self):
        print('Eingeloggt.')
        channel = self.get_channel(740526658699657306) # set log-channel
        
        # build time and format correctly
        timeEdit = str(asctime(localtime(time())))
        timeEdit = timeEdit.replace('  ', '')
        timeList = timeEdit.split(' ')
        timeEdit = timeList[2]
        timeEdit += ', ' + timeList[1] + '. '

        # set status and log
        await client.change_presence(status=dc.Status.online, activity=dc.Game('seit ' + timeEdit))
        await channel.send(':green_circle: Bot jetzt online. Zeit: ' + timeEdit)

        # refresh password
        botPw = rdi(0,999)
        print(botPw)


    async def on_error(self):
        print('Bot-Fehler')

    async def on_disconnect(self):
        print('Bot geschlossen.')
    

    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith(cmdPrefix + 'wiki '):
            # load wiki page
            print(message.content)
            cmd = message.content
            cmdEnd = cmd[6:]
            wikiSearch = wiki.search(cmdEnd)
            wikiSearch = str(wikiSearch[:5])

            # clean-up wiki-search
            wikiSearch = wikiSearch.replace("'",'"')
            wikiSearch = wikiSearch.replace('[','')
            wikiSearch = wikiSearch.replace(']','')

            # clean-up headings
            wikiSum = wiki.summary(cmdEnd, sentences=10)
            wikiSum = wikiSum.replace('== ', ':white_medium_small_square: **')
            wikiSum = wikiSum.replace(' ==', '**')
            wikiSum = wikiSum.replace('''

''', '''
''') # delete unnecessary lines

            # clean-up subheadings
            wikiSum = wikiSum.replace('=:white_medium_small_square: ', ':white_small_square: ')
            wikiSum = wikiSum.replace('''=
''', '\n') # delete unnecessary lines

            try:
                searchTopics = ':mag_right: Ähnliche Themen: ' + wikiSearch + ' \n'+ '▔'*50 + '\n' + wikiSum # suggest similar topics

            except:
                outp_Content = (':x: Tut mir leid, da ist wohl was schief gelaufen. Versuche es nochmal!')

            try:
                # generate embed and send
                embed = dc.Embed(colour=dc.Colour(0x52b0ff), description=f'{outp_Content}')
                embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/270px-Wikipedia-logo-v2.svg.png')
                embed.set_author(name='Wikipedia Search')
                embed.set_footer(text='HeyStyx Bot', icon_url='https://betaneostyx.files.wordpress.com/2020/07/dcstyxbot-1.png')
                embedMsg = await message.channel.send(embed=embed)

            # except:

            #     try:
            #         await message.channel.send(outp_Content[:2000] + '\n _Artikel gekürzt._')

            except:
                await message.channel.send(':x: Der Begriff "'+ cmdEnd + '" konnte leider nicht gefunden werden. Möglicherweise ist "' + lang + '" die falsche Sprache?')


        if message.content.startswith(cmdPrefix + 'wiki.lang'):
            cmd = message.content
            lang = cmd[11:]
            wiki.set_lang(cmdEnd) # try-except doesn't work here somehow
            await message.channel.send(':white_check_mark: Sprache geändert zu "' + lang + '".')
            

        if message.content.startswith(cmdPrefix + 'py'):
            # build command
            cmd = message.content
            cmdEnd = cmd[4:]
            
            try:
                outpCMD = eval(cmdEnd)

                if outpCMD == 'None' or outpCMD == '':
                    outpCMD = ':warning: Ausgabe ist leer.'

                else:
                    pass

                await message.channel.send('```' + str(outpCMD) + '```') # send as code-block in discord

            except:
                await message.channel.send(':x: Ungültiger "eval()"-Befehl. Versuche es noch einmal.')

        
        if message.content.startswith(cmdPrefix + 'off ' + str(botPw)):
            # build time and format it correctly
            timeEdit = str(asctime(localtime(time())))
            timeEdit = timeEdit.replace('  ', '')
            timeList = timeEdit.split(' ')
            timeEdit = timeList[2]
            timeEdit += ', ' + timeList[1] + '. '

            # set status and log
            channel = self.get_channel(740526658699657306)
            await client.change_presence(status=dc.Status.idle, activity=dc.Game('off seit ' + timeEdit))
            await message.channel.send('Neues Passwort wurde generiert.\n :warning: **BOT WIRD UMPROGRAMMIERT!**')
            await channel.send(':red_circle: Bot jetzt inaktiv. Zeit: ' + timeEdit)

            # refresh password and print it
            botPw = rdi(0,999)
            print(botPw)


        if message.content.startswith(cmdPrefix + 'on ' + str(botPw)):
            # build time and format it correctly
            timeEdit = str(asctime(localtime(time())))
            timeEdit = timeEdit.replace('  ', '')
            timeList = timeEdit.split(' ')
            timeEdit = timeList[2]
            timeEdit += ', ' + timeList[1] + '. '

            # set status and log
            channel = self.get_channel(740526658699657306)
            await client.change_presence(status=dc.Status.online, activity=dc.Game('wieder seit ' + timeEdit))
            await message.channel.send('Neues Passwort wurde generiert.\n :green_circle: **BOT WIEDER AKTIV!**')
            await channel.send(':blue_circle: Bot wieder online. Zeit: ' + timeEdit)

            # refresh password and print it
            botPw = rdi(0,999)
            print(botPw)



# client run
client = MyClient()
client.run(token)
