#!/usr/bin/python3
"""
Write a Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function do_deploy:

Prototype: def do_deploy(archive_path):
Returns False if the file at the path archive_path doesn’t exist

The script should take the following steps:
Upload the archive to the /tmp/ directory of the web server
Uncompress the archive to the folder 
/data/web_static/releases/<archive filename without extension> on the web server

Delete the archive from the web server
Delete the symbolic link /data/web_static/current from the web server
Create a new the symbolic link /data/web_static/current on the web server,
linked to the new version of your code 
(/data/web_static/releases/<archive filename without extension>)

All remote commands must be executed on your both web servers
(using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)

Returns True if all operations have been done correctly,
otherwise returns False
You must use this script to deploy it on your servers: xx-web-01 and xx-web-02
"""

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
        run("tar xzvf /tmp/" + archiveName + " -C " +
            "/data/web_static/releases/" +
            archiveNamenoext +
            " --strip-components=1")
        run("rm -f /tmp/" + archiveName)
        run("rm -f /data/web_static/current")
        run("ln -sf /data/web_static/releases/" + archiveNamenoext +
            " /data/web_static/current")
        return True

    Except:
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
        local("tar -czvf versions/" + tarArchiveName + " web_static")
        return ("versions/" + tarArchiveName)
    except:
        return None
