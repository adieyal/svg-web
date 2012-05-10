
from pyPdf import PdfFileWriter, PdfFileReader
import os

import logging

import svgweb.util.phantomjs as pjs

log = logging.getLogger('svg-web')


def remove_pages(pdf_file, max_pages=1):
    output = PdfFileWriter()

    with open(pdf_file, 'r') as pdf:
        input = PdfFileReader(pdf)

        total_pages = input.getNumPages()

        for i in xrange(max_pages):
            if i >= total_pages:
                break

            p = input.getPage(i)
            output.addPage(p)

        with open(pdf_file + '.tmp', 'w') as pdf:
            output.write(pdf)

    os.remove(pdf_file)
    os.rename(pdf_file + '.tmp', pdf_file)
    return pdf_file


def merge_pages(pdf_files):
    output = PdfFileWriter()

    for x in pdf_files:
        log.info('input %s' % x)
        path = x['path']
        input = PdfFileReader(open(path, 'r'))
        total_pages = input.getNumPages()

        for i in xrange(total_pages):
            log.info('adding page %d from %s' % (i, path))
            p = input.getPage(i)
            output.addPage(p)

    fileinfo = pjs.get_file('.pdf')
    output.write(open(fileinfo['path'], 'w'))

    return fileinfo['file']


if __name__ == '__main__':
    print merge_pages(['out.pdf', 'out-2.pdf'])
