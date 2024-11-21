INSTALLED_APPS = [
  "rest_framwork_simplejwt"
]

REST_FRAMEWORK = {
  "DEFAULT_AUTHENTICATION_CLASSES": (
    "rest_framework_simplejwt.authentication.JWTAuthentication",
  ),
}

SIMPLE_JWT = {
  "ACCESS_TOKEN_LIFETIME": timedelta(minutes=15),
  "REFRESH_TOKEN_LIFETIME": timedelta(days=5),
  "ROTATE_REFRESH_TOKENS": False,
  "BLACKLIST_AFTER_ROTATION": True
}

