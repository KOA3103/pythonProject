import requests
from my_token import token
from pprint import pprint
from pathlib import Path

"""
Работа с библиотекой requests, http-запросы.
Программа, которая принимает на вход путь до файла на компьютере
и сохраняет на Яндекс.Диск с таким же именем.
"""
class YaUploader:
    URL_FILES_LIST: str = 'https://cloud-api.yandex.net/v1/disk/resources/files'
    URL_FILES_RESOURCES: str = 'https://cloud-api.yandex.net/v1/disk/resources'
    URL_UPLOAD_LINK: str = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
    header = {"Content-Type": "application/json", "Authorization": f"OAuth {token}"}

    def __init__(self, token: str):
        self.token = token

    def get_flat_list_of_all_files(self):
        response = requests.get(self.URL_FILES_LIST, headers=self.header)
        json_info = response.json().get("items")
        pprint(json_info)
        return

    def _get_upload_link(self, ya_disk_path: str = "new"):  # Думал что тут можно выбрать куда загружать файлы.
        params = {"path": ya_disk_path, "overwrite": "true"}
        response = requests.get(self.URL_UPLOAD_LINK, headers=self.header, params=params)
        upload_url = response.json().get("href")
        return upload_url

    def upload(self, file_path: str):

        """Метод загружает файлы по списку file_list на яндекс диск"""

        list_files = list(Path(file_path).glob("*.*"))  # тут можно выбрать какие файлы загружать.
        for i in list_files:
            file_name = str(i).split('\\')
            # Запрос URL для загрузки.
            upload_link = self._get_upload_link(file_name[-1])
            with open(i, 'rb') as file_obj:
                # Загрузка файла на полученный URL
                response = requests.put(upload_link, data=file_obj)
                if response.status_code == 201:
                    print(f"Файл <{file_name[-1]}>\n  из <{file_path}> \n   загружен на Яндекс.Диск.\n")
        return

    def create_folder_into_YaDisk(self, ya_disk_path):
        create_folder = requests.put(self.URL_FILES_RESOURCES, headers=self.header, params={"path": ya_disk_path})
        if create_folder.status_code == 201:
            print(f"Папка <{ya_disk_path}> создана! Статус {create_folder.status_code}.")
        else:
            print(f'{create_folder.json().get("message")} Статус {create_folder.status_code}.')
        return

    def delete_file_folder(self, ya_disk_path: str):
        params = {"path": ya_disk_path, "permanently": "true"}
        response = requests.delete(self.URL_FILES_RESOURCES, headers=self.header, params=params)
        if response.status_code == 204 or response.status_code == 202:
            print(f"Успешно удален {ya_disk_path}. Статус {response.status_code}.")
        return


uploader = YaUploader(token)

# Загружает все файлы из папки проекта upload_folder можно выбоать др. указав путь
uploader.upload('upload_folder')

# Создать папку.
# uploader.create_folder_into_YaDisk("new")

# Плоский список всех файлов.
# uploader.get_flat_list_of_all_files()

# Удаляет файл.
# uploader.delete_file_folder('1.txt')
