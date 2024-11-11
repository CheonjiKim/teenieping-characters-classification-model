import requests
from bs4 import BeautifulSoup
import os
import time
from urllib.parse import urljoin

def download_images(character, num_images):
   
    count = 0
    for i in range(25):
        # 웹 페이지 요청 https://www.google.com/search?q=heartsping&udm=2
        search_url = f"https://www.google.com/search?q={character}&udm=2"
        response = requests.get(search_url)

        # BeautifulSoup 객체 생성
        soup = BeautifulSoup(response.text, 'html.parser')
        # 원하는 데이터 추출
        # 예: 모든 <p> 태그 찾기
    
        img_tags = soup.find_all('img')
        urls = [img['src'] for img in img_tags if 'src' in img.attrs]

        if not os.path.exists(character):
            os.makedirs(character)

        for url in urls:
            try:
                if count >= num_images:
                    break

                # img_url = urljoin(search_url, url)
                img_url = url
                img_data = requests.get(img_url).content
                with open(f'{character}/{character}_{count}.jpg', 'wb') as handler:
                    handler.write(img_data)

                count += 1
                print(f"Downloaded {count} images for {character}")
                time.sleep(0.5)  # To avoid overwhelming the server

            except Exception as e:
                print(f"Error downloading image: {e}")

        search_url += "&start=" + str(i * 10)
    print(f"Finished downloading {count} images for {character}")

characters = ["heartsping", "fluffyping", "shashaping", "jellyping"]
num_images_per_character = 250

for character in characters:
    download_images(character, num_images_per_character)