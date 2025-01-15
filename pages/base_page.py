from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging

logger = logging.getLogger(__name__)

class BasePage:
    def __init__(self, driver):
        # Inicializa el driver de Selenium
        self.driver = driver

    def open(self, url):
        # Abre una URL en el navegador
        try:
            self.driver.get(url)
            logger.info(f"Abriendo URL: {url}")
        except Exception as e:
            logger.error(f"Error al abrir la URL {url}: {e}")
            raise Exception(f"Error al abrir la URL {url}: {str(e)}") 

    def find_element(self, by, value):
        # Encuentra un elemento en la pagina utilizando un localizador (by, value)
        try:
            element = self.driver.find_element(by, value)
            logger.info(f"Elemento encontrado: ({by}, {value})")
            return element
        except Exception as e:
            logger.error(f"Error al encontrar el elemento ({by}, {value}): {e}")
            raise Exception(f"Error al encontrar el elemento ({by}, {value}): {str(e)}")  

    def click(self, by, value):
        # Busca el elemento y hace clic sobre el
        try:
            element = self.find_element(by, value)
            element.click()
            logger.info(f"Haciendo clic en el elemento: ({by}, {value})")
        except Exception as e:
            logger.error(f"Error al hacer clic en el elemento ({by}, {value}): {e}")
            raise Exception(f"Error al hacer clic en el elemento ({by}, {value}): {str(e)}")  

    def send_keys(self, by, value, text):
        # Escribe un texto en un campo de entrada
        try:
            element = self.find_element(by, value)
            element.send_keys(text)
            logger.info(f"Ingresando texto '{text}' en el campo: ({by}, {value})")
        except Exception as e:
            logger.error(f"Error al escribir en el campo ({by}, {value}): {e}")
            raise Exception(f"Error al escribir en el campo ({by}, {value}): {str(e)}")  

    def wait_for_element(self, by, value, timeout=10):
        # Espera hasta que un elemento este presente en la pagina
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.presence_of_element_located((by, value)))
        except TimeoutException as e:
            logger.error(f"Timeout esperando el elemento ({by}, {value}): {e}")
            raise Exception(f"Timeout esperando el elemento ({by}, {value}): {str(e)}")  

    def wait_for_visibility(self, by, value, timeout=10):
        # Espera hasta que el elemento sea visible
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.visibility_of_element_located((by, value)))
        except TimeoutException as e:
            logger.error(f"Timeout esperando visibilidad para el elemento ({by}, {value}): {e}")
            raise Exception(f"Timeout esperando visibilidad para el elemento ({by}, {value}): {str(e)}") 

    def wait_for_clickable(self, by, value, timeout=10):
        # Espera hasta que el elemento sea clickeable
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.element_to_be_clickable((by, value)))
        except TimeoutException as e:
            logger.error(f"Timeout esperando el elemento clickeable ({by}, {value}): {e}")
            raise Exception(f"Timeout esperando el elemento clickeable ({by}, {value}): {str(e)}")
