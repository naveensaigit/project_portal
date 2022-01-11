from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.auth.models import User

class MyAccountAdapter(DefaultAccountAdapter):

    def pre_social_login(self, request, sociallogin):
        user = User.objects.filter(email=sociallogin.user.email).first()
        if user and not sociallogin.is_existing:
            sociallogin.connect(request, user)
