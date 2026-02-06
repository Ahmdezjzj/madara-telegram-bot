import requests

class MadaraUploader:
    def __init__(self, site, user, password):
        self.site = site
        self.auth = (user, password)

    def upload_manga(self, url):
        # هنا لاحقًا نربط سكربر المواقع
        title = "اسم المانهوا تجريبي"
        chapters = 10

        return {
            "title": title,
            "chapters": chapters,
            "link": self.site
        }
