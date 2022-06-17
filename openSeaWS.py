
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time 


def openSeaWS():
    firefox_options = Options()
    firefox_options.add_argument("--headless")
    driver = webdriver.Firefox(executable_path=r'./geckodriver',options=firefox_options)

    url = 'https://opensea.io/rankings'

    driver.maximize_window()

    response = driver.get(url)
    i= 1
    nftNames = []
    while(True):
        try:

            screen_height = driver.execute_script("return window.screen.height;")

            i+=1 
            htmlTest = driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div[2]/div/div[3]').get_attribute('outerHTML')
            print(f"the html is {len(htmlTest)}")
            if len(htmlTest)>124:


                button = driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div[3]/button[2]')
                textNft = driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div[2]/div/div[3]')

                nftNames.append(textNft.text)
                scroll_height= driver.execute_script("return document.body.scrollHeight;")
                time.sleep(5)
                print(f"the value of i is: {i}")
                print(f"the screen height is: {screen_height}")
                print(f"the scroll height is:{scroll_height}")
                driver.execute_script("window.scrollTo(0,{screen_height}*{i});".format(screen_height=screen_height,i=i))
                print(f"the screen height * i = {screen_height*i}")
                if (screen_height)* i > scroll_height:
                    print("if is being trigger")
                    i = 1
                    button.click()
                    time.sleep(10)
            else:
                print("the inner html is lower that 124")
                break
        except:
            print("braking")
            break


    driver.quit()

    with open('nftCollections.txt','w') as f:
        for nfts in nftNames:
            f.write("%s\n" % nfts)
        print("Done writing the file")

if __name__ =='__main__':
     openSeaWS()   