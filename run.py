#!/usr/bin/env python
# Sajat komment

from flask_script import Manager

from app import app

manager = Manager(app)

manager.run()
