import selenium
from selenium import webdriver
import wget
import os
from selenium.webdriver.common.keys import Keys
import time


output_directory = 'photos'
outdir = os.listdir(output_directory)

driver = webdriver.Firefox()
print('what do you want to search?')
print('Example: cars')
criteria = input('Search: ')

driver.get('https://unsplash.com/s/photos/%s' % criteria)
figure = 1
counter =0
html = driver.find_element_by_tag_name('html')

'/html/body/div/div/div[3]/div[3]/div/div[1]/div/div/div[1]/div[2]/figure/div/div[1]/div/a'
'/html/body/div/div/div[3]/div[3]/div/div[1]/div/div/div[2]/div[2]/figure/div/div[1]/div/a'
'/html/body/div/div/div[3]/div[3]/div/div[1]/div/div/div[1]/div[3]/figure/div/div[1]/div/a'

for x in range(1,500):
    try:
        
        try:
            counter = counter + 1
            print(x)
            y = str(counter)
            #title = driver.find_element_by_xpath('/html/body/div/div/div[3]/div[3]/div/div[1]/div/div/div['+y+']/figure['+str(figure)+']/div/div/div[1]/div/a').get_attribute("title")
            title = driver.find_element_by_xpath('/html/body/div/div/div[3]/div[3]/div/div[1]/div/div/div['+y+']/div['+str(figure)+']/figure/div/div[1]/div/a').get_attribute("title")
            title = title.replace(' ','-')
            #link = driver.find_element_by_xpath('/html/body/div/div/div[3]/div[3]/div/div[1]/div/div/div['+y+']/figure['+str(figure)+']/div/div/div[1]/div/a').get_attribute("href")
            link = driver.find_element_by_xpath('/html/body/div/div/div[3]/div[3]/div/div[1]/div/div/div['+y+']/div['+str(figure)+']/figure/div/div[1]/div/a').get_attribute("href")
            href=link+"/download?force=true"
            fileid = href.split('photos/')[1].split('/')[0]
            download = 'yes'
            for z in outdir:
                if fileid in z:
                    download = 'no'
            if download == 'yes':            
                print(href)
                filename = wget.download(href, out=output_directory+'/'+title+'_'+fileid+'.jpg')

        except:
            html.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
            counter = 1
            figure = figure +1
            y = str(counter)
            title = driver.find_element_by_xpath('/html/body/div/div/div[3]/div[3]/div/div[1]/div/div/div['+y+']/div['+str(figure)+']/figure/div/div[1]/div/a').get_attribute("title")
            title = title.replace(' ','-')
            link = driver.find_element_by_xpath('/html/body/div/div/div[3]/div[3]/div/div[1]/div/div/div['+y+']/div['+str(figure)+']/figure/div/div[1]/div/a').get_attribute("href")
            href=link+"/download?force=true"
            fileid = href.split('photos/')[1].split('/')[0]
            download = 'yes'
            for z in outdir:
                if fileid in z:
                    download = 'no'
            if download == 'yes':            
                print(href)
                filename = wget.download(href, out=output_directory+'/'+title+'_'+fileid+'.jpg')
    except:
        print('Error!')
        pass
