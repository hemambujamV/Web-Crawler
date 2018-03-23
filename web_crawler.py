import urllib
import re
import sys

out = []
movie = []
urltemp = "http://www.imdb.com/title/tt0"
number = "468569"
final = "Rating\tMovie\n"
#print int(number)+1

for num in range(int(number),int(number)+10):
    #print num
    
    concate = urltemp+str(num)
    #print concate
    h1= urllib.urlopen(concate)
    html = h1.read()
    #print html


    rating = re.search(r'<span itemprop="ratingValue">(.*?)</span>',html)
    if rating:
        out= rating.group(1)
        #print rating.group(1)
    
    title = re.search(r'<title>(.*?)- IMDb</title>', html) 
    if title:
        movie= title.group(1)

    final += str(out)+"\t"+str(movie)+"\n"
    out = []
    movie= []

#print final
file = open("testfile.csv","w")
file.write(final)
file.close()
