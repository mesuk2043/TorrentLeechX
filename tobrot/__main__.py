#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | gautamajay52 | Amirul Andalib

import io
import logging
import os
import sys
import traceback

from pyrogram import Client, filters, idle
from pyrogram.raw import functions, types
from pyrogram.handlers import CallbackQueryHandler, MessageHandler

from tobrot import app, bot
from tobrot import ( 
    CLEAR_THUMBNAIL,
    LOGGER,
    RENEWME_COMMAND,
    RENAME_COMMAND,
    SAVE_THUMBNAIL,
    YTDL_COMMAND,
    TSEARCH_COMMAND
)
from tobrot.helper_funcs.download import down_load_media_f
from tobrot.plugins.call_back_button_handler import button
# the logging things
from tobrot.plugins.torrent_search import searchhelp
from tobrot.plugins.choose_rclone_config import rclone_command_f
from tobrot.plugins.custom_thumbnail import clear_thumb_nail, save_thumb_nail
from tobrot.plugins.incoming_message_fn import (g_clonee, g_yt_playlist,
                                                incoming_message_f,
                                                incoming_purge_message_f,
                                                incoming_youtube_dl_f,
                                                rename_tg_file)
from tobrot.plugins.new_join_fn import help_message_f, new_join_f
from tobrot.plugins.speedtest import get_speed
from tobrot.plugins.rclone_size import check_size_g, g_clearme
from tobrot.plugins.status_message_fn import (
    cancel_message_f,
    eval_message_f,
    exec_message_f,
    status_message_f,
    upload_document_f,
    upload_log_file,
    upload_as_doc,
    upload_as_video
)
'''
botcmds = [
        (f'{BotCommands.YtdlCommand}','upload yt-dlp supported video links to Telegram'),
        (f'{BotCommands.SaveCommand}','Save Thumbnail For Telegram Uploads'),
        (f'{BotCommands.ClearCommand}','Clear Thumbnail to default For Telegram Uploads'),
        (f'{BotCommands.RenameCommand}','Rename Telegram File and reupload it to telegram'),
        (f'{BotCommands.TsHelpCommand}','To search your Torrent or Torrent Search Module')

    ]
'''
if __name__ == "__main__":
    # create download directory, if not exist
    if not os.path.isdir(DOWNLOAD_LOCATION):
        os.makedirs(DOWNLOAD_LOCATION)
  #mera   
app.start()
logging.info(f"@{(app.get_me()).username} Has Started Running...🏃💨💨")
idle()
