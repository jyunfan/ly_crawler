// ==UserScript==
// @name        lci link extractor
// @namespace   jtsai
// @grant       GM_xmlhttpRequest
// @include     http://lci.ly.gov.tw/lcew/*
// @version     1
// @require     http://code.jquery.com/jquery-1.7.2.min.js
// ==/UserScript==

var dispatchMouseEvent = function(target, var_args) {
  var e = document.createEvent("MouseEvents");
  e.initEvent.apply(e, Array.prototype.slice.call(arguments, 1));
  target.dispatchEvent(e);
};

function reportLink(key, datahash) {
  GM_xmlhttpRequest({
    method: 'POST',
    url: "http://localhost:8080/link/" + encodeURIComponent(key),
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    data: jQuery.param(datahash),
    //onload: function(responseDetails) { }
  });
}

// Fetch "議事錄" links
function fetch_journal_link(button) {
  var journal = {};
  var site_prefix = 'http://lci.ly.gov.tw/lcew/';

  // Get first 3 columns in the table
  var tds = button.parent().parent().parent().find("td");
  $.map(tds, function(item, index) {
    if (index==0) {
      journal['category'] = $(item).text();
    } else if (index==1) {
      journal['session'] = $(item).text();
    } else if (index==2) {
      journal['date'] = $(item).text().replace(/\s/g, "");
    } else {
      return null;
    }
  });

  // Click to show pop-up panel with links
  button.click();
  setTimeout(function() {
    journal['doc']  = site_prefix + $("a:contains('doc')").attr('href');
    journal['html'] = $("a:contains('htm')").attr('href');
    dispatchMouseEvent(jQuery("a:contains('關閉視窗')")[0], 'click', true, true);

    var key = journal['session'].replace(/[^\d]/g, '');
    if (journal['category'].match('常會'))
      key = 'N' + key;
    else
      key = 'T' + key;

    reportLink(key, journal);
  }, 1500);
}

function extract_page() {
  var button_count = 0;
  var index_shift = 10;
  var gap = 3000;
  $("button:contains('原始檔')").each(function(index) {
    if (index<index_shift) {
      return;
    }
    var button = $(this);
    ++button_count;
    setTimeout(function() { fetch_journal_link(button); }, button_count*gap);
  });

  var nextbtn = $('a:contains("Next")')[0];
  if (nextbtn) {
    setTimeout(function() { dispatchMouseEvent(nextbtn, 'click', true, true); },
        (button_count+1)*gap);
    setTimeout(function() { extract_page(); },
        (button_count+2)*gap);
  }
}

$(function(){
  setTimeout(function() {
    dispatchMouseEvent($('a:contains("議事錄")')[0], 'click', true, true);
  }, 2000);

  setTimeout(function() {
    dispatchMouseEvent($('span:contains("議　事　錄　查　閱")')[0], 'click', true, true)
  }, 4000);

  setTimeout(function() {
    extract_page();
  }, 6000);
});
