from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import logging
from config import BASE_URL, TEST_USER  # Importamos los datos de configuración

logger = logging.getLogger(__name__)

class LoginPage(BasePage):
    # Método para ingresar el correo electrónico
    def enter_email(self, email=None):
        email = email or TEST_USER["email"]  # Usa el correo del config.py si no se proporciona uno
        try:
            logger.info(f"Ingresando correo electrónico: {email}")
            self.send_keys(By.ID, "input-email", email)
        except Exception as e:
            logger.error(f"Error al ingresar el correo electrónico: {e}")
            raise Exception(f"Error al ingresar el correo electrónico: {str(e)}")

    # Método para ingresar la contraseña
    def enter_password(self, password=None):
        password = password or TEST_USER["password"]  # Usa la contraseña del config.py si no se proporciona una
        try:
            logger.info(f"Ingresando contraseña.")
            self.send_keys(By.ID, "input-password", password)
        except Exception as e:
            logger.error(f"Error al ingresar la contraseña: {e}")
            raise Exception(f"Error al ingresar la contraseña: {str(e)}")

    # Método para enviar el formulario de inicio de sesión
    def submit(self):
        try:
            logger.info("Enviando formulario de inicio de sesión.")
            # Usamos el selector proporcionado
            self.click(By.CSS_SELECTOR, "#content > div > div:nth-child(2) > div > form > input")
        except Exception as e:
            logger.error(f"Error al enviar el formulario de inicio de sesión: {e}")
            raise Exception(f"Error al enviar el formulario de inicio de sesión: {str(e)}")

    # Método para verificar si el inicio de sesión fue exitoso
    def is_logged_in(self):
        try:
            # Verifica si un elemento que aparece solo después de iniciar sesión está presente
            self.wait_for_element(By.LINK_TEXT, "My Account")
            logger.info("Inicio de sesión exitoso.")
            return True
        except Exception as e:
            logger.error("Inicio de sesión fallido.")
            return False
