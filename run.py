#!/usr/bin/env python

from app import create_app
from flask_script import Manager, Server

tourist_guide = create_app('config')
manager = Manager(tourist_guide)
manager.add_command("runserver", Server(use_debugger=True))

manager.run()
