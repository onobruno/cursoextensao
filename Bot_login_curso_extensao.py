'''
Created on 11 Jun 2019

@author: brunoandradeono
'''

#import pip
#pip.main(['install','datefinder'])

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

## string of destination path inside computer
location = ''

def teste_login():
    
    ###read file
    df = pd.read_excel(location)
    
    ###string for destination of chromedriver
    
    location2 = ''
    driver = webdriver.Chrome(location2) 
    
    #listas de logins e senhas
    
    logins = list()
    senhas = list()
    nomes = list()
    cursos = list()
    
    #listas de logins com problema
    erro_login = []
    erro_senha = []
    erro_nome = []
    erro_curso = []
    
    counter = 0
    
    try:
        for posicao in range(127,len(logins)):
            
            counter += 1
            print ('Counter: ',counter, ' - linha :', posicao)
            #Login e senha -> string
            login = str(logins[posicao])
            senha = str(senhas[posicao])
            nome = str(nomes[posicao])
            curso = str(cursos[posicao])
              
            #acessar o site:
            driver.get(site1)
              
            #primeiro clique no botao "acessar" da pag principal
            driver.find_element_by_css_selector("a[class='btn btn-custom btn-sm'][data-target='#ModalCenter']").click()
              
            #wait a period for elements appear at browser
            time.sleep(0.7)
      
            #Fill login and password and click
            driver.find_element_by_css_selector("input[name='username'][class='form-control blog-details f-15 pt-2']").send_keys(login) #usuário
            driver.find_element_by_css_selector("input[name='password'][class='form-control blog-details f-15 pt-2']").send_keys(senha) #senha
            driver.find_element_by_css_selector("input[type='submit'][class='btn-block btn btn-custom'][value='Acessar']").click()
            
            driver.get(site1)
             
            site = site1
            site_erro = site2
              
            if driver.current_url == site:
                  
                #Desconnect of moodle's account aria-hidden="true"
                driver.find_element_by_css_selector("img[role='presentation'][aria-hidden='true']").click()
                driver.find_element_by_css_selector("span[class='menu-action-text'][id='actionmenuaction-7']").click()
                  
            else: 
                #pass login and password
                erro_login.append(login)
                erro_senha.append(senha)
                erro_nome.append(nome)
                erro_curso.append(curso)
                print ('Erro linha -',posicao)
                  
    except:
        df = pd.DataFrame({'CPF':erro_login,'RA':erro_senha,'Nome':erro_nome,'Curso':erro_curso})
        print(df.head(),df.shape)
        df.to_excel(location + 'resultado_bot_logins ' + str(posicao)+ '.xlsx',index=False)

teste_login()


