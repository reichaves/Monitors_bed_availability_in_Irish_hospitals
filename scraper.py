import scraperwiki

html = scraperwiki.scrape('https://web.archive.org/web/20120318184750/http://www.inmo.ie/6022')

import lxml.html
root = lxml.html.fromstring(html) # turn our HTML into an lxml object

tds = root.cssselect('td') # get all the <td tags

for td in tds:
	record = { "td" : td.text } # column name and value
	try:
		scraperwiki.sqlite.save(["td"], record) # save the records one by one
	except:
		record = { "td" : "NO ENTRY" } # column name and value
		scraperwiki.sqlite.save(["td"], record) # save the records one by one
