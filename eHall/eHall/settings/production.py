from eHall.settings.base import *

# dj_database_url configuration for Heroku
import dj_database_url
DATABASES = {
	'default': dj_database_url.config()
}

ALLOWED_HOSTS += (
	'gti525-gestionnaire-salle.herokuapp.com',
)
