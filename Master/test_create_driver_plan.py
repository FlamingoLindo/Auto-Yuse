import time
import random
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

# Pytest metadata
TEST_TITLE = 'CRIAÇÃO DE PERFIL DE MOTORISTA'
QA = 'Vitor Flamingo Lindo'
BACK = 'LEO LARDO'
TYPE = 'MASTER'

class TesteCreateProfilePlan(unittest.TestCase):
    """
    
    """

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.wait = WebDriverWait(cls.driver, 10)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_01_open_login_page(self) -> None:
        """
        """
        self.driver.get(os.getenv('MASTER_URL'))
        
        adm_text = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.iOjYQY')))
        assert adm_text.text == 'Área do administrador'
        
        email_input = self.driver.find_element(By.NAME, 'email')
        email_input.send_keys(os.getenv('MASTER_EMAIL'))
        
        pass_word_input = self.driver.find_element(By.NAME, 'password')
        pass_word_input.send_keys(os.getenv('MASTER_PASSWORD'))
        pass_word_input.submit()
        
    def test_02_open_plan_registration(self) -> None:
        """
        """
        driver_plan_pg = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.fBEZKJ')))
        assert driver_plan_pg.text == 'Planos do motorista'
        
    def test_03_fill_plan_data(self) -> None:
        """
        """
        amount = 5
        categ_loop = 2
        for i in range(amount):
            register_btn = self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/main/div[2]/div/main/div[1]/button[2]')))
            assert register_btn.text == 'Cadastrar plano'
            register_btn.click()
            
            trip_type = random.choices([True, False])
            if trip_type:
                # Delivery option
                self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div[2]/div/main/form/div[1]/label[2]'))).click()
            else:
                # Passagenrs option
                self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div[2]/div/main/form/div[1]/label[3]'))).click()
            
            # Plan name
            self.driver.find_element(By.NAME, 'name').send_keys(f'Plano de teste automatico {i}')
            
            # Benefits
            self.driver.find_element(By.NAME, 'benefits').send_keys(f'Beneficios do plano de teste automatico {i}')
            
            occurrence_type = random.choices([True, False])
            if occurrence_type:
                # Daily option
                self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div[2]/div/main/form/div[4]/label[2]'))).click()
            else:
                # Monthly option
                self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div[2]/div/main/form/div[4]/label[3]'))).click()
            
            # Occurrence amount
            occurrence_amount = random.randint(1, 1000)
            occurrence_amount_input = self.driver.find_element(By.NAME, 'qtdRecurrence')
            occurrence_amount_input.send_keys(occurrence_amount)
            
            # Categories option
            categories_dropdown = self.driver.find_element(By.XPATH, '/html/body/main/div[2]/div/main/form/div[6]/div/div/div[1]/div')
            ActionChains(self.driver).scroll_to_element(categories_dropdown).perform()
            categories_dropdown.click() 
            categories_opt = self.wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="react-select-{categ_loop}-option-3"]')))
            ActionChains(self.driver).scroll_to_element(categories_opt).perform()
            categories_opt.click()
            
            # Currency
            currency_type = random.choices([True, False])
            only_reais_option = self.driver.find_element(By.XPATH, '/html/body/main/div[2]/div/main/form/div[7]/div[1]/div/span/input')
            reais_input = self.driver.find_element(By.NAME, 'value')
            yuse_cash_input = self.driver.find_element(By.CSS_SELECTOR, '.ekwsWv')
            if currency_type:
                only_reais_option.click()
                reais_input.send_keys(random.randint(1, 1000))
            else:
                reais_input.send_keys(random.randint(1, 1000))
                yuse_cash_input.send_keys(random.randint(1, 1000))
            
            # Min and max amount of trips
            min_trips_input = self.driver.find_element(By.NAME, 'qtdMinTrips')
            min_trips_input.send_keys(random.randint(1, 1000))
            
            max_trips_input = self.driver.find_element(By.NAME, 'qtdMaxTrips')
            max_trips_input.send_keys(random.randint(1001, 9999))
            
            # Use limit
            limit_input = self.driver.find_element(By.NAME, 'limit')
            limit_input.send_keys(random.randint(1, 1000))
            
            # Expiration
            expiration_date_type = random.choices([True, False])
            if expiration_date_type:
                no_exp_date = self.driver.find_element(By.XPATH, '/html/body/main/div[2]/div/main/form/div[11]/div[1]/div/span/input')
                ActionChains(self.driver).scroll_to_element(no_exp_date).perform()
                no_exp_date.click()
            else:
                inital_date = self.driver.find_element(By.NAME, 'initialValidityDate')
                inital_date.send_keys('17/12/2024')
                
                end_date = self.driver.find_element(By.NAME, 'finalValidityDate')
                end_date.send_keys('30/12/2045')
                
            # Plan term?
            inital_date_term = self.driver.find_element(By.NAME, 'initialEffectiveDate')
            inital_date_term.send_keys('17/12/2024')
            
            end_date_term = self.driver.find_element(By.NAME, 'finalEffectiveDate')
            end_date_term.send_keys('30/12/2045')
            
            register_btn = self.driver.find_element(By.CSS_SELECTOR, '.esjRQJ')
            assert register_btn.text == 'Cadastrar'
            ActionChains(self.driver).scroll_to_element(register_btn).perform()

            # Plan application
            plan_application = random.choices([True, False])
            if plan_application:
                new_drivers_opt = self.driver.find_element(By.XPATH, '/html/body/main/div[2]/div/main/form/div[13]/label[2]')
                new_drivers_opt.click()
            else:
                all_drivers = self.driver.find_element(By.XPATH, '/html/body/main/div[2]/div/main/form/div[13]/label[3]')
                all_drivers.click()
                
            register_btn.click()
            
            modal_go_back = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.jtnXjh')))
            assert modal_go_back.text == 'Voltar'
            modal_go_back.click()
            
            i += 1
            categ_loop += 1