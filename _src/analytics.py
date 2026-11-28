# -*- coding: utf-8 -*-
"""Google Analytics on the marketing pages, behind a choice the visitor can change.

Only `site_pages.layout` uses this, so the home page, How it works, Pricing and
the guides count visits. The Support, About, Privacy, Terms and Your data pages
(`gen.page`, the ones the app itself opens) never load it.

What the script in `head()` does, in order:

  * Advertising storage, ad user data and ad personalisation are denied for
    everybody, always. Google signals is off here and in the property.
  * A visitor whose clock is set to a European time zone is asked first.
    Until they answer OK, Google's script is not requested at all.
  * As a second net, Google's own consent mode denies the analytics cookie in
    the EEA, the United Kingdom and Switzerland whatever the clock says.
  * A browser that sends Global Privacy Control is treated as a "no".
  * Everybody can change their mind: "Cookie choices" in the footer, or any
    link to `/#cookie-choices`, opens the banner again. A "no" also removes
    the cookies an earlier "yes" set.

The privacy policy describes exactly this (`p.web.b` in `_src/words/`). Change
one, change the other.

Set GA_ID to "" and every trace of this leaves the built pages.
"""
import json

from i18n import t

GA_ID = "G-G2F9HVRK0F"

# Where consent mode denies the analytics cookie until the visitor says yes:
# the EEA, the United Kingdom, Switzerland, and the French overseas
# departments that carry a country code of their own.
ASK_FIRST = ("AT BE BG HR CY CZ DK EE FI FR DE GR HU IE IT LV LT LU MT NL PL PT RO SK SI ES SE "
             "IS LI NO GB CH GF GP MQ YT RE MF").split()

SCRIPT = """(function(){
var id=%(id)s,key='analytics-choice',choice=null,loaded=false,tz='';
try{choice=localStorage.getItem(key)}catch(e){}
try{tz=Intl.DateTimeFormat().resolvedOptions().timeZone||''}catch(e){}
var asks=/^(Europe\\/|Arctic\\/|Atlantic\\/(Azores|Canary|Faroe|Madeira|Reykjavik)|Asia\\/(Nicosia|Famagusta))/.test(tz);
if(choice===null&&navigator.globalPrivacyControl)choice='no';
window.dataLayer=window.dataLayer||[];
function gtag(){dataLayer.push(arguments)}
function consent(v){return{ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',analytics_storage:v}}
var here=consent('denied');here.region=%(region)s;
gtag('consent','default',consent(choice==='no'?'denied':'granted'));
gtag('consent','default',here);
if(choice==='yes')gtag('consent','update',{analytics_storage:'granted'});
function load(){
if(loaded)return;loaded=true;
gtag('js',new Date());
gtag('config',id,{allow_google_signals:false,allow_ad_personalization_signals:false});
var s=document.createElement('script');s.async=true;
s.src='https://www.googletagmanager.com/gtag/js?id='+id;document.head.appendChild(s);
}
function forget(){
document.cookie.split(';').forEach(function(c){
var n=c.split('=')[0].trim();if(n.indexOf('_ga')!==0)return;
['',location.hostname,'.'+location.hostname].forEach(function(d){
document.cookie=n+'=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/'+(d?';domain='+d:'');
});
});
}
function choose(v){
choice=v;try{localStorage.setItem(key,v)}catch(e){}
gtag('consent','update',{analytics_storage:v==='yes'?'granted':'denied'});
if(v==='yes')load();else forget();
}
if(choice==='yes'||(choice===null&&!asks))load();
document.addEventListener('DOMContentLoaded',function(){
var bar=document.getElementById('consent');if(!bar)return;
function open(focus){bar.hidden=false;if(focus)bar.focus()}
bar.addEventListener('click',function(e){
var v=e.target.getAttribute&&e.target.getAttribute('data-choice');
if(!v)return;choose(v);bar.hidden=true;
if(location.hash==='#cookie-choices')history.replaceState(null,'',location.pathname+location.search);
});
document.addEventListener('click',function(e){
var a=e.target.closest&&e.target.closest('a[href$="#cookie-choices"]');
if(a){e.preventDefault();open(true)}
});
if(location.hash==='#cookie-choices')open(true);
else if(choice===null&&asks)open(false);
});
})();"""


def head():
    """The script for a page's <head>, or nothing while analytics is off."""
    if not GA_ID:
        return ""
    script = SCRIPT % {"id": json.dumps(GA_ID), "region": json.dumps(ASK_FIRST, separators=(",", ":"))}
    return f"<script>{script}</script>\n"


def banner(base, prefix=""):
    """The bar that asks. Hidden until the script decides it is needed."""
    if not GA_ID:
        return ""
    return f"""<div class="consent" id="consent" role="region" aria-label="{t("Cookie choices")}" tabindex="-1" hidden>
  <p>{t("This website counts visits with Google Analytics. Is a cookie for that OK with you?")} <a href="{base}{prefix}/privacy/#web">{t("What it collects")}</a></p>
  <div class="consent-btns"><button type="button" data-choice="no">{t("No thanks")}</button><button type="button" data-choice="yes">{t("OK")}</button></div>
</div>
"""


def footer_link(base):
    """The way back to the choice, for the footer's list of legal links."""
    if not GA_ID:
        return ""
    return f'\n    <li><a href="{base}/#cookie-choices">{t("Cookie choices")}</a></li>'
