#!/usr/bin/python3
# Fabric file that generates compressed .tgz archive
# All .tgz files should be added to archive
# Archive name: web_static_<year><month><day><hour><minute><second>.tgz
# Point is to always have history of changes with datetime in name

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Pack up web_static directory
    Run with: fab -f 1-pack_web_static.py do_pack
    """

    # Ensures successful operation every time
    try:
        now = datetime.now()
        # Create web_static_datetime.tgz file name
        # .tgz extension for compressed archive created by "tar" command
        tarArchiveName = "web_static_" + now.strftime("%Y%m%d%H%M%S") + ".tgz"
        # Create path as ArchiveName in versions folder
        tarArchivePath = "versions/" + tarArchiveName

        # Uses fabric to make versions directory
        # local command executes shell command locally
        local("mkdir -p versions")

        # Uses fabric to create "tarball" aka compressed archive file
        # -c creates, -z filters through gzip, # -v is verbose, -f uses file
        # Creates tarball in path using all files in web_static directory
        # Just memorize these options for creating
        local("tar -czvf " + tarArchivePath + " web_static")

        # Returns compressed archive in new folder
        return tarArchivePath
    except:
        return None
