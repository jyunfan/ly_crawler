// ==UserScript==
// @name        lci link extracter
// @grant       none
// @include     http://lci.ly.gov.tw/lcew/*
// @version     1
// @require     http://code.jquery.com/jquery-1.7.2.min.js
// ==/UserScript==

var dispatchMouseEvent = function(target, var_args) {
  var e = document.createEvent("MouseEvents");
  e.initEvent.apply(e, Array.prototype.slice.call(arguments, 1));
  target.dispatchEvent(e);
};

function fetch_link(button) {
    var tds = button.parent().parent().parent().find("td");
    var arr = $.map(tds, function(item, index) {
        if (index<3) {
            return $(item).text();
        } else {
            return null;
        }
    });

    button.click();
    setTimeout(function() {
        arr.push( $("a:contains('doc')").attr('href') );
        arr.push( $("a:contains('htm')").attr('href') );
        console.debug(arr.join(';'));
        dispatchMouseEvent(jQuery("a:contains('關閉視窗')")[0], 'click', true, true);
    }, 1000);
}

$(function(){
    setTimeout(function() {
        dispatchMouseEvent(jQuery('a:contains("議事錄")')[0], 'click', true, true);
        setTimeout(function() {
            var button_count = 0;
            jQuery("button:contains('原始檔')").each(function(i) {
                var button = $(this);
                ++button_count;
                setTimeout(function() { fetch_link(button); }, button_count*2000);
            });
        }, 1000);
    }, 3000);
}); // ready

