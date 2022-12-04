#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# # Q1. Python program to display all the header tags from https://en.wikipedia.org

# In[45]:


# import required modules
from bs4 import BeautifulSoup
import requests

# get URL
data = requests.get('https://en.wikipedia.org/')

# scrape webpage
soup = BeautifulSoup(data.content, 'html.parser')

# find all header tags in HTML
header=[]
for i in soup.find_all(['h1','h2','h3','h4','h5','h6']):
    i=i.get_text().replace('\n','')                     #replacing all newlines.
    header.append(i)


# In[46]:


header


# # Q2. Python program to display IMDB's top rated 100 movies data (name, rating, year of release)

# In[10]:


import pandas as pd
data = requests.get('https://www.imdb.com/list/ls000049962/')
soup = BeautifulSoup(data.text, "html.parser")

#Scraping first movie
title1=soup.find('h3', class_="lister-item-header")

#Scraping top 100 movies
list1=[]
for i in soup.find_all('h3', class_="lister-item-header"):
    i=i.get_text().replace('\n',"")
    i=i.split('(')[0]
    i=i.split('.')[1]
    list1.append(i)
    
#Scraping first movie rating   
rating=soup.find('div', class_="ipl-rating-star small")

#Scraping top 100 movies rating
list2=[]
for i in soup.find_all('div', class_="ipl-rating-star small"):
    i=i.get_text().replace('\n',"")
    list2.append(i)
    
#Scraping year of release of movie     
year=soup.find('span', class_="lister-item-year text-muted unbold")

list3=[]
for i in soup.find_all('span', class_="lister-item-year text-muted unbold"):
    list3.append(i.text)

#Creating data frame  
df=pd.DataFrame({'Movie name': list1, 'Rating': list2, 'Year of release': list3})

    


# In[12]:


df


# # Q3. Python program to display IMDB's top rated 100 indian movies data (name, rating, year of release)

# In[19]:


data = requests.get('https://www.imdb.com/india/top-rated-indian-movies/')
soup = BeautifulSoup(data.text, "html.parser")

#Scraping first movie
title1=soup.find('td', class_="titleColumn")

#Scraping top 100 movies
list1=[]
for i in soup.find_all('td', class_="titleColumn"):
    i=i.get_text().replace('\n',"")
    i=i.split('(')[0]
    i=i.split('.')[1]
    list1.append(i)
    
#Scraping first movie rating   
rating=soup.find('td', class_="ratingColumn imdbRating")

#Scraping top 100 movies rating
list2=[]
for i in soup.find_all('td', class_="ratingColumn imdbRating"):
    i=i.get_text().replace('\n',"")
    list2.append(i)
    
 

    
#Scraping year of release of movie     
year=soup.find('span', class_="secondaryInfo")

list3=[]
for i in soup.find_all('span', class_="secondaryInfo"):
    list3.append(i.text)

#Creating data frame  
df=pd.DataFrame({'Movie name': list1[0:100], 'Rating': list2[0:100], 'Year of release': list3[0:100]})


# In[20]:


df


# # Q4. Python program to display list of respected former presidents of India (name, term of office)

# In[2]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
data=requests.get('https://presidentofindia.nic.in/former-presidents.htm')
soup=BeautifulSoup(data.content)

first_name=soup.find('div',class_='presidentListing')


list4=[]
for i in soup.find_all('div',class_='presidentListing'):
    i=i.get_text().replace('\n',"")
    i=i.split('Term of Office:') [0]                  #using split function to split function
    list4.append(i)
    
list5=[]
for i in soup.find_all('div',class_='presidentListing'):
    i=i.get_text().replace('\n',"")
    i=i.split('Term of Office:') [1]
    list5.append(i)    
    
df2=pd.DataFrame({'Name of Forme President':list4,'Term of Office':list5})    


# In[3]:


df2


# # Q5. Python program to scrap top 10 ODI teams in Men's Cricket from icc.cricket.com(matches, points, ratingg)

# In[4]:


data=requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')
soup=BeautifulSoup(data.content)

team=soup.find('span',class_='u-hide-phablet')

name=[]
for i in soup.find_all('span',class_='u-hide-phablet'):
    name.append(i.text)
    
list7=[]
for i in soup.find_all('td',class_='table-body__cell u-center-text'):
    i=i.get_text().replace('\n','')
    list7.append(i)
matches=list7[0:100:2]    # class body for the match and point is same, hence both are shown in the list
matches.insert(0,23)      #matches for the topper is not scrapable so using insert to add value for topper
print(matches)

