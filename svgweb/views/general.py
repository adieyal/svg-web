from flask import Module, request, render_template

mod = Module(__name__)

import logging
import json

log = logging.getLogger('svg-web')

import svgweb.util.phantomjs as pjs
import svgweb.util.pdf_util as pdf


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

    if not 'max_pages' in a:
        max_pages = 1
    else:
        max_pages = int(a['max_pages'])

    url = a['url']
    if not url.startswith('http://') and \
        not url.startswith('https://'):
        url = 'http://' + url

    pages = 1
    if 'pages' in a:
        pages = int(a['pages'])

    logging.info('found %d pages' % pages)

    data = []
    for x in xrange(pages):
        check_url = url
        if x > 0:
            check_url = url + '?page=%d' % (x + 1)
        fileinfo = None
        if not 'clip_top' in a:
            fileinfo = pjs.convert_url(check_url, ext=ext)
            logging.info(fileinfo)
        else:
            clip = make_clip(a['clip_top'],
                            a['clip_left'],
                            a['clip_height'],
                            a['clip_width'])

            fileinfo = pjs.convert_url(check_url, clip=clip, ext=ext)

        if fileinfo['file'] is None:
            return ajax_error('unable to convert %s' % check_url)
        data.append(fileinfo)
        if ext == '.pdf':
            pdf.remove_pages(fileinfo['path'], max_pages)

    if len(data) > 1:
        filename = pdf.merge_pages(data)
    else:
        filename = data[0]['file']

    return ajax_ok(filename)


def make_clip(top, left, height, width):
    return {'top': top, 'left': left, 'height': height, 'width': width}


def ajax_ok(data):
    return json.dumps({'status': 'OK', 'data': data})


def ajax_error(data):
    return json.dumps({'status': 'ERROR', 'data': data})
