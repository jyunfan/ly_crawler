ly_crawler
==========

由立法院網站取得立法院議事錄，並產生純文字格式檔案。

Extract links of journals from Taiwanese Congress website.
Data come from http://lci.ly.gov.tw/lcew/index_5.zul

執行程式需求
------------
* Firefox 15+
* Firebug 1.10+  https://addons.mozilla.org/zh-TW/firefox/addon/firebug/
* Greasemonkey 1.0  https://addons.mozilla.org/zh-TW/firefox/addon/greasemonkey/
* Python 2.7+

安裝
----
* 建議使用Linux
* 安裝Firefix add-on: Greasemonkey
* 下載程式 https://github.com/jyunfan/ly_crawler/zipball/master
* 解壓縮至任意目錄
* 安裝使用者腳本: 在Firefox中打開檔案 lci_link_extractor.user.js，會有安裝提示訊息

* Make sure you installed Greasemonkey, a Firefox add-on
* Download source from https://github.com/jyunfan/ly_crawler/zipball/master
* Extract the zip file.
* Open lci_link_extractor.user.js in Firefox.  Follow the instruction.

使用
----
* 切換至安裝目錄，執行update_db.py。如: $ python update_db.py
* 開啟Firefox，打開立法院公報暨議事錄系統。程式將自動啟動，你會看到網頁自動切換，請等待約15分鐘。
* 完成後請執行腳本 process.sh
* Open the source directory and find the output link.db
* $ python shelve2json.py link > link.json

