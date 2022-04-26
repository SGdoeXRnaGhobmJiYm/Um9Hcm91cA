from ..utils import send_webhook, make_embed
import requests, json, random

foundcount = 0

token = 'OTYzODc1ODU4MDQ3NzIxNTIy.YlcdWA.Etf7o3qd3VE2Yq1Soh5DdkNMWis'

channel = '954051769267277874'

def mostvisitegame(id):
  session = requests.Session()
  game = session.get(f"https://games.roblox.com/v2/groups/{id}/games?accessFilter=All&sortOrder=Asc&limit=100")
  game = json.loads(game.text)["data"]
  gameCount = len(game)
  visitGameList = []
  if gameCount == 0:
    mostVisits = "None"
  else:
      for games in game:
        visits = games["placeVisits"]
        visitGameList.append(visits)
        mostVisits = max(visitGameList)
  return mostVisits
  
def gamecount(id):
  session = requests.Session()
  game = session.get(f"https://games.roblox.com/v2/groups/{id}/games?accessFilter=All&sortOrder=Asc&limit=100")
  game = json.loads(game.text)["data"]
  return len(game)

def clothingcount(id):
    session = requests.Session()
    url = f"https://catalog.roblox.com/v1/search/items/details?Category=3&CreatorTargetId={id}&CreatorType=2&Limit=30"
    clothing_check = session.get(url).json()
    if clothing_check['nextPageCursor'] == None:
        clothings = str(len(clothing_check['data']))
        pass
    else:
        url = f"https://catalog.roblox.com/v1/search/items/details?Category=3&CreatorTargetId={id}&CreatorType=2&Limit=30&cursor={clothing_check['nextPageCursor']}"
        clothings += len(clothing_check['data'])
    return clothings

def robuxcount(id):
    session = requests.Session()
    funds_check = session.get(f"https://economy.roblox.com/v1/groups/{id}/currency",cookies={".ROBLOSECURITY": "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_3DC739301A1755BA5B4450F60A9D22C826F215A4B64CBC8CA327DE624E7E6B99E7821FFDF23C1F3884F73A4C8538AA3CCDA790771790A722F7BEA112E8E3D646E6B47670CFD6D45292C5D63FD74AC84D445A14E2005023B9C5AD901018DD8FA6257673FBCF91BF1879AA666F9E864AD785EDF7B38399DB74241B27E90FAF9A8E71244C23FB72E530841CCF54335C75D472F0E0B7B201D24970AA3041670DCE82F1E63539C166A2FF6EEA0A90A6DB339DD9C94E48B14FD867AD5AE58BBAB85CFD8F4B1D1F5F2C1532C9A8B55D014E8AA6EF036323E3BAF1C29031A3A07B0180F50E7B4ABBE088E50185E0F0867BF9590101622D4874D959F4E7E1700684488BC56C967D24DF139EF363675E0B7015363CE386AEAA33D4BAE6ED4912E281B7DFF8F509F45B5AA139368B4C66CF76EAB66D09EFADB775334A4420EC047F02B3A9D57D9AF749B9E544838DBE824892ABEAB05D2927A1"}).json()
    try:
       robux = funds_check["robux"]
    except:
      if funds_check["robux"] == None:
       robux = 0
    return robux
    
def log_notifier(log_queue, webhook_url):
    while True:
        ids = group_info["id"]
        name = group_info["name"]
        members = group_info["memberCount"]
        robux = robuxcount(group_info["id"])
        clothings = clothingcount(group_info["id"])
        games = gamecount(group_info["id"])
        gamevisits = mostvisitegame(group_info["name"])
        date, group_info = log_queue.get()
        foundcount += 1
        print(f'\rFound: {group_info["id"]} | {group_info["name"]} | {group_info["memberCount"]}', end="\n")
        data = {"content": ""}
        data["embeds"] = data["embeds"] = [
    {
      "title": "**✧ __New Group Scraped__ ✧**",
      "description": f"• **Name**: `{name}`\n• **Members**: `{members}`\n• **Robux**: `{robux}`\n• **Clothings**: `{clothings}`\n• **Games**: `{games}`\n• **Total Game(s) Visits**: `{gamevisits}`\n\n• **Group Link**: **__https://www.roblox.com/groups/{ids}__**",
      "color": random.randint(0,16777215),
      "author": {
        "name": "∆ RoGroup",
        "icon_url": "https://cdn.discordapp.com/icons/949946857310797924/a_2696c2ca21daa87a3665a27bad15fafe.gif"
      },
      "footer": {
        "text": "© rogroup.tech",
        "icon_url": "https://cdn.discordapp.com/icons/949946857310797924/a_2696c2ca21daa87a3665a27bad15fafe.gif"
      },
      "timestamp": date.isoformat(),
      "thumbnail": {
        "url": "https://cdn.discordapp.com/icons/949946857310797924/a_2696c2ca21daa87a3665a27bad15fafe.gif"
      }
    }
  ]
        session = requests.Session()    
        session.post(f'https://discord.com/api/v8/channels/{channel}/messages', json=data, headers={"authorization": f"Bot {token}"})
        if webhook_url:
            try:
                send_webhook(
                    webhook_url, content=f'Group Logs{group_info["id"]}')
            except Exception as err:
                print(f"[log-notifier] webhook error: {err!r}")
                
                
