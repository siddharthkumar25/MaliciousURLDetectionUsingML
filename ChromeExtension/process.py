import numpy as np
import pandas as pd
from urllib.parse import urlparse
from tld import get_tld
import os.path
import re
from sklearn.externals import joblib
import scipy as sp
import pickle as p
from scipy.sparse import hstack
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer


def feature_processing(url):
    
#TESTING ARRAY
    test_array = np.array([])
    
#LENGTH FEATURES
    match = re.search(
        '(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.'
        '([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|'  # IPv4
        '((0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\/)' # IPv4 in hexadecimal
        '(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}', url)  # Ipv6
    if match:
        # print match.group()
        use_of_ip =  -1
    else:
        # print 'No matching pattern found'
        use_of_ip = 1
        
    url_length = len(url)
    hostname_length = len(urlparse(url).netloc)
    path_length = len(urlparse(url).path)
    
    try:
        fd_length = len(urlparse(url).path.split('/')[1])
    except:
        fd_length = 0
        
    try:
        tld_length = len(get_tld(url,fail_silently=True))
    except:
        tld_length = -1
        
    
    
    match_short = re.search('bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|'
                      'yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|'
                      'short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|'
                      'doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|'
                      'db\.tt|qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|'
                      'q\.gs|is\.gd|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|'
                      'x\.co|prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|'
                      'tr\.im|link\.zip\.net',
                      url)
    if match_short:
        short_url =  -1
    else:
        short_url =  1
    
    
#COUNT FEATURES
    digits = 0 
    for i in url:
        if i.isnumeric():
            digits = digits + 1
    
    letters = 0
    for i in url:
        if i.isalpha():
            letters = letters + 1 
            

            
    countdash = url.count('-')
    countat = url.count('@')
    countquestion = url.count('?')
    countpercent = url.count('%')
    countdot = url.count('.')
    countequal = url.count('=')
    count_http = url.count('http')
    count_https = url.count('https')
    count_www = url.count('www')
    count_digits = digits
    count_letters = letters
    count_directory= urlparse(url).path.count('/') 
    """
    
    'url_length', 'hostname_length',
       'path_length', 'fd_length', 'tld_length', 'count-', 'count@', 'count?',
       'count%', 'count.', 'count=', 'count-www', 'count-digits',
       'count-letters', 'count_dir', 'use_of_ip', 'short_url'
    """    
    test_array = np.append(test_array,[url_length,hostname_length,path_length,fd_length,tld_length,countdash,countat,countquestion,
                                       countpercent,
                                       countdot,countequal,count_www,count_digits,count_letters,count_directory,
                                      use_of_ip,short_url])
    test_array = test_array.reshape(1,-1)
    return test_array