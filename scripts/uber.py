import sys
sys.path.append('app/libs')
from selenium_tools import Uber

def run():
    ub = Uber(driver=True, sleep=5, headless=False)
    ub.login_v2()
    ub.download_payments_order()
    ubr = ub.save_report()
    ub.quit()


 