import os
import subprocess
from datetime import datetime

from constants import LOG_DIR
from constants import LOG_FILE
from constants import LOG_LEVEL


def log(s: str, level: int = 0, prefix: str = ""):
    content = ''
    if not os.path.isfile(LOG_FILE):
        content += "LOG started: " + str(datetime.now()) + "\n"

    content += prefix + s
    if level >= LOG_LEVEL.value:
        try:
            with open(LOG_FILE, "a") as file:
                file.write(content + "\n")
        except FileNotFoundError:
            mkdir_cmd = ['mkdir', '-p', LOG_DIR]
            subprocess.run(mkdir_cmd)
            log("Created logging directory")
            log(s, level=1)
            return

    print(content)
