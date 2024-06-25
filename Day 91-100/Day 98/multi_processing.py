import multiprocessing
import requests

def downloadFile(url, name):
    print(f"Started Downloading {name}")
    response = requests.get(url)
    open(f"Day 91-100/Day 98/files/file{name}.jpg", "wb").write(response.content)
    print(f"Finished Downloading {name}")

url = "https://picsum.photos/2000/3000"
pros = []

for i in range(5):
#   downloadFile(url, i)  ###direct without multiprocessing
    p = multiprocessing.Process(target=downloadFile, args=[url, i])
    p.start()
    pros.append(p)

for p in pros:
    p.join()