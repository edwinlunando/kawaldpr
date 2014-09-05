
/*******************************************************************************

    Title :  Kuliah Kita
    Date  :  Maret 2014
    Author:  Suitmedia (http://www.suitmedia.com)

********************************************************************************/

function checkDocumentHeight(callback){
    var lastHeight = document.body.clientHeight, newHeight, timer;

    (function run(){
        newHeight = document.body.clientHeight;
        if( lastHeight != newHeight )
            callback();
        lastHeight = newHeight;
        timer = setTimeout(run, 200);
    })();
}

$(function () {
    'use strict';

    var Site = {

        assets: {
            // Set the assets here

        },

        init: function () {
            // Call function here

        },
        // Implement function here

    };

    Site.init();
});

function reloadPage() {
    location.reload(true);
}























/* Project specific Javascript goes here. */
