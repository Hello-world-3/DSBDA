#Scrapper to fetch HTML code of a website to run execute python scrapper.py or python3 scrapper.py if you are having python3 installed on your system
import requests

def fetch_html(url):
 try:
    response = requests.get(url)
    response.raise_for_status() 
    return response.text
 except requests.exceptions.RequestException as e:
    print("Error fetching data:", e)
    return None
def main():
 url = input("Enter the URL of the website: ")
 html_code = fetch_html(url)
 
 if html_code:
    print("\nHTML Code:")
    print(html_code)
if __name__ == "__main__":
 main()