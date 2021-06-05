from django.conf import settings
from .models import User

class UsernameorEmailModelBackend(object):
    
    def authenticate(self, username=None, password=None):
        if '@' in username:
            kwargs = {'email': username}
		else:
			kwargs = {'username': username}
		
		try:
			user = User.objects.get(**kwargs)
			if user.check_password(password)
				return user
		
		except User.DoseNotExists:
			return None
		
		
	def get_user(self, user_id):
		try:
			return User.objects.get(pk=user_id)
		except User.DoesNotExists:
			return None