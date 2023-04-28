# StreamCraftRemote
## Introduction
Remote service that connects the StreamCraft twitch extension to your minecrat server. This allows you to configure minecraft commands your viewers can trigger, that directly effect your server! The streamcraftremote service runs on the streamers computer and communicates between twitch and your minecraft server.

## Requirements
You need to have your own private (Java) Minecraft server, you can use a Hosted server, run a Docker container or run the server jar download here (https://www.minecraft.net/en-us/download/server). This will not work with Bedrock (yet). Your server needs to have RCon Enabled, to do this you need both of these properties set in your server.properties file. (Yes you need to specify a password, not blank)
> rcon.port=25575 \
rcon.password=secret

Alternatively, you can use the docker examples below which can set up a minecraft server for you.

### Version info
You may try other versions, but here are the versions streamcraftremote.py has been tested with:
* (Java) Minecraft server > 1.18.1
* Python 3.9.6
* pip 21.1.3 
* Flask==2.0.2
* mctools==1.1.2
* The Port 3210 needs to be open on the streamers computer

### Windows
Download the pre compiled version of streamcraftremote.exe under Release (https://github.com/chilliwebs/StreamCraftRemote/releases/tag/1.0.0). And double click the streamcraftremote.exe. It will open a command terminal and also create a log of transactions and actions triggered by your viewers under streamcraftremote.log

### Python (supports multiple OS)
Download this GitHub repo as a zip file (see the green "code" button, and select "Download ZIP") \
Next download python download here (https://www.python.org/downloads/). You can then run pip to install the dependencies and run the script using the commands below:
> pip install -r requirements.txt \
python streamcraftremote.py

### Docker
Download this GitHub repo as a zip file (see the green "code" button, and select "Download ZIP") \
You will then need to download Docker or Docker Desktop download here (https://www.docker.com/products/docker-desktop)
And from here you have 2 options you can individually run the docker containers for a minecraft server and streamcraftremote using the following commands:
* Note: that rcon options are already specified for you, and you can change the RCON_PASSWORD. Just remember the password and port you pick because those are needed when setting up the StreamCraft extension on your Twitch extension dashboard. You can read more information on this minecraft server container here https://github.com/itzg/docker-minecraft-server

For the minecraft server:
> docker run -d -p 25565:25565 -p 25575:25575 -e ENABLE_RCON=true -e RCON_PASSWORD=secret -e BROADCAST_RCON_TO_OPS=FALSE -e EULA=TRUE --name mc itzg/minecraft-server

For the streamcraftremote service (these commands need to be executed in the folder where you downloaded streamcraftremote source from GitHub):
> docker build -t streamcraftremote . \
docker run -it -p 3210:3210 --name streamcraftremote streamcraftremote

Another option is to run the docker-compose.yaml supplied which will start up both the minecraft server and streamcraftremote for you
* Note: that rcon options are specified in the docker-compose.yaml
> docker compose up

(this command needs to be executed in the folder where you downloaded streamcraftremote source from GitHub)

## Configure
![extension_config1](https://github.com/chilliwebs/StreamCraftRemote/blob/main/docs/extension_config1.jpg?raw=true)

**If you dont see the green "connected" check your minecraft server settings**

Navigate to your extensions in your twitch streamer dashboard and click configure (looks like a gear icon). From here you need to specify:
* "host/ip address" (in most cases should be "localhost" unless you use a minecraft server hosting service, \
 if you are running the remote and server in a docker shown above this needs to be "172.17.0.1" or "host.docker.internal" or "docker.for.mac.host.internal") 
* "port number" (this is 25575 unless you changed it) and password (secret unless you changed it)

You can see next to remote status as the twitch extension periodically checks for the running streamcraftremote service.
* "not connected, remote not running?" means you have not started streamcraftremote
* "remote detected, but cannot connect to rcon, is the minecraft server running?" indicates that your minecraft server is not running is unreachable or your rcon configuration does not match what you have for your server
* "connected, script executed" means the StreamCraft twitch config can now send commands to your server

You can now test this out by entering a valid minecraft slash command (without the slash) into the text area and click "Test Command" here are some examples:
> say Hello StreamCraft! \
> execute at @p run summon zombie

You can enter multiple commands on separate lines and streamcraftremote will execute each one in order!

You can now click "Add an Action" and begin setting up viewer actions. "display" is the text placed on the action displayed to your viewer in thier extension panel and mobile phone. Next you need to assign "bits" to this action (you are limited to the number of actions at a specific bit). "description" helps communicate to the viewer what the action does. "command" is the single or multiple minecraft commands you want to execute when the viewer chooses this action.

You can log into your private minecraft server and test these actions out easily by clicking the "Test" button

Don't forget to click "Save Configuration" often so you don't lose your customizations.

## Usage
In order for StreamCraft to work you need to have the StreamCraft twitch live popout window open, and the streamcraftremote running on your streaming computer. You can open this window from your "Stream Manager", on the right side there are "Quick Actions" and StreamCraft should be visible (if you installed it under "Extensions -> My Extensions"). There are 3 different ways to run the streamcraftremote service: windows exe, python script, and Docker container.

**Remember to open your live panel from your stream manager!**

![stream_manager](https://github.com/chilliwebs/StreamCraftRemote/blob/main/docs/stream_manager.jpg?raw=true)

**This window has to remain open inorder for it to send twitch commands to StreamCraftRemote!**

![live_panel](https://github.com/chilliwebs/StreamCraftRemote/blob/main/docs/live_panel.jpg?raw=true)

**Run StreamCraftRemote.exe! and see logs for user actions**

![streamcraft_remote_terminal](https://github.com/chilliwebs/StreamCraftRemote/blob/main/docs/streamcraft_remote_terminal.jpg?raw=true)

**clicking the sliker "temporarily disable actions for viewers", will block user actions and show "Please wait for streamer to start"**

## Troubleshooting

**If your viewers see this:**

![viewer_panel_waiting](https://github.com/chilliwebs/StreamCraftRemote/blob/main/docs/viewer_panel_waiting.jpg?raw=true)

**It means either you are not running the live panel mention above, or your server and remote are not running**

![live_panel_noremote](https://github.com/chilliwebs/StreamCraftRemote/blob/main/docs/live_panel_noremote.jpg?raw=true)

![live_panel_noserver](https://github.com/chilliwebs/StreamCraftRemote/blob/main/docs/live_panel_noserver.jpg?raw=true)

**in the config you see this, it means you are running the StreamCraftRemote.exe**

![extension_config3](https://github.com/chilliwebs/StreamCraftRemote/blob/main/docs/extension_config3.jpg?raw=true)

**this error means your server is not running or, the rcon password, host/ip/port is incorrect**

![extension_config4](https://github.com/chilliwebs/StreamCraftRemote/blob/main/docs/extension_config4.jpg?raw=true)

**If you see these errors repeated in the StreamCraftRemote.exe, it means StreamCraftRemote is unable to connect to your minecraft server, and its is not running or, the rcon password, host/ip/port is incorrect**

![streamcraft_remote_terminal](https://github.com/chilliwebs/StreamCraftRemote/blob/main/docs/streamcraft_remote_terminal_err.jpg?raw=true)

# You are responsible for testing your commands
If your commands fail you will need to remedy this with your viewers. It is not recommended to change the configuration or actions while you are streaming. This can lead to command mistakes and you are resposible for them.

## Example Commands
if you are playing with other users on your server you may want to change "@p" the the username you use on you server, other wise these commands will execute on every player on the server!

### Give Player 1 Dimond
> give @p diamond

### Spawn Zombie at player location
> execute at @p run summon zombie

### Kill the player instantly
> kill @p

### Summon Named Zombie
> execute at @p run summon zombie {CustomName:'{"text":"CHILLIDOGG7"}'}

### Launch the player to Space
> effect give @p levitation 5 100

### Blind the player for 20s
> effect give chillidogg7 blindness 20 1

### Summon a Hoard os Zombies on the player
> execute at @p run summon zombie \
execute at @p run summon zombie \
execute at @p run summon zombie \
execute at @p run summon zombie \
execute at @p run summon zombie \
execute at @p run summon zombie \
execute at @p run summon zombie \
execute at @p run summon zombie \
execute at @p run summon zombie \
execute at @p run summon zombie

### Summon a flying kamakazi creeper
this summons a short fuse charged creeper flying on a phantom !!! LOL
> execute at @p run summon phantom ~10 ~ ~10 {Passengers:[{id:creeper,Fuse:5,powered:1}]}

### Baby You're A Firework!
this one is silly, a nearby entity will say "baby you're a firework!", the player will quickly levitate up, while a firework spawns on their location. its obnoxious, they take some explosion, fall, and EMOTIONALLLL DAMAGE
> execute as @e[type=!player,limit=1,sort=nearest] run say baby you're a firework! \
effect give @p levitation 1 10 \
execute at @p run summon firework_rocket ~ ~1 ~ {LifeTime:10,FireworksItem:{id:firework_rocket,Count:1,tag:{Fireworks:{Explosions:[{Type:0,Flicker:0,Trail:0,Colors:[I;16777215],FadeColors:[I;16777215]},{Type:4,Flicker:0,Trail:0,Colors:[I;16777215],FadeColors:[I;16777215]},{Type:3,Flicker:0,Trail:0,Colors:[I;16777215],FadeColors:[I;16777215]},{Type:2,Flicker:0,Trail:0,Colors:[I;16777215],FadeColors:[I;16777215]}]}}}}

## Conclusion
get creative with your commands, there are so many things you can summon, create, gift, and do with minecraft commands. search around you can combine things that don't naturally occur in minecraft.
## But Always Test your commands!!
