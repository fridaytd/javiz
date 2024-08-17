import logging
import pathlib


def get_logger(
    name: str,
    level: int = logging.INFO,
) -> logging.Logger:
    logger: logging.Logger = logging.getLogger(name=name)
    logger.setLevel(level=level)
    handler: logging.Handler = logging.StreamHandler()
    formatter: logging.Formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s :: %(message)s",
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
