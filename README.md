I made this as a fuck you to Banned who is selling a shitty script like this for 8.50 a month. This one will only cost you like a dollar per month as lolz.guru requires you to pay for market access.



Setup:

1. Go to https://zelenka.guru/account/api
2. Add a new client and enter whatever it doesn't matter just make sure you enter a valid url
3. Goto https://api.zelenka.guru/oauth/authorize?response_type=token&client_id=CLIENT_ID&scope=read+post+market replacing CLIENT_ID with your API key
4. Copy the access_token and paste that in the lolzAPI variable.
5. Go make a webhook and paste the url in the webhookURL variable.
6. Install the packages

```
pip install discord-webhook
pip install requests
```
