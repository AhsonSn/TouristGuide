from app.users.forms import LoginForm, RegisterForm


class FormExtractor(object):

    @staticmethod
    def extract(form):
        if isinstance(form, RegisterForm):
            ret = (form.name.data, form.pwd.data, form.email.data,
                   form.fullName.data, form.birthDate.data, form.avatar)
            return ret