import logging
from logging.handlers import TimedRotatingFileHandler
from logging import handlers
import sys

log = logging.getLogger("")
log.setLevel(logging.INFO)
format = logging.Formatter(
    fmt="[%(asctime)s][%(levelname)s] %(message)s", datefmt="%d/%m/%y|%H:%M:%S"
)

ch = logging.StreamHandler(sys.stdout)
ch.setFormatter(format)
log.addHandler(ch)

fh = handlers.RotatingFileHandler("Moneky", maxBytes=(1048576 * 5), backupCount=7)
fh.setFormatter(format)
fh.suffix = "%Y-%m-%d.log"
log.addHandler(fh)

disclog = logging.getLogger("discord")
disclog.setLevel(logging.ERROR)