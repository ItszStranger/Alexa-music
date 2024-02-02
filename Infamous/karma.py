# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX
# https://t.me/O_okarma

# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from Mikobot import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
START_IMG = [
    "https://te.legra.ph/file/f482b87a141d22eaf0e4b.jpg",
    "https://te.legra.ph/file/abf6c760e30badc7cc260.jpg",
    "https://te.legra.ph/file/e4023c057e87ba5f2fe37.jpg",
    "https://te.legra.ph/file/54bab6b6f15d2bf194191.jpg",
    "https://te.legra.ph/file/abf6c760e30badc7cc260.jpg",
    "https://te.legra.ph/file/28b7361b286bad233a100.jpg",
    "https://te.legra.ph/file/e4023c057e87ba5f2fe37.jpg",
]

HEY_IMG = "https://te.legra.ph/file/8c4b7ef12ee1445ad3276.jpg"

ALIVE_ANIMATION = [
    "https://telegra.ph//file/f9e2b9cdd9324fc39970a.mp4",
    "https://telegra.ph//file/8d4d7d06efebe2f8becd0.mp4",
    "https://telegra.ph//file/c4c2759c5fc04cefd207a.mp4",
    "https://telegra.ph//file/b1fa6609b1c4807255927.mp4",
    "https://telegra.ph//file/f3c7147da6511fbe27c25.mp4",
    "https://telegra.ph//file/39071b73c02e3ff5945ca.mp4",
    "https://telegra.ph//file/8d4d7d06efebe2f8becd0.mp4",
    "https://telegra.ph//file/6efdd8e28756bc2f6e53e.mp4",
]

BAN_GIFS = [
    "https://te.legra.ph/file/ea0f7581cfd3c09645fca.mp4",
]


KICK_GIFS = [
    "https://te.legra.ph/file/2eca660c64dd64e2400e7.mp4",
]


MUTE_GIFS = [
    "https://te.legra.ph/file/ee2a903707ed78a37f70a.mp4",
]

FIRST_PART_TEXT = "✨ *ʙᴜᴅᴅʏ🪄✨* `{}` . . ."

PM_START_TEXT = "✨ *ɪ ᴀᴍ ˹ 𝐀ʟᴇxᴀ ✘ 𝗥𝙾𝙱𝙾 ˼, ━━━━━━━━━━━━━━━━━━━━━━

๏ ɪ ᴀᴍ  ᴀɴᴅ ɪ ʜᴀᴠᴇ sᴘᴇᴄɪᴀʟ ғᴇᴀᴛᴜʀᴇs.

๏  ᴛʜᴇᴍᴇ ➛ ᴀɴɪᴍᴇ ʙᴀsᴇᴅ
๏  ғᴇᴀᴛᴜʀᴇ ➛ ᴠᴄ ᴍᴜsɪᴄ + ᴍᴀɴᴀɢᴇᴍᴇɴᴛ + ᴀɪ 

๏ ᴛʜɪs ɪs ᴍᴏsᴛ ᴘᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ʙᴏᴛ, ғᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ*"

START_BTN = [
    [
        InlineKeyboardButton(
            text="ᴄʜᴀᴛ ɢʀᴏᴜᴘ",
            url=f"https://t.me/mastiwithfriendsx",
        ),
    ],
    [
        InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴍɴᴅs", callback_data="help_back"),
    ],
    [
        InlineKeyboardButton(text="ᴀʙᴏᴜᴛ ᴀʟᴇxᴀ", callback_data="Miko_"),
        InlineKeyboardButton(text="ɢᴘᴛ & ᴍᴏʀᴇ", callback_data="ai_handler"),
        InlineKeyboardButton(text="ᴍᴜsɪᴄ ᴄᴍɴᴅ", callback_data="git_source"),
    ],
    [
        InlineKeyboardButton(text="𝐀ᴅᴅ ᴍᴇ 𝐁ᴀʙʏ ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
    ],
]

GROUP_START_BTN = [
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ ᴅᴀʀʟᴏ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="ʜᴏᴜsᴇ", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text="sᴛ ᴡᴏʀʟᴅ", url=f"https://t.me/mastiwithfriendsx"),
    ],
]

ALIVE_BTN = [
    [
        ib(text="ᴜᴘᴅᴀᴛᴇs", url="https://t.me/about_x_alexa"),
        ib(text="sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ", url="https://t.me/Alexa_X_Support"),
    ],
    [
        ib(
            text=" ᴋɪᴅɴᴀᴘ ᴍᴇ ʙᴀʙʏ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

HELP_STRINGS = """
🫧 *˹ 𝐀ʟᴇxᴀ ✘ 𝗥𝙾𝙱𝙾 ˼* 🫧

☉ * ๏ ᴄʜᴏᴏsᴇ ᴛʜᴇ ᴄᴀᴛᴇɢᴏʀʏ ғᴏʀ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴɴᴀ ɢᴇᴛ ʜᴇʟᴩ

๏ ᴀsᴋ ʏᴏᴜʀ ᴅᴏᴜʙᴛs ᴀᴛ➠ [sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ](https://t.me/alexa_x_support).*

๏ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ ➠ /
"""
