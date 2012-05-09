from flask import Module, request, render_template

mod = Module(__name__)

import logging
import json

log = logging.getLogger('svg-web')

import svgweb.util.phantomjs as pjs


@mod.route('/')
def index():
    return render_template('index.html')


@mod.route('/ajax/convert/')
def convert():
    a = request.args
    if not 'url' in a:
        return ajax_error('no url given')

    if not 'ext' in a:
        return ajax_error('no extension given')

    ext = a['ext']
    if ext != '.png' and ext != '.pdf':
        return ajax_error('invalid format png/pdf only')

    url = a['url']
    filename = None

    if not 'clip_top' in a:
        filename = pjs.convert_url(url, ext=ext)

    else:
        clip = make_clip(a['clip_top'],
                        a['clip_left'],
                        a['clip_height'],
                        a['clip_width'])

        filename = pjs.convert_url(url, clip=clip, ext=ext)

    if filename is None:
        return ajax_error('unable to convert %s' % url)

    return ajax_ok(filename)


def make_clip(top, left, height, width):
    return {'top': top, 'left': left, 'height': height, 'width': width}


def ajax_ok(data):
    return json.dumps({'status': 'OK', 'data': data})


def ajax_error(data):
    return json.dumps({'status': 'ERROR', 'data': data})
