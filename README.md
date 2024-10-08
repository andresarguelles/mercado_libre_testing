# Mercado Libre Testing

Script de prueba para busqueda automatizada de consolas "PlayStation 5" en articulos de Mercado Libre utilizando Selenium.

## Requisitos

1. **Python**: Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/).

2. **Selenium**: Instala el paquete de Selenium utilizando pip:
    ```sh
    pip install selenium
    ```
3. **WebDriver module**: Instala el paquete chromedriver utilizando pip:
    ```sh
    pip install chromedriver_binary
    ```

4. **Forcing WebDriver update and compatibility**: Aveces el driver no será compatible con la version de navegador que tengas, por lo que es buena opcion que instales el siguiente paquete, que basicamente se asegura de que tengas la version de chromedriver compatible con tu navegador chromium de forma automatica:
    ```sh
    pip install chromedriver-binary-auto
    pip install --upgrade --force-reinstall chromedriver-binary-auto
    ```

5. **NOTA:**: Necesitas un WebDriver compatible con la versión de tu navegador. Por ejemplo, si usas Chrome, descarga `chromedriver`. Asegúrate de que el `chromedriver` esté en tu PATH o especifica su ubicación en el script.

## Ejecución

1. Clona este repositorio o descarga los archivos.

2. Navega al directorio del proyecto:
    ```sh
    cd ruta/al/directorio
    ```

3. Ejecuta el script:
    ```sh
    python mercado_libre_testing.py
    ```

## Notas

- Asegúrate de que el WebDriver que descargues sea compatible con tu versión y tipo de navegador.
- De ser necesario modifica el script para adaptarlo a tus necesidades específicas de prueba.