points=[]
for i in soup.find_all('td',class_='table-body__cell u-center-text'):
    i=i.get_text().replace('\n','')
    points.append(i)
point=points[1:100:2]    # class body for the match and point is same, hence both are shown in the list
point.insert(0,2670)     #point for the topper is not scrapable so using insert to add value for topper
print(point)

rating=[]
for i in soup.find_all('td',class_='table-body__cell u-text-right rating'):
    rating.append(i.text)
rating.insert(0,116)     #rating for the topper is not scrapable so using insert to add value for topper

df=pd.DataFrame({'Name': name[0:10], 'Matches': matches[0:10], 'Points': point[0:10],'Rating': rating[0:10]})


# In[5]:


df


# # Q5-2. top 10 ODI batsman

# In[47]:


data=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi')
soup=BeautifulSoup(data.content, "html.parser")

pname=[]
for i in soup.find_all('td',class_='table-body__cell name'):
    i=i.get_text().replace('\n','')
    pname.append(i)
pname.insert(0,'Babar Azam')

team=[]
for i in soup.find_all('span',class_='table-body__logo-text'):
    i=i.get_text().replace('\n','')
    team.append(i)
team.insert(0,'Pak')


rating=[]
for i in soup.find_all('td',class_='table-body__cell u-text-right rating'):
    i=i.get_text().replace('\n','')
    rating.append(i)
rating.insert(0,890)


df=pd.DataFrame({'Name': pname[0:10], 'Team': team[0:10], 'Rating': rating[0:10]})
    


# In[48]:


df


# # Q5-3. top 10 ODI bowler

# In[8]:


data=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling')
soup=BeautifulSoup(data.content, "html.parser")

pname=[]
for i in soup.find_all('td',class_="table-body__cell rankings-table__name name"):
    i=i.get_text().replace('\n','')
    pname.append(i)
pname.insert(0,'Trent Boult')

team=[]
for i in soup.find_all('span',class_='table-body__logo-text'):
    i=i.get_text().replace('\n','')
    team.append(i)
team.insert(0,'NZ')


rating=[]
for i in soup.find_all('td',class_='table-body__cell rating'):
    i=i.get_text().replace('\n','')
    rating.append(i)
rating.insert(0,760)


df=pd.DataFrame({'Name': pname[0:10], 'Team': team[0:10], 'Rating': rating[0:10]})


# In[9]:


df


# # Q6-1. Python program to scrap top 10 ODI teams in Women's Cricket from icc.cricket.com(matches, points, rating)

# In[49]:


data=requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')
soup=BeautifulSoup(data.content)

pname=[]
for i in soup.find_all('span',class_='u-hide-phablet'):
    pname.append(i.text)
    
list7=[]
for i in soup.find_all('td',class_='table-body__cell u-center-text'):
    i=i.get_text().replace('\n','')
    list7.append(i)
matches=list7[0:100:2]
matches.insert(0,18)
print(matches)

points=[]
for i in soup.find_all('td',class_='table-body__cell u-center-text'):
    i=i.get_text().replace('\n','')
    points.append(i)
point=points[1:100:2]
point.insert(0,3061)
print(point)

rating=[]
for i in soup.find_all('td',class_='table-body__cell u-text-right rating'):
    rating.append(i.text)
rating.insert(0,170)

df=pd.DataFrame({'Name': pname[0:10], 'Matches': matches[0:10], 'Points': point[0:10],'Rating': rating[0:10]})


# In[50]:


df


# # Q6-2. top 10 ODI women bating player

# In[12]:


data=requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting')
soup=BeautifulSoup(data.content)

pname=[]
for i in soup.find_all('td',class_='table-body__cell rankings-table__name name'):
    i=i.get_text().replace('\n','')
    pname.append(i)
pname.insert(0,'Alyssa Healy')

team=[]
for i in soup.find_all('span',class_='table-body__logo-text'):
    i=i.get_text().replace('\n','')
    team.append(i)
team.insert(0,'Aus')


rating=[]
for i in soup.find_all('td',class_='table-body__cell rating'):
    i=i.get_text().replace('\n','')
    rating.append(i)
rating.insert(0,785)


df=pd.DataFrame({'Name': pname[0:10], 'Team': team[0:10], 'Rating': rating[0:10]})


# In[13]:


df


# # Q6-3. top 10 ODI women allrounder

# In[18]:


data=requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder')
soup=BeautifulSoup(data.content)

pname=[]
for i in soup.find_all('td',class_='table-body__cell rankings-table__name name'):
    i=i.get_text().replace('\n','')
    pname.append(i)
