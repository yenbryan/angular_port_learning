from rest_framework.authtoken.models import Token
from portfolio.models import User

for user in User.objects.all():
    Token.objects.get_or_create(user=user)