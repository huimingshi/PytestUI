cd  ./testCases
pytest  -s  --alluredir  ../outputs/reports/tmp  --clean-alluredir
allure serve ../outFiles/report/tmp