import os
import requests

def scrap_linkedin_profile():
    api_endpoint = "https://gist.githubusercontent.com/raul-medina-nussbaum/65091bb5c8d509180d70f1da3188677a/raw/e6fb4ae707a9d8bc10673e837a66ce5dc2590233/raul-medina-nussbaum.json"
    
    response = requests.get(
        api_endpoint
    )

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
            and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data