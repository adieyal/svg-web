from flask import Module

mod = Module(__name__)

import logging

log = logging.getLogger('svg-web')


@mod.route('/')
def index():
    return 'Hello World'
