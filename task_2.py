# -*- coding: utf-8 -*-

import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload?path={file_path}'.format(file_path=file_path.split("\\")[-1])
        header = {'Authorization': f'OAuth {self.token}'}
        response = requests.get(url, headers=header).json()

        with open(file_path, 'rb') as file:
            try:
                requests.put(response['href'], files={'file':file})
            except KeyError:
                print(response)


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'F:\\development\\netology\\homework_learn_requests\\task_1.py'
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
