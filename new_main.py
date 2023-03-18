import requests


# Задание №1

def super_heroes(lst_super_heroes: list):
    url = requests.get("https://akabab.github.io/superhero-api/api/all.json")
    super_url = url.json()
    list_heroes = sorted([[i["powerstats"]["intelligence"], i["name"]]
                          for i in super_url
                          if lst_super_heroes.count(i["name"])])
    print(f"Самый умный герой: {list_heroes[-1][1]} ")
    return


super_heroes(["Hulk", "Captain America", "Thanos"])


# Задание №2

class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.file_url = "https://cloud-api.yandex.net/v1/disk"

    def upload(self):
        return {
            "Content-Type": "application/json",
            "Authorization": f"OAuth {self.token}"
        }

    def get_upl_link(self, disc_name_p):
        headers = self.upload()
        params = {'path': f'disk:/{disc_name_p}'}
        response = requests.get(f"{self.file_url}, /resources/upload", headers=headers, params=params)

        return response.json()

    def file_to_disc(self, filename):
        if "/" not in filename:
            href = self.get_upl_link(filename)["href"]
        else:
            disc_name = filename[filename.rfind('/') + 1:]
            href = self.get_upl_link(disc_name)['href']
        with open(filename, "rb") as f:
            response = requests.put(href, data=f)

        if response.status_code == 201:
            print(f"Загружен {filename}")


if __name__ == '__main__':
    path_to_file = r"C:\Users\19ala\PycharmProjects\Project1\qqq.jpg"
    token = "...."
    uploader = YaUploader(token)
    result = uploader.get_upl_link(path_to_file)
