from django.contrib.auth.tokens import default_token_generator
from djoser import utils
from djoser.conf import settings
from templated_mail.mail import BaseEmailMessage

# to_do Задание со звездочкой. Здесь необходимо переместиться в исходный код
# to_do Djoser и правильно переопределит адрес сервера (в нашем случае это localhost:3000)


class PasswordResetEmail(BaseEmailMessage):
    template_name = "email/password_reset.html"

    def get_context_data(self):
        # PasswordResetEmail can be deleted
        pass
        # context = super().get_context_data()
        #
        # user = context.get("user")
        # context["uid"] = utils.encode_uid(user.pk)
        # context["token"] = default_token_generator.make_token(user)
        # context["url"] = settings.PASSWORD_RESET_CONFIRM_URL.format(**context)
        # context["domain"] = '127.0.0.1:3000'
        # return context
