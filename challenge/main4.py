import pdfplumber
import json

def extract_information_and_tables(pdf_path: str) -> dict:
    """Extract both text and table data from each page of the PDF document."""
    extracted_data = {
        "text": [],  # Store extracted text
        "tables": []  # Store extracted tables as lists of dictionaries
    }
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            # Extract text from the page and add it to extracted_data["text"]
            extracted_data["text"].append(page.extract_text())
            
            # Extract table data from the page, process it into dictionaries, and add to extracted_data["tables"]
            tables = page.extract_tables()
            for table in tables:
                table_data = []
                for row in table:
                    table_data.append(row)
                extracted_data["tables"].append(table_data)
                
    return extracted_data

def save_extracted_data(data: dict, output_file: str):
    """Save the extracted data to a JSON file."""
    with open(output_file, 'w') as f:
        json.dump(data, f)

def main():
    pdf_path = 'input.pdf'  # Specify the path to the input PDF file
    output_file = 'output.json'  # Specify the path to the output JSON file
    
    # Extract data from PDF
    extracted_data = extract_information_and_tables(pdf_path)
    
    # Save the extracted data
    save_extracted_data(extracted_data, output_file)
    
    print(f"Extracted data has been saved to {output_file}")

if __name__ == "__main__":
    main()
