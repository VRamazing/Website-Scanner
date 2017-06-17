import urllib.request 
#to get data from net/get/post
import io 
#to get in readable format

def get_robots_text(url):
	if url.endswith('/'):
		path = url
	else:
		path = url + '/'
	req = urllib.request.urlopen(path + 'robots.txt')
	data=io.TextIOWrapper(req,encoding='utf-8')
	return data.read()

