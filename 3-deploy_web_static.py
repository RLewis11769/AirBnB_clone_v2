#!/usr/bin/python3
# Fabric file that generates compressed .tgz archive
# All .tgz files should be added to archive
# Archive name: web_static_<year><month><day><hour><minute><second>.tgz
# Point is to always have history of changes with datetime in name

from fabric.api import local, run, put, env
from datetime import datetime
import os.path

env.hosts = ['54.174.125.120', '34.234.63.53']


def deploy():
    """
    Creates and distributes archive to your web servers
    Combines do_pack and do_deploy to be useable
    Run with: fab -f 3-deploy_web_static.py deploy -i "privateKey" -u ubuntu
    """

    # Calls do_pack() and stores path of created archive
    archive = do_pack()

    # Returns False if no archive has been created
    if archive is None:
        return False

    # Calls do_deploy(archive_path) and uses new path of new archive to unzip
    status = do_deploy(archive)

    # Returns true if able to, false if failure
    return status


def do_deploy(archive_path):
    """
    Deploys archive to web_server aka puts archive on server
    Run with: fab -f 2-do_deploy_web_static.py do_deploy:archive_path=versions/
        web_static_"datetime".tgz -i "privateKey" -u ubuntu
    """

    # Returns immediately if file doesn't exist
    if not os.path.exists(archive_path):
        return False

    # Ensures successful operation every time
    try:
        # archiveName is web_static_datetime.tgz created in do_pack
        archiveName = archive_path[9:]  # after "versions/"
        woExtension = archiveName[:-4]  # before "".tgz"

        # put uploads file from local to remote
        # Uploads tarball archive from local to /tmp/ directory
        put(archive_path, '/tmp/' + archiveName)
        # Makes new directory for storing history of releases
        run("mkdir -p /data/web_static/releases/" + woExtension)
        # Uses fabric to unzip compressed archive file into releases dir
        # -x extracts, -z filters through gzip, -v is verbose, -f uses file
        # -C changes to directory, --strip-components=1 strips numbers
        run("tar -xzvf /tmp/" + archiveName + " -C " +
            "/data/web_static/releases/" + woExtension +
            " --strip-components=1")

        # Removes archive from server if exists
        run("rm -f /tmp/" + archiveName)
        run("rm -f /data/web_static/current")
        # Creates symbolic link "current" that points at file just unzipped
        # -s is symbolic, -f removes existing destination file
        # Fabric/python way of doing 0-setup_web_static.sh
        run("sudo ln -sf /data/web_static/releases/" +
            woExtension + " /data/web_static/current")
        return True
    except:
        return False


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
        # -c creates, -z filters through gzip, -v is verbose, -f uses file
        # Creates archive in path using all files in web_static directory
        local("tar -czvf " + tarArchivePath + " web_static")

        # Returns compressed archive in new folder
        return tarArchivePath
    except:
        return None
