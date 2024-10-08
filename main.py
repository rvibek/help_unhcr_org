import json

import country_converter as coco
import requests
from bs4 import BeautifulSoup

url = "https://help.unhcr.org/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

cc = coco.CountryConverter()

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the div with id='content4'
content4_div = soup.find('div', id='content4')

result = []

if content4_div:
    # Find all country divs
    country_divs = content4_div.find_all('div', class_='hcr-hb')

    for country_div in country_divs:
        country_name = country_div.find('h4').text.strip()
        
        # Special cases for specific country names
        if country_name == "The Pacific":
            iso3 = [
                "COK",  # Cook Islands
                "FSM",  # Federated States of Micronesia
                "FJI",  # Fiji
                "KIR",  # Kiribati
                "MHL",  # Republic of the Marshall Islands
                "NRU",  # Nauru
                "NIU",  # Niue
                "PLW",  # Palau
                "PNG",  # Papua New Guinea
                "WSM",  # Samoa
                "SLB",  # Solomon Islands
                "TON",  # Tonga
                "TUV",  # Tuvalu
                "VUT"   # Vanuatu
        ]
        elif country_name == "Switzerland and Liechtenstein":
            iso3 = [
                "CHE", # Switzerland 
                "LIE"  # Liechtenstein
                ]
        else:
            # Handle potential errors when getting ISO3 code
            try:
                iso3 = cc.convert(names=country_name, to='ISO3')
            except AttributeError:
                iso3 = ""  # Set to empty string if country not found
        
        
        help_website = []
        
        language_links = country_div.find_all('a', hreflang=True)
        for link in language_links:
            language = link.text.strip()
            url = link['href']
            help_website.append({"language": language, "url": url})
        
        result.append({
            "country": country_name,
            "iso3": iso3,
            "help_website": help_website
        })

# Convert the result to JSON
json_output = json.dumps(result, indent=2, ensure_ascii=False)

# Print or save the JSON output
# print(json_output)

# Optionally, save to a file
with open('unhcr_help_pages.json', 'w', encoding='utf-8') as f:
    f.write(json_output)
