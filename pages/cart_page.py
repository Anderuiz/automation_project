from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)  # Hereda las funcionalidades de BasePage

    # Método para abrir el carrito
    def open_cart(self):
        try:
            self.click(By.ID, "cart-total")
            logger.info("Carrito abierto exitosamente.")
        except Exception as e:
            logger.error(f"Error al abrir el carrito: {e}")
            raise Exception(f"Error al abrir el carrito: {str(e)}")  

    # Método para proceder con el checkout
    def checkout(self):
        try:
            # Intentamos localizar el botón de checkout dentro del iframe
            try:
                # Cambiar el contexto al iframe donde se encuentra el botón de checkout
                iframe = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, "//iframe"))
                )
                self.driver.switch_to.frame(iframe)
                logger.info("Cambiado al iframe exitosamente.")

                # Intentamos localizar el botón de checkout
                checkout_button = WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/header/div/div/div[3]/div/ul/li[2]/div/p/a[2]"))
                )
                
                # Desplaza el foco hacia el botón si es necesario
                self.driver.execute_script("arguments[0].scrollIntoView(true);", checkout_button)
                logger.info("Botón de Checkout encontrado, procediendo a hacer clic.")
                checkout_button.click()
                logger.info("Procediendo al checkout exitosamente.")
            
            # Si el botón no se encuentra, redirigimos al link de checkout directamente
            except Exception as e:
                logger.error(f"No se pudo proceder con el botón de Checkout: {e}. Redirigiendo a la página de checkout.")
                self.driver.get("https://opencart.abstracta.us/index.php?route=checkout/checkout")
                logger.info("Redireccionado a la página de checkout.")
            
            # Cambiar el contexto nuevamente al contenido principal (fuera del iframe)
            self.driver.switch_to.default_content()
            logger.info("Regresado al contexto principal.")
            
        except Exception as e:
            logger.error(f"Error al proceder al checkout: {e}")
            raise Exception(f"Error al proceder al checkout: {str(e)}")  

 # Método para llenar la información de la dirección de pago
def fill_payment_address(self):
    try:
        # Manejar posibles alertas antes de interactuar con el botón
        try:
            alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert.accept()  # Cierra la alerta si aparece
        except:
            pass  # Si no hay alerta, continuamos

        # Esperar hasta que el botón de continuar esté presente
        continue_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='button-payment-address']"))
        )
        
        continue_button.click()
        logger.info("Dirección de pago completada.")
    except Exception as e:
        logger.error(f"Error al llenar la dirección de pago: {e}")
        raise Exception(f"Error al llenar la dirección de pago: {str(e)}")


    # Método para elegir el método de envío
    def choose_shipping_method(self):
        try:
            self.click(By.ID, "button-shipping-address")  # Continuar con la dirección de envío
            self.click(By.ID, "button-shipping-method")  # Elegir el método de envío
            logger.info("Método de envío seleccionado.")
        except Exception as e:
            logger.error(f"Error al elegir el método de envío: {e}")
            raise Exception(f"Error al elegir el método de envío: {str(e)}")  

    # Método para aceptar los términos y condiciones
    def accept_terms(self):
        try:
            self.click(By.NAME, "agree")
            logger.info("Términos y condiciones aceptados.")
        except Exception as e:
            logger.error(f"Error al aceptar los términos y condiciones: {e}")
            raise Exception(f"Error al aceptar los términos y condiciones: {str(e)}") 

    # Método para seleccionar el método de pago
    def select_payment_method(self):
        try:
            self.click(By.ID, "button-payment-method")
            logger.info("Método de pago seleccionado.")
        except Exception as e:
            logger.error(f"Error al seleccionar el método de pago: {e}")
            raise Exception(f"Error al seleccionar el método de pago: {str(e)}")  

    # Método para confirmar el pedido
    def confirm_order(self):
        try:
            self.click(By.ID, "button-confirm")
            logger.info("Pedido confirmado.")
        except Exception as e:
            logger.error(f"Error al confirmar el pedido: {e}")
            raise Exception(f"Error al confirmar el pedido: {str(e)}")  

    # Método para cerrar sesión
    def logout(self):
        try:
            self.click(By.LINK_TEXT, "Logout")
            logger.info("Sesión cerrada exitosamente.")
        except Exception as e:
            logger.error(f"Error al cerrar sesión: {e}")
            raise Exception(f"Error al cerrar sesión: {str(e)}")
