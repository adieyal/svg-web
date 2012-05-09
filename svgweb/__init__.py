from flask import Flask

import logging


log = logging.getLogger('svg-web')
log.setLevel(logging.DEBUG)

fh = logging.FileHandler('/home/blayne/findr.log')
fh.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)


log.addHandler(fh)
log.addHandler(ch)


app = Flask(__name__)
app.debug = True

from svgweb.views import general

app.register_module(general.mod)
