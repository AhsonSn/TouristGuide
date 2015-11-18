#!/usr/bin/env python
# Sajat komment

from flask_script import Manager

from app import tourist_guide

manager = Manager(tourist_guide)

manager.run()
