from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurar el controlador de Selenium
driver = webdriver.Chrome() 

# Abre la página web
driver.get('https://utest.com/')

# Esperar a que el botón "Join Today" esté disponible antes de continuar
button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'a.unauthenticated-nav-bar__sign-up'))
)

# Hacer clic en el botón "Join Today"
button.click()

# Completar el formulario de registro
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input#firstName'))
)
driver.find_element(By.CSS_SELECTOR, 'input#firstName').send_keys('John')

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input#lastName'))
)
driver.find_element(By.CSS_SELECTOR, 'input#lastName').send_keys('Doe')

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input#email'))
)
driver.find_element(By.CSS_SELECTOR, 'input#email').send_keys('john.doe@example.com')

# Seleccionar la fecha de nacimiento (puedes ajustar los valores según tus necesidades)
driver.find_element(By.CSS_SELECTOR, 'select#birthMonth').send_keys('January')
driver.find_element(By.CSS_SELECTOR, 'select#birthDay').send_keys('1')
driver.find_element(By.CSS_SELECTOR, 'select#birthYear').send_keys('1990')

# Esperar 10 segundos antes de hacer clic en el botón "Next: Location"
time.sleep(10)

# Hacer clic en el botón "Next: Location"
next_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'a.btn.btn-blue[ng-click="validateBasicInfoStep(userForm);"]'))
)
next_button.click()

# Esperar 10 segundos antes de hacer clic en el botón "Next: Location"
time.sleep(10)

# Hacer clic en el botón "Next: Devices"
next_devices_button = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'a.btn.btn-blue[ng-click="validateAddressInfoStep(forms.userForm);"]'))
)
next_devices_button.click()

# Esperar a que la página "Next: Last Step" se cargue
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//span[text()="Next: Last Step"]'))
)

# Hacer clic en el botón "Next: Last Step"
next_last_step_button = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'a.btn.btn-blue[ng-click="validateDevices(userForm);"]'))
)
next_last_step_button.click()

# Llenar el formulario de la última etapa
password_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input#password'))
)
password_input.send_keys('your_password')

confirm_password_input = driver.find_element(By.CSS_SELECTOR, 'input#confirmPassword')
confirm_password_input.send_keys('your_password')

# Registra los checkboxes
newsletter_checkbox = driver.find_element(By.CSS_SELECTOR, 'input[name="newsletterOptIn"]')
newsletter_checkbox.click()

terms_of_use_checkbox = driver.find_element(By.CSS_SELECTOR, 'input#termOfUse')
terms_of_use_checkbox.click()

privacy_setting_checkbox = driver.find_element(By.CSS_SELECTOR, 'input#privacySetting')
privacy_setting_checkbox.click()

# Esperar 10 segundos antes de hacer clic en el botón "Next: Location"
time.sleep(10)

# Hacer clic en el botón "Complete Setup"
complete_setup_button = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'a.btn.btn-blue[ng-click="submitForm(userForm);"]'))
)
complete_setup_button.click()

# Cerrar el controlador de Selenium
driver.quit()
