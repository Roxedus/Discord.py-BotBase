# Discord Packages
import discord
from discord.ext import commands

# Bot Utilities
from cogs.utils.logging import Logger
from cogs.utils.settings import Settings
from cogs.utils.bot_version import Bot_version

import os
import time
import traceback
from argparse import ArgumentParser, RawTextHelpFormatter


def _get_prefix(bot, message):
    if not message.guild:
        prefix = bot.settings.default_prefix
        return commands.when_mentioned_or(prefix)(bot, message)
    prefixes = settings.prefix
    return commands.when_mentioned_or(*prefixes)(bot, message)


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=_get_prefix)
        self.logger = logger
        self.logger.debug("Logging level: %s" % level.upper())
        self.data_dir = data_dir
        try:
            self.settings = settings.extra
        except AttributeError:
            pass

    async def on_message(self, message):
        if message.author.bot:
            return
        await self.process_commands(message)

    async def on_ready(self):
        if not hasattr(self, "uptime"):
            self.uptime = time.time()

        login_msg = [
            f"Logged in as: {self.user.name} in {len(self.guilds)} servers.",
            f"Discord.py Version: {discord.__version__}",
            f"Bot version: {Bot_version}"
        ]

        for msg in login_msg:
            if level not in ["debug", "info"]:
                print(msg)
            self.logger.debug("%s" % msg)

        extensions = ["cogs.misc", "cogs.errors"]
        for extension in extensions:
            try:
                self.logger.debug("Loading extension %s" % extension)
                self.load_extension(extension)
            except Exception:
                self.logger.exception("Loading of extension %s failed" % extension)

    def run(self):
        try:
            super().run(settings.token)
        except Exception as e:
            tb = e.__traceback__
            logger.error(traceback.extract_tb(tb))
            print(e)


if __name__ == "__main__":
    parser = ArgumentParser(prog="BaseBot",
                            description="Discord bot base",
                            formatter_class=RawTextHelpFormatter)

    parser.add_argument("-D", "--debug", action="store_true", help="Sets debug to true")
    parser.add_argument("-l", "--level", help="Sets debug level",
                        choices=["critical", "error", "warning", "info", "debug"], default="warning")
    parser.add_argument("-d", "--data-directory", help="Define an alternate data directory location", default="data")
    parser.add_argument("-f", "--log-to-file", action="store_true", help="Save log to file", default=True)

    args = parser.parse_args()

    data_dir = os.environ.get("BOT_DATA_DIR", args.data_directory)
    level = os.environ.get("BOT_LOG_LEVEL", args.level)
    to_file = os.environ.get("BOT_LOG_TO_FILE", args.log_to_file)

    if os.environ.get("BOT_DEBUG", args.debug):
        level = "debug"

    logger = Logger(location=data_dir, level=level, to_file=to_file).logger
    logger.debug("Data folder: %s" % data_dir)
    settings = Settings(data_dir=data_dir)
    Bot().run()
