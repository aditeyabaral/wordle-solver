import warnings
warnings.filterwarnings("ignore")

import json
import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')

url = "https://www.nytimes.com/games/wordle/"
driver = webdriver.Chrome(options=options)
driver.get(url)
time.sleep(0.3)

js_snippet = '''return window.localStorage'''
local_storage = driver.execute_script(js_snippet)
solution = json.loads(local_storage['nyt-wordle-state'])['solution'].upper()
print(solution)
driver.quit()