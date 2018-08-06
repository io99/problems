

#pip install requests
import requests, json
from requests.auth import HTTPBasicAuth
data = {
    "urls": ["https://s3-us-west-2.amazonaws.com/nanonets/replace_me.jpg"], \
    "modelId":"701e1d2f-c1c8-4717-8469-3cbc71ffbcc3"
}

headers = {
    'accept': 'application/x-www-form-urlencoded'
}


url = "https://app.nanonets.com/api/v2/ImageCategorization/LabelUrls/"
r = requests.post(url, headers=headers, data=data, auth=HTTPBasicAuth('un7xK43z0YwxupiAsc8tgbXQLwDW01Ha', ''))
print r.content

