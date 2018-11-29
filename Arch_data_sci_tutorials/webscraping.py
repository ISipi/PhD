from bs4 import BeautifulSoup
import urllib.request
import time

url = 'http://apsa.anu.edu.au/sample?order=asc&page=1&sort=spec'

html = urllib.request.urlopen(url).read()
urllib.request.urlopen(url).close()

img_base_url = 'http://apsa.anu.edu.au/assets/images/'
sample_code = []


soup = BeautifulSoup(html, 'html.parser')
table = soup.find("table", "browse-table")
tr_rows = table.find_all("tr")

species_list = []
image_list = []
specimen_dict = {} #{"species": [[list of images], "species code"]}

for row in tr_rows:
    for item in row:
        if item.find("a") is None or item.find("a")== -1 or item.find("a")=="":
            continue
        else:
            species=item.find("a")
            specimen_dict[species.get_text()] = []

    '''
    species_link = i.find("a")
    species_list.append(species_link.get_text())
    image_type = i.find_all("div", "preview-image-caption")
    print(image_type)
    if len(image_type)>0:
        for item in image_type:
            image_list.append(item.get_text())
    '''
    #print(image_type)
    #print("---")
print(specimen_dict)
#print(image_list)
#species_list = species_list[1:]
#tr_odd = [t_row.get_text() for row in t_row]
tr_even = [table.get_text() for evens in table.find_all("tr", "even")]



#title = [table.get_text() for txt in table.find_all("a")]
#print(t_row)
#print(soup.find_all("td"))

# loop through a website, find species name, image views, and code
def get_sample_code():

    return dictionary