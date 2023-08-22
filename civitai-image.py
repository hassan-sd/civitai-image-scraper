import requests
from PIL import Image
from io import BytesIO
import os
import re
from tqdm import tqdm

# User inputs
min_width = int(input("Enter the minimum width for images (in pixels): "))
min_height = int(input("Enter the minimum height for images (in pixels): "))
save_location = input("Enter the location to save the images and metadata: ")
max_images = int(input("Enter the maximum number of images to download: "))

# Ensure the directory exists
if not os.path.exists(save_location):
    os.makedirs(save_location)

# Replace with your API key
api_key = "xxxxx"
# API endpoint
url = "https://civitai.com/api/v1/images"
headers = {"Authorization": f"Bearer {api_key}"}

current_page = 1
page_size = 100  # assuming this, adjust based on the API's actual page size
total_downloaded = 0

while total_downloaded < max_images:
    # Modify the API request to include the current page
    response = requests.get(url + f"?page={current_page}", headers=headers)
    response_data = response.json()

    # If there are no items in the response, break out of the loop
    if not response_data['items']:
        break

    # Filter images
    filtered_images = [image for image in response_data['items'] if image['stats']['heartCount'] > 10 and image['meta'] is not None and 'prompt' in image['meta'] and image['meta']['prompt']]

    for image in tqdm(filtered_images, desc=f"Saving images and metadata (Page {current_page})", unit="image"):
        # If total_downloaded reaches or exceeds max_images, stop processing
        if total_downloaded >= max_images:
            break

        image_id = image['id']
        image_url = image['url']
        image_meta = image['meta']

        # Download image
        image_response = requests.get(image_url)
        img = Image.open(BytesIO(image_response.content))

        # Check size and skip if below requirements
        if img.size[0] < min_width or img.size[1] < min_height:
            continue

        # Convert to RGB if necessary
        if img.mode == 'RGBA':
            img = img.convert('RGB')

        # Save image to the specified location
        img_filename = os.path.join(save_location, f"{image_id}.jpg")
        img.save(img_filename)

        # Remove content inside tags and save meta.prompt
        cleaned_meta_prompt = re.sub(r'<[^>]+>', '', image_meta['prompt'])
        meta_filename = os.path.join(save_location, f"{image_id}.txt")
        with open(meta_filename, "w") as meta_file:
            meta_file.write(cleaned_meta_prompt)

        total_downloaded += 1

    # Go to the next page
    current_page += 1

print(f"Downloaded and saved {total_downloaded} images and metadata files to {save_location}.")
