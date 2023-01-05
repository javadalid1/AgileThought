from selenium.common.exceptions import NoSuchElementException, \
    ElementClickInterceptedException, StaleElementReferenceException, \
    ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.support.select import Select


class ProductsPage:
    """
    POM referente a la página principal de productos.
    """

    nombres_productos_tarjetas_xpath = "//div[@class = 'item-name']"
    precios_productos_tarjetas_xpath = "//span[@class = 'ng-star-inserted']"
    tarjetas_xpath = "//mat-card"
    nombre_producto_dentro_tarjeta_xpath = "//h1"
    precio_producto_tarjeta_xpath = "//p[@class='item-price']"
    mi_cuenta_xpath = "/descendant::*[text() = 'Mi cuenta'][1]"
    tab_vender_xpath = "//a[text()='Vender']"

    def __init__(self, driver):
        self.driver = driver

    def get_num_tarjetas(self):
        """
        Obtiene el número de tarjetas que se despliegan.
        Returns: El número de tarjetas como int. None en caso de que no se
        hayan encontrado.
        """
        for _ in range(5):
            try:
                tarjetas = self.driver.find_elements(By.XPATH,
                                                     self.tarjetas_xpath)
                return len(tarjetas)
            except:
                sleep(1)
        else:
            return None

    def get_nombre_tarjeta(self, num: int):
        """
        Obtiene el nombre desplegado en la tarjeta.
        Args:
            num: El número de tarjeta (div) como entero.
        Returns: El nombre desplegado como String y None en caso de que no
        haya podido extraerse.
        """
        for _ in range(5):
            try:
                nombres = self.driver.find_elements(By.XPATH,
                                                    self.nombres_productos_tarjetas_xpath)
                return nombres[num].text
            except:
                sleep(1)
        else:
            return None

    def get_precio_tarjeta(self, num: int):
        """
        Obtiene el precio desplegado en la tarjeta.
        Args:
            num: El número de tarjeta (div) como entero.
        Returns: El precio desplegado como String y None en caso de que no
        haya podido extraerse.
        """
        for _ in range(5):
            try:
                precios = self.driver.find_elements(By.XPATH,
                                                    self.precios_productos_tarjetas_xpath)
                return precios[num].text
            except:
                sleep(1)
        else:
            return None

    def click_tarjeta(self, num: int):
        """
        Realiza un click en la tarjeta deseada.
        Args:
            num: El número de tarjeta (div) como entero.
        Returns: True si fue posible realizar la acción y False en caso
        contrario.
        """
        for _ in range(5):
            try:
                tarjetas = self.driver.find_elements(By.XPATH,
                                                    self.tarjetas_xpath)
                tarjetas[num].click()
                return True
            except:
                sleep(1)
        else:
            return False

    def get_nombre_tarjeta_abierta(self):
        """
        Obtiene el nombre desplegado en la tarjeta a la que se le hizo click.
        Returns: El nombre desplegado como String y None en caso de que no
        haya podido extraerse.
        """
        for _ in range(5):
            try:
                nombre = self.driver.find_element(By.XPATH,
                                                    self.nombre_producto_dentro_tarjeta_xpath)
                return nombre.text
            except:
                sleep(1)
        else:
            return None

    def get_precio_tarjeta_abierta(self):
        """
        Obtiene el precio desplegado en la tarjeta a la que se le hizo click.
        Returns: El precio desplegado como String y None en caso de que no
        haya podido extraerse.
        """
        for _ in range(5):
            try:
                nombre = self.driver.find_element(By.XPATH,
                                                    self.precio_producto_tarjeta_xpath)
                return nombre.text
            except:
                sleep(1)
        else:
            return None