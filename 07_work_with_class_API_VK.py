import requests
from pathlib import Path
from urllib.parse import urlencode
from my_token import TOKEN_VK, user_id_VK, token_y
from pprint import pprint

"""Работа с классами на примере API VK"""

# list_of_photos = []


class VK:

    def __init__(self, access_token, user_id_VK, version='5.131'):
        self.token = access_token
        self.id = user_id_VK
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}

    def get_photos_info(self):
        url = "https://api.vk.com/method/photos.get"
        params = {
            "access_token": self.token,
            "v": "5.131",
            "album_id": "profile",
            "extended": 1,
        }
        response = requests.get(url, params=params)
        response_json = response.json()["response"]["items"]
        list_of_links_avatar_photo = list()
        for photo in response_json:
            sorted(photo)
            list_of_sizes_avatar_photo = list()
            for sizes in photo['sizes']:
                list_of_sizes_avatar_photo.append(
                    (photo['likes']['count'], photo['date'], sizes["width"], sizes["type"], sizes["url"]))
            list_of_sizes_avatar_photo = sorted(list_of_sizes_avatar_photo, key=lambda type: type[2])
            list_of_links_avatar_photo.append(list_of_sizes_avatar_photo[-1])
        # Naming of files by attaching extention JPG to Like or Date.
        list_of_photos = []
        # Поиск повторяющихся элементов в списке (множестве) по индексу во всех списках (множествах).
        for item in list_of_links_avatar_photo:
            a = item[0]  # Выбор искомого индекса.
            # Checking name for repeating.
            list_of_photo = []
            counter = 0
            for i in list_of_links_avatar_photo:
                if i[0] == a:
                    counter += 1
            if counter == 1:
                # Name is not repeated, it's naming by quantities of Likes.
                list_of_photo.append(str(item[0]) + ".jpg")
                list_of_photo.append(item[1])
                list_of_photo.append(item[2])
                list_of_photo.append(item[3])
                list_of_photo.append(item[4])
                list_of_photos.append(list_of_photo)
            else:  # Name is repeated, it's naming by Date.
                list_of_photo.append(item[0])
                list_of_photo.append(str(item[1]) + ".jpg")
                list_of_photo.append(item[2])
                list_of_photo.append(item[3])
                list_of_photo.append(item[4])
                list_of_photos.append(list_of_photo)
        return list_of_photos


class YaUploader:
    URL_FILES_LIST: str = 'https://cloud-api.yandex.net/v1/disk/resources/files'
    URL_FILES_RESOURCES: str = 'https://cloud-api.yandex.net/v1/disk/resources'
    URL_UPLOAD_LINK: str = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
    header = {"Content-Type": "application/json", "Authorization": f"OAuth {token_y}"}

    # file_path_to_y = ''
    def __init__(self, token: str):
        self.token = token

    def create_folder_into_YaDisk(self):
        """Создание папки. \n path: Путь к создаваемой папке."""
        file_path_to_y = input("Введите название папки куда загрузить файлы: ")
        target_folder = requests.put(f'{self.URL_FILES_RESOURCES}?path={file_path_to_y}', headers=self.header)
        if target_folder.status_code == 201:
            print(f"Папка <{file_path_to_y}> создана! Статус {target_folder.status_code}.")
        else:
            print(f'{target_folder.json().get("message")} Статус {target_folder.status_code}.')
        return file_path_to_y

    # def _get_upload_link(self, file_path_to_y: str = "new"):  # Tут можно выбрать куда загружать файлы.
    #     params = {"path": file_path_to_y, "overwrite": "true"}
    #     response = requests.get(self.URL_UPLOAD_LINK, headers=self.header, params=params)
    #     upload_url = response.json().get("href")
    #     return upload_url

    def upload(self, savefile, replace=False):

        """Метод загружает файлы по списку file_list на яндекс диск"""
        # sourse_url = "https://cloud-api.yandex.net/v1/disk/resources/upload?path=%2F1%2F&url=https%3A%2F%2Fsun9-70.userapi.com%2Fimpf%2FtrrtxJzEDNIpfLsrO8aBDeIRBR6Bg8J10LOKmQ%2FwrNSyGe3TKU.jpg%3Fsize%3D506x479%26quality%3D96%26sign%3D6e3cfb78fa04ce181be9a465676b349d%26c_uniq_tag%3DBnWamsQDEcoeNNLS-EkVCMjQHNqA5q1Zwi1k8-llbMc%26type%3Dalbum&disable_redirects=false"

        for i in vk.get_photos_info():
            file_name = str(i[0])
            file_name_with_path = (f'{self.create_folder_into_YaDisk()}/{file_name}')
            # Запрос URL для загрузки.
            # upload_link = self._get_upload_link()
            res = requests.get(f'{self.URL_FILES_RESOURCES}/{file_name_with_path}?path={savefile}&overwrite={replace}', headers=self.header).json()
            with open(i[-1], 'rb') as file_obj:
                try:
                    # Загрузка файла на полученный URL
                    response = requests.put(res['href'], data=file_obj)
                    if response.status_code == 201:
                        print(f"Файл <{file_name}>\n  загружен на Яндекс.Диск.\n")
                except KeyError:
                    print(res)



# Инициализация токенов.
vk = VK(TOKEN_VK, user_id_VK)
y_uploader = YaUploader(token_y)

# Получаем список [(Likes, Date, Type, URL), (....), (....)].
# pprint(vk.get_photos_info())

# Создаёт папку на Яндекс.Диске.
# y_uploader.create_folder_into_YaDisk()  # Путь (название папки) указываем в кавычках.

# Загружает все файлы из папки проекта upload_folder можно выбоать др. указав путь.
# y_uploader.upload('upload_folder')


y_uploader.upload("4.jpg")
