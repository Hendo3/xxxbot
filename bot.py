'''
Developer: Hendo
          leorsousa

'''



import os
import telebot
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def open_url(link):
    
    path = ChromeDriverManager().install()
    opt = webdriver.ChromeOptions()
    opt.add_argument("--headless")
    nav = webdriver.Chrome(executable_path=path, options=opt)
    nav.get(link)

    email, password = "shadowknight9921@hotmail.com", "fewinf9034@dw098$D"
    

    first_step = nav.find_element_by_css_selector('.btn')
    time.sleep(2)
    first_step.click()

    time.sleep(3)

    try:
        click_here = nav.find_element_by_css_selector('#video-premium-alert')
        time.sleep(2)
        click_here.click()
    
    except:
        print('Dont have')

    time.sleep(2)

    try:
        try:
            click_again = nav.find_element_by_css_selector('#tab-2signin')
            time.sleep(2)
            click_again.click()

        except Exception as e:
            print(f"erro: {e}")
            click_again = nav.find_element_by_css_selector('.btn.btn-login.menu-login-acct')
            time.sleep(2)
            click_again.click()

    except:
        click_again = nav.find_element_by_css_selector('#main-signin-btn')
        time.sleep(2)
        click_again.click()

    time.sleep(2)

    mail_form = nav.find_element_by_css_selector("#signin-form_login")
    time.sleep(2)
    mail_form.send_keys(email)

    password_form = nav.find_element_by_css_selector("#signin-form_password")
    time.sleep(1)
    password_form.send_keys(password)

    time.sleep(1)
    WebDriverWait(nav, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.login-submit"))).click()
    time.sleep(2)
    soup = BeautifulSoup(nav.page_source, element_classes=[])

    nav.get(link)
    time.sleep(4)
    soup = soup.prettify().split('\n')
    
    ls = []
    for i in soup:
        if "html5player.setVideoUrl" in i:
            ls.append(i)
    ls = [ls[i].split('"') for i in range(len(ls))]
    print(ls)
    ls = str(ls[-1])
    ls = ls.replace("\\t", "")
    ls = ls.replace("[", "")
    ls = ls.replace("]", "")
    ls = ls.replace("'", "")
    ls = ls.replace(" ", "")
    ls = ls.replace("html5player.setVideoUrlHigh", "")
    ls = ls.replace("(", "")
    ls = ls.replace(")", "")
    ls = ls.replace(";", "")
    return ls



bot = telebot.TeleBot("5526075354:AAFL56BsHP2qy4FxfCbITXgPqO-yYy-oCzY")

@bot.message_handler(commands=['start'])
def send_welcome(message):
   bot.reply_to(message, "Digite o link do video que deseja acessar")

@bot.message_handler(content_types=['text'])
def generic_url(message):
    hour = time.time()-3600
    link = message.text

    bot.send_message(message.chat.id, "Gerando o link...")
    bot.send_message(message.chat.id, "Por favor aguarde um segundo...")
    link_2 = str(open_url(link)).replace('"', "")
    print(link_2)
    url_1 = link_2[len(link_2)//2:]
    url_2 = link_2[:len(link_2)//2]
    if url_2 + url_1 == link_2:

        site_url = "assistirxvideosepornhubgratis.xyz/?url=" + link_2
        generic_url = f"shrtfly.com/st?api=e10e67900386537c825ed6e4a5f1eba75d56bb79&url={site_url}"
        print(generic_url)
        bot.send_message(message.chat.id, generic_url)
        bot.send_message(message.chat.id, "Por favor copie o link e cole no navegador para poder acessar o conte??do/nDigite /start para pedir outro v??deo") 
        return link_2
    else:
        bot.send_message(message.chat.id, "Link inv??lido")
        return False

bot.polling()
