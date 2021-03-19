# -*- coding: utf-8 -*-

import json
from urllib.parse import urlencode
from urllib.request import urlopen

my = """
██╗░░░██╗████████╗░░░░░░██████╗░░█████╗░██████╗░░██████╗███████╗██████╗░  ██████╗░██╗░░░██╗
╚██╗░██╔╝╚══██╔══╝░░░░░░██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗  ██╔══██╗╚██╗░██╔╝
░╚████╔╝░░░░██║░░░█████╗██████╔╝███████║██████╔╝╚█████╗░█████╗░░██████╔╝  ██████╦╝░╚████╔╝░
░░╚██╔╝░░░░░██║░░░╚════╝██╔═══╝░██╔══██║██╔══██╗░╚═══██╗██╔══╝░░██╔══██╗  ██╔══██╗░░╚██╔╝░░
░░░██║░░░░░░██║░░░░░░░░░██║░░░░░██║░░██║██║░░██║██████╔╝███████╗██║░░██║  ██████╦╝░░░██║░░░
░░░╚═╝░░░░░░╚═╝░░░░░░░░░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝  ╚═════╝░░░░╚═╝░░░

░██████╗░█████╗░██╗░░██╗██╗███████╗░█████╗░███████╗██████╗░
██╔════╝██╔══██╗██║░░██║██║╚════██║██╔══██╗██╔════╝██╔══██╗
╚█████╗░██║░░╚═╝███████║██║░░███╔═╝██║░░██║█████╗░░██║░░██║
░╚═══██╗██║░░██╗██╔══██║██║██╔══╝░░██║░░██║██╔══╝░░██║░░██║
██████╔╝╚█████╔╝██║░░██║██║███████╗╚█████╔╝███████╗██████╔╝
╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝╚══════╝░╚════╝░╚══════╝╚═════╝░"""

def main():
    print(my+'\n')
    try:
        id_video = input('Введите ссылку на видео: ').replace('https://www.youtube.com/watch?v=', '')
        api_params = {
            'key': 'API_KEY',
            'part': 'snippet',
            'videoId': id_video,
            'maxResults': 100,
        }

        results = get_comments(api_params)
        fileComment = open('comments.txt', "w", encoding="utf-8")
        for item in results['items']:
            comments = item['snippet']['topLevelComment']['snippet']['textOriginal']
            fileComment.write(comments + '\n')
        input("Press enter to close program")
    except Exception as e:
        print(e)
        print('Что-то пошло не так!')
        input("Press enter to close program")


def get_comments(api_params):
    api_endpoint = 'https://www.googleapis.com/youtube/v3/commentThreads'
    encoded_params = urlencode(api_params)

    with urlopen(f'{api_endpoint}?{encoded_params}') as response:
        return json.load(response)


if __name__ == "__main__":
    main()
