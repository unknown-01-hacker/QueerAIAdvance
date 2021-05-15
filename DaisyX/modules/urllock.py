import asyncio

from pyrogram import filters

from DaisyX import BOT_ID
from DaisyX.db.mongo_helpers.lockurl import add_chat, get_session, remove_chat
from DaisyX.function.pluginhelpers import (
    admins_only,
    edit_or_reply,
    get_url,
    member_permissions,
)
from DaisyX.services.pyrogram import pbot


@pbot.on_message(filters.command("urllock") & ~filters.edited & ~filters.bot)
@admins_only
async def hmm(_, message):
    global daisy_chats
    if not "can_change_info" in (
        await member_permissions(message.chat.id, message.from_user.id)
    ):
        await message.reply_text("**You don't have enough permissions**")
        return
    if len(message.command) != 2:
        await message.reply_text(
            "I only recognize `/urllock on` and /urllock `off only`"
        )
        return
    status = message.text.split(None, 1)[1]
    message.chat.id
    if status == "ON" or status == "on" or status == "On":
        lel = await edit_or_reply(message, "`Processing...`")
        lol = add_chat(int(message.chat.id))
        if not lol:
            await lel.edit("URL Block Already Activated In This Chat")
            return
        await lel.edit(
            f"URL Block Successfully Added For Users In The Chat {message.chat.id}"
        )

    elif status == "OFF" or status == "off" or status == "Off":
        lel = await edit_or_reply(message, "`Processing...`")
        Escobar = remove_chat(int(message.chat.id))
        if not Escobar:
            await lel.edit("URL Block Was Not Activated In This Chat")
            return
        await lel.edit(
            f"URL Block Successfully Deactivated For Users In The Chat {message.chat.id}"
        )
    else:
        await message.reply_text(
            "I only recognize `/urllock on` and /urllock `off only`"
        )


@pbot.on_message(
    filters.incoming & filters.text & ~filters.private & ~filters.channel & ~filters.bot
)
async def hi(client, message):
    if not get_session(int(message.chat.id)):
        message.continue_propagation()
    if not len(await member_permissions(message.chat.id, message.from_user.id)) < 1:
        message.continue_propagation()
    if len(await member_permissions(message.chat.id, BOT_ID)) < 1:
        message.continue_propagation()
    if not "can_delete_messages" in (await member_permissions(message.chat.id, BOT_ID)):
        sedlyf = await message.reply_text(
            "**I don't have enough permissions to delete messages here**"
        )
        await asyncio.sleep(10)
        await sedlyf.delete()

    lel = get_url(message)
    if lel:
        try:
            await message.delete()
            sender = message.from_user.mention()
            lol = await client.send_message(
                message.chat.id,
                f"{sender}, Your message was deleted as it contain a link(s). \n ❗️ Links are not allowed here",
            )
            await asyncio.sleep(10)
            await lol.delete()
        except Exception:
            message.continue_propagation()
    else:
        message.continue_propagation()


__mod_name__ = "Music Player"
__help__ = """
<b> Queer ♕ Music Player </b>

Queer Music Player plays plays music in your group's voice chat
 
Assistant name >> @QueerMusicPlayer

<b>Setting up</b>

Add @QueerMusicPlayer in the group where you want to play music.

<b>Commands</b>

=>> Song Playing 🎧 

- /play: Play song using YouTube music.
- /play [yt url] : Play the given YouTube url
- /dplay : Plays the song via deezer
- /splay : Plays the song via saavn

=>> Playback ⏯ 

/skip: Skips the current track
 /pause: Pause track
 /resume: Resumes the paused track
 /end: Stops media playback

=>> More tools 🧑‍🔧

 /admincache: Updates admin info of your group. Try if bot isn't recognize admin
 /userbotjoin : Invite @QueerMusicPlayer userbot to your chat
 
<i>Player cmd and all other cmds except /play, /dplay, /splay are only for admins who manages group.</i>

👀 Read full manual of Queer ♕ Music Player <a href="https://telegra.ph/Queer-Music-Player-04-18-2">here!</a>
"""
