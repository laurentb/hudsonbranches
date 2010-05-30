import urllib2

pwdmgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
pwdmgr.add_password(None, 'http://hudson.example.org/',
                            'penguins', 'are_awesome');
handler = urllib2.HTTPDigestAuthHandler(pwdmgr)
opener = urllib2.build_opener(handler)

baseurl = "http://hudson.example.org/"

# if you don't have any authentication necessary, only baseurl is useful
