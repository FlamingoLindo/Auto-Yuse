"""
This module generates random Brazilian address details using the Faker library.
The details returned include the street name, street number, city, postal code (CEP),
and state.
"""

from faker import Faker

fake = Faker('pt_BR')


def create_address():
    """
    Generates a random Brazilian address with full details.

    The function uses the Faker library to generate a Brazilian address, 
    which includes:
    - Street name (rua)
    - Street number (numero)
    - City (cidade)
    - Postal code (CEP)
    - State (estado)

    The address is split into multiple lines, and the function extracts and cleans
    each part of the address.

    Returns:
        tuple: A tuple containing the following details:
            - str: Street name (rua)
            - str: Street number (numero)
            - str: City (cidade)
            - str: Postal code (CEP)
            - str: State (estado)
    """
    while True:
        address = fake.address()
        lines = address.splitlines()

        try:
            rua, numero = lines[0].split(',', 1)
        except ValueError:
            continue

        cidade = lines[1]

        try:
            cep, estado = lines[2].split(' ', 1)
        except ValueError:
            continue

        estado = estado.split('/')[1]

        if not numero.strip():
            continue

        return rua.strip(), numero.strip(), cidade.strip(), cep.strip(), estado.strip()