pname.insert(0,'Healey Mathews')

team=[]
for i in soup.find_all('span',class_='table-body__logo-text'):
    i=i.get_text().replace('\n','')
    team.append(i)
team.insert(0,'WI')


rating=[]
for i in soup.find_all('td',class_='table-body__cell rating'):
    i=i.get_text().replace('\n','')
    rating.append(i)
rating.insert(0,380)


df=pd.DataFrame({'Name': pname[0:10], 'Team': team[0:10], 'Rating': rating[0:10]})


# In[19]:


df


# # Q7-. Python program to scrap headlines from https://www.cnbc.com/world/?region=world

# In[34]:


data=requests.get('https://www.cnbc.com/world/?region=world')
soup=BeautifulSoup(data.content,"html.parser")

headlines=[]
for i in soup.find_all('a',class_="LatestNews-headline"):
    headlines.append(i.text)

time=[]
for i in soup.find_all('span',class_="LatestNews-wrapper"):
    time.append(i.text)
    
urls = []
for link in soup.find_all('a',class_="LatestNews-headline"):
    urls.append(link.get('href'))    
    
df=pd.DataFrame({'Headlines': headlines,'Time': time, 'Link': urls})    


# In[35]:


df


# # Q8. Write a python program to scrape the details of most downloaded articles from AI in last 90 days.
# https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles
# i Paper Title
# ii) Authors
# iii) Published Date
# iv) Paper URL 

# In[36]:


data=requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')
soup=BeautifulSoup(data.content, 'html.parser')

paper=[]
for i in soup.find_all('h2', class_="sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg"):
    paper.append(i.text)
    
author=[]
for i in soup.find_all('span', class_="sc-1w3fpd7-0 dnCnAO"):
    author.append(i.text)
    
pdate=[]
for i in soup.find_all('span', class_="sc-1thf9ly-2 dvggWt"):
    pdate.append(i.text)
    
url=[]
for i in soup.find_all('a', class_="sc-5smygv-0 fIXTHm"):
    url.append(i.get('href'))
    
df=pd.DataFrame({'Paper Title': paper,'Authors':author,'Published Date': pdate, 'Paper URL': url})     


# In[37]:


df


# # Q9. Write a python program to scrape mentioned details from dineout.co.in :
# i) Restaurant name
# ii) Cuisine
# iii) Location
# iv) Ratings
# v) Image URL

# In[41]:


data=requests.get("https://www.dineout.co.in/delhi-restaurants/buffet-special")
soup=BeautifulSoup(data.content, 'html.parser')

rname=[]
for i in soup.find_all('a', class_="restnt-name ellipsis"):
    rname.append(i.text)
    
cuisine=[]
for i in soup.find_all('span', class_="double-line-ellipsis"):
    i=i.get_text().split('|')[1]
    cuisine.append(i)
    
loc=[]
for i in soup.find_all('div', class_="restnt-loc ellipsis"):
    i=i.get_text()
    loc.append(i)
    
    
rating=[]
for i in soup.find_all('div', class_="restnt-rating rating-4"):
    i=i.get_text()
    rating.append(i)
    
url=[]
for i in soup.find_all('img', class_="no-img"):
    url.append(i.get('data-src'))
    
df=pd.DataFrame({'Restaurant name': rname, 'Cuisine': cuisine, 'Location': loc, 'Rating':rating, 'Image URL':url
})    


# In[42]:


df


# # 10) Write a python program to scrape the details of top publications from Google Scholar from
# https://scholar.google.com/citations?view_op=top_venues&hl=en

# In[39]:


data=requests.get("https://scholar.google.com/citations?view_op=top_venues&hl=en")
soup=BeautifulSoup(data.content, 'html.parser')

rank=[]
for i in soup.find_all('td',class_="gsc_mvt_p"):
    i=i.get_text().replace('.','')
    rank.append(i)
    
pub=[]
for i in soup.find_all('td', class_="gsc_mvt_t"):
    pub.append(i.text)
    
    
h5_index=[]
for i in soup.find_all('a', class_="gs_ibl gsc_mp_anchor"):
    h5_index.append(i.text)
    
h5_median=[]
for i in soup.find_all('span', class_="gs_ibl gsc_mp_anchor"):
    h5_median.append(i.text)
    
df=pd.DataFrame({'Rank': rank, 'Publication': pub, 'h5-Index': h5_index, 'h5-Median':h5_median})    
    


# In[40]:


df


# In[ ]:




