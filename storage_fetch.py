import base64
import requests
def get_as_base64(url):
    return base64.b64encode(requests.get(url).content)

url="https://firebasestorage.googleapis.com/v0/b/crud-firebase-19085.appspot.com/o/cat_dectect.jpg?alt=media&token=f234d6b9-f4cc-494d-8bbc-c173208c09bf"
fh=open("image_fetch1.jpg","wb")
fh.write(base64.b64decode(get_as_base64(url)))
fh.close
