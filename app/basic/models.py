import os
import random
import string

from flask import current_app


class UploadManager(object):
    @staticmethod
    def upload_avatar(image):
        if image.content_type:
            filename = generate_random_string(20) + \
                       os.path.splitext(image.filename)[1]
            image.save(os.path.join(current_app.config['AVATAR_UPLOAD_FOLDER'],
                                    filename))
            print("Image uploaded: {}".format(filename))
            return filename


def generate_random_string(length):
    return "".join(random.choice(string.ascii_letters + string.digits)
                   for _ in range(length))


sidebar_items = [
    ('/tours', 'tours', 'Túrák'),
]

ceo_sidebar_items = [
    ('/tours', 'tours', 'Túrák'),
    ('/statistics', 'statistics', 'Statisztikák'),
    ('/add-tour', 'add_tour', 'Túra hozzáadás'),
]
