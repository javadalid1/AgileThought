# Imports area
import random

from src.testproject.decorator import report_assertion_errors
from utils.utils import Utils
from pom.products_page import ProductsPage as Pp
import os
import json


class VerifyTitlePrice:
    """
    Test to verify that the product card can be opened and that the card
    title and price displayed corresponds to the ones shown before clicking
    on it.
    """
    data = Utils.read_data()
    driver = Utils.generate_driver(os.getenv('HEADLESS'), os.getenv(
        'DISABLE_REPORTING'), os.getenv('BROWSER'),
                                   "Verification Title and Price - Product")
    utils = Utils(driver)
    utils.disable_cmd_reports()
    pp = Pp(driver)

    @report_assertion_errors(screenshot=True)
    def testTitlePrice(self):
        try:
            self.step_1_navigate_url()
            self.step_2_click_card()
            self.step_3_verify_name_price()
            self.driver.quit()
        except Exception as e:
            raise AssertionError("El test falló: " + str(e))

    def step_1_navigate_url(self):
        self.description = "Navigate to the url of the online store."
        self.driver.get(self.data['url'])
        self.utils.get_evidence(self.description)

    def step_2_click_card(self):
        self.description = "Extract the title/name and price of any of the " \
                           "displayed cards in a random way. Then click on " \
                           "the product card."
        num_tarjetas = self.pp.get_num_tarjetas()
        self.utils.assertNotNone(num_tarjetas,
                                 "No fue posible extraer el número total de "
                                 "tarjetas.")
        rand = random.randint(0, num_tarjetas - 1)
        self.nombre = self.pp.get_nombre_tarjeta(rand)
        self.precio = self.pp.get_precio_tarjeta(rand)
        self.utils.assertNotNone(self.nombre,
                                 "No fue posible extraer el nombre de la "
                                 "tarjeta")
        self.utils.assertNotNone(self.precio,
                                 "No fue posible extraer el precio de la "
                                 "tarjeta")
        self.utils.get_evidence(self.description)
        self.utils.assertTrue(self.pp.click_tarjeta(rand),
                              "No fue posible dar click en la tarjeta deseada.")

    def step_3_verify_name_price(self):
        self.description = "Extract the title/name and price of " \
                           "the displayed open card and compares it " \
                           "with the extracted before clicking on it. " \
                           "It is expected to be the same."
        nombre = self.pp.get_nombre_tarjeta_abierta()
        precio = self.pp.get_precio_tarjeta_abierta()
        self.utils.assertNotNone(nombre,
                                 "No fue posible extraer el nombre de la "
                                 "tarjeta.")
        self.utils.assertNotNone(precio,
                                 "No fue posible extraer el precio de la "
                                 "tarjeta.")
        self.utils.assertEquals(nombre, self.nombre,
                                f"El nombre desplegado antes de dar click en "
                                f"la tarjeta: {self.nombre}, no coincide con "
                                f"el que se visualiza al hacer click: {nombre}")
        self.utils.assertEquals(precio, self.precio,
                                f"El precio desplegado antes de dar click en "
                                f"la tarjeta: {self.precio}, no coincide con "
                                f"el que se visualiza al hacer click: {precio}")
        self.utils.get_evidence(self.description)
