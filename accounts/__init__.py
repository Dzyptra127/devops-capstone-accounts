from flask import Flask
from flask_cors import CORS
from talisman import Talisman

app = Flask(__name__)

# Aktifkan CORS
CORS(app)

# Konfigurasi Talisman untuk tajuk keamanan
Talisman(
    app,
    content_security_policy={
        'default-src': "'self'"
    },
    force_https=True,
    frame_options='DENY',
    hsts_preload=True
)

from . import routes
