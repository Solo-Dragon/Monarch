import os
import sys
import glob
import time
import yaml
import shlex
import random
import shutil
import asyncio
import inspect
import logging
import aiofiles
import importlib
import traceback
import contextlib
import multiprocessing
from typing import Any, Dict, List, Union, Optional
from pyrogram.types import User, Message, CallbackQuery
from pyrogram.errors.exceptions.bad_request_400 import (
    MessageEmpty, PeerIdInvalid, MessageTooLong, MessageIdInvalid,
    MessageNotModified, UserNotParticipant)

def register_on_cmd(
        self,
        cmd: Union[str, List[str]],
        cmd_help: dict = {},
        pm_only: bool = False,
        group_only: bool = False,
        channel_only: bool = False,
        just_exc: bool = False,
        requires_input: bool = False,
        requires_reply: bool = False,
        bot_mode_unsupported: bool = False,
        # Incase a command can't be performed by an bot.
        group=1,
        disallow_if_sender_is_channel=False,
    ):
        cmd_help_ = cmd_help.get("help") or "Not Given"
        cmd_help_ex = cmd_help.get("example") or "Not Given"
        user_args = dict(cmd_help.get("user_args")) if cmd_help.get("user_args") else {}
        cmd = cmd if isinstance(cmd, list) else [cmd]
        self.cmd_list_s.extend(cmd)
        previous_stack_frame = inspect.stack()[1]
        file_name = os.path.basename(previous_stack_frame.filename.replace(".py", ""))
        self.add_help_to_cmdlist(
            cmd=cmd,
            file_name=file_name,
            cmd_help=cmd_help_,
            example=cmd_help_ex,
            user_args=user_args,
            requires_input=requires_input,
            requires_reply=requires_reply,
            group_only=group_only,
            channel_only=channel_only,
            pm_only=pm_only,
        )
