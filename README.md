# Discord.py-BotBase

<details>
    <summary>Manually</summary>
  
Only tested on python 3.8

```bash
git clone https://github.com/Roxedus/Discord.py-BotBase botbase
python -m pip install -r /botbase/requirements.txt
cp /botbase/settings.example.json /botbase/data/settings.json
```

</details>

<details>
  <summary>Docker</summary>

This image does __not__ exist, its just a placeholder

Example docker-compose.yml

```yml
  base:
    container_name: botbase
    image: roxedus/botbase:latest
    networks:
      - internal
    volumes:
      - ./botbase:/app/data
```
  
</details>

Create [bot-token](https://discordapp.com/developers/docs/topics/oauth2#bots), and baste it in the token field in the `/botbase/data/settings.json` file.

You are now set to start.
