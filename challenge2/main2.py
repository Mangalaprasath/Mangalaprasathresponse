import json
from collections import Counter
from typing import List, Tuple

def load_data(filename: str) -> List[int]:
    """Load a list of integers from a JSON file."""
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def calculate_frequency(numbers: List[int]) -> List[Tuple[int, int]]:
    """Calculate the frequency of each unique number and return sorted by frequency descending."""
    # Use Counter to count frequencies
    counter = Counter(numbers)
    # Sort by frequency (descending) and then by number (ascending)
    sorted_freq = sorted(counter.items(), key=lambda x: (-int(x[1]) if isinstance(x[1], int) else float('inf'), x[0]))
    return sorted_freq


def get_third_highest_frequency(frequencies: List[Tuple[int, int]]) -> Tuple[int, int]:
    """Retrieve the third highest frequency from the list of (number, frequency) tuples."""
    if len(frequencies) < 3:
        return None, None  # Return None if there are fewer than 3 unique numbers

    # Find the third highest frequency
    third_highest_freq = frequencies[2][1]
    
    # Find all numbers with the third highest frequency
    third_highest_numbers = [num for num, freq in frequencies if freq == third_highest_freq]
    
    # Return the third highest frequency and the list of numbers with that frequency
    return third_highest_freq, third_highest_numbers

def save_output(data: dict, filename: str) -> None:
    """Save the given data as JSON in a file."""
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    numbers = load_data('data.json')
    frequencies = calculate_frequency(numbers)
    third_highest_freq, third_highest_numbers = get_third_highest_frequency(frequencies)
    
    output = {
        "sorted_frequency_distribution": frequencies,
        "third_highest_frequency": third_highest_freq,
        "numbers_with_third_highest_frequency": third_highest_numbers
    }
    
    save_output(output, 'output.json')
    
    print("Output saved to output.json")

if __name__ == "__main__":
    main()
