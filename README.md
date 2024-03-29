# PaLM-Discord-Bot

Google PaLM API in Discord.

![](https://img.shields.io/badge/License-MIT-lightgrey)

~~Google PaLM API only works in the United States.~~

## Notice

Discord only can handle 2000 characters per message, so I manually set the PaLM can only outputting no more than 145 tokens. If your channel can handle 4000 or even more, make the `output_token_limit= 145` in `main.py` value doubled or more.

Also, I dropped the temperature option, you can always add it back.

## To-do

- **Adapt the latest Google Vertex AI platform for Gemini(pro)**
- Use .env instead
- Integrate this with any other AIGC APIs and make this more versatile?


## Example:
![](https://github.com/nonefffds/PaLM-Discord-Bot/blob/main/image/test.png)
![](https://github.com/nonefffds/PaLM-Discord-Bot/blob/main/image/test2.png)

## Command

`/palm` to chat with PaLM.

## Installation

### Get your Discord API

1. Go [Discord Dev](https://discord.com/developers/applications)
2. Go `Application` on the left part
3. Go `New Application`, create a new Bot
4. Go `Bot` on the left
5. Click `Add bot`
6. Turn on `MESSAGE CONTENT INTENT`
7. `Save Change`
8. View and save your API Key on the top of page `View Token`, or reset one if you don't remember
9. Click OAuth2 on the left part
10. Click on `URL Generator`
11. Choose `bot` in `SCOPES`, `Administrator` in `BOT PERMISSIONS`
12. Copy the link at bottom into your browser, add bot and authorize to you server.
### Get your PaLM API
1. Join the waitlist [here](https://developers.generativeai.google/), after you passed the waitlist, you'll receive an email like this:
![](https://github.com/nonefffds/PaLM-Discord-Bot/blob/main/image/welcome.png)
1. Go [MakerSuite](https://makersuite.google.com/), and create an API key for this application.
### Deploy on your machine
1. Star this project I guess
2. git clone this repository
3. `pip install discord google-generativeai`
4. `cd PaLM-Discord-Bot`
5. `nano main.py`
6. replace with your Discord API Key and PaLM API Key at following lines:
`palm.configure(api_key = "PaLM_API_KEY")`
`client.run("DISCORD_TOKEN")`
7. `python3 main.py`

If you want to run it background, you can try Screen.

## Reference: 

Huge thanks to following projects.

https://github.com/TheExplainthis/ChatGPT-Discord-Bot

https://discordpy.readthedocs.io/en/stable/#getting-started

https://developers.generativeai.google/api/python/google/generativeai

## License:
This work is under MIT License.
