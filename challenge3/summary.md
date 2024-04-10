1. The script defines a function perform_google_search to execute a Google search query using requests library, passing the query as a parameter and returning the HTML content of the search results page.

2. Another function parse_search_results utilizes BeautifulSoup to extract relevant information like title, link, and details of search results from the HTML content.

3. The save_results function saves the parsed search results into a JSON file named "results.json".

4. In the main function, the user is prompted to input a search query, then the script fetches search results using `perform_google_search`, parses them using `parse_search_results`, saves them using `save_results`, and finally prints a success message if results were successfully saved.

5. the script enables users to perform Google searches programmatically, extract relevant information from the search results, and store them in a structured format for further analysis or processing.
