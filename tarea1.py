from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def BuscarElement(Nombre_Elemento,mensaje):
    element=driver.find_element_by_name(Nombre_Elemento)
    element.click()
    element.send_keys(mensaje)
def SeleccionarElement(Nombre,mens):
    select=Select(driver.find_element_by_id(Nombre))
    select.select_by_visible_text(mens)

codigo_postal=8320000
Nombre='Francisco'
Apellido1='rodriguez'
Apellido2="cerda"
contraseña='patricio_Alka'
correo='drabernine16@gmail.com'
Fecha="23/06/1997"
new_contraseña="1234567890qwertyuiopñlkjhgfdsazxcvbnm,.1234567890poiuyhjklñmnasdfgzxcvbnmqweasdfghoqasdfghjiopkalmskjuioazhbvf12345qwerttienajshfg13489aklñ"#139
opcion=int(input("¿Que pagina desea auditar?\n  1. smartmobile\n  2. totamona\n "))
if opcion== 1:
    opcion2=int(input("¿Que deseas realizar?\n 1.Crear cuenta\n 2.iniciar sesion\n 3.restablecer contraseña\n 4.modificar contraseña\n"))
    if opcion2==1:
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        time.sleep(1)
        driver.get("https://smartmobile.cl/")
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div/div[1]/div[1]/div/ul[2]/li[4]/a'))).click()
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div/div[2]/div/div/div/main/article/div/div/div/div[2]/div[2]/form/p[3]/input'))).send_keys(contraseña)
        BuscarElement('email',correo)
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div/div[2]/div/div/div/main/article/div/div/div/div[2]/div[2]/form/p[4]/button'))).click()
    
    elif opcion2==2:
        iteracion=int(input("¿cuantas veces desea loguear?\n"))
        i=0
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        while i<iteracion:
            time.sleep(1)
            driver.get("https://smartmobile.cl/")
            WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div/div[1]/div[1]/div/ul[2]/li[4]/a'))).click()
            BuscarElement('username',correo)
            BuscarElement('password',contraseña)
            WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div/div[2]/div/div/div/main/article/div/div/div/div[2]/div[1]/form/p[4]/button'))).click()
            if i+1<iteracion:
                WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div/div[2]/div/div/div/main/article/div/div/div/p[1]/a'))).click()
            i=i+1
    
    elif opcion2==3:
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        time.sleep(1)
        driver.get("https://smartmobile.cl/")
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div/div[1]/div[1]/div/ul[2]/li[4]/a'))).click()
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div/div[2]/div/div/div/main/article/div/div/div/div[2]/div[1]/form/p[5]/a'))).click()
        BuscarElement('user_login',correo)
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div/div[2]/div/div/div/main/article/div/div/form/p[3]/button'))).click()
    
    elif opcion2==4:
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        time.sleep(1)
        driver.get("https://smartmobile.cl/")
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div/div[1]/div[1]/div/ul[2]/li[4]/a'))).click()
        BuscarElement('username',correo)
        BuscarElement('password',contraseña)
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div/div[2]/div/div/div/main/article/div/div/div/div[2]/div[1]/form/p[4]/button'))).click()
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div/div[2]/div/div/div/main/article/div/div/nav/ul/li[5]/a'))).click()
        driver.find_element_by_id('password_current').send_keys(contraseña)
        driver.find_element_by_id('password_1').send_keys(new_contraseña)
        driver.find_element_by_id('password_2').send_keys(new_contraseña)
        driver.find_element_by_id('account_first_name').send_keys(Nombre)
        driver.find_element_by_id('account_last_name').send_keys(Apellido1)
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div/div[2]/div/div/div/main/article/div/div/div/form/p[5]/button'))).click()

elif opcion==2:
    opcion2=int(input("¿Que deseas realizar?\n 1.Crear cuenta\n 2.iniciar sesion\n 3.restablecer contraseña\n 4.modificar contraseña\n"))
    if opcion2==1:
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        time.sleep(1)
        driver.get("https://totamona.com/es/")
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/main/div[7]/div[1]/div[4]/div[2]/div/a'))).click()
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/main/section/div/section/section/section/section/div/div[2]/a'))).click()
        BuscarElement("firstname",Nombre)
        BuscarElement("lastname",Apellido1)
        BuscarElement("email",correo)
        BuscarElement("birthday",Fecha)
        BuscarElement("password",contraseña)
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/main/section/div/section/section/section/div/div[1]/div/div/form/footer/div[2]/div/label/span[1]'))).click()
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/main/section/div/section/section/section/div/div[1]/div/div/form/footer/button'))).click()
    
    elif opcion2==2:
        iteracion=int(input("¿cuantas veces desea loguear?\n"))
        i=0
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        while i<iteracion:
            time.sleep(1)
            driver.get("https://totamona.com/es/")
            WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/main/div[7]/div[1]/div[4]/div[2]/div/a'))).click()
            BuscarElement('email',correo)
            BuscarElement('password',contraseña)
            WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/main/section/div/section/section/section/section/form/footer/div[1]/div/button'))).click()
            if i+1<iteracion:
                WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/main/section/div/section/section/p[3]/a'))).click()
            i=i+1
    
    elif opcion2==3:
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        time.sleep(1)
        driver.get("https://totamona.com/es/")
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/main/div[7]/div[1]/div[4]/div[2]/div/a'))).click()
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/main/section/div/section/section/section/section/form/section/div[2]/div/a'))).click()
        BuscarElement("email",correo)
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/main/section/div/section/section/section/div/form/section/div/div[2]/button'))).click()

    elif opcion2==4:
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        time.sleep(1)
        driver.get("https://totamona.com/es/")
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/main/div[7]/div[1]/div[4]/div[2]/div/a'))).click()
        BuscarElement('email',correo)
        BuscarElement('password',contraseña)
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/main/section/div/section/section/section/section/form/footer/div[1]/div/button'))).click()
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/main/div[7]/div[1]/div[4]/div[2]/div/a'))).click()
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/main/section/div/section/section/div/div/div/a[4]'))).click()
        BuscarElement("password",contraseña)
        BuscarElement("new_password",new_contraseña)
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/main/section/div/section/section/div/div/form/div[1]/div[1]/div/label/span[1]'))).click()
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/main/section/div/section/section/div/div/form/div[1]/div[3]/div/label/span[1]'))).click()
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/main/section/div/section/section/div/div/form/footer/button'))).click()