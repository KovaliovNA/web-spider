import urllib.parse as urlparse
import mechanize
import traceback

url = input("Enter a link: ")
br = mechanize.Browser()

urls = [url]
visited = [url]

count = 0
while len(urls) > 0:
    try:
        br.open(urls[0])
        urls.pop(0)
        for link in br.links():
            newurl = urlparse.urljoin(link.base_url, link.url)
            # print newurl
            if newurl not in visited and url in newurl:
                visited.append(newurl)
                urls.append(newurl)
                print(newurl)
                count += 1
    except:
        traceback.print_exc()
        urls.pop(0)

print("Count of links: " + count)
