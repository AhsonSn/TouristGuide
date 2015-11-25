from werkzeug.utils import secure_filename


class UploadManager(object):
    @staticmethod
    def upload_avatar(image):
        filename = secure_filename(image.filename)
        print("Image uploaded: {}".format(filename))
        return filename


sidebar_items = [
    ('/login', 'login', 'Bejelentkezés'),
    ('/register', 'register', 'Regisztráció'),
    ('/tours', 'tours', 'Túrák'),
    ('/statistics', 'statistics', 'Statisztikák'),
    ('/add-tour', 'add_tour', 'Túra hozzáadás'),
    ('/edit-tour', 'edit_tour', 'Túra szerkesztés'),
    ('/weather', 'get_weather', 'Időjárás előrejelzés')
]
