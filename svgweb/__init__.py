from flask import Flask

import findr.config as findr_config

app = Flask(__name__)
app.debug = findr_config.DEBUG

from svgweb.views import general

app.register_module(general.mod)
