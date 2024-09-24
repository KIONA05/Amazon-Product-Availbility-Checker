import requests
from bs4 import BeautifulSoup


def check_amazon_availability(product_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
    }

    try:
        response = requests.get(product_url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")

        # Extracting the title
        title = soup.find("span", {"id": "productTitle"})
        title_text = title.get_text(strip=True) if title else "Product title not found"

        # Extracting availability
        availability = soup.find("div", {"id": "availability"})
        availability_text = availability.get_text(strip=True) if availability else "Availability not found"

        if "out of stock" in availability_text.lower():
            print(f"{title_text} is currently out of stock on Amazon.")
        else:
            print(f"{title_text} is available on Amazon.")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    product_url = "AMAZON URL"
    check_amazon_availability(product_url)
