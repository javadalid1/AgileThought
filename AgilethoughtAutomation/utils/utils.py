"""
Imports area
"""
import configparser
import inspect
import json

import os.path
import pathlib

from datetime import date, timedelta, datetime
from time import sleep

from msedge.selenium_tools import EdgeOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from src.testproject.enums.report_type import ReportType
from src.testproject.sdk.drivers import webdriver


class Utils:
    """
    Class containing utilities for data reading, reporting, assertions, etc.
    """

    # Init statement. Receives driver (Webdriver) as parameter.
    def __init__(self, driver):
        self.driver = driver

    def set_mobile_resolution(self, data):
        """
        Set the driver window size, depending on the values provided.
        Args:
            data: The data element generated in the first part of the test (
            dictionary that reads the JSON file.
        :return: True if mobile resolution is detected, False otherwise.
        """
        mobile_flag = False
        try:
            if data['tamaño']['anchoPx'] < 1200:
                mobile_flag = True
            self.driver.set_window_size(data['tamaño']['anchoPx'],
                                        data['tamaño']['altoPx'])
        except:
            pass
        return mobile_flag

    @staticmethod
    def get_file_path(file):
        """
        Get the full path of the file.
        file: The name of the file with its extension inside the folder. As
        String.
        :return: path: The full path as string.
        """
        caller_frame = inspect.stack()[1]
        first_path = os.path.abspath(os.curdir)
        first_path = pathlib.Path(first_path, "data")
        first_path = pathlib.Path(first_path, "files")
        second_path = (caller_frame.filename[caller_frame.filename.index(
            "tests"):].replace("tests", "").replace(".py", ""))
        path = str(first_path) + second_path
        path = pathlib.Path(path, file)
        return str(path)

    @staticmethod
    def read_data():
        """
        Function to read the JSON data file
        :return: data: A dictionary after reading the JSON file.
        """
        caller_frame = inspect.stack()[1]
        caller_filename_full = caller_frame.filename
        path = caller_filename_full.replace("tests", "data").replace(".py",
                                                                     ".json")
        file = open(path, encoding="utf-8")
        data = json.load(file)
        file.close()
        return data

    def get_evidence(self, description="", wait=0, message="",
                     passed=True, ss=True):
        """
        Method for taking screenshots.
        Args:
            description: The description as string which
            will be printed on the PDF report.
            wait: Time to wait for the ss to be taken in seconds. As float.
            message: Additional message as string if required.
            passed: Test status as boolean.
            ss: Screenshot to be taken as boolean.

        """
        sleep(wait)
        self.driver.report().step(description=description, message=message,
                                  passed=passed, screenshot=ss)

    def disable_cmd_reports(self, flag=True):
        """
        Method used for disabling the reporting of each command or action.
        Args:
            flag: Toggles the reporting feature. As boolean. True by Default.
        """
        self.driver.report().disable_command_reports(disabled=flag)

    @staticmethod
    def assertIn(firstArg, secondArg, message=""):
        """
        Assert In function.

        :param firstArg: First argument to evaluate
            if it is inside the second one.
        :param secondArg: Second argument corresponding to the entire statement.
        :param message: Optional message to be displayed if it fails. As string.
        :return: An assertion.
        """
        assert str(firstArg) in str(secondArg), message

    @staticmethod
    def assertNotIn(firstArg, secondArg, message=""):
        """
        Assert Not In function.
        :param firstArg: First argument to evaluate
        if it is not inside the second one.
        :param secondArg: Second argument corresponding to the entire statement.
        :param message: Optional message to be displayed if it fails. As string.
        :return: An assertion.
        """
        assert str(firstArg) not in str(secondArg), message

    @staticmethod
    def assertTrue(arg, message=""):
        """
        Assert True function.
        :param arg: Argument to evaluate if it is true, as boolean.
        :param message: Optional message to be displayed
        if it is False. As string.
        :return: An assertion.
        """
        assert arg, message

    @staticmethod
    def assertFalse(arg, message=""):
        """
        Assert False function.
        :param arg: Argument to evaluate if it is false, as boolean.
        :param message: Optional message to be displayed
        if it is True. As string.
        :return: An assertion.
        """
        assert not arg, message

    @staticmethod
    def assertEquals(arg, arg2, message=""):
        """
        Assert Equals function.
        :param arg: First argument to evaluate.
        :param arg2: Second argument to be evaluated.
        :param message: Optional message to be displayed
        if it is Equal. As string.
        :return: An assertion.
        """
        assert arg == arg2, message

    @staticmethod
    def assertNotEquals(arg, arg2, message=""):
        """
        Assert Not Equals function.
        :param arg: First argument to evaluate.
        :param arg2: Second argument to be evaluated.
        :param message: Optional message to be displayed
        if it is not Equal. As string.
        :return: An assertion.
        """
        assert arg != arg2, message

    @staticmethod
    def assertNotNone(arg, message=""):
        """
        Assert Not None function.
        :param arg: Argument to evaluate.
        :param message: Optional message to be displayed
        if it is not None. As string.
        :return: An assertion.
        """
        assert arg is not None, message

    @staticmethod
    def assertNone(arg, message=""):
        """
        Assert None function.
        :param arg: Argument to evaluate.
        :param message: Optional message to be displayed
        if it is None. As string.
        :return: An assertion.
        """
        assert arg is None, message

    @classmethod
    def generate_driver(cls, headless, reporting, browser, job_name):
        """
        Genera el WebDriver necesario para la ejecución del test.

        Args:
             headless: Variable de entorno que provee la configuración para
                que el test se ejecute en modo Headless (sin interfaz gráfica)
             reporting: Variable de entorno que provee la configuración para
                ejecutar el test sin generar reportes en TestProject
             browser: Variable de entorno que contiene el nombre del
                navegador a utilizar para la ejecución. (chrome, edge, firefox,
                safari)
             job_name: Nombre del job en TestProject. Como String.

        Return:
            El webdriver con las configuraciones necesarias.
        """
        project_name = 'Automatizacion AgileThought'
        token = cls.get_token()
        path = pathlib.Path
        ruta_reporte = path(path.home(), "Documents", job_name)
        if ruta_reporte.exists() is False:
            path.mkdir(ruta_reporte)
            ruta_reporte = str(ruta_reporte)
        else:
            ruta_reporte = str(ruta_reporte)
        nombre_reporte = (job_name +
                          " " +
                          datetime.now().strftime("%d-%m-%Y %H-%M-%S.%f"))
        browsers = (
            {"chrome": ChromeOptions(), "edge": EdgeOptions(),
             "firefox": FirefoxOptions(), "mozilla": FirefoxOptions(),
             "safari": None})
        if browser is None:
            nav = "chrome"
        else:
            nav = browser.lower()
        options = browsers.get(nav, "No se encontró el navegador deseado")
        if nav == "chrome":
            if eval(headless):
                options.add_argument("headless")
                options.add_argument("window-size=1280,1024")
            if eval(reporting):
                driver = webdriver.Chrome(chrome_options=options,
                                          token=token,
                                          project_name=project_name,
                                          job_name=job_name,
                                          disable_reports=json.loads(
                                              reporting.lower()))
            else:
                driver = webdriver.Chrome(chrome_options=options,
                                          token=token,
                                          project_name=project_name,
                                          job_name=job_name,
                                          report_type=ReportType.LOCAL,
                                          report_name=nombre_reporte,
                                          report_path=ruta_reporte)
        elif nav == "edge":
            if eval(headless):
                options.use_chromium = True
                options.add_argument("headless")
                options.add_argument('disable-gpu')
                options.add_argument("window-size=1280,1024")
            if eval(reporting):
                driver = webdriver.Edge(edge_options=options, token=token,
                                        project_name=project_name,
                                        job_name=job_name,
                                        disable_reports=json.loads(
                                            reporting.lower()))
            else:
                driver = webdriver.Edge(edge_options=options, token=token,
                                        project_name=project_name,
                                        job_name=job_name,
                                        report_type=ReportType.LOCAL,
                                        report_name=nombre_reporte,
                                        report_path=ruta_reporte)
        elif nav == "firefox":
            if eval(headless):
                options.headless = True
                options.add_argument('disable-gpu')
                options.add_argument("window-size=1280,1024")
            if eval(reporting):
                driver = webdriver.Firefox(firefox_options=options,
                                           token=token,
                                           project_name=project_name,
                                           job_name=job_name,
                                           disable_reports=json.loads(
                                               reporting.lower()))
            else:
                driver = webdriver.Firefox(firefox_options=options,
                                           token=token,
                                           project_name=project_name,
                                           job_name=job_name,
                                           report_type=ReportType.LOCAL,
                                           report_name=nombre_reporte,
                                           report_path=ruta_reporte)
        elif nav == "safari":
            if eval(headless):
                raise AssertionError("Por el momento Safari no se puede "
                                     "ejecutar en modo Headless")
            else:
                driver = webdriver.Safari(token=token,
                                          project_name=project_name,
                                          job_name=job_name,
                                          report_type=ReportType.LOCAL,
                                          report_name=nombre_reporte,
                                          report_path=ruta_reporte)
        else:
            raise AssertionError(
                "Selenium no tiene soporte para el navegador indicado.")
        return driver
