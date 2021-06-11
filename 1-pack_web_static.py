#!/usr/bin/python3
"""Cottonmouth snekery"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """Pack up the webstatic"""

    now = datetime.now()

    tarArchiveName = "web_static_" + now.strftime("%Y%m%d%H%M%S") + ".tgz"


    local("mkdir -p versions")

    local("tar -czvf versions/" + tarArchiveName + " web_static")
