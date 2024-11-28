#!/bin/bash

# Run pytest with Allure
pytest --alluredir=allure-results

# Generate Allure report
allure generate allure-results -o allure-report --clean

# Open Allure report
allure open allure-report