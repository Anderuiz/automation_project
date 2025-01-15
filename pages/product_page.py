from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import logging
from config import TEST_USER  # Importamos datos del archivo de configuración

logger = logging.getLogger(__name__)

class ProductPage(BasePage):
    # Método para seleccionar la categoría 'Cameras'
    def select_category(self, category_name="Cameras"):
        try:
            logger.info(f"Seleccionando la categoría: {category_name}")
            # Hacer clic en la categoría "Cameras"
            self.click(By.LINK_TEXT, category_name)
        except Exception as e:
            logger.error(f"Error al seleccionar la categoría: {e}")
            raise Exception(f"Error al seleccionar la categoría: {str(e)}")
    
    # Método para seleccionar un producto por su nombre
    def select_product(self, product_name=None):
        product_name = product_name or TEST_USER["product"]  # Usa el producto del config.py si no se proporciona uno
        try:
            logger.info(f"Seleccionando producto: {product_name}")
            self.click(By.LINK_TEXT, product_name)
        except Exception as e:
            logger.error(f"Error al seleccionar el producto: {e}")
            raise Exception(f"Error al seleccionar el producto: {str(e)}")

    # Método para seleccionar un color del producto
    def select_color(self, color=None):
        color = color or TEST_USER["color"]  # Usa el color del config.py si no se proporciona uno
        try:
            logger.info(f"Seleccionando color: {color}")
            # Esperamos que el menú de opciones de color esté visible
            self.wait_for_element(By.ID, "input-option226")
            
            # Hacemos clic en el menú de selección de color
            self.click(By.ID, "input-option226")
            
            # Seleccionamos el color usando el valor adecuado (por ejemplo, '15' para el color 'Red')
            # Esto selecciona el color en base al valor del input correspondiente
            self.click(By.CSS_SELECTOR, f"option[value='{color}']")
            
        except Exception as e:
            logger.error(f"Error al seleccionar el color: {e}")
            raise Exception(f"Error al seleccionar el color: {str(e)}")

    # Método para agregar el producto al carrito
    def add_to_cart(self):
        try:
            logger.info("Agregando producto al carrito.")
            # Esperamos que el botón de agregar al carrito esté visible
            self.wait_for_element(By.ID, "button-cart")
            self.click(By.ID, "button-cart")
        except Exception as e:
            logger.error(f"Error al agregar el producto al carrito: {e}")
            raise Exception(f"Error al agregar el producto al carrito: {str(e)}")
