#!/usr/bin/env python3
"""Fabric script that creates and distributes an archive to your web servers"""

from fabric.api import local, env
from os.path import isfile
from datetime import datetime
from pathlib import Path

env.hosts = [52.3.246.65, 34.224.15.114]


def do_pack():
    """Create a compressed archive of the web_static folder"""
    try:
        local("mkdir -p versions")
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(timestamp)
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except Exception as e:
        return None


def do_deploy(archive_path):
    """Distributes an archive to web servers"""
    if not isfile(archive_path):
        return False

    try:
        # ... (same content as in the previous script)

        return True
    except Exception as e:
        return False


def deploy():
    """Creates and distributes an archive to web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False

    return do_deploy(archive_path)
