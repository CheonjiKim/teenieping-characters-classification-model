import os
import requests
from duckduckgo_search import DDGS

def download_image(url, folder, filename):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            os.makedirs(folder, exist_ok=True)
            file_path = os.path.join(folder, filename)
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded: {filename}")
        else:
            print(f"Failed to download: {url}")
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")

def search_and_download_images(query, num_images=250):
    # Use relative path for the folder
    folder = os.path.join(os.path.dirname(__file__), query)
    with DDGS() as ddgs:
        images = ddgs.images(query, max_results=num_images)
        for i, image in enumerate(images, start=1):
            if i > num_images:
                break
            image_url = image['image']
            file_extension = os.path.splitext(image_url)[-1].lower()
            if file_extension not in ['.jpg', '.jpeg', '.png', '.gif']:
                file_extension = '.jpg'
            filename = f"{query}_{i}{file_extension}"
            download_image(image_url, folder, filename)

def main():
    queries = ["하츄핑", "포실핑", "샤샤핑", "젤리핑"]
    for query in queries:
        print(f"Searching and downloading images for: {query}")
        search_and_download_images(query)
        print(f"Finished downloading images for: {query}")

if __name__ == "__main__":
    main()