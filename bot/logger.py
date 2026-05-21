import logging


def setup_logger():
    logger = logging.getLogger("tading_bot")
    logger.setLevel(logging.INFO)

    file = logging.FileHandler("bot.log")
    file_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    file.setFormatter(file_format)
    logger.addHandler(file)

    return logger



