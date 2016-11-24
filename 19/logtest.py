log = open('./logfile.txt','w')
import urllib
url = "http:www.baidu.com"
print >> log, ('Downloading file from URL %s' % url)

text = urllib.urlopen(url).read()

print >>log,"file successfully downloaded"
