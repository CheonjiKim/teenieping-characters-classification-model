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

def search_and_download_images(query, num_images):
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
    """
        duckduckgo 포털 사이트에서 이미지를 크롤링하는 코드이다.
        queries, num_images 이 두 변수만 설정하고 코드를 실행하면 된다.

        queries에는 검색어를 문자열로 넣으면 된다.
        검색어 별로 num_images만큼의 이미지를 다운로드한다.
    """

    # 검색어 쿼리를 배열에 담는다.
    queries = ["또너핑", "또너핑 이미지", "또너핑 배경화면", "donutping", "donutping image"]
    
    # 각 쿼리별 다운로드할 이미지의 개수
    num_images = 50

    for query in queries:
        print(f"Searching and downloading images for: {query}")
        search_and_download_images(query, num_images)
        print(f"Finished downloading images for: {query}")

if __name__ == "__main__":
    main()