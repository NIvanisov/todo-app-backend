import logging
from logging.handlers import RotatingFileHandler


class FilterData(logging.Filter):
    def filter(self, record):
        return "password" not in record.getMessage().lower()


def configure_logging(level=logging.INFO):
    root_logger = logging.getLogger()
    if not root_logger.handlers:

        handlers = [
                logging.StreamHandler(),
                RotatingFileHandler("app.log",
                                    maxBytes=1_000_000,
                                    backupCount=2,
                                    encoding="utf-8")
            ]

        for handler in handlers:
            handler.addFilter(FilterData())

        logging.basicConfig(
            level=level,
            datefmt="%Y-%m-%d %H:%M:%S",
            format="[%(asctime)s.%(msecs)03d] %(name)-14s|%(module)-5s:%(lineno)3d %(levelname)-7s - %(message)s",
            handlers=handlers
        )

    logging.getLogger("app").setLevel(logging.INFO)