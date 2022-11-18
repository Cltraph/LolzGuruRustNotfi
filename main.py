import sqlite3
from lolzapi import LolzteamApi
from time import sleep
from discord_webhook import DiscordWebhook, DiscordEmbed
from datetime import datetime


connection_obj = sqlite3.connect(r'database.db')
brandName = ""
webhookURL = ""
lolzAPI = ""
banned = False

while True:
    api = LolzteamApi(lolzAPI)
    response = api.market_list("steam",pmax=403, optional={'game[]': '252490'})
    for listings in response['items']:
        cur = connection_obj.cursor()
        cur.execute("""SELECT ids FROM listings WHERE ids=(?)""", (int(listings['item_id']),))
        result = cur.fetchone()
        if result:
            continue
        else:
            for bans in listings['account_bans']:
                if int(bans) == 252490:
                    banned = True
            webhook = DiscordWebhook(url=webhookURL, rate_limit_retry=True)
            embed = DiscordEmbed(description=f"> **Item price:** {str(listings['price'])}\n> **Rust hours:** {str(listings['account_full_games']['list']['252490']['playtime_forever'])}\n> **Guarantee time:** {listings['guarantee']['durationPhrase']}\n> **Banned:** {banned}\n> **Last active:** {datetime.utcfromtimestamp(int(listings['account_last_activity'])).strftime('%Y-%m-%d %H:%M:%S')}\n> **Publish date:** {datetime.utcfromtimestamp(int(listings['published_date'])).strftime('%Y-%m-%d %H:%M:%S')}", color='03b2f8')
            embed.set_timestamp()
            embed.set_author(name='Rust Account', url=str(listings['accountLink']).removesuffix('/steam-preview'))
            embed.set_footer(text=brandName)
            webhook.add_embed(embed)
            response = webhook.execute()
            cur.execute("INSERT INTO listings(ids) VALUES (?)", (listings['item_id'],))
            connection_obj.commit()
        
    sleep(5)
    