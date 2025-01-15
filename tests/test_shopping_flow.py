import pytest
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from config import TEST_USER  # Importando los datos de usuario de config.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import logging

# Configuración de logging
logger = logging.getLogger(__name__)

# Configuración de pytest para usar fixtures
@pytest.fixture(scope="module")
def driver():
    print("Abriendo el navegador...")
    # Configuración del driver de Selenium con ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()  # Maximizar la ventana del navegador
    yield driver
    print("Cerrando el navegador...")
    driver.quit()

@pytest.fixture(scope="module")
def registration_page(driver):
    print("Inicializando RegistrationPage...")
    return RegistrationPage(driver)

@pytest.fixture(scope="module")
def login_page(driver):
    print("Inicializando LoginPage...")
    return LoginPage(driver)

@pytest.fixture(scope="module")
def product_page(driver):
    print("Inicializando ProductPage...")
    return ProductPage(driver)

@pytest.fixture(scope="module")
def cart_page(driver):
    print("Inicializando CartPage...")
    return CartPage(driver)

# Función para esperar hasta que un elemento sea visible
def wait_for_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((by, value))
    )

# Test de registro
def test_register_user(registration_page: RegistrationPage):
    print("Iniciando prueba de registro...")
    registration_page.open("https://opencart.abstracta.us/index.php?route=account/register")
    
    # Esperar a que el formulario de registro esté disponible
    wait_for_element(registration_page.driver, By.ID, "input-firstname")
    
    # Usar los datos de config.py en lugar de hardcodearlos
    registration_page.enter_first_name(TEST_USER["first_name"])
    registration_page.enter_last_name(TEST_USER["last_name"])
    registration_page.enter_email(TEST_USER["email"])
    registration_page.enter_telephone(TEST_USER["telephone"])
    registration_page.enter_password(TEST_USER["password"])
    registration_page.enter_password_confirm(TEST_USER["password"])
    registration_page.accept_agreement()
    registration_page.submit()
    
    # Esperar a que la página de éxito esté cargada
    wait_for_element(registration_page.driver, By.XPATH, "//h1[text()='Your Account Has Been Created!']")
    
    # Validación con un mensaje claro
    assert "Your Account Has Been Created!" in registration_page.get_page_source(), "El registro no se completó exitosamente."
    print("Prueba de registro completada con éxito.")

# Test de inicio de sesión
def test_login_user(login_page: LoginPage):
    print("Iniciando prueba de inicio de sesión...")
    login_page.open("https://opencart.abstracta.us/index.php?route=account/login")
    
    # Esperar a que el campo de correo esté disponible
    wait_for_element(login_page.driver, By.ID, "input-email")
    
    # Usar los datos de config.py
    login_page.enter_email(TEST_USER["email"])
    login_page.enter_password(TEST_USER["password"])
    login_page.submit()

    # Esperar a que el texto "My Account" esté visible
    wait_for_element(login_page.driver, By.XPATH, "//h1[text()='My Account']")
    
    # Validación con un mensaje claro
    assert "My Account" in login_page.get_page_source(), "El inicio de sesión no fue exitoso."
    print("Prueba de inicio de sesión completada con éxito.")

# Test de selección de producto y agregar al carrito
def test_add_to_cart(product_page: ProductPage):
    print("Iniciando prueba de agregar al carrito...")
    product_page.open("https://opencart.abstracta.us/index.php?route=product/category&path=20")
    
    # Esperar a que el enlace 'Cameras' esté disponible y hacer clic en él
    wait_for_element(product_page.driver, By.LINK_TEXT, "Cameras")
    product_page.select_category("Cameras")  # Asegurándote de seleccionar la categoría Cameras
    
    # Esperar a que el producto esté visible y hacer clic en él
    wait_for_element(product_page.driver, By.CSS_SELECTOR, ".product-layout:nth-child(1) .hidden-xs")
    product_page.select_product(TEST_USER["product"])
    
    # Seleccionar el color y agregar el producto al carrito
    product_page.select_color(TEST_USER["color"])
    product_page.add_to_cart()

    # Esperar a que el mensaje de éxito esté visible
    wait_for_element(product_page.driver, By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    # Validación con un mensaje claro
    assert "Success: You have added" in product_page.get_page_source(), "El producto no se agregó al carrito correctamente."
    print("Prueba de agregar al carrito completada con éxito.")

# Test de checkout, pago y cierre de sesión
def test_checkout(cart_page: CartPage):
    print("Iniciando prueba de checkout...")
    cart_page.open_cart()

    try:
        # Cambiar el contexto al iframe donde se encuentra el botón de checkout
        iframe = wait_for_element(cart_page.driver, By.XPATH, "//iframe")
        cart_page.driver.switch_to.frame(iframe)

        # Intentar encontrar y hacer clic en el botón de checkout dentro del iframe
        checkout_button = wait_for_element(cart_page.driver, By.XPATH, "/html/body/header/div/div/div[3]/div/ul/li[2]/div/p/a[2]/strong/i")
        checkout_button.click()
        logger.info("Botón de Checkout clickeado exitosamente dentro del iframe.")
    except Exception as e:
        # Si no se encuentra el botón de checkout, redirigir directamente a la página de checkout
        logger.error(f"No se pudo hacer clic en el botón de Checkout: {e}. Redirigiendo a la página de checkout.")
        cart_page.driver.get("https://opencart.abstracta.us/index.php?route=checkout/checkout")
        logger.info("Redirigido a la página de checkout.")

    # Cambiar el contexto nuevamente al contenido principal (fuera del iframe)
    cart_page.driver.switch_to.default_content()

    # Llenar la dirección de pago
    wait_for_element(cart_page.driver, By.ID, "input-payment-firstname")
    cart_page.fill_payment_address()

    # Elegir método de envío
    cart_page.choose_shipping_method()

    # Aceptar términos y condiciones
    cart_page.accept_terms()

    # Seleccionar método de pago
    cart_page.select_payment_method()

    # Confirmar la orden
    wait_for_element(cart_page.driver, By.ID, "button-confirm")
    cart_page.confirm_order()

    # Esperar a que el mensaje de confirmación del pedido esté visible
    wait_for_element(cart_page.driver, By.XPATH, "//h1[text()='Your order has been placed!']")

    # Validación con un mensaje claro
    assert "Your order has been placed!" in cart_page.get_page_source(), "El pedido no fue confirmado correctamente."

    # Ir a 'My Account' y luego cerrar sesión
    wait_for_element(cart_page.driver, By.LINK_TEXT, "My Account")
    cart_page.logout()

    # Verificar que se haya cerrado sesión correctamente
    wait_for_element(cart_page.driver, By.XPATH, "//h1[text()='Account Logout']")
    
    assert "Account Logout" in cart_page.get_page_source(), "No se cerró sesión correctamente."
    print("Prueba de checkout completada con éxito.")
