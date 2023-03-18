
url = 'https://hedigital.sgp1.digitaloceanspaces.com/national-survey/images/2023-03-22/MerchandisingPresence_Planogram_BATB_SYL-15-00927_1_Mar-22-2023.png'


import json

data = s.json()
with open('result.json', 'w') as f:
    json.dump(data, f)


    