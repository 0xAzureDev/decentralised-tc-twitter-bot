# Decentralised THORChain Twitter Bot

A proposal consensus mechanism for decentralising [@THORChain](https://twitter.com/THORChain)'s twitter account.

## How to download it

- Clone/Download the repository
  - To clone it and get the updates you can definitely use the command
    `git clone`
- Create a discord bot [here](https://discord.com/developers/applications)
- Get your bot token
- Invite your bot on servers using the following invite:
  <https://discord.com/oauth2/authorize?&client_id=YOUR_APPLICATION_ID_HERE&scope=bot+applications.commands&permissions=PERMISSIONS> (
  Replace `YOUR_APPLICATION_ID_HERE` with the application ID and replace `PERMISSIONS` with the required permissions
  your bot needs that it can be get at the bottom of a this
  page <https://discord.com/developers/applications/YOUR_APPLICATION_ID_HERE/bot>)
- Follow this tutorial on how to setup your Twitter account authentication: <https://youtu.be/BdmUhQnPToM>

## How to set up

To set up the bot I made it as simple as possible. I now created a [config.json](config.json) file where you can put the
needed things to edit.

Here is an explanation of what everything is:

| Variable                      | What it is                                     |
| ----------------------------- | ---------------------------------------------- |
| YOUR_BOT_PREFIX_HERE          | The prefix you want to use for normal commands |
| YOUR_BOT_TOKEN_HERE           | The token of your bot                          |
| YOUR_API_KEY_HERE             | Twitter API key                                |
| YOUR_API_SECRET_HERE          | Twitter API secret key                         |
| YOUR_BEARER_TOKEN_HERE        | Twitter bearer token                           |
| YOUR_ACCESS_TOKEN_HERE        | Twitter access token                           |
| YOUR_ACCESS_TOKEN_SECRET_HERE | Twitter access token secret                    |

## How to start

To start the bot you simply need to launch, either your terminal (Linux, Mac & Windows), or your Command Prompt (
Windows)
.

Before running the bot you will need to install all the requirements with this command:

```bash
pip install -r requirements.txt
```

If you have multiple versions of python installed (2.x and 3.x) then you will need to use the following command:

```bash
python3 bot.py
```

or eventually

```bash
python3.x bot.py
```

Replace `x` with the version of Python you have installed.

If you have just installed python today, then you just need to use the following command:

```bash
python bot.py
```

## Built With

- [Python 3.9.12](https://www.python.org/)

## Contributing

1. Fork it (<https://github.com/0xAzureDev/decentralised-tc-twitter-bot/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'feat: some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## License

Distributed under the `MIT` License. See `LICENSE` for more information.
LicenseContributing

### Disclaimer: Template forked from [kkrypt0nn](https://github.com/kkrypt0nn/Python-Discord-Bot-Template)
