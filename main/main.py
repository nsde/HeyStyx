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
from time import asctime, sleep, localtime, time
from random import randint as rdi

cmdPrefix = '.'
wiki.set_lang('de')
lang = 'de'

class MyClient(dc.Client):

    #Einloggen
    async def on_ready(self):
        print('Eingeloggt.')
        channel = self.get_channel(740526658699657306) # der Log-Channel
        
        # Uhrzeit für den Log aufbauen
        timeEdit = str(asctime(localtime(time())))
        timeEdit = timeEdit.replace('  ', '')
        timeList = timeEdit.split(' ')
        timeEdit = timeList[2]
        timeEdit += ', ' + timeList[1] + '. '

        # Status setzen und loggen
        await client.change_presence(status=dc.Status.online, activity=dc.Game('seit ' + timeEdit))
        await channel.send(':green_circle: Bot jetzt online. Zeit: ' + timeEdit)

        # Passwort aktualisieren und ausgeben
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
            # Wiki-Seite laden
            print(message.content)
            cmd = message.content
            cmdEnd = cmd[6:]
            wikiSearch = wiki.search(cmdEnd)
            wikiSearch = str(wikiSearch[:5])

            # schöner machen
            wikiSearch = wikiSearch.replace("'",'"')
            wikiSearch = wikiSearch.replace('[','')
            wikiSearch = wikiSearch.replace(']','')

            # Überschriften schöner machen
            wikiSum = wiki.summary(cmdEnd, sentences=10)
            wikiSum = wikiSum.replace('== ', ':white_medium_small_square: **')
            wikiSum = wikiSum.replace(' ==', '**')
            wikiSum = wikiSum.replace('''

''', '''
''') # unnötig große Zeilenumbrüche ersetzen

            # Unterüberschriften schöner machen
            wikiSum = wikiSum.replace('=:white_medium_small_square: ', ':white_small_square: ')
            wikiSum = wikiSum.replace('''=
''', '\n') # unnötig große Zeilenumbrüche ersetzen

            try:
                searchTopics = ':mag_right: Ähnliche Themen: ' + wikiSearch + ' \n'+ '▔'*50 + '\n' + wikiSum # ähnliche Themen vorschlagen

            except:
                outp_Content = (':x: Tut mir leid, da ist wohl was schief gelaufen. Versuche es nochmal!')

            try:
                # Embed erzeugen und absenden
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
            wiki.set_lang(cmdEnd) # leider funktioniert try-except hier nicht richtg :(
            await message.channel.send(':white_check_mark: Sprache geändert zu "' + lang + '".')
            

        if message.content.startswith(cmdPrefix + 'py'):
            # Befehl aufbauen
            cmd = message.content
            cmdEnd = cmd[4:]
            
            try:
                outpCMD = eval(cmdEnd)

                if outpCMD == 'None' or outpCMD == '':
                    outpCMD = ':warning: Ausgabe ist leer.'

                else:
                    pass

                await message.channel.send('```' + str(outpCMD) + '```') # als Code-Block ausgeben

            except:
                await message.channel.send(':x: Ungültiger "eval()"-Befehl. Versuche es noch einmal.')

        
        if message.content.startswith(cmdPrefix + 'off ' + str(botPw)):
            # Uhrzeit für den Log aufbauen
            timeEdit = str(asctime(localtime(time())))
            timeEdit = timeEdit.replace('  ', '')
            timeList = timeEdit.split(' ')
            timeEdit = timeList[2]
            timeEdit += ', ' + timeList[1] + '. '

            # Status setzen und loggen
            channel = self.get_channel(740526658699657306)
            await client.change_presence(status=dc.Status.idle, activity=dc.Game('off seit ' + timeEdit))
            await message.channel.send('Neues Passwort wurde generiert.\n :warning: **BOT WIRD UMPROGRAMMIERT!**')
            await channel.send(':red_circle: Bot jetzt inaktiv. Zeit: ' + timeEdit)

            # Passwort aktualisieren und ausgeben
            botPw = rdi(0,999)
            print(botPw)


        if message.content.startswith(cmdPrefix + 'on ' + str(botPw)):
            # Uhrzeit für den Log aufbauen
            timeEdit = str(asctime(localtime(time())))
            timeEdit = timeEdit.replace('  ', '')
            timeList = timeEdit.split(' ')
            timeEdit = timeList[2]
            timeEdit += ', ' + timeList[1] + '. '

            # Status setzen und loggen
            channel = self.get_channel(740526658699657306)
            await client.change_presence(status=dc.Status.online, activity=dc.Game('wieder seit ' + timeEdit))
            await message.channel.send('Neues Passwort wurde generiert.\n :green_circle: **BOT WIEDER AKTIV!**')
            await channel.send(':blue_circle: Bot wieder online. Zeit: ' + timeEdit)

            # Passwort aktualisieren und ausgeben
            botPw = rdi(0,999)
            print(botPw)



# Client Run
client = MyClient()
client.run(token)
