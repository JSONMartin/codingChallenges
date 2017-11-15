import requests, bs4, logging, os, threading
BeautifulSoup = bs4.BeautifulSoup

XKCD_URL = 'https://xkcd.com'
CHUNK_SIZE = 100000

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
counter = 0

# os.chdir('Misc/AutomateTheBoringStuffWithPython')

downloadThreads = []

def scrape_for_image(url):
    logging.info(f"Scraping url:{url}")
    global counter
    global downloadThreads
    counter += 1
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "lxml")

    imageUrl = soup.select('#comic > img')[0].attrs['src']
    url = f"https:{imageUrl}"

    downloadThreads += [threading.Thread(target=save_image, args=[url])]
    downloadThreads[-1].start()
    # save_image(f"https:{imageUrl}")

    try:
        prevButton = soup.select('a[rel=prev]')[0]
        prevBtnUrl = prevButton.attrs['href']
        scrape_for_image(f"{XKCD_URL}{prevBtnUrl}") # Recursively Scrape until there is no more button
    except:
        print("There are no more prev buttons, so it must be done.")
        print(f"Success! Scraped [{counter}] images")

def save_image(url):
    print(f"Download thread started, thread length: {len(downloadThreads)}")
    imageResult = requests.get(url)
    fileName = imageResult.url.split('/')[-1]

    file = open(f"XKCD_SCRAPE/{fileName}", 'wb')
    for chunk in imageResult.iter_content(CHUNK_SIZE):
        file.write(chunk)

    file.close()
    logging.info(f"Successfully wrote {fileName}")

scrape_for_image(XKCD_URL)

for download in downloadThreads:
    print("Download thread:", download)

print("All downloads done!")