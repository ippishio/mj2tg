# Midjourney to Telegram Bot🖌️🤖 

## About
Telegram bot that allows to interact with Midjourney using automated user client and discord bot.

## ⚠️WIP⚠️
 - Minor changes to `DiscordBot` class
 - Change the type of interaction between scripts (currently getting results from cout using PIPE)
 - Queue for image generation
 - MidJourney arguments for the prompt
  
## Quick start
```console
foo@bar:~$ pipenv install
foo@bar:~$ pipenv run python main.py
```
Note that for the first launch you should set `debug=True` in `Discord Bot` class in [main.py](main.py?plain=1#L10), so you can pass the CAPTCHA. This need to be done once, to create authorized session.

