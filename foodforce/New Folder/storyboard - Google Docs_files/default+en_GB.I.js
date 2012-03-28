(function() {
var _UDS_CONST_LOCALE = 'en-GB';
var _UDS_CONST_SHORT_DATE_PATTERN = 'DMY'; 
var _UDS_MSG_SEARCHER_IMAGE = ('Image'); 
var _UDS_MSG_SEARCHER_WEB = ('Web'); 
var _UDS_MSG_SEARCHER_BLOG = ('Blog'); 
var _UDS_MSG_SEARCHER_VIDEO = ('Video'); 
var _UDS_MSG_SEARCHER_LOCAL = ('Local'); 
var _UDS_MSG_SEARCHCONTROL_SAVE = ('save'); 
var _UDS_MSG_SEARCHCONTROL_KEEP = ('keep'); 
var _UDS_MSG_SEARCHCONTROL_INCLUDE = ('include'); 
var _UDS_MSG_SEARCHCONTROL_COPY = ('copy'); 
var _UDS_MSG_SEARCHCONTROL_CLOSE = ('close'); 
var _UDS_MSG_SEARCHCONTROL_SPONSORED_LINKS = ('Sponsored Links'); 
var _UDS_MSG_SEARCHCONTROL_SEE_MORE = ('see more...'); 
var _UDS_MSG_SEARCHCONTROL_WATERMARK = ('clipped from Google'); 
var _UDS_MSG_SEARCHER_CONFIG_SET_LOCATION = ('Search location'); 
var _UDS_MSG_SEARCHER_CONFIG_DISABLE_ADDRESS_LOOKUP = ('Disable address lookup'); 
var _UDS_MSG_SEARCHER_NEWS = ('News'); 
function _UDS_MSG_MINUTES_AGO(AGE_MINUTES_AGO) {return ('' + AGE_MINUTES_AGO + ' minutes ago');} 
var _UDS_MSG_ONE_HOUR_AGO = ('1 hour ago'); 
function _UDS_MSG_HOURS_AGO(AGE_HOURS_AGO) {return ('' + AGE_HOURS_AGO + ' hours ago');} 
function _UDS_MSG_NEWS_ALL_N_RELATED(NUMBER) {return ('all ' + NUMBER + ' related');} 
var _UDS_MSG_NEWS_RELATED = ('Related Articles'); 
var _UDS_MSG_BRANDING_STRING = ('powered by Google'); 
var _UDS_MSG_SORT_BY_DATE = ('Sort by date'); 
var _UDS_MSG_MONTH_ABBR_JAN = ('Jan'); 
var _UDS_MSG_MONTH_ABBR_FEB = ('Feb'); 
var _UDS_MSG_MONTH_ABBR_MAR = ('Mar'); 
var _UDS_MSG_MONTH_ABBR_APR = ('Apr'); 
var _UDS_MSG_MONTH_ABBR_MAY = ('May'); 
var _UDS_MSG_MONTH_ABBR_JUN = ('Jun'); 
var _UDS_MSG_MONTH_ABBR_JUL = ('Jul'); 
var _UDS_MSG_MONTH_ABBR_AUG = ('Aug'); 
var _UDS_MSG_MONTH_ABBR_SEP = ('Sep'); 
var _UDS_MSG_MONTH_ABBR_OCT = ('Oct'); 
var _UDS_MSG_MONTH_ABBR_NOV = ('Nov'); 
var _UDS_MSG_MONTH_ABBR_DEC = ('Dec'); 
var _UDS_MSG_DIRECTIONS = ('directions'); 
var _UDS_MSG_CLEAR_RESULTS = ('clear results'); 
var _UDS_MSG_SHOW_ONE_RESULT = ('show one result'); 
var _UDS_MSG_SHOW_MORE_RESULTS = ('show more results'); 
var _UDS_MSG_SHOW_ALL_RESULTS = ('show all results'); 
var _UDS_MSG_SETTINGS = ('settings'); 
var _UDS_MSG_SEARCH = ('search'); 
var _UDS_MSG_SEARCH_UC = ('Search'); 
var _UDS_MSG_POWERED_BY = ('powered by'); 
function _UDS_MSG_LOCAL_ATTRIBUTION(LOCAL_RESULTS_PROVIDER) {return ('Business listings provided by ' + LOCAL_RESULTS_PROVIDER);} 
var _UDS_MSG_SEARCHER_BOOK = ('Book'); 
function _UDS_MSG_FOUND_ON_PAGE(FOUND_ON_PAGE) {return ('Page ' + FOUND_ON_PAGE);} 
function _UDS_MSG_TOTAL_PAGE_COUNT(PAGE_COUNT) {return ('' + PAGE_COUNT + ' pages');} 
var _UDS_MSG_SEARCHER_BY = ('by'); 
var _UDS_MSG_SEARCHER_CODE = ('Code'); 
var _UDS_MSG_UNKNOWN_LICENSE = ('Unknown Licence'); 
var _UDS_MSG_SEARCHER_GSA = ('Search Appliance'); 
var _UDS_MSG_SEARCHCONTROL_MORERESULTS = ('More results'); 
var _UDS_MSG_SEARCHCONTROL_PREVIOUS = ('Previous'); 
var _UDS_MSG_SEARCHCONTROL_NEXT = ('Next'); 
var _UDS_MSG_GET_DIRECTIONS = ('Get directions'); 
var _UDS_MSG_GET_DIRECTIONS_TO_HERE = ('To here'); 
var _UDS_MSG_GET_DIRECTIONS_FROM_HERE = ('From here'); 
var _UDS_MSG_CLEAR_RESULTS_UC = ('Clear results'); 
var _UDS_MSG_SEARCH_THE_MAP = ('search the map'); 
var _UDS_MSG_SCROLL_THROUGH_RESULTS = ('scroll through results'); 
var _UDS_MSG_EDIT_TAGS = ('edit tags'); 
var _UDS_MSG_TAG_THIS_SEARCH = ('tag this search'); 
var _UDS_MSG_SEARCH_STRING = ('search string'); 
var _UDS_MSG_OPTIONAL_LABEL = ('optional label'); 
var _UDS_MSG_DELETE = ('delete'); 
var _UDS_MSG_DELETED = ('deleted'); 
var _UDS_MSG_CANCEL = ('cancel'); 
var _UDS_MSG_UPLOAD_YOUR_VIDEOS = ('upload your own video'); 
var _UDS_MSG_IM_DONE_WATCHING = ('I have finished watching this'); 
var _UDS_MSG_CLOSE_VIDEO_PLAYER = ('close video player'); 
var _UDS_MSG_NO_RESULTS = ('No Results'); 
var _UDS_MSG_LINKEDCSE_ERROR_RESULTS = ('This Custom Search Engine is loading. Try again in a few seconds.'); 
var _UDS_MSG_COUPONS = ('Coupons'); 
var _UDS_MSG_BACK = ('back'); 
var _UDS_MSG_SUBSCRIBE = ('Subscribe'); 
var _UDS_MSG_SEARCHER_PATENT = ('Patent'); 
var _UDS_MSG_USPAT = ('US Pat.'); 
var _UDS_MSG_USPAT_APP = ('US Pat. App'); 
var _UDS_MSG_PATENT_FILED = ('Filed'); 
var _UDS_MSG_ADS_BY_GOOGLE = ('Ads by Google'); 
var _UDS_MSG_SET_DEFAULT_LOCATION = ('Set default location'); 
var _UDS_MSG_NEWSCAT_TOPSTORIES = ('Top Stories'); 
var _UDS_MSG_NEWSCAT_WORLD = ('World'); 
var _UDS_MSG_NEWSCAT_NATION = ('Nation'); 
var _UDS_MSG_NEWSCAT_BUSINESS = ('Business'); 
var _UDS_MSG_NEWSCAT_SCITECH = ('Sci/Tech'); 
var _UDS_MSG_NEWSCAT_ENTERTAINMENT = ('Entertainment'); 
var _UDS_MSG_NEWSCAT_HEALTH = ('Health'); 
var _UDS_MSG_NEWSCAT_SPORTS = ('Sports'); 
var _UDS_MSG_NEWSCAT_POLITICS = ('Politics');
var c=true,g=null,i=encodeURIComponent,j=google_exportSymbol,k=window,l=google,m=navigator,n=document,o="appendChild",p="push",q="status",r="createElement",s="ServiceBase",t="length",u="language",v="style",w="loader",x={};x.blank="&nbsp;";x.image=_UDS_MSG_SEARCHER_IMAGE;x.web=_UDS_MSG_SEARCHER_WEB;x.blog=_UDS_MSG_SEARCHER_BLOG;x.video=_UDS_MSG_SEARCHER_VIDEO;x.local=_UDS_MSG_SEARCHER_LOCAL;x.news=_UDS_MSG_SEARCHER_NEWS;x.book=_UDS_MSG_SEARCHER_BOOK;x.patent="Patent";x["ads-by-google"]=_UDS_MSG_ADS_BY_GOOGLE;
x.cse="Custom Search Control";x.save=_UDS_MSG_SEARCHCONTROL_SAVE;x.keep=_UDS_MSG_SEARCHCONTROL_KEEP;x.include=_UDS_MSG_SEARCHCONTROL_INCLUDE;x.copy=_UDS_MSG_SEARCHCONTROL_COPY;x.close=_UDS_MSG_SEARCHCONTROL_CLOSE;x["sponsored-links"]=_UDS_MSG_SEARCHCONTROL_SPONSORED_LINKS;x["see-more"]=_UDS_MSG_SEARCHCONTROL_SEE_MORE;x.watermark=_UDS_MSG_SEARCHCONTROL_WATERMARK;x["search-location"]=_UDS_MSG_SEARCHER_CONFIG_SET_LOCATION;x["disable-address-lookup"]=_UDS_MSG_SEARCHER_CONFIG_DISABLE_ADDRESS_LOOKUP;
x["sort-by-date"]=_UDS_MSG_SORT_BY_DATE;x.pbg=_UDS_MSG_BRANDING_STRING;x["n-minutes-ago"]=_UDS_MSG_MINUTES_AGO;x["n-hours-ago"]=_UDS_MSG_HOURS_AGO;x["one-hour-ago"]=_UDS_MSG_ONE_HOUR_AGO;x["all-n-related"]=_UDS_MSG_NEWS_ALL_N_RELATED;x["related-articles"]=_UDS_MSG_NEWS_RELATED;x["page-count"]=_UDS_MSG_TOTAL_PAGE_COUNT;var y=[];y[0]=_UDS_MSG_MONTH_ABBR_JAN;y[1]=_UDS_MSG_MONTH_ABBR_FEB;y[2]=_UDS_MSG_MONTH_ABBR_MAR;y[3]=_UDS_MSG_MONTH_ABBR_APR;y[4]=_UDS_MSG_MONTH_ABBR_MAY;y[5]=_UDS_MSG_MONTH_ABBR_JUN;
y[6]=_UDS_MSG_MONTH_ABBR_JUL;y[7]=_UDS_MSG_MONTH_ABBR_AUG;y[8]=_UDS_MSG_MONTH_ABBR_SEP;y[9]=_UDS_MSG_MONTH_ABBR_OCT;y[10]=_UDS_MSG_MONTH_ABBR_NOV;y[11]=_UDS_MSG_MONTH_ABBR_DEC;x["month-abbr"]=y;x.directions=_UDS_MSG_DIRECTIONS;x["clear-results"]=_UDS_MSG_CLEAR_RESULTS;x["show-one-result"]=_UDS_MSG_SHOW_ONE_RESULT;x["show-more-results"]=_UDS_MSG_SHOW_MORE_RESULTS;x["show-all-results"]=_UDS_MSG_SHOW_ALL_RESULTS;x.settings=_UDS_MSG_SETTINGS;x.search=_UDS_MSG_SEARCH;x["search-uc"]=_UDS_MSG_SEARCH_UC;
x["powered-by"]=_UDS_MSG_POWERED_BY;x.sa=_UDS_MSG_SEARCHER_GSA;x.by=_UDS_MSG_SEARCHER_BY;x.code=_UDS_MSG_SEARCHER_CODE;x["unknown-license"]=_UDS_MSG_UNKNOWN_LICENSE;x["more-results"]=_UDS_MSG_SEARCHCONTROL_MORERESULTS;x.previous=_UDS_MSG_SEARCHCONTROL_PREVIOUS;x.next=_UDS_MSG_SEARCHCONTROL_NEXT;x["get-directions"]=_UDS_MSG_GET_DIRECTIONS;x["to-here"]=_UDS_MSG_GET_DIRECTIONS_TO_HERE;x["from-here"]=_UDS_MSG_GET_DIRECTIONS_FROM_HERE;x["clear-results-uc"]=_UDS_MSG_CLEAR_RESULTS_UC;
x["search-the-map"]=_UDS_MSG_SEARCH_THE_MAP;x["scroll-results"]=_UDS_MSG_SCROLL_THROUGH_RESULTS;x["edit-tags"]=_UDS_MSG_EDIT_TAGS;x["tag-search"]=_UDS_MSG_TAG_THIS_SEARCH;x["search-string"]=_UDS_MSG_SEARCH_STRING;x["optional-label"]=_UDS_MSG_OPTIONAL_LABEL;x["delete"]=_UDS_MSG_DELETE;x.deleted=_UDS_MSG_DELETED;x.cancel=_UDS_MSG_CANCEL;x["upload-video"]=_UDS_MSG_UPLOAD_YOUR_VIDEOS;x["im-done"]=_UDS_MSG_IM_DONE_WATCHING;x["close-player"]=_UDS_MSG_CLOSE_VIDEO_PLAYER;x["no-results"]=_UDS_MSG_NO_RESULTS;
x["linked-cse-error-results"]=_UDS_MSG_LINKEDCSE_ERROR_RESULTS;x.back=_UDS_MSG_BACK;x.subscribe=_UDS_MSG_SUBSCRIBE;x["us-pat"]="US Pat.";x["us-pat-app"]="US Pat. App";x["us-pat-filed"]="Filed";var _json_cache_defeater_=(new Date).getTime(),_json_request_require_prep=c;function z(a,b){A("msie")&&B("msie 6.0")?k.setTimeout(C(this,D,[a,b]),0):D(a,b)}
function D(a,b){var e=n.getElementsByTagName("head")[0];e||(e=n.body.parentNode[o](n[r]("head")));var d=n[r]("script");d.type="text/javascript";d.charset="utf-8";a=_json_request_require_prep?a+"&key="+l[w].ApiKey+"&v="+b:a;if(A("msie")||A("safari")||A("konqueror"))a=a+"&nocache="+_json_cache_defeater_++;d.src=a;var f=function(){d.onload=g;d.parentNode.removeChild(d);delete d};a=function(h){h=(h?h:k.event).target?(h?h:k.event).target:(h?h:k.event).srcElement;if(h.readyState=="loaded"||h.readyState==
"complete"){h.onreadystatechange=g;f()}};if(m.product=="Gecko")d.onload=f;else d.onreadystatechange=a;e[o](d)}function C(a,b,e){return function(){return b.apply(a,e)}}function A(a){if(a in E)return E[a];return E[a]=m.userAgent.toLowerCase().indexOf(a)!=-1}function B(a){if(a in F)return F[a];return F[a]=m.appVersion.toLowerCase().indexOf(a)!=-1}var E={},F={},G,H;if(k.n){G=c;if(k.XMLHttpRequest)H=c};if(!I)var I=j;if(!J)var J=google_exportProperty;
l[u].d={AFRIKAANS:"af",ALBANIAN:"sq",AMHARIC:"am",ARABIC:"ar",ARMENIAN:"hy",AZERBAIJANI:"az",BASQUE:"eu",BELARUSIAN:"be",BENGALI:"bn",BIHARI:"bh",BULGARIAN:"bg",BURMESE:"my",CATALAN:"ca",CHEROKEE:"chr",CHINESE:"zh",CHINESE_SIMPLIFIED:"zh-CN",CHINESE_TRADITIONAL:"zh-TW",CROATIAN:"hr",CZECH:"cs",DANISH:"da",DHIVEHI:"dv",DUTCH:"nl",ENGLISH:"en",ESPERANTO:"eo",ESTONIAN:"et",FILIPINO:"tl",FINNISH:"fi",FRENCH:"fr",GALICIAN:"gl",GEORGIAN:"ka",GERMAN:"de",GREEK:"el",GUARANI:"gn",GUJARATI:"gu",HEBREW:"iw",
HINDI:"hi",HUNGARIAN:"hu",ICELANDIC:"is",INDONESIAN:"id",INUKTITUT:"iu",IRISH:"ga",ITALIAN:"it",JAPANESE:"ja",KANNADA:"kn",KAZAKH:"kk",KHMER:"km",KOREAN:"ko",KURDISH:"ku",KYRGYZ:"ky",LAOTHIAN:"lo",LATVIAN:"lv",LITHUANIAN:"lt",MACEDONIAN:"mk",MALAY:"ms",MALAYALAM:"ml",MALTESE:"mt",MARATHI:"mr",MONGOLIAN:"mn",NEPALI:"ne",NORWEGIAN:"no",ORIYA:"or",PASHTO:"ps",PERSIAN:"fa",POLISH:"pl",PORTUGUESE:"pt-PT",PUNJABI:"pa",ROMANIAN:"ro",RUSSIAN:"ru",SANSKRIT:"sa",SERBIAN:"sr",SINDHI:"sd",SINHALESE:"si",SLOVAK:"sk",
SLOVENIAN:"sl",SPANISH:"es",SWAHILI:"sw",SWEDISH:"sv",TAJIK:"tg",TAMIL:"ta",TAGALOG:"tl",TELUGU:"te",THAI:"th",TIBETAN:"bo",TURKISH:"tr",UKRAINIAN:"uk",URDU:"ur",UZBEK:"uz",UIGHUR:"ug",VIETNAMESE:"vi",WELSH:"cy",YIDDISH:"yi",UNKNOWN:""};I("google.language.Languages",l[u].d);
var L={AMHARIC:"am",ARMENIAN:"hy",AZERBAIJANI:"az",BASQUE:"eu",BENGALI:"bn",BIHARI:"bh",BURMESE:"my",CHEROKEE:"chr",DHIVEHI:"dv",ESPERANTO:"eo",GEORGIAN:"ka",GUARANI:"gn",GUJARATI:"gu",INUKTITUT:"iu",KANNADA:"kn",KAZAKH:"kk",KHMER:"km",KURDISH:"ku",KYRGYZ:"ky",LAOTHIAN:"lo",MALAYALAM:"ml",MONGOLIAN:"mn",MARATHI:"mr",NEPALI:"ne",ORIYA:"or",PASHTO:"ps",PUNJABI:"pa",SANSKRIT:"sa",SINDHI:"sd",SINHALESE:"si",TAJIK:"tg",TAMIL:"ta",TELUGU:"te",TIBETAN:"bo",URDU:"ur",UZBEK:"uz",UIGHUR:"ug"},M={},N={},O=100;
function P(a,b){var e="id"+O++;N[e]=function(d){d=b(d);a(d);delete N[e]};return"google.language.callbacks."+e}function Q(a,b){var e="id"+O++;N[e]=function(d,f,h,K,W){d=b(d,f,h,K,W);a(d);delete N[e]};return"google.language.callbacks."+e}l[u].k=function(a){return M[a]};I("google.language.isTranslatable",l[u].k);
function R(a,b){var e="horizontal";if(b&&b.type)e=b.orientation;var d=x["powered-by"],f=l[w][s]+"/css/small-logo"+(G&&!H?".gif":".png");b=['<div style="font-family:arial,sans-serif;','font-size:11px;margin-bottom:1px" class="gBrandingText">',d,'</div><div><img src="',f,'"/></div>'];d=['<span style="vertical-align:middle;font-family:arial,sans-serif;','font-size:11px;" class="gBrandingText">',d,'<img style="padding-left:1px;vertical-align:',G?'bottom;" ':'middle;" ','src="',f,'"/></span>'];d=e=="horizontal"?
d:b;f=d.join("");e=n[r]("div");e.className="gBranding";e[v].color="#676767";if(d==b)e[v].textAlign="center";e.innerHTML=f;if(a){b=g;(b=typeof a=="string"?n.getElementById(a):a)&&b[o]&&b[o](e)}return e}var S;for(S in l[u].d)M[l[u].d[S]]=c;for(S in L)M[L[S]]=false;j("google.language.callbacks",N);j("google.language.getBranding",R);j("google.language.HORIZONTAL_BRANDING","horizontal");j("google.language.VERTICAL_BRANDING","vertical");j("google.language.CurrentLocale",_UDS_CONST_LOCALE);
j("google.language.ShortDatePattern",_UDS_CONST_SHORT_DATE_PATTERN);l[u].l=function(a,b,e){b=P(b,T);var d="http://www.google.com/complete/search";d+="?json=t&jsonp="+b+"&client=uds";if(e)d+="&hl="+i(e);d+="&q="+i(a);a=d;_json_request_require_prep=false;z(a,g);_json_request_require_prep=c};I("google.language.suggest",l[u].l);function T(a){var b={};b.query=a[0];b.suggestions=[];var e=a[1];a=a[2];for(var d=0;d<e[t];d++){var f={};f.name=e[d];f.count=parseInt(a[d].replace(",",""),10);f.results=a[d];b.suggestions[p](f)}return b};l[u].f={TEXT:"text",HTML:"html"};I("google.language.ContentType",l[u].f);l[u].translate=function(a,b,e,d){var f,h=g;if(typeof a=="string")f=a;else if(a.text&&a.type){f=a.text;h=a.type}else throw"Invalid first argument";if(f[t]<=5120)a=false;else{a=U(g,g,400,"the string to be translated exceeds the maximum length allowed",g);d(a);a=c}if(!a){d=Q(d,U);d=l[w][s]+"/Gtranslate?callback="+d;d+="&context=22";d+="&q="+i(f);d+="&langpair="+i(b+"|"+e);if(h)d+="&format="+i(h);z(d,l[u].Version)}};
I("google.language.translate",l[u].translate);function U(a,b,e,d){a={};a.status={code:e};if(d)a[q].message=d;if(e!=200){a.error=a[q];a.translation=""}else{a.translation=b.translatedText;if(b.detectedSourceLanguage)a.detectedSourceLanguage=b.detectedSourceLanguage}return a}l[u].i=function(a,b){b=Q(b,V);b=l[w][s]+"/GlangDetect?callback="+b;b+="&context=22";b+="&q="+i(a);z(b,l[u].Version)};I("google.language.detect",l[u].i);
function V(a,b,e,d){a={};a.status={code:e};if(d)a[q].message=d;if(e!=200){a.error=a[q];a.language=""}else{a.language=b[u];a.isReliable=b.isReliable;a.confidence=b.confidence}return a};var X={"en|ar":"arabic","en|bn":"indic","en|fa":"persian","en|gu":"indic","en|hi":"indic","en|kn":"indic","en|ml":"indic","en|mr":"indic","en|ne":"indic","en|pa":"indic","en|ta":"indic","en|te":"indic","en|ur":"indic"};l[u].m=function(a,b,e,d){if(typeof d!="function")throw"Invalid callback";if(aa(a,b,e,d)){d=Q(d,Y);b=[l[w][s],"/Gtransliterate?callback=",d,"&context=22","&langpair=",i(b+"|"+e)];for(e=0;e<a[t];e++){b[p]("&q=");b[p](i(a[e]))}z(b.join(""),l[u].Version)}};
I("google.language.transliterate",l[u].m);
function aa(a,b,e,d){var f="";if(typeof a!="object"||!a[t])f="Words needs to be an array.";else if(a[t]<1)f="No words to transliterate.";else if(a[t]>5)f="Number of words to transliterate exceeds the limit of 5";else if(b)if(e){var h;if(b&&e)h=X[b+"|"+e];h||(f="Transliteration not supported for the language pair. Source Language - "+b+" Destination Language - "+e+".")}else f="Destination language not specified.";else f="Source language not specified.";if(f[t]>0){var K=Y(g,g,400,f,g);k.setTimeout(function(){d(K)},
0);return false}return c}function Y(a,b,e,d){a={status:{code:e,message:d}};if(e!=200){a.error=a[q];a.transliterations=[]}else a.transliterations=b.transliterations;return a};var ba={hi:c,kn:c,ml:c,ta:c,te:c};l[u].c={h:0,g:1,e:2};l[u].j=function(a){a=a.toLowerCase();return a in ba?ca(a):l[u].c.e};I("google.language.FontRenderingStatus.SUPPORTED",l[u].c.g);I("google.language.FontRenderingStatus.UNSUPPORTED",l[u].c.h);I("google.language.FontRenderingStatus.UNKNOWN",l[u].c.e);I("google.language.isFontRenderingSupported",l[u].j);
function ca(a){switch(a){case "ml":a=[];var b="\u0d23\u0d4d\u0d23\u0d28\u0d4d\u0d31";a[p]({a:"\u0d23\u0d28\u0d4d\u200d",b:b});b="\u0d23\u0d4d\u0d23\u0d28\u0d4d\u200d\u0d31";a[p]({a:"\u0d23\u0d28\u0d4d\u200d",b:b});return Z(a);case "hi":a="\u0915\u094d\u0930\u0930\u094d\u0925";b="\u0915\u0925";return Z([{a:a,b:b}]);case "kn":a="\u0c95\u0ccd\u0cb2";b="\u0c95";return Z([{a:a,b:b}]);case "te":a="\u0c15\u0c4d\u0c32";b="\u0c15";return Z([{a:a,b:b}]);case "ta":a="\u0b95\u0bcd";b="\u0b95";return Z([{a:a,
b:b}])}}function Z(a){for(var b=0;b<a[t];b++){var e=a[b],d=e.a,f=e.b;e=n[r]("span");e[v].fontSize="10px";var h=e[v];if("opacity"in h)h.opacity=0.1;else if("MozOpacity"in h)h.MozOpacity=0.1;else if("filter"in h)h.filter="alpha(opacity=10)";n.body[o](e);e.innerHTML=d;d=$(e).width;e.innerHTML=f;f=$(e).width;n.body.removeChild(e);if(d==f)return c}return false}
function $(a){if(a[v].display!="none")return{width:a.offsetWidth,height:a.offsetHeight};var b=a[v],e=b.display,d=b.visibility,f=b.position;b.visibility="hidden";b.position="absolute";b.display="";var h=a.offsetWidth;a=a.offsetHeight;b.display=e;b.position=f;b.visibility=d;return{width:h,height:a}};
google.loader.loaded({"module":"language","version":"1.0","components":["default"]});
google.loader.eval.language = function() {eval(arguments[0]);};if (google.loader.eval.scripts && google.loader.eval.scripts['language']) {(function() {var scripts = google.loader.eval.scripts['language'];for (var i = 0; i < scripts.length; i++) {google.loader.eval.language(scripts[i]);}})();google.loader.eval.scripts['language'] = null;}})();