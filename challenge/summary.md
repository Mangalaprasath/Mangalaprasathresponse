The provided code extracts both text and table data from each page of a PDF document using the `pdfplumber` library. It then saves the extracted data into a JSON file. The `extract_information_and_tables` function iterates over each page, extracts text and table data, and stores them in a dictionary. 
The save_extracted_data function writes the extracted data to a JSON file. 
The main function orchestrates the entire process, from extraction to saving, and prints a message upon completion.
