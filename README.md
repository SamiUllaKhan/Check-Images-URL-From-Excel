📸 Image URL Validator from Excel
This Python script reads an Excel file containing image URLs or file names, checks each URL's validity, and generates a new Excel file containing only the invalid image URLs.

✅ Features
Reads image paths from a specified Excel column

Prepends a base image URL path if needed

Validates image URLs using HTTP HEAD requests

Saves all invalid image entries to a new Excel file

Logs progress for each URL checked

📁 Example Input
Your Excel file (input.xlsx) should have a column (e.g., "ImageUrl") like:

ProductID	ImageUrl
1001	image1.jpg
1002	missing_image.jpg
1003	folder/sub/image3.png

🧪 Output
The script generates a new file:
invalid_images.xlsx
This contains all rows from the original Excel file where the image URL is invalid or unreachable.

🧰 Requirements
Python 3.6+

Dependencies:

bash
Copy
Edit
pip install pandas requests openpyxl
⚙️ Configuration
Edit these variables at the top of the script:

python
Copy
Edit
INPUT_FILE = 'input.xlsx'                # Your input Excel file
OUTPUT_FILE = 'invalid_images.xlsx'      # Output Excel file
IMAGE_URL_COLUMN = 'ImageUrl'            # Column name in Excel file
IMAGE_PATH_PREFIX = 'https://yourdomain.com/images/'  # Prefix to prepend
🚀 Usage
Place your input.xlsx file in the project folder.

Update the script config if needed.

Run the script:

bash
Copy
Edit
python image_url_checker.py
If invalid image URLs are found, they will be saved in invalid_images.xlsx.

📦 Sample Project Structure
pgsql
Copy
Edit
📁 image-url-validator/
├── image_url_checker.py
├── input.xlsx
├── invalid_images.xlsx (generated)
└── README.md
📝 License
MIT License — free to use and modify.

Let me know if you'd like a version with:

Image download instead of just checking

Parallel requests for speed

CSV support instead of Excel
