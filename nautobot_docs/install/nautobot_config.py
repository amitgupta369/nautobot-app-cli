import os
import sys

from nautobot.core.settings import *  # noqa F401,F403
from nautobot.core.settings_funcs import is_truthy, parse_redis_connection

#########################
#                       #
#   Required settings   #
#                       #
#########################

# This is a list of valid fully-qualified domain names (FQDNs) for the Nautobot server. Nautobot will not permit write
# access to the server via any other hostnames. The first FQDN in the list will be treated as the preferred name.
#
# Example: ALLOWED_HOSTS = ['nautobot.example.com', 'nautobot.internal.local']
#
ALLOWED_HOSTS = ["*"] #os.getenv("NAUTOBOT_ALLOWED_HOSTS", "").split(" ")
WHITENOISE_USE_FINDERS = True

# Database configuration. See the Django documentation for a complete list of available parameters:
#   https://docs.djangoproject.com/en/stable/ref/settings/#databases
#
DATABASES = {
     "default": {
         "NAME": os.getenv("NAUTOBOT_DB_NAME", "nautobot"),  # Database name
         "USER": os.getenv("NAUTOBOT_DB_USER", "nautobot"),  # Database username
         "PASSWORD": os.getenv("NAUTOBOT_DB_PASSWORD", "P@55w0rd@123"),  # Database password
         "HOST": os.getenv("NAUTOBOT_DB_HOST", "localhost"),  # Database server
         "PORT": os.getenv("NAUTOBOT_DB_PORT", "5432"),  # Database port (leave blank for default)
         "CONN_MAX_AGE": int(os.getenv("NAUTOBOT_DB_TIMEOUT", "300")),  # Database timeout
         "ENGINE": os.getenv(
             "NAUTOBOT_DB_ENGINE",
             "django_prometheus.db.backends.postgresql" if METRICS_ENABLED else "django.db.backends.postgresql",
         ),  # Database driver ("mysql" or "postgresql")
     }
}

# Ensure proper Unicode handling for MySQL
#
if DATABASES["default"]["ENGINE"].endswith("mysql"):
    DATABASES["default"]["OPTIONS"] = {"charset": "utf8mb4"}

# This key is used for secure generation of random numbers and strings. It must never be exposed outside of this file.
# For optimal security, SECRET_KEY should be at least 50 characters in length and contain a mix of letters, numbers, and
# symbols. Nautobot will not run without this defined. For more information, see
# https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-SECRET_KEY
SECRET_KEY = os.getenv("NAUTOBOT_SECRET_KEY", "yg_$vvs2%(0fxz3__$!aanujyvx_=i7=(ug^t6%rgqq51h1qzk")

#####################################
#                                   #
#   Optional Django core settings   #
#                                   #
#####################################



# Set to True to enable server debugging. WARNING: Debugging introduces a substantial performance penalty and may reveal
# sensitive information about your installation. Only enable debugging while performing testing. Never enable debugging
# on a production system.
#
DEBUG = True #is_truthy(os.getenv("NAUTOBOT_DEBUG", "False"))






# Send anonymized installation metrics when `nautobot-server post_upgrade` command is run.
#
INSTALLATION_METRICS_ENABLED = is_truthy(os.getenv("NAUTOBOT_INSTALLATION_METRICS_ENABLED", "False"))




# Enable installed plugins. Add the name of each plugin to the list.
#
PLUGINS = ["nautobot_vlan_request"]

# Plugins configuration settings. These settings are used by various plugins that the user may have installed.
# Each key in the dictionary is the name of an installed plugin and its value is a dictionary of settings.
#
# PLUGINS_CONFIG = {
#     'my_plugin': {
#         'foo': 'bar',
#         'buzz': 'bazz'
#     }
# }



# Storage of various file types
#
STORAGES = {
     # The default storage backend, for things like user-uploaded image attachments, etc.
     "default": {
         "BACKEND": "django.core.files.storage.FileSystemStorage",
     },
#     # The storage backend to use for static file serving
     "staticfiles": {
         "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
     },
#     # The storage backend to use for Job input files and Job output files
#     # Note: default is for backwards compatibility and it's recommended to change if possible for your deployment.
     "nautobotjobfiles": {
         "BACKEND": "db_file_storage.storage.DatabaseFileStorage",
     },
}
