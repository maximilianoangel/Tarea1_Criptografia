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
def Clickear(elemento):
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,elemento))).click()

codigo_postal=8320000
Nombre='Jaime'
Apellido1='Coloma'
Apellido2="Parra"
contraseña='mitimiti_Palta'
correo='Probando.1234123@gmail.com'
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
        Clickear('/html/body/div[3]/div/div[1]/div[1]/div/ul[2]/li[4]/a')
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div/div[2]/div/div/div/main/article/div/div/div/div[2]/div[2]/form/p[3]/input'))).send_keys(contraseña)
        BuscarElement('email',correo)
        Clickear('/html/body/div[3]/div/div[2]/div/div/div/main/article/div/div/div/div[2]/div[2]/form/p[4]/button')
    
    elif opcion2==2:
        iteracion=int(input("¿cuantas veces desea loguear?\n"))
        i=0
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        while i<iteracion:
            time.sleep(1)
            driver.get("https://smartmobile.cl/")
            Clickear('/html/body/div[3]/div/div[1]/div[1]/div/ul[2]/li[4]/a')
            BuscarElement('username',correo)
            BuscarElement('password',contraseña)
            Clickear('/html/body/div[3]/div/div[2]/div/div/div/main/article/div/div/div/div[2]/div[1]/form/p[4]/button')
            if i+1<iteracion:
                Clickear('/html/body/div[3]/div/div[2]/div/div/div/main/article/div/div/div/p[1]/a')
            i=i+1
    
    elif opcion2==3:
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        time.sleep(1)
        driver.get("https://smartmobile.cl/")
        Clickear('/html/body/div[3]/div/div[1]/div[1]/div/ul[2]/li[4]/a')
        Clickear('/html/body/div[3]/div/div[2]/div/div/div/main/article/div/div/div/div[2]/div[1]/form/p[5]/a')
        BuscarElement('user_login',correo)
        Clickear('/html/body/div[3]/div/div[2]/div/div/div/main/article/div/div/form/p[3]/button')
    
    elif opcion2==4:
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        time.sleep(1)
        driver.get("https://smartmobile.cl/")
        Clickear('/html/body/div[3]/div/div[1]/div[1]/div/ul[2]/li[4]/a')
        BuscarElement('username',correo)
        BuscarElement('password',contraseña)
        Clickear('/html/body/div[3]/div/div[2]/div/div/div/main/article/div/div/div/div[2]/div[1]/form/p[4]/button')
        Clickear('/html/body/div[3]/div/div[2]/div/div/div/main/article/div/div/nav/ul/li[5]/a')
        driver.find_element_by_id('password_current').send_keys(contraseña)
        driver.find_element_by_id('password_1').send_keys(new_contraseña)
        driver.find_element_by_id('password_2').send_keys(new_contraseña)
        driver.find_element_by_id('account_first_name').send_keys(Nombre)
        driver.find_element_by_id('account_last_name').send_keys(Apellido1)
        Clickear('/html/body/div[3]/div/div[2]/div/div/div/main/article/div/div/div/form/p[5]/button')

elif opcion==2:
    opcion2=int(input("¿Que deseas realizar?\n 1.Crear cuenta\n 2.iniciar sesion\n 3.restablecer contraseña\n 4.modificar contraseña\n"))
    if opcion2==1:
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        time.sleep(1)
        driver.get("https://totamona.com/es/")
        Clickear('/html/body/main/div[7]/div[1]/div[4]/div[2]/div/a')
        Clickear('/html/body/main/section/div/section/section/section/section/div/div[2]/a')
        BuscarElement("firstname",Nombre)
        BuscarElement("lastname",Apellido1)
        BuscarElement("email",correo)
        BuscarElement("birthday",Fecha)
        BuscarElement("password",contraseña)
        Clickear('/html/body/main/section/div/section/section/section/div/div[1]/div/div/form/footer/div[2]/div/label/span[1]')
        Clickear('/html/body/main/section/div/section/section/section/div/div[1]/div/div/form/footer/button')
    
    elif opcion2==2:
        iteracion=int(input("¿cuantas veces desea loguear?\n"))
        i=0
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        while i<iteracion:
            time.sleep(1)
            driver.get("https://totamona.com/es/")
            Clickear('/html/body/main/div[7]/div[1]/div[4]/div[2]/div/a')
            BuscarElement('email',correo)
            BuscarElement('password',contraseña)
            Clickear('/html/body/main/section/div/section/section/section/section/form/footer/div[1]/div/button')
            print(i)
            if i+1<iteracion:
                Clickear('/html/body/main/section/div/section/section/p[3]/a')
            i=i+1
    
    elif opcion2==3:
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        time.sleep(1)
        driver.get("https://totamona.com/es/")
        Clickear('/html/body/main/div[7]/div[1]/div[4]/div[2]/div/a')
        Clickear('/html/body/main/section/div/section/section/section/section/form/section/div[2]/div/a')
        BuscarElement("email",correo)
        Clickear('/html/body/main/section/div/section/section/section/div/form/section/div/div[2]/button')

    elif opcion2==4:
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        time.sleep(1)
        driver.get("https://totamona.com/es/")
        Clickear('/html/body/main/div[7]/div[1]/div[4]/div[2]/div/a')
        BuscarElement('email',correo)
        BuscarElement('password',contraseña)
        Clickear('/html/body/main/section/div/section/section/section/section/form/footer/div[1]/div/button')
        Clickear('/html/body/main/div[7]/div[1]/div[4]/div[2]/div/a')
        Clickear('/html/body/main/section/div/section/section/div/div/div/a[4]')
        BuscarElement("password",contraseña)
        BuscarElement("new_password",new_contraseña)
        Clickear('/html/body/main/section/div/section/section/div/div/form/div[1]/div[1]/div/label/span[1]')
        Clickear('/html/body/main/section/div/section/section/div/div/form/div[1]/div[3]/div/label/span[1]')
        Clickear('/html/body/main/section/div/section/section/div/div/form/footer/button')