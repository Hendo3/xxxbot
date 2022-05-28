try:
    import telebot
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium import webdriver
    from selenium import webdriver
    import time
    import re
    from bs4 import BeautifulSoup
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time
except ImportError:
    import os
    os.system('pip install -r requirements.txt')
import os

from more_itertools import first
from traitlets import link

def open_url(link):
    path = ChromeDriverManager().install()
    opt = webdriver.ChromeOptions()
    opt.add_argument("--headless")
    nav = webdriver.Chrome(executable_path=path, options=opt)
    nav.get(link)

    email, password = "shadowknight9921@hotmail.com", "11225544def"
    

    first_step = nav.find_element_by_css_selector('.btn')
    time.sleep(1)
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
            time.sleep(1)
            click_again.click()

        except Exception as e:
            print(f"erro: {e}")
            click_again = nav.find_element_by_css_selector('.btn.btn-login.menu-login-acct')
            time.sleep(1)
            click_again.click()

    except:
        click_again = nav.find_element_by_css_selector('#main-signin-btn')
        time.sleep(1)
        click_again.click()

    time.sleep(2)

    mail_form = nav.find_element_by_css_selector("#signin-form_login")
    time.sleep(2)
    mail_form.send_keys(email)

    password_form = nav.find_element_by_css_selector("#signin-form_password")
    time.sleep(.5)
    password_form.send_keys(password)

    time.sleep(.5)
    WebDriverWait(nav, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.login-submit"))).click()
    time.sleep(1)
    soup = BeautifulSoup(nav.page_source, 'html5lib')

    nav.get(link)
    soup = BeautifulSoup(nav.page_source, 'html5lib')

    time.sleep(4)

    texto = soup.text

    html = texto.split("html5player.setVideoUrlHigh('")
    for i in range(len(html)):
        if i > 0:
            html = html[i].split("');")[0]

    link_2 = html[0]

    print(link)

    return link_2


bot = telebot.TeleBot("5301712423:AAFickOb9minMx4j4ty9SEr0KP8j9C8VzF0")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Versão 1.0.0")
    bot.reply_to(message, "Digite o link do video que deseja acessar")
    bot.send_message(message.chat.id, "Devido ao bot estar em beta, pedimos que use o navegador Chrome")

@bot.message_handler(content_types=['text'])
def generic_url(message):
    hour = time.time()-3600
    link = message.text

    bot.send_message(message.chat.id, "Acessando o link...")
    link_2 = open_url(link)
    site_url = "assistirxvideosepornhubgratis.xyz/?url=" + link_2
    generic_url = f"https://shrtfly.com/st?api=752c5cdfec332eb03ca68179a0a0788f71711af1&url={site_url}&alias=CustomAlias&expire={hour}"
    bot.send_message(message.chat.id, generic_url)
    return link_2

bot.polling()
