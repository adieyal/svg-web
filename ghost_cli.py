#!/usr/bin/env python

from ghost import Ghost

js_get_svg = """var svg = document.getElementsByTagName("svg");
var output = [];
for (var i =0; i < svg.length; i++) {
    var node = svg[i];
    var id = node.id;
    if (id === undefined || id == ''){
        id = node.parentNode.id
    }
    if (id !== undefined && id != ''){
        output.push(id);
    }
}
console.log(output)
return output;
"""


def get_svg_elements(url):

    ghost = Ghost()
    page, extra_resources = ghost.open(url)
    result, e = ghost.evaluate(js_get_svg)


if __name__ == '__main__':
    url = 'http://localhost/freelancer/1564040-d3-graph/d3graph/example/'
    elements = get_svg_elements(url)

    for x in elements:
        print x
