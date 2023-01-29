class script(object):
    TEMPLATES = """https://github.com/Tamilgram/Templates"""
    COMMANDS = """Here Is Commands to use This Bot ⍖"""
    FEATURES = """💙 Features : 

✅ Auto Filter

✅ URL Shortner (Your Website)

✅ 300k+ Files Available

✅ Custom Welcome Message

✅ Custom Tutorial (How To Download ) Video Button

✅ More Fast

✅ And more Features"""
    START_TXT = """Hey Bro How Are You ? \n\nDo You Want Money By Uploading Movies ? \n\nYes But How ? \n\nHere I am for you. Just Add In Your Group And Earn Money Via Your Subscribers. For More Details Click Here"""
    HELP_TXT = """<b>How To Use @RolexSirBot ?</b>

To Use @RolexSirBot You Just Have A Account In Any URL Shortener 

Go To Dashboard -> Menu -> Tools -> Devoloper Api. 

Copy The Api And Add @RolexSirBot In Group.

To Connect Your Api Give Command /rolex_api your api.

<b>How To Add Url Shortener Website ?</b>

Go To Url Shortener Website And Copy Website Link (Without https://)

Example : droplink.co

To Add Your Website Give Command /rolex_web WEBSITE.
Now Enjoy Your Profit 💸"""
    ABOUT_TXT = """Adding....."""
    SOURCE_TXT = """<b>NOTE:</b>
Current CPM - $1 (About 75-80Rs)

More INFO - https://ldisk.xyz/member/dashboard
Minimum Withdrawal Ammount Is 2-5$ For Defferent Withdrawal Types 
Paypal - 5$ 
UPI - 3$ 
Mobile Recharge - 2$
Tv Recharge -2$ 
Other Payment Methods Comeing Soon 
More INFO - https://ldisk.xyz/member/users/profile """
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Ldisk Search Bot will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Ldisk Search Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Ldisk Search Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Ldisk Search Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/Ldisk_Search_Bot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Ldisk Search Bot

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    TUTORIAL_TXT = """ How To Use Ldisk Movie Search Bot ? 🔘

To Use Ldisk Movie Search You Just Have A Account In Ldisk.xyz |

Go To Dashboard -> Menu -> Tools -> Devoloper Api . 

Copy The Api And Add Ldisk Search Bot In Group .

To Connect Your Api Give Command /set_api your api  .

Now Enjoy Your Profit 💸 """
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""

    MAKEBOT = """Make Your Own Bot For Like This ❤️

What will it contain?

Any Auto Filter Repo I will Add URL Shortener 300rs

For More Information : @Yali_Kk"""

    WHATSNEW = """
1.0.6
Url Shortener On/Off Feature Added

1.0.5
⎉ Updated 🎬 𝖳𝖱𝖤𝖭𝖣𝖨𝖭𝖦 𝖭𝖮𝖶 🎬 Button

1.0.4
⎉ Added Bigg Boss S6 (Tamil) Buttons

1.0.3
⎉ Added KeyboardButtons For Easy Use

1.0.2
⎉ Added Tamil Quotes (70+)

1.0.1

⎉ Added URL Shortener
⎉ Custom Templates Adding Option Enabled
⎉ Bugs Fixed."""

    VERSION = """Current Version Of Bot : 1.0.6
Old : 1.0.1, 2, 3, 4, 5"""
