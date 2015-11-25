import random
import string
import os
from flask import current_app


class UploadManager(object):
    @staticmethod
    def upload_avatar(image):
        filename = generate_random_string(20) + os.path.splitext(image.filename)[1]
        image.save(os.path.join(current_app.config['AVATAR_UPLOAD_FOLDER'], filename))
        print("Image uploaded: {}".format(filename))
        return filename


def generate_random_string(length):
    return "".join(random.choice(string.ascii_letters + string.digits)
                   for _ in range(length))


sidebar_items = [
    ('/login', 'login', 'Bejelentkezés'),
    ('/register', 'register', 'Regisztráció'),
    ('/tours', 'tours', 'Túrák'),
    ('/statistics', 'statistics', 'Statisztikák'),
    ('/add-tour', 'add_tour', 'Túra hozzáadás'),
    ('/edit-tour', 'edit_tour', 'Túra szerkesztés'),
    ('/weather', 'get_weather', 'Időjárás előrejelzés')
]
