import requests
from bs4 import BeautifulSoup
import json

def perform_google_search(query: str) -> str:
    base_url = 'https://www.google.com/search'
    params = {'q': query}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        response = requests.get(base_url, params=params, headers=headers)
        response.raise_for_status()  # Raise an HTTPError if the request was unsuccessful
        return response.text
    except requests.exceptions.RequestException as e:
        print("Error during request:", e)
        return ""
    except Exception as e:
        print("Error:", e)
        return ""

def parse_search_results(html_content: str):
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        results = []
        for result in soup.select('.tF2Cxc')[:10]:  # Limit to top 10 results
            title = result.select_one('h3').get_text() if result.select_one('h3') else 'No Title'
            link = result.select_one('a')['href'] if result.select_one('a') else 'No Link'
            details = result.select_one('.IsZvec').get_text() if result.select_one('.IsZvec') else 'No Details'
            results.append({
                'title': title,
                'link': link,
                'details': details
            })
        return results
    except Exception as e:
        print("Error during processing:", e)
        return []

def save_results(results):
    with open("results.json", "w") as f:
        json.dump(results, f, indent=2)

def main():
    query = input("Enter your search query: ")
    html_content = perform_google_search(query)
    if html_content:
        results = parse_search_results(html_content)
        if results:
            save_results(results)
            print("Results saved successfully.")
        else:
            print("No results found.")
    else:
        print("Failed to retrieve search results.")
        print("HTML Content:", html_content)


if __name__ == "__main__":
    main()
