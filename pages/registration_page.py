from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from config import TEST_USER  # Importando los datos de configuración
import logging

logger = logging.getLogger(__name__)

class RegistrationPage(BasePage):
    # Método para ingresar el primer nombre
    def enter_first_name(self, first_name=TEST_USER["first_name"]):
        self._enter_field(By.ID, "input-firstname", first_name, "primer nombre")

    # Método para ingresar el apellido
    def enter_last_name(self, last_name=TEST_USER["last_name"]):
        self._enter_field(By.ID, "input-lastname", last_name, "apellido")

    # Método para ingresar el correo electrónico
    def enter_email(self, email=TEST_USER["email"]):
        self._enter_field(By.ID, "input-email", email, "correo electrónico")

    # Método para ingresar el teléfono
    def enter_telephone(self, telephone=TEST_USER["telephone"]):
        self._enter_field(By.ID, "input-telephone", telephone, "teléfono")

    # Método para ingresar la contraseña
    def enter_password(self, password=TEST_USER["password"]):
        self._enter_field(By.ID, "input-password", password, "contraseña")

    # Método para confirmar la contraseña
    def enter_password_confirm(self, confirm_password=TEST_USER["password"]):
        self._enter_field(By.ID, "input-confirm", confirm_password, "confirmación de contraseña")

    # Método para aceptar el acuerdo de los términos
    def accept_agreement(self):
        try:
            logger.info("Aceptando acuerdo de términos")
            self.wait_for_visibility(By.NAME, "agree")
            self.click(By.NAME, "agree")
        except Exception as e:
            logger.error(f"Error al aceptar el acuerdo de términos: {e}")
            raise

    # Método para enviar el formulario de registro
    def submit(self):
        try:
            logger.info("Enviando formulario de registro")
            self.click(By.CSS_SELECTOR, ".btn-primary")
        except Exception as e:
            logger.error(f"Error al enviar el formulario de registro: {e}")
            raise

    # Método genérico para ingresar datos en los campos
    def _enter_field(self, by, locator, text, field_name):
        try:
            logger.info(f"Ingresando {field_name}: {text}")
            self.wait_for_visibility(by, locator)
            self.send_keys(by, locator, text)
        except Exception as e:
            logger.error(f"Error al ingresar {field_name}: {e}")
            raise
