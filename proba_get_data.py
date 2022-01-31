from tracemalloc import start
from tornado.httpclient import HTTPClient

def synchronous_fetch(url):
    http_client = HTTPClient()
    response = http_client.fetch(url)
    return response.body

if __name__ == '__main__':
    url = 'https://www.google.com/search?q=how+to+split+image+text+into+lines&sxsrf=APq-WBvPc984TKA_bEV1vmRvNkVa3EoVEg%3A1643640104825&source=hp&ei=KPX3YenaLZWVrwS8h5XYCw&iflsig=AHkkrS4AAAAAYfgDOKDRmUdYthNiQgny3pGHYQUD6LIk&oq=&gs_lcp=Cgdnd3Mtd2l6EAEYADIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJ1AAWABgshxoAXAAeACAAQCIAQCSAQCYAQCwAQo&sclient=gws-wiz'
    f_r = open('file_result.html', 'w')
    f_r.write(str(synchronous_fetch(url)))
    f_r.close()
    
    