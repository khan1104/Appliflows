# import requests
# from urllib.parse import urlparse

# HUNTER_API_KEY = "d668e73ea7e7eaebd438d656812d48373e0255a5"

# def extract_domain(url_or_domain: str):
#     if "://" in url_or_domain:
#         parsed = urlparse(url_or_domain)
#         return parsed.netloc.replace("www.", "")
#     return url_or_domain.replace("www.", "")

# def get_contacts_from_domain(input_url_or_domain: str):
#     domain = extract_domain(input_url_or_domain)
#     url = "https://api.hunter.io/v2/domain-search"
#     params = {
#         "domain": domain,
#         "api_key": HUNTER_API_KEY
#     }

#     response = requests.get(url, params=params)
#     print(response)

#     if response.status_code != 200:
#         return {"error": "API call failed", "status_code": response.status_code}

#     data = response.json().get("data", {})
#     emails = data.get("emails", [])
#     result = []
#     for person in emails:
#         # Try extracting LinkedIn from sources
#         linkedin = person.get("linkedin")
#         if not linkedin:
#             for src in person.get("sources", []):
#                 if "linkedin.com" in src.get("uri", ""):
#                     linkedin = src["uri"]
#                     break

#         result.append({
#             "name": f"{person.get('first_name', '')} {person.get('last_name', '')}".strip(),
#             "email": person.get("value"),
#             "title": person.get("position"),
#             "seniority": person.get("seniority"),
#             "linkedin": linkedin,

#         })

#     return result


# data=get_contacts_from_domain("https://www.flipkart.com/")

# for c in data:
#     print(c)

from urllib.parse import urlparse
def extract_domain(url_or_domain: str) -> str:
    """
    Removes protocols and www. from a given URL like:
    'https://www.amazon.in' → 'amazon.in'
    """
    if "://" in url_or_domain:
        parsed = urlparse(url_or_domain)
        return parsed.netloc.replace("www.", "")
    return url_or_domain.replace("www.", "")


print(extract_domain("https://www.amazon.in"))