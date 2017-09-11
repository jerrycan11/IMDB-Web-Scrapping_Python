
# coding: utf-8

# In[ ]:

import requests
from bs4 import BeautifulSoup

num = 1;

text_file = open("Output1.csv", "w")

            
with open("Output1.csv", "w") as text_file:
    
    st = "index"+","+"title"+","+"rtime"+","+"rating"+","+"votes"+","+"genre"+","+"country"+","+"releasedate"+","+"filminglocation"+","+"prodco"+","+"years"+","+"director"+","+"writer"+","+"actors"+","+"color"+","+"budget"+","+"gross"+","+"aspectratio"+","+"movielink"
    print(st)
    print(st, file=text_file)
    
    while True:    

        
        nxtlink = "http://www.imdb.com/search/title?count=100&title_type=feature,tv_series&sort=num_votes,desc&page=" + str(num) + "&ref_=adv_nxt"
        num = num+1

        page = requests.get(nxtlink)
        soup = BeautifulSoup(page.content, 'xml')
        
        
        
        for link in soup.findAll('div', attrs ={"class":"lister-item-content"}):
            country=""
            releasedate=""
            filminglocation=""
            prodco=""
            years=""
            director=""
            writer=""
            actors=""
            movielink=""
            index=""
            title=""
            rtime=""
            rating=""
            votes=""
            genre=""
            budget=""
            gross=""
            color=""
            aspectratio=""
            
            try:     
                movielink = "http://www.imdb.com"+link.find_next('a')['href']
               # print(movielink)
                
                index = link.find_next('span', attrs ={"class":"lister-item-index unbold text-primary"}).getText().replace('.','').replace(',','')
               # print(index)
                title = link.find_next('a').getText().replace('#','').replace(',',' ')
               # print(title)
                rtime = link.find_next('span', attrs ={"class":"runtime"}).getText().replace(' ', '')
               # print(rtime)
                rating = link.find_next('strong').getText().replace(' ', '') 
               # print(rating)
                votes = link.find_next('span', attrs ={"name":"nv"}).getText().replace(' ', '').replace(',', '')
               # print(votes)
                genre = link.find_next('span', attrs ={"class":"genre"}).getText()
                genre = genre.replace('\n', ' ').replace(' ','').replace(',','|')
               # print(genre)
                
                
                subpage = requests.get(movielink)
                soup = BeautifulSoup(subpage.content, 'xml')
                
                for link in soup.findAll('div', attrs ={"id":"root"}):
                    for link in soup.findAll('div', attrs ={"class":"credit_summary_item"}):
                        line = link.get_text()
                        if "Director" in line:
                            director = director+line.replace('Director:','').replace(' ','').replace(',','|').replace('\n','').replace('itemtype="http://schema.org/Person">','')+" "
                        if "Writers" in line:
                            writer = writer+line.replace('Writers:','').replace(' ','').replace(',','|').replace('\n','').replace('itemtype="http://schema.org/Person">','').replace('2morecredits','')
                    
                    for link in soup.findAll('div', attrs ={"class":"title_wrapper"}):
                        for link in soup.findAll('span', attrs ={"id":"titleYear"}):
                            years = link.getText().replace('(','').replace(')','')
                
                    for link in soup.findAll('table', attrs ={"class":"cast_list"}):
                        for link in soup.findAll('tr',attrs ={"class":"odd"}):
                            actors = actors+link.find_next('td',attrs ={"itemprop":"actor"}).getText().replace('itemtype="http://schema.org/Person">','').replace('\n','').replace(' ','')+"|"
                        for link in soup.findAll('tr',attrs ={"class":"even"}):
                            actors = actors+link.find_next('td',attrs ={"itemprop":"actor"}).getText().replace('itemtype="http://schema.org/Person">','').replace('\n','').replace(' ','')+"|"
                    for link in soup.find_all('div', attrs ={"class":"txt-block"}):
                        line = link.get_text()
                        if "Country" in line:
                            country = line.replace('Country:','').replace(' ','').replace(',','|').replace('\n','')
                        if "Release Date" in line:
                            releasedate = line.replace('Release Date:','').replace('See more','').replace(' ','').replace(',','|').replace('\n','')
                        if "Filming Locations" in line:
                            filminglocation = line.replace(' ','').replace(',','|').replace('Filming Locations:','').replace('FilmingLocations:','').replace('\n','').replace('Seemore','')
                        if "Production Co" in line:
                            prodco = line.replace(' ','').replace(',','|').replace('Production Co:','').replace('ProductionCo:','').replace('itemtype="http://schema.org/Organization">','').replace('\n','').replace('Seemore','')
                        if "ProductionCo" in line:
                            prodco = line.replace(' ','').replace(',','|').replace('Production Co:','').replace('ProductionCo:','').replace('itemtype="http://schema.org/Organization">','').replace('\n','').replace('Seemore','')
                        if "Budget" in line:
                            budget = line.replace(',','').replace(' ','').replace('Budget:','').replace('itemtype="http://schema.org/Organization">','').replace('\n','').replace('See more','').replace('(',' ').replace(')',' ')
                        if "Gross" in line:
                            gross = line.replace(',','').replace(' ','').replace('Gross:','').replace('itemtype="http://schema.org/Organization">','').replace('\n','').replace('See more','')
                        if "Color" in line:
                            color = line.replace(' ','').replace(',','|').replace('Color:','').replace('itemtype="http://schema.org/Organization">','').replace('\n','').replace('See more','')
                        if "Aspect Ratio" in line:
                            aspectratio = line.replace(' ','').replace(',','|').replace('Aspect Ratio:','').replace('AspectRatio:','').replace('itemtype="http://schema.org/Organization">','').replace('\n','').replace('See more','')
                        
                st = index+","+title+","+rtime+","+rating+","+votes+","+genre+","+country+","+releasedate+","+filminglocation+","+prodco+","+years+","+director+","+writer+","+actors+","+color+","+budget+","+gross+","+aspectratio+","+movielink

                #cursor = db.cursor()
                #strc = "insert into imdb_popularity values("+index+",'"+title+"','"+rtime+"','"+rating+"','"+votes+"','"+genre+"','"+country+"','"+releasedate+"','"+filminglocation+"','"+prodco+"','"+years+"','"+director+"','"+writer+"','"+actors+"','"+color+"','"+budget+"','"+gross+"','"+aspectratio+"','"+movielink+"')"
                #print(strc)
                #cursor.execute(strc)
                #db.close()
                
                print(st)
                print(st, file=text_file)
                
            except:
                st = index+","+title+","+rtime+","+rating+","+votes+","+genre+","+country+","+releasedate+","+filminglocation+","+prodco+","+years+","+director+","+writer+","+actors+","+movielink
                
                #cursor = db.cursor()
                #cursor.execute("insert into imdb_popularity values("+index+",'"+title+"','"+rtime+"','"+rating+"','"+votes+"','"+genre+"','"+country+"','"+releasedate+"','"+filminglocation+"','"+prodco+"','"+years+"','"+director+"','"+writer+"','"+actors+"','"+color+"','"+budget+"','"+gross+"','"+aspectratio+"','"+movielink+"')")
                #db.close()
                
                print(st)
                print(st, file=text_file)
                

text_file.close()


# In[ ]:



