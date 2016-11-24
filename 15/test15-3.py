from urllib import urlopen
from bs4 import BeautifulSoup
text = urlopen('http://python.org/community/jobs').read()
soup = BeautifulSoup(text)

jobs = set()

for header in soup('p'):            
    links = header('a', 'reference')
    print header
    print links
    if not links:continue
    link = links[0]
    jobs.add('%s(%s)' %(link.string, link['href']))
print '\n'.join(sorted(jobs,key=lambda s:s.lower()))
