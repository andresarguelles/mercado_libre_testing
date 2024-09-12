from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

brave_path = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'

# # Configuramos el navegador para Brave
options = webdriver.ChromeOptions()
options.binary_location = brave_path

# Inicializamos el driver con opciones personalizadas
driver = webdriver.Chrome(options=options)

try:
    # Abrimos el sitio de Mercado Libre
    driver.get("https://www.mercadolibre.com")

    # Asignamos el boton de Mexico
    mexico_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[id='MX']"))
    )
    mexico_button.click()

    # Buscamos el producto
    search_box = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
    search_box.send_keys("PlayStation 5")
    search_box.send_keys(Keys.RETURN)

    # Cerramos el banner de cookies si es que aparece
    try:
        cookie_banner = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.cookie-consent-banner-opt-out__container button"))
        )
        cookie_banner.click()
    except:
        pass  

    # Seleccionamos el filtro de "Nuevo"
    nuevo_filter = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.ui-search-link[title*='Nuevo']"))
    )
    nuevo_filter.click()

    # Seleccionamos la ciudad "Distrito Federal"
    ciudad_filter = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.ui-search-link[title*='Distrito Federal']"))
    )
    ciudad_filter.click()

    # Seleccionamos el filtro de orden
    filtro_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".andes-dropdown__trigger"))
    )
    filtro_button.click()

    # Seleccionamos la opcion de precio de mayor a menor dentro del filtro de orden
    de_mayor_a_menor_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "li.andes-list__item[data-key='price_desc']"))
    )
    de_mayor_a_menor_button.click()

    #Obtenemos el titulo y precio con el tipo de moneda de los primeros 5 articulos
    for i in range(5):
        product = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f".ui-search-layout__item:nth-child({i+1})"))
        )
        title = product.find_element(By.CSS_SELECTOR, "h2.ui-search-item__title").text
        currency_simbol = product.find_element(By.CSS_SELECTOR, "span.andes-money-amount__currency-symbol").text
        price = product.find_element(By.CSS_SELECTOR, "span.andes-money-amount__fraction").text
        print(f"Producto {i+1}: {title} - Precio: {currency_simbol + price}")

finally:
    driver.quit()
