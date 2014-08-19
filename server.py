import web
import urllib
urls=(
	'/searchBook','searchBook',
	'/getBookDetail','getBookDetail'
)
app = web.application(urls,globals())

class searchBook:
	def GET(self):
		i = web.input(_unicode=False)
		q = i.q
		start = i.start
		max = i.max
		apiKey = 'apikey=0d053730b529ef0d270fa5921f7dcd27&'
		searchURL = 'http://api.douban.com/book/subjects?q=%s&start-index=%s&max-results=%s'%(q,start,max)
		remoteFile = urllib.urlopen(searchURL)
		receivedData = remoteFile.readlines()
		remoteFile.close()
		result = ''.join(s.decode('utf-8','ignore').encode('utf-8') for s in receivedData)
		print searchURL
		return result
		
class getBookDetail:
	def GET(self):
		i = web.input(_unicode=False)
		id = i.id
		idURL = id
		remoteFile = urllib.urlopen(idURL)
		receivedData = remoteFile.readlines()
		remoteFile.close()
		result = ''.join(s.decode('utf-8','ignore').encode('utf-8') for s in receivedData)
		return result
		
		
if __name__ == "__main__":
	app.run()		
			