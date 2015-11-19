#!/usr/bin/env python
# Sajat komment

from app import create_app
from flask_script import Manager

tourist_guide = create_app('config')
manager = Manager(tourist_guide)

manager.run()
