from pytube import YouTube

print("WELCOME , TO MY PROGRAM THIS PROGRAM IS TO DOWNLOAD YOUTUBE VIDEOS/PLAYLISTS.\n")
link = input("PLEASE PASTE THE LINK OF VIDEO ,YOU WANT TO DOWNLOAD : ")
youtube_1 = YouTube(link)
print("\nPress 1 for thumbnail \nPress 2 for video/audio")
num = int(input("Enter choice : "))
if num == 1:
    print(youtube_1.thumbnail_url)
if num == 2:
    ch = int(input("\nPress 1 for audio \nPress 2 for video \n"))
    if ch == 1:
        youtube_1.streams.filter(only_audio=True, mime_type="audio/mp4").first().download()
        print("YOUR AUDIO IS DOWNLOADED SUCCESFULLY, JUST GO AND ENJOY IT.")
    elif ch == 2:
        videos = youtube_1.streams.filter(mime_type="video/mp4", progressive="True").order_by('resolution').desc()
        video = list(enumerate(videos))
        for i in video:
            print(i)
        print()
        strm = int(input("ENTER YOUR CHOICE IN WHICH STREAM YOU WANT TO DOWNLOAD VIDEO : "))
        videos[strm].download()
        print("YOUR VIDEO IS DOWNLOADED SUCCESFULLY, JUST GO AND ENJOY IT.")
