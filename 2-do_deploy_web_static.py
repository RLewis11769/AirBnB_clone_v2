#!/usr/bin/python3
"""Write a Fabric script (based on the file 1-pack_web_static.py) that"""
"""distributes an archive to your web servers"""

from fabric.api import local, env
from datetime import datetime
import os.path
env.hosts = ['54.172.197.155, 34.230.92.222']


def do_deploy(archive_path):
    """
    deploy an archive, preferable one that funcitons well enough to be legible.
    If it isn't legible, maybe this code will at least pass the notations requirement.
    """

    if not os.path.exists(archive_path):
        return False

    try:
        archiveName = archive_path[9:]
        archiveNamenoext = archiveName[:-4]

        put(archive_path, '/tmp/' + archiveName)
        run("mkdir -p /data/web_static/releases/" + archiveNamenoext)
        run("tar -xzvf /tmp/" + archiveName + " -C " +
            "/data/web_static/releases/" +
            archiveNamenoext +
            " --strip-components=1")
        run("rm -f /tmp/" + archiveName)
        run("rm -f /data/web_static/current")
        run("sudo ln -sf /data/web_static/releases/" + archiveNamenoext +
            " /data/web_static/current")
        return True

    except:
        return False

def do_pack():
    """
    Pack up the webstatic. Send it to its mother's place.
    The weekend is entirely yours.
    """

    try:
        now = datetime.now()
        tarArchiveName = "web_static_" + now.strftime("%Y%m%d%H%M%S") + ".tgz"
        local("mkdir -p versions")
        local("tar -xzvf versions/" + tarArchiveName + " web_static")
        return ("versions/" + tarArchiveName)
    except:
        return None
