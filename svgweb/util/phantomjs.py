import random
import svgweb.config as config
import os

alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'

import subprocess
import logging

log = logging.getLogger('svg-web')


def randstr(len):
    return ''.join(random.choice(alphabet)
                       for i in range(len))


def convert_url(url, clip=None, ext='.pdf'):
    if not clip is None:
        if ext == '.pdf':
            # cant clip and export as png
            ext = '.png'

    fileinfo = get_file(ext)

    log.info(fileinfo)
    command = [config.phantom_path,
                config.phantom_convert_path,
                url,
                fileinfo['path']]

    use_clip = False
    if not clip is None:

        clip_arry = []
        for x in ['top', 'left', 'width', 'height']:
            clip_arry.append(clip[x])

            if clip[x] != 0:
                use_clip = True

    if use_clip:
        command.extend(clip_arry)

    proc = subprocess.Popen(command)
    log.info(proc.communicate(5))

    return fileinfo['file']


def convert_pdf(url, clip=None):
    return get_file('.pdf')


def get_file_path(filename):
    path = os.path.join(config.output_dir, filename[0:2])

    if not os.path.isdir(path):
        os.makedirs(path)
    return os.path.join(path, filename)


def get_file(ext):
    output = {'file': '', 'path': ''}
    output['file'] = randstr(10) + ext
    output['path'] = get_file_path(output['file'])
    return output
