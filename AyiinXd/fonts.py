# Ayiin - Ubot
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/AyiinXd/AyiinUbot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AyiinXd/AyiinUbot/blob/main/LICENSE/>.
#
# FROM AyiinUbot <https://github.com/AyiinXd/AyiinUbot>
# t.me/AyiinChat & t.me/AyiinSupport & t.me/HyperSupportQ 


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

from fipper import Client
from fipper.types import Message

from pyHyper import Hyper, CMD_HELP
from pyHyper.pyrogram import eor

from . import *


arguments = [
    "smallcap",
    "monospace",
    "outline",
    "script",
    "blackbubbles",
    "bubbles",
    "bold",
    "bolditalic"
]

fonts = [
    "smallcap",
    "monospace",
    "outline",
    "script",
    "blackbubbles",
    "bubbles",
    "bold",
    "bolditalic"
]

_default = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
_smallcap = "ᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘϙʀsᴛᴜᴠᴡxʏᴢABCDEFGHIJKLMNOPQRSTUVWXYZ"
_monospace = "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉"
_outline = "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ"
_script = "𝒶𝒷𝒸𝒹𝑒𝒻𝑔𝒽𝒾𝒿𝓀𝓁𝓂𝓃𝑜𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵"
_blackbubbles = "🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩"
_bubbles = "ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ"
_bold = "𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭"
_bolditalic = "𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕"


def gen_font(text, new_font):
    new_font = " ".join(new_font).split()
    for q in text:
        if q in _default:
            new = new_font[_default.index(q)]
            text = text.replace(q, new)
    return text


@Hyper(["font"])
async def font_ling(client: Client, message: Message):
    if message.reply_to_message or ling.get_cmd(message):
        font = ling.get_cmd(message)
        text = message.reply_to_message.text
        if not font:
            return await eor(message, f"<code>{font} Tidak Ada Dalam Daftar Font Kentod...</code>")
        if font == "smallcap":
            lingex = gen_font(text, _smallcap)
        elif font == "monospace":
            lingex = gen_font(text, _monospace)
        elif font == "outline":
            lingex = gen_font(text, _outline)
        elif font == "script":
            lingex = gen_font(text, _script)
        elif font == "blackbubbles":
            lingex = gen_font(text, _blackbubbles)
        elif font == "bubbles":
            lingex = gen_font(text, _bubbles)
        elif font == "bold":
            lingex = gen_font(text, _bold)
        elif font == "bolditalic":
            lingex = gen_font(text, _bolditalic)
        await eor(message, yinsxd)

    else:
        return await message.reply("Balas Teks Dan Isi Nama Font Yang Bener Bego!!!")


@Hyper(["lf", "listfont"])
async def fonts(client: Client, msg: Message):
    await eor(
        msg,
        "<b>❯❯ ᴅᴀғᴛᴀʀ ғᴏɴᴛs ❮❮</b>\n"
        "<b>         ☟︎︎︎☟☟︎︎︎☟︎︎︎☟︎︎</b>\n\n\n"
        "<b>• smallcap » ʜʏᴘᴇʀ</b>\n"
        "<b>• monospace » 𝙷𝚈𝙿𝙴𝚁</b>\n"
        "<b>• outline » ℍ𝕐ℙ𝔼ℝ</b>\n"
        "<b>• script » 𝓗𝓨𝓟𝓔𝓡</b>\n"
        "<b>• blackbubbles » 🅷🆈🅿🅴🆁</b>\n"
        "<b>• bubbles » ⒽⓎⓅⒺⓇ</b>\n"
        "<b>• bold » 𝗛𝗬𝗣𝗘𝗥</b>\n"
        "<b>• bolditalic » 𝙃𝙔𝙋𝙀𝙍</b>\n\n"
        "<b>   ✧ 𝙷𝚈𝙿𝙴𝚁-𝚄𝚂𝙴𝚁𝙱𝙾𝚃 ✧</b>"
    )


CMD_HELP.update(
    {"fonts": (
        "fonts",
        {
            "font <reply text>": "Membuat Text Dengan Gaya Font Berbeda.",
            "lf": "Untuk Melihat Daftar Font.",
        }
    )
    }
)
