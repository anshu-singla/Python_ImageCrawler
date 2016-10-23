import sys
import os
import shutil
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
def download(url):
	url=url.split('//')
	if url[0]=='http://' or url[0]=='https://':
		prefix=url[0]
	else:
		prefix='http://'
	url=url[-1].split('/')[0]
	if os.path.exists(url):
   		shutil.rmtree(url)
	os.makedirs(url)
	URL=url
	url=prefix+url
	r=requests.get(url)
	if r.status_code !=200:
		return 
	img_tags_srcs=BeautifulSoup(r.text,"lxml").find_all('img')
	list=[]
	i=0
	visited=set()
	for link in img_tags_srcs:
		link=link.attrs['src']
		if link[:7]=='http://' or link[:8]=='https://':
			list.append(link)
		if link[:1]!='/':
			link=urljoin('/',link)
		list.append(urljoin(url,link))
	for link in list:
		try:
			img_res=requests.get(link)
		except:
			continue
		i=i+1;
		filename=str(i)+'.'+link.split('.')[-1]
		f=open(URL+'/'+filename,'wb')
		f.write(img_res.content)
		f.close()
print(__file__) #contains full path
print(__name__) # __name__ == file name while importing
if __name__=='__main__' :
	if len(sys.argv)<2:
		print('Usage : python_latest_version filepath Website_Url')
	else:
		download(sys.argv[1])

# Use Ctrl+Z to stop the excecution in between
# __Thankyou:)__ 