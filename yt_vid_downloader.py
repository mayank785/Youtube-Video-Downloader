from pytube import YouTube
import csv

links = {}

with open('vid_url.csv', 'r') as urls:
        read = csv.reader(urls)
        links = {rows[0]:rows[1] for rows in read}
        urls.close()

def downloader():
    yt = YouTube(link)
    t = yt.title
    videos = yt.streams.all()
    vid = list(enumerate(videos))
    for i in vid:
        print(i)
    print()
    strm = int(input("Enter the index number of file you want to download : "))
    print(f"Downloading : {t}")
    videos[strm].download()
    print("Success...")

for i in links:
    link = links[i]
    downloader()
