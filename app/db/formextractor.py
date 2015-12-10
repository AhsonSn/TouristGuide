from flask import request
from app.users.forms import LoginForm, RegisterForm


class FormExtractor(object):
    @staticmethod
    def extract(form):
        if isinstance(form, RegisterForm):
            return dict(name=form.name.data, pwd=form.pwd.data,
                        email=form.email.data, fullName=form.fullName.data,
                        birth=form.birthDate.data,
                        phone=form.phoneNumber.data
                        if form.phoneNumber.data else None,
                        avatar=request.files['avatar']
                        if form.avatar.has_file() else None)

        if isinstance(form, LoginForm):
            return dict(name=form.name.data, pwd=form.pwd.data)
