#!/usr/bin/python3
"""The best lies aren't fabrications"""

from fabric.api import local, env
from datetime import datetime
import os.path
env.hosts = ['54.172.197.155, 34.230.92.222']


def deploy():
    """comment"""
    archive = do_pack()
    if archive is None:
        return False
    status = do_deploy(archive)


def do_deploy(archive_path):
    """deploy an archive"""

    if not os.path.exists(archive_path):
        return False

    archiveName = archive_path[9:]
    archiveNamenoext = archiveName[:-4]

    put(archive_path, '/tmp/' + archiveName)
    run("mkdir -p /data/web_static/releases/" + archiveNamenoext)
    run("tar xzvf /tmp/" + archiveName + " -C " +
        archiveNamenoext + " --strip-components=1")
    run("rm -f /tmp/" + archiveName)
    run("rm -f /data/web_static/current")
    run("ln -sf /data/web_static/releases/" + archiveNamenoext +
        " /data/web_static/current")


def do_pack():
    """Pack up the webstatic"""

    try:
        now = datetime.now()
        tarArchiveName = "web_static_" + now.strftime("%Y%m%d%H%M%S") + ".tgz"
        local("mkdir -p versions")
        local("tar -czvf versions/" + tarArchiveName + " web_static")
    except:
        return None
