appVersion = 1.0
appStatus = 'Alpha'

# TOKEN GEHEIM!!!
token = 'NzM5NTU2Njc4ODMxMTc3NzQw.XycL1A.e-P2anfPzTci0SMyR6LzPuz95kA'

# HeyStyx Discord Bot
# For information, see: github.com/nsde/heystyx/
# Created in 2020 with <3 by:
# Felix Orosz (github@nsde) and Benedikt (github@beban09)
# Huge thanks to 'The Morpheus Tutorials' and 'https://leovoel.github.io/embed-visualizer/'

import json
import discord as dc
import requests as rq
import wikipedia as wiki
from time import asctime, sleep, localtime, time
from random import randint as rdi

cmdPrefix = '§'
wiki.set_lang('de')
lang = 'de'

class MyClient(dc.Client):
    #Einloggen
    async def on_ready(self):
        print('Eingeloggt.')
        channel = self.get_channel(740526658699657306)
        
        timeEdit = str(asctime(localtime(time())))
        timeEdit = timeEdit.replace('  ', '')
        timeList = timeEdit.split(' ')
        timeEdit = timeList[2]
        timeEdit += ', ' + timeList[1] + '. '

        await client.change_presence(status=dc.Status.online, activity=dc.Game('seit ' + timeEdit))
        await channel.send(':green_circle: Bot jetzt online. Zeit: ' + timeEdit)

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
            print(message.content)
            cmd = message.content
            cmdEnd = cmd[6:]
            wikiSearch = wiki.search(cmdEnd)
            wikiSearch = str(wikiSearch[:5])
            wikiSearch = wikiSearch.replace("'",'"') # lol
            wikiSearch = wikiSearch.replace('[','')
            wikiSearch = wikiSearch.replace(']','')

            wikiSum = wiki.summary(cmdEnd, sentences=10)
            wikiSum = wikiSum.replace('== ', ':white_medium_small_square: **')
            wikiSum = wikiSum.replace(' ==', '**')
            wikiSum = wikiSum.replace('''

''', '''
''')

            wikiSum = wikiSum.replace('=:white_medium_small_square: ', ':white_small_square: ')
            wikiSum = wikiSum.replace('''=
''', '\n')

            try:
                outp_Content = ':mag_right: Ähnliche Themen: ' + wikiSearch + ' \n'+ '▔'*50 + '\n' + wikiSum

            except:
                outp_Content = (':x: Tut mir leid, da ist wohl was schief gelaufen. Versuche es nochmal!')

            try:
                # await message.channel.send(outp_Content)
                embed = dc.Embed(colour=dc.Colour(0x52b0ff), description=f'{outp_Content}')
                embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/270px-Wikipedia-logo-v2.svg.png')
                embed.set_author(name='Wikipedia Search')
                embed.set_footer(text='HeyStyx Bot', icon_url='https://betaneostyx.files.wordpress.com/2020/07/dcstyxbot-1.png')
                await channel.send(embed=embed)

            # except:

            #     try:
            #         await message.channel.send(outp_Content[:2000] + '\n _Artikel gekürzt._')

            except:
                await message.channel.send(':x: Der Begriff "'+ cmdEnd + '" konnte leider nicht gefunden werden. Möglicherweise ist "' + lang + '" die falsche Sprache?')


        if message.content.startswith(cmdPrefix + 'wiki.lang'):
            cmd = message.content
            lang = cmd[11:]
            wiki.set_lang(cmdEnd) # leider funktioniert try-except hier nicht richtg :(
            await message.channel.send(':white_check_mark: Sprache geändert zu "' + lang + '".')
            

        if message.content.startswith(cmdPrefix + 'py'):
            cmd = message.content
            cmdEnd = cmd[4:]
            
            try:
                outpCMD = eval(cmdEnd)

                if outpCMD == 'None' or outpCMD == '':
                    outpCMD = ':warning: Ausgabe ist leer.'

                elif outpCMD == 69:
                    outpCMD = "( ͡° ͜ʖ ͡°)"
                    # outpCMD = "(\u0361\u00B0\u035C\u0296\u0361\u00B0)" # lennyface easteregg

                else:
                    pass

                await message.channel.send('```' + str(outpCMD) + '```')

            except:
                await message.channel.send(':x: Ungültiger "eval()"-Befehl. Versuche es noch einmal.')

        
        if message.content.startswith(cmdPrefix + 'off ' + str(botPw)):
            timeEdit = str(asctime(localtime(time())))
            timeEdit = timeEdit.replace('  ', '')
            timeList = timeEdit.split(' ')
            timeEdit = timeList[2]
            timeEdit += ', ' + timeList[1] + '. '

            channel = self.get_channel(740526658699657306)
            await client.change_presence(status=dc.Status.idle, activity=dc.Game('off seit ' + timeEdit))
            await message.channel.send('Neues Passwort wurde generiert.\n :warning: **BOT WIRD UMPROGRAMMIERT!**')
            await channel.send(':red_circle: Bot jetzt inaktiv. Zeit: ' + timeEdit)

            botPw = rdi(0,999)
            print(botPw)


        if message.content.startswith(cmdPrefix + 'on ' + str(botPw)):
            timeEdit = str(asctime(localtime(time())))
            timeEdit = timeEdit.replace('  ', '')
            timeList = timeEdit.split(' ')
            timeEdit = timeList[2]
            timeEdit += ', ' + timeList[1] + '. '

            channel = self.get_channel(740526658699657306)
            await client.change_presence(status=dc.Status.online, activity=dc.Game('wieder seit ' + timeEdit))
            await message.channel.send('Neues Passwort wurde generiert.\n :green_circle: **BOT WIEDER AKTIV!**')
            await channel.send(':blue_circle: Bot wieder online. Zeit: ' + timeEdit)

            botPw = rdi(0,999)
            print(botPw)



# Client Run
client = MyClient()
client.run(token)