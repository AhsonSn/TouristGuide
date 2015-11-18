#!/usr/bin/env python
#Zoli nem megy

from flask_script import Manager

from app import app

manager = Manager(app)

manager.run()
