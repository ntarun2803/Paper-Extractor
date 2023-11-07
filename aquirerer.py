from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request


PATH = "C:\\Users\\ntaru\\OneDrive\\Desktop\\chromedriver.exe"

#set download location for the driver
options = webdriver.ChromeOptions() 
options.add_experimental_option('prefs', {
"download.default_directory": "D:\\docs\\LGSVL"
})

driver = webdriver.Chrome(options=options)


fil  = open("D:\\docs\\LGSVL\\New Text Document.txt",encoding='utf8')

count = 0

# run a for loop for each link, checking if the download for the paper is available and if so, download paper
for i in fil:
    try: 
        tabname = "tab" + str(count+2)
        driver.execute_script("window.open('about:blank', '{}');".format(tabname))
        driver.switch_to.window('{}'.format(tabname))
        driver.get("https://sci-hub.se/")
        hello = driver.find_element(By.NAME,"request")
        hello.send_keys(i)
        time.sleep(5)
        

        if(driver.find_element(By.XPATH,'//*[@id="buttons"]/button')):
            but = driver.find_element(By.XPATH,'//*[@id="buttons"]/button')
            but.click()
            
        time.sleep(5)
        
        
    except:
        print("file not found in sci hub " + i)
        
    count+=1


print("program ended with {} iterations".format(count))

time.sleep(30)
driver.quit()