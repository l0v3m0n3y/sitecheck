import requests
class Client():
	def __init__(self):
		self.api="https://sitecheck.sucuri.net/api/v3"
		self.headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36","x-requested-with": "XMLHttpRequest"}
	def scan_url(self,url):
		return requests.get(f"{self.api}/?scan={url}",headers=self.headers).json()