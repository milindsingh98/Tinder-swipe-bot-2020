from selenium import webdriver
from time import sleep
from secrets import username, password


#open the tinder web window
chrome_browser = webdriver.Chrome(executable_path='E:\\Selenium\\chromedriver.exe')  # the executtable path should be set to location where chromedriver.exe is installed
chrome_browser.get('https://www.tinder.com')
chrome_browser.maximize_window()
sleep(15)

#click on the more_option_button 
more_optn = chrome_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/span/button') #more option button
more_optn.click()
sleep(3)

#click on the facebook button
fb_btn = chrome_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/span/div[2]/button')
fb_btn.click()
sleep(2)

 # switch to login popup
base_window = chrome_browser.window_handles[0]
chrome_browser.switch_to_window(chrome_browser.window_handles[1])


email = chrome_browser.find_element_by_id('email')
email.send_keys(username)  #sending the email_id to the web page
passw = chrome_browser.find_element_by_id('pass')
passw.send_keys(password)  # sending password to the web page
login = chrome_browser.find_element_by_id('loginbutton')
login.click()
sleep(2)

#navigate back to the main window
chrome_browser.switch_to_window(base_window)

sleep(10)

allow_btn = chrome_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]/span')
allow_btn.click()
sleep(5)

not_intrstd = chrome_browser.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
not_intrstd.click()
sleep(3)

def like():
        like_btn = chrome_browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()

def dislike():
    dislike_btn = chrome_browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
    dislike_btn.click()

def auto_swipe():
    num_of_swipes = 0
    while num_of_swipes !=5:
        sleep(0.5)
        try:
            like()
            num_of_swipes+=1
        except Exception:
            try:
                close_popup()
            except Exception:
                close_match()
    return num_of_swipes

def close_popup():
    popup_3 = chrome_browser.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
    popup_3.click()

def close_match():
    match_popup = chrome_browser.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
    match_popup.click()

print(auto_swipe())   # It starts the auto swiping and at the end prints the total profiles swiped right
chrome_browser.close()  # to close the browser window after executing
