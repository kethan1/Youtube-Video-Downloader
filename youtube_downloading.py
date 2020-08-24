import pytube


def verify(url):
    """
	To check whether `url` belongs to YouTube, if yes returns True
	else False
	"""
    if "youtube.com" in url or "youtu.be" in url:
        return True
    return False


def get_media(url, choice):
    try:

        if url == "":

            pass

        else:

            if choice == 1:

                youtube = pytube.YouTube(url)

                video = youtube.streams.filter(only_audio=True).first()

                video.download('./tmp/audio/', filename="audio_1")


            elif choice == 2:

                youtube = pytube.YouTube(url)

                video = youtube.streams.get_highest_resolution()

                video.download('./tmp/videos/', filename="video_1")


    except Exception as e:  # for any other unknown errors,  used it to get the other exceptions mentioned above, while debugging used to print `e`

        return e


if __name__ == "___main__":

    print("This is a borrowed script")

else:
    url = ""
    choice = 1
    verify(url)
    get_media(url, choice)

