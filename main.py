import pandas as pd
import requests

# === Configuration ===
INPUT_FILE = 'input.xlsx'                  # Input Excel file
OUTPUT_FILE = 'invalid_images.xlsx'        # Output Excel file
IMAGE_URL_COLUMN = 'ImageUrl'              # Column containing image names/paths
IMAGE_PATH_PREFIX = "https://imagesm.plexussquare.in/VIPULSHOES/"  # Base path for images

def is_image_url_valid(url):
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        content_type = response.headers.get('Content-Type', '')
        is_valid = response.status_code == 200 and 'image' in content_type.lower()
        print(f"Checked: {url} --> {'Valid' if is_valid else 'Invalid'}")
        return is_valid
    except Exception as e:
        print(f"Error checking {url}: {e}")
        return False

def find_invalid_images(input_file, column_name):
    df = pd.read_excel(input_file)

    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in the Excel file.")

    def check_url(url):
        if pd.isna(url):
            return False
        full_url = IMAGE_PATH_PREFIX + str(url).strip()
        return is_image_url_valid(full_url)

    invalid_rows = df[~df[column_name].apply(check_url)]
    return invalid_rows

def main():
    print("🔍 Starting image URL validation...")
    invalid_images_df = find_invalid_images(INPUT_FILE, IMAGE_URL_COLUMN)

    if not invalid_images_df.empty:
        invalid_images_df.to_excel(OUTPUT_FILE, index=False)
        print(f"⚠️  Found invalid images. Results saved to '{OUTPUT_FILE}'.")
    else:
        print("✅ All image URLs are valid.")

if __name__ == "__main__":
    main()
