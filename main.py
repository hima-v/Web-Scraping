from bs4 import BeautifulSoup
import time
import requests
print("Which skill are you unfamiliar with?")
unfamiliar_skill=input('>>')
print("Filtering the mentioned skills")
companies=[]
html_text= requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text #requests info from specific website url.
soup=BeautifulSoup(html_text,'lxml')
# company_name=soup.find_all('h3',class_='joblist-comp-name')
# for cname in company_name:
#     companies.append(cname.text)
# print(companies)
def jobsfinding():
    jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date=job.find('span',class_='sim-posted').span.text
        if 'few' not in published_date:
            comp_name=job.find('h3',class_='joblist-comp-name').text.replace(' ','')
            skills=job.find('span',class_='srp-skills').text.replace(' ','')
            more_info=job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt','w') as f:
                    f.write(f"Company Name:  {comp_name.replace('(MoreJobs)','').strip()} \n")
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f"Links: {more_info} \n")
                print(f'File saved:{index} ') 
if __name__ == '__main__' :
    while True:
        jobsfinding()
        print()
        time_wait=1
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait*10)

##rewrite, write