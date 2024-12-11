"""
This module generates random personal and business information using the Faker 
library for Brazilian Portuguese locale. It includes functions for generating 
names, emails, identification numbers (CNPJ, CPF), phone numbers, passwords, 
and birth dates.
"""

import unicodedata
import random
from faker import Faker

fake = Faker('pt_BR')


def create_random_full_name():
    """
    Generates a random full name using the Faker library.

    Returns:
        str: A randomly generated full name in Portuguese (Brazilian).
    """
    name = fake.name()
    return name


def create_random_first_name():
    """
    Generates a random first name using the Faker library.

    Returns:
        str: A randomly generated first name in Portuguese (Brazilian).
    """
    while True:
        name = fake.first_name()
        
        # Verificar se o nome tem menos de 3 caracteres
        if len(name) < 3:
            continue

        # Verificar se o nome contém acentos
        normalized_name = unicodedata.normalize('NFKD', name).encode('ASCII', 'ignore').decode('ASCII')
        if name != normalized_name:
            continue

        return name

def create_random_surname():
    """
    Generates a random surname using the Faker library.

    Returns:
        str: A randomly generated surname in Portuguese (Brazilian).
    """
    name = fake.name().split(' ')[1]
    return name


def create_random_email():
    """
    Generates a random email address using the Faker library.

    Returns:
        str: A randomly generated email address.
    """
    email = fake.email()
    return email


def create_cnpj():
    """
    Generates a random CNPJ (Cadastro Nacional da Pessoa Jurídica), which is a 
    Brazilian business identification number, using the Faker library.

    Returns:
        str: A randomly generated CNPJ number in Brazilian format.
    """
    cnpj = fake.cnpj()
    return cnpj


def create_cpf():
    """
    Generates a random CPF (Cadastro de Pessoas Físicas), which is a Brazilian 
    personal identification number, using the Faker library.

    Returns:
        str: A randomly generated CPF number in Brazilian format.
    """
    cpf = fake.cpf()
    return cpf


def create_phone():
    """
    Generates a random phone number within a range for Brazilian phone numbers.

    Returns:
        int: A randomly generated phone number in numeric format.
    """
    phone = random.randint(1111111111, 99999999999)
    return phone


def create_password():
    """
    Generates a random password using the Faker library.

    Returns:
        str: A randomly generated password.
    """
    password = fake.password()
    return password


def create_birth_day():
    """
    Generates a random date of birth for an individual born in or before 2003, 
    formatted in the Brazilian day/month/year format.

    Returns:
        str: A randomly generated birth date in "DD/MM/YYYY" format.
    """
    while True:
        birth_day = fake.date_of_birth()
        if birth_day.year <= 2003:
            break

    birth_day_br = birth_day.strftime("%d/%m/%Y")
    return birth_day_br
