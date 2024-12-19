import time
import os
import sys
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(path_to_add)

from Utils.person import (create_random_first_name, create_random_surname, create_cpf, create_birth_day, create_phone)
from Utils.address import create_address

pfp_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../Images", "eu.jpg"))
document_file= os.path.abspath(os.path.join(os.path.dirname(__file__), "../Images", "cnh.jpg"))
crime_rec_file= os.path.abspath(os.path.join(os.path.dirname(__file__), "../Images", "crim_rec.png"))

# Pytest metadata
TEST_TITLE = 'CRIAÇÃO DE MOTORISTA'
QA = 'Vitor Flamingo Lindo'
BACK = 'LEO LARDO'
TYPE = 'LANDING PAGE'

class TestCreateDriver(unittest.TestCase):
    """
    
    """

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.wait = WebDriverWait(cls.driver, 10)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_01_lading_page(self) -> None:
        """
        """
        self.driver.get(os.getenv('LANDING_URL'))
        
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.eFevOM')))

    def test_02_open_registration_page(self) -> None:
        registration_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.eFevOM')))
        registration_button.click()
        
        start_btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.gCRiVp')))
        start_btn.click()
        
    def test_03_fill_step_one(self) -> None:

        pfp_input = self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/form/div[1]/label')))
        time.sleep(2)
        pfp_input.send_keys(pfp_file)
        
        name_input = self.driver.find_element(By.ID, 'firstName')
        name_input.send_keys(create_random_first_name())

        sur_name_input = self.driver.find_element(By.ID, 'lastName')
        sur_name_input.send_keys(create_random_surname())
        
        cpf_input = self.driver.find_element(By.ID, 'document')
        cpf_input.send_keys(create_cpf())
        
        birth_day_input = self.driver.find_element(By.ID, 'birthday')
        birth_day_input.send_keys(create_birth_day())
        
        phone_input = self.driver.find_element(By.ID, 'phone')
        phone_input.send_keys(create_phone())
        
        document_file_input = self.driver.find_element(By.XPATH, '//*[@id="documentPhoto"]')
        document_file_input.send_keys(document_file)
        
        # cnh_file_input = self.driver.find_element(By.XPATH, '//*[@id="cnhPhoto"]')
        # cnh_file_input.send_keys(document_file)
        cnh_input = self.driver.find_element(By.NAME, 'cnhRegisterNumber')
        cnh_input.send_keys('123456789')
        
        # cnh_file_input = self.driver.find_element(By.XPATH, '//*[@id="documentPhoto"]')
        # cnh_file_input.send_keys(document_file)
    
        # cnh_file_input = self.driver.find_element(By.XPATH, '//*[@id="criminalRecord"]')
        # cnh_file_input.send_keys(crime_rec_file)
        
        address = create_address()
        cep_input = self.driver.find_element(By.ID, 'zipCode')
        cep_input.send_keys(address[3])
        
        city_input = self.driver.find_element(By.ID, 'city')
        city_input.send_keys(address[2])
        
        state_input = self.driver.find_element(By.ID, 'state')
        state_input.send_keys(address[4])
        
        log_input = self.driver.find_element(By.ID, 'address')
        log_input.send_keys('log')
        
        neighborhood_input = self.driver.find_element(By.ID, 'neighborhood')
        neighborhood_input.send_keys(address[0])
        
        number_input = self.driver.find_element(By.ID, 'number')
        number_input.send_keys(address[0])
        
        complement_input = self.driver.find_element(By.ID, 'complement')
        complement_input.send_keys('Complemento')
        complement_input.submit()
        time.sleep(10)
        
if __name__ == '__main__':
    unittest.main()
