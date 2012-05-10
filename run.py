#!/usr/bin/env python
from svgweb import app as application

if __name__ == '__main__':
    application.run(host='0.0.0.0')


# needs
# apt-get install
#    libicu48
#    phantomjs
# pip install flask
# framebuffer http://code.google.com/p/phantomjs/wiki/XvfbSetup
