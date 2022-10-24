cd  ./testCases
pytest  -s  --alluredir  ../outputs/reports/tmp  --clean-alluredir
allure serve ../outputs/reports/tmp