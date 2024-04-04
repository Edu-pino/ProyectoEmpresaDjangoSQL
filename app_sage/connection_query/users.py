from django.contrib.auth.models import User
import time


users = User.objects.all()
print(users)
