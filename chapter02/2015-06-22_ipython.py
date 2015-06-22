"""
Nothing! Do not view, just command record.
"""
JianWoodeMacBook-Pro:manning Jian$ ipython
Python 2.7.6 (default, Sep  9 2014, 15:04:36)
Type "copyright", "credits" or "license" for more information.

IPython 3.1.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: teacher = "Mr.Morton"

In [2]: teacher
Out[2]: 'Mr.Morton'

In [3]: print teacher
Mr.Morton

In [4]: ls
chapter01/ chapter02/

In [5]: clear

In [6]: print "(1+2)"
(1+2)

In [7]: print "int(1+2)"
int(1+2)

In [8]: print "int(float(1+2))"
int(float(1+2))

In [9]: first = 3

In [10]: second =
  File "<ipython-input-10-ae82413d6d79>", line 1
      second =
                   ^
                   SyntaxError: invalid syntax


                   In [11]: second = 5

                   In [12]: print f
                   %%file     file       filter     finally    first      float      for        format     from       frozenset

                   In [12]: print first + se
                   %set_env  second    set       setattr

                   In [12]: print first + second
                   8

                   In [13]: t = first + second

                   In [14]: t
                   Out[14]: 8

                   In [15]: print t
                   8

                   In [16]: myt = "梁静茹"

                   In [17]: myt
                   Out[17]: '\xe6\xa2\x81\xe9\x9d\x99\xe8\x8c\xb9'

                   In [18]: print myt
                   梁静茹

                   In [19]: yourt = myt

                   In [20]: myt
                   Out[20]: '\xe6\xa2\x81\xe9\x9d\x99\xe8\x8c\xb9'

                   In [21]: yourt
                   Out[21]: '\xe6\xa2\x81\xe9\x9d\x99\xe8\x8c\xb9'

                   In [22]: print myt
                   梁静茹

                   In [23]: print yourt
                   梁静茹

                   In [24]: print myt, yourt
                   梁静茹 梁静茹

                   In [25]: myt = "Tony"

                   In [26]: print myt
                   Tony

                   In [27]: print yourt
                   梁静茹

                   In [28]: long_str = """
                      ....: hi, Mr.li
                         ....: I am jwoo.
                            ....: I want to work in CXGC.
                               ....: I Will Do It.
                                  ....: Beijing, Wait Me.
                                     ....: """

                                     In [29]: long_str
                                     Out[29]: '\nhi, Mr.li\nI am jwoo.\nI want to work in CXGC.\nI Will Do It.\nBeijing, Wait Me.\n'

                                     In [30]: print long_str

                                     hi, Mr.li
                                     I am jwoo.
                                     I want to work in CXGC.
                                     I Will Do It.
                                     Beijing, Wait Me.


                                     In [31]: long_str = """
                                     hi, Mr.li
                                     I am jwoo.
                                     I want to work in CXGC.
                                     I Will Do It.
                                     Beijing, Wait Me."""

                                     In [32]: long_str = """hi, Mr.li
                                     I am jwoo.
                                     I want to work in INNOVATION WORKS.
                                     I Will Do It.
                                     Beijing, Wait Me."""

                                     In [33]: print lon
                                     long      long_str

                                     In [33]: print long_str
                                     hi, Mr.li
                                     I am jwoo.
                                     I want to work in INNOVATION WORKS.
                                     I Will Do It.
                                     Beijing, Wait Me.

                                     In [34]: import re
                                     re        readline  repr      requests  resource  rexec

                                     In [34]: import requests

                                     In [35]: my_url = "http://weibo.com/iwrecruiting"

                                     In [36]: re_result = requests.get(my_url)

                                     In [37]: print re
                                     %recall           %reload_ext       %rerun            %reset_selective  reduce            repr              return
                                     %rehashx          %rep              %reset            re_result         reload            requests          reversed

                                     In [37]: print re_result.text
                                     <!DOCTYPE html>
                                     <html>
                                     <head>
                                         <meta http-equiv="Content-type" content="text/html; charset=gb2312"/>
                                             <title>Sina Visitor System</title>
                                             </head>
                                             <body>
                                             <span id="message"></span>
                                             <script type="text/javascript" src="/js/visitor/mini.js"></script>
                                             <script type="text/javascript">
                                                 window.use_fp = "1" == "1"; // ÊÇ·ñ²É¼¯Éè±¸Ö¸ÎÆ¡£
                                                     var url = url || {};
                                                         (function () {
                                                                     this.l = function (u, c) {
                                                                                     try {
                                                                                                         var s = document.createElement("script");
                                                                                                                         s.type = "text/javascript";
                                                                                                                                         s[document.all ? "onreadystatechange" : "onload"] = function () {

                                                                                                                                                             if (document.all && this.readyState != "loaded" && this.readyState != "complete") {
                                                                                                                                                                                         return
                                                                                                                                                                                                             }
                                                                                                                                                                                 this[document.all ? "onreadystatechange" : "onload"] = null;
                                                                                                                                                                                                     this.parentNode.removeChild(this);
                                                                                                                                                                                                                         if (c) {
                                                                                                                                                                                                                                                     c()
                                                                                                                                                                                                                                                                         }
                                                                                                                                                                                                                                         };
                                                                                                     s.src = u;
                                                                                                                     document.getElementsByTagName("head")[0].appendChild(s)
                                                                                                                                 } catch (e) {
                                                                                                                                                 }
                                                                                                                                         };
                                                                                                                                             }).call(url);

                                                             // Á÷³ÌÈë¿Ú¡£
                                                                 wload(function () {

                                                                             try {

                                                                                             var need_restore = "1" == "1"; // ÊÇ·ñ×ß»Ö¸´Éí·ÝÁ÷³Ì¡£

                                                                                                         // Èç¹ûÐèÒª×ß»Ö¸´Éí·ÝÁ÷³Ì£¬³¢ÊÔ´Ó cookie »ñÈ¡ÓÃ»§Éí·Ý¡£
                                                                                                                     if (!need_restore || !Store.CookieHelper.get("SRF")) {

                                                                                                                                         // Èô»ñÈ¡Ê§°Ü×ß´´½¨·Ã¿ÍÁ÷³Ì¡£
                                                                                                                                                         // Á÷³ÌÖ´ÐÐÊ±¼ä¹ý³¤£¨³¬¹ý 3s£©£¬ÔòÈÏÎª³ö´í¡£
                                                                                                                                                                         var error_timeout = window.setTimeout("error_back()", 3000);

                                                                                                                                                                                         tid.get(function (tid, where, confidence) {
                                                                                                                                                                                                                 // È¡Ö¸ÎÆË³ÀûÍê³É£¬Çå³ý³ö´í timeout ¡£
                                                                                                                                                                                                                                     window.clearTimeout(error_timeout);
                                                                                                                                                                                                                                                         incarnate(tid, where, confidence);
                                                                                                                                                                                                                                                                         });
                                                                                                                                                                                                     } else {
                                                                                                                                                                                                                         // ÓÃ»§Éí·Ý´æÔÚ£¬³¢ÊÔ»Ö¸´ÓÃ»§Éí·Ý¡£
                                                                                                                                                                                                                                         restore();
                                                                                                                                                                                                                                                     }
                                                                                                                                                                                                                                                             } catch (e) {
                                                                                                                                                                                                                                                                             // ³ö´í¡£
                                                                                                                                                                                                                                                                                         error_back();
                                                                                                                                                                                                                                                                                                 }
                                                                                                                                                                                                                                                                 });

                                                                                 // ¡°·µ»Ø¡± »Øµ÷º¯Êý¡£
                                                                                     var return_back = function (response) {

                                                                                                     if (response["retcode"] == 20000000) {
                                                                                                                     back();
                                                                                                                             } else {
                                                                                                                                             // ³ö´í¡£
                                                                                                                                                         error_back(response["msg"]);
                                                                                                                                                                 }
                                                                                                                                 };

                                                                                         // Ìø×ª»Ø³õÊ¼µØÖ·¡£
                                                                                             var back = function() {

                                                                                                             var url = "http://weibo.com/iwrecruiting";
                                                                                                                     if (url != "none") {
                                                                                                                                     window.location.href = url;
                                                                                                                                             }
                                                                                                                         };

                                                                                                 // ¿çÓò¹ã²¥¡£
                                                                                                     var cross_domain = function (response) {

                                                                                                                     var from = "weibo";
                                                                                                                             if (response["retcode"] == 20000000) {

                                                                                                                                             var crossdomain_host = "login.sina.com.cn";
                                                                                                                                                         if (crossdomain_host != "none") {

                                                                                                                                                                             var cross_domain_intr = window.location.protocol + "//" + crossdomain_host + "/visitor/visitor?a=crossdomain&cb=return_back&s=" +
                                                                                                                                                                                                     encodeURIComponent(response["data"]["sub"]) + "&sp=" + encodeURIComponent(response["data"]["subp"]) + "&from=" + from + "&_rand=" + Math.random();
                                                                                                                                                                                                                     url.l(cross_domain_intr);
                                                                                                                                                                                                                                 } else {

                                                                                                                                                                                                                                                     back();
                                                                                                                                                                                                                                                                 }
                                                                                                                                                                                                                                         } else {

                                                                                                                                                                                                                                                         // ³ö´í¡£
                                                                                                                                                                                                                                                                     error_back(response["msg"]);
                                                                                                                                                                                                                                                                             }
                                                                                                                                                                                                                                             };

                                                                                                         // ÎªÓÃ»§¸³Óè·Ã¿ÍÉí·Ý ¡£
                                                                                                             var incarnate = function (tid, where, conficence) {

                                                                                                                             var gen_conf = "";
                                                                                                                                     var from = "weibo";
                                                                                                                                             var incarnate_intr = window.location.protocol + "//" + window.location.host + "/visitor/visitor?a=incarnate&t=" +
                                                                                                                                                             encodeURIComponent(tid) + "&w=" + encodeURIComponent(where) + "&c=" + encodeURIComponent(conficence) +
                                                                                                                                                                             "&gc=" + encodeURIComponent(gen_conf) + "&cb=cross_domain&from=" + from + "&_rand=" + Math.random();
                                                                                                                                                                                     url.l(incarnate_intr);
                                                                                                                                                                                         };

                                                                                                                 // »Ö¸´ÓÃ»§¶ªÊ§µÄÉí·Ý¡£
                                                                                                                     var restore = function () {

                                                                                                                                     var from = "weibo";
                                                                                                                                             var restore_intr = window.location.protocol + "//" + window.location.host +
                                                                                                                                                             "/visitor/visitor?a=restore&cb=restore_back&from=" + from + "&_rand=" + Math.random();

                                                                                                                                                                     url.l(restore_intr);
                                                                                                                                                                         };

                                                                                                                         // ¿çÓò»Ö¸´¶ªÊ§µÄÉí·Ý¡£
                                                                                                                             var restore_back = function (response) {

                                                                                                                                             // Éí·Ý»Ö¸´³É¹¦×ß¹ã²¥Á÷³Ì£¬·ñÔò×ß´´½¨·Ã¿ÍÁ÷³Ì¡£
                                                                                                                                                     if (response["retcode"] == 20000000) {

                                                                                                                                                                     var url = "http://weibo.com/iwrecruiting";
                                                                                                                                                                                 var alt = response["data"]["alt"];
                                                                                                                                                                                             var savestate = response["data"]["savestate"];
                                                                                                                                                                                                         if (alt != "" && url != "none") {

                                                                                                                                                                                                                             var params = "entry=sso&alt=" + encodeURIComponent(alt) + "&returntype=META&url=" + encodeURIComponent(url) +
                                                                                                                                                                                                                                                     "&gateway=1&savestate=" + encodeURIComponent(savestate);
                                                                                                                                                                                                                                                                     window.location.href = "http://login.sina.com.cn/sso/login.php?" + params;
                                                                                                                                                                                                                                                                                 } else {

                                                                                                                                                                                                                                                                                                     cross_domain(response);
                                                                                                                                                                                                                                                                                                                 }
                                                                                                                                                                                                                                                                                         } else {

                                                                                                                                                                                                                                                                                                         tid.get(function (tid, where, confidence) {
                                                                                                                                                                                                                                                                                                                             incarnate(tid, where, confidence);
                                                                                                                                                                                                                                                                                                                                         });
                                                                                                                                                                                                                                                                                                                 }
                                                                                                                                                                                                                                                                                             };

                                                                                                                                 // ³ö´íÇé¿ö·µ»ØµÇÂ¼Ò³¡£
                                                                                                                                     var error_back = function (msg) {

                                                                                                                                                     var url = "http://weibo.com/iwrecruiting";
                                                                                                                                                             if (url != "none") {

                                                                                                                                                                             if (url.indexOf("ssovie4c55=0") === -1) {
                                                                                                                                                                                                 url += (((url.indexOf("?") === -1) ? "?" : "&") + "ssovie4c55=0");
                                                                                                                                                                                                             }
                                                                                                                                                                                         window.location.href = "http://weibo.com/login.php";
                                                                                                                                                                                                 } else {

                                                                                                                                                                                                                 if(document.getElementById("message")) {
                                                                                                                                                                                                                                     document.getElementById("message").innerHTML = "Error occurred" + (msg ? (": " + msg) : ".");
                                                                                                                                                                                                                                                 }
                                                                                                                                                                                                                         }
                                                                                                                                                                                                     }

                                                                                                                                     </script>
                                                                                                                                     </body>
                                                                                                                                     </html>

                                                                                                                                     In [38]: teacher
                                                                                                                                     Out[38]: 'Mr.Morton'

                                                                                                                                     In [39]: teacher = "Mr.Smith"

                                                                                                                                     In [40]: teacher
                                                                                                                                     Out[40]: 'Mr.Smith'
