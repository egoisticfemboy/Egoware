import cv2
import requests
import numpy as np
import ctypes
from bs4 import BeautifulSoup
import random

def cock_sucker(url):
    response = requests.get(url)
    image_data = np.frombuffer(response.content, dtype=np.uint8)
    image = cv2.imdecode(image_data, cv2.IMREAD_COLOR)
    return image

def random_cock_sucker():
    query = "femboy"
    url = f"https://www.google.com/search?q={query}&tbm=isch"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/547.36(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    img_tags = soup.find_all("img")
    img_urls = [img['src'] for img in img_tags if 'src' in img.attrs]

    if img_urls:
        return random.choice(img_urls)
    return None

def main_cock_sucker():
    img_url = random_cock_sucker()
    
    if img_url is None:
        print("Failed to find a random femboy image onh google")
        return -1
    
    image = cock_sucker(img_url)
    if image is None:
        print(f"Failed to download from URL: {img_url}")
        return -1
    
    user32 = ctypes.windll.user32
    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)

    x_pos = screen_width - image.shape(1)
    y_pos = 0 

    window_name = "Random Cocksucker Picture"
    cv2.nameWindow(window_name, cv2.WINDOW_NORMAL)

    cv2.imshow(window_name, image)
    user32.SetWindowPos(
        cv2.getWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN),
        0, x_pos, y_pos, 0, 0, 0x0001
    )

    cv2.waitKey(0)
    return 0

if __name__ == "__main__":
    main_cock_sucker()