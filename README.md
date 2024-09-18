# help_unhcr_org

Listing the websites from [help.unhcr.org](https://help.unhcr.org/) organized by country. Each entry in the dataset includes:

- Country: The name of the country the help website is associated with.
- ISO3 Code: The three-letter ISO code representing the country.
- Help Website: An array of objects detailing the available help resources in various languages. Each object contains:
    - Language: The language of the help resource, including any relevant translations or scripts.
    - URL: The direct link to the help website in the specified language.

The dataset is available in JSON format.



## Example

```json
[
  {
    "country": "Afghanistan",
    "iso3": "AFG",
    "help_website": [
      {
        "language": "English  •",
        "url": "https://help.unhcr.org/afghanistan/"
      },
      {
        "language": "Dari | دری",
        "url": "https://help.unhcr.org/afghanistan/fa-af/"
      },
      {
        "language": "Pashto | پښتو",
        "url": "https://help.unhcr.org/afghanistan/ps/"
      }
    ]
  },
  {
    "country": "Albania",
    "iso3": "ALB",
    "help_website": [
      {
        "language": "English  •",
        "url": "https://help.unhcr.org/albania/"
      },
      {
        "language": "Ukrainian | Українська",
        "url": "https://help.unhcr.org/albania/uk/"
      }
    ]
  }
]
```