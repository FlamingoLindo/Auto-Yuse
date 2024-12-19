import base64  
import os  
import pytest  
import pytest_html  
from pytest_metadata.plugin import metadata_key

"""
Landing Page
"""
from Landing_Page.test_create_driver_account import (TEST_TITLE, QA, BACK, TYPE)
def pytest_html_report_title(report):  
    report.title = TEST_TITLE
  
def pytest_configure(config):
    config.option.htmlpath = 'Reports/report.html'
  
    config.stash[metadata_key]["Projeto"] = f"Bamburey {TYPE}"  
    config.stash[metadata_key]["QA"] = f"{QA}" 
    config.stash[metadata_key]["Back"] = f"{BACK}"
    
    config.stash[metadata_key]["Ambiente"] = "Produção"
    config.stash[metadata_key]["Versão"] = "1.0.0"
    config.stash[metadata_key]["Build"] = "12345"