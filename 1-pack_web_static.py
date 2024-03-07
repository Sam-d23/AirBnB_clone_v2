#!/usr/bin/env bash
"""
Generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack.
"""

from fabric.api import local
from datetime import datetime

def do_pack():
    """Generates a .tgz archive from the contents of web_static folder."""
    try:
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_{}.tgz".format(timestamp)
        archive_path = "versions/{}".format(archive_name)

        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(archive_path))

        return archive_path
    except Exception as e:
        return None
