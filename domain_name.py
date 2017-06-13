import tld
def get_domain(url):
	return tld.get_tld(url)
print(get_domain("https://www.vigneshramesh.in"))
