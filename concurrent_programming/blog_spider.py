import requests


urls = [
        f"https://www.cnblogs.com/#P{page}"
        for page in range(1, 50+1)
    ]

def craw(url):
    r = requests.get(url)
    print(url, len(r.text))


if __name__ == "__main__":
    craw(urls[0])