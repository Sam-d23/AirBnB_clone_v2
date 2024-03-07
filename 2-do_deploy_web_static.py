#!/usr/bin/env python3
"""Fabric script that distributes an archive to your web servers"""

from fabric.api import env, put, run
from os.path import exists
from datetime import datetime

env.hosts = ['<IP web-01>', 'IP web-02']


def do_deploy(archive_path):
    """Distributes an archive to web servers"""
    if not exists(archive_path):
        return False

    try:
        # Upload archive to /tmp/ directory on the web server
        put(archive_path, "/tmp/")

        # Extract the archive to /data/web_static/releases/
        file_name = archive_path.split('/')[-1]
        file_name_no_ext = file_name.split('.')[0]
        run("mkdir -p /data/web_static/releases/{}/".format(file_name_no_ext))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(file_name, file_name_no_ext))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(file_name))

        # Move the contents of the extracted folder to the web_static directory
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(file_name_no_ext,
                                                   file_name_no_ext))

        # Remove the web_static folder
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(file_name_no_ext))

        # Delete the symbolic link /data/web_static/current
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link /data/web_static/current
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(file_name_no_ext))

        return True
    except Exception as e:
        return False
