import os

import requests
from pytube import YouTube
from pytube.exceptions import VideoUnavailable, PytubeError

my = """
░██████╗░█████╗░██╗░░██╗██╗███████╗░█████╗░███████╗██████╗░  ██╗░░░██╗░░███╗░░░░░██████╗░░░░░░███╗░░
██╔════╝██╔══██╗██║░░██║██║╚════██║██╔══██╗██╔════╝██╔══██╗  ██║░░░██║░████║░░░░░╚════██╗░░░░████║░░
╚█████╗░██║░░╚═╝███████║██║░░███╔═╝██║░░██║█████╗░░██║░░██║  ╚██╗░██╔╝██╔██║░░░░░░░███╔═╝░░░██╔██║░░
░╚═══██╗██║░░██╗██╔══██║██║██╔══╝░░██║░░██║██╔══╝░░██║░░██║  ░╚████╔╝░╚═╝██║░░░░░██╔══╝░░░░░╚═╝██║░░
██████╔╝╚█████╔╝██║░░██║██║███████╗╚█████╔╝███████╗██████╔╝  ░░╚██╔╝░░███████╗██╗███████╗██╗███████╗
╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝╚══════╝░╚════╝░╚══════╝╚═════╝░  ░░░╚═╝░░░╚══════╝╚═╝╚══════╝╚═╝╚══════╝"""


def start():
    print(my)
    path = input('\nВведите путь папки: ')
    if not os.path.exists(path):
        os.makedirs(path)
    fileVideos = input('Введите путь к файлу с ссылками на видео: ')
    if os.path.exists(fileVideos) and os.path.isfile(fileVideos):
        with os.path.exists(fileVideos) and open(fileVideos, 'r') as f:
            nums = f.read().splitlines()
            for i in range(len(nums)):
                print('Загрузка: ' + str(i + 1) + '/' + str(len(nums)))
                downloadYouTube(nums[i], path + '/videos/' + str(i + 1))
    else:
        print('Не нашли файл!')

    input("Press enter to close program")


def downloadYouTube(videourl, path):
    try:
        global yt
        yt = YouTube(videourl)
        description = yt.description
        tags = yt.keywords
        previewURL = yt.thumbnail_url
        yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if not os.path.exists(path):
            os.makedirs(path)
        yt.download(path)
        print('Video download completed')
        with open(path + '/description.txt', "w", encoding="utf-8") as descriptionFile:
            descriptionFile.write(description)
            print('Description download completed')
        with open(path + '/tags.txt', "w", encoding="utf-8") as tagsFile:
            tagsFile.write(str(tags).replace('[', '').replace(']', '').replace("'", ""))
            print('Tags download completed')
        with open(path + '/preview.jpg', "wb") as previewIMG:
            img = requests.get(previewURL)
            previewIMG.write(img.content)
            print('Preview download completed')
    except VideoUnavailable as e:
        print('Видео недоступно, проверьте ссылку: https://www.youtube.com/watch?v=' + e.video_id)
    except PytubeError:
        print('Что-то пошло не так! Проверьте свои видео!')


start()
