
if (phantom.args.length < 2){
    console.log('not enough arguments!\n Usage, phantom_cli.js <url> <output> [clip_x clip_y clip_width clip_height]');
    phantom.exit();
}

var url = phantom.args[0];
var output = phantom.args[1];
var clip;

if (phantom.args.length > 2){
    if (phantom.args.length < 6){
        console.log('not enough arguments!\n Usage, phantom_cli.js <url> <output> [clip_x clip_y clip_width clip_height]');
        phantom.exit();
    }
    clip = {
        top: phantom.args[2],
        left: phantom.args[3],
        width: phantom.args[4],
        height: phantom.args[5]
    };
    console.log('using clipping');
}



var page = require('webpage').create();
console.log ('loading ' + url);

page.viewportSize = {'width':1920, 'height': 1080};
page.open(url, function (status) {
  // do something
    if( clip !== undefined){
        page.clipRect = clip;
    }

    page.render(output);
    console.log(output + ' Saved');
    phantom.exit();
});