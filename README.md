# Amazon Product Availability Checker

## Overview

The Amazon Product Availability Checker is a Python script that checks the availability of a specified product on Amazon. It scrapes the product page and reports whether the item is in stock or out of stock, along with the product title.

## Features

- **Product Title Retrieval**: Fetches the title of the product for easy identification.
- **Availability Status**: Checks if the product is currently available or out of stock.
- **Error Handling**: Catches and reports various types of errors that may occur during the request.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Installation

1. **Clone the repository** (if applicable):
   ```bash
   git clone https://github.com/yourusername/amazon-product-availability-checker.git
   cd amazon-product-availability-checker
   ```

2. **Install the required libraries**:
   ```bash
   pip install requests beautifulsoup4
   ```

3. **Update the User-Agent**: Open the script and replace the `User-Agent` string in the headers with a valid User-Agent from your web browser.

## Usage

1. **Open the script** (`amazon_availability_checker.py`) in your favorite text editor.
2. **Set the product URL**: Update the `product_url` variable with the Amazon product link you want to check.
3. **Run the script**:
   ```bash
   python amazon_availability_checker.py
   ```

## Example

To check the availability of a product, set the `product_url` variable as follows:

```python
product_url = "https://www.amazon.com/dp/B08N5WRWNW"
```

When you run the script, it will output whether the product is available or out of stock.

## Error Handling

The script includes error handling for:
- HTTP errors (e.g., 404 Not Found)
- Request exceptions (e.g., network issues)
- Parsing errors if the HTML structure changes

## Notes

- Be aware that scraping Amazon’s website may violate their terms of service. Use this tool responsibly and avoid making excessive requests.
- The HTML structure of Amazon's pages may change, which could break the script. You may need to update the selectors accordingly.

## License

This project is open-source and available under the MIT License.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements! 
