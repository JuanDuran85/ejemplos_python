"""

Working with python-whois library
-Create a simple importable Python module which will produce parsed WHOIS data for a given domain.
-Able to extract data for all the popular TLDs (com, org, net, ...)
-Query a WHOIS server directly instead of going through an intermediate web service like many others do

"""

import whois

domain = "https://alirafael.com/"
domain_info = whois.whois(domain)
print(domain_info)
for key,value in domain_info.items():
    print(key,value)


