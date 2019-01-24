import requests
import pygame
import pygame.camera

subscription_key = '19a47ce8abd540fc9fcc3dfc06c11342'
assert subscription_key
face_api_url = 'https://eastasia.api.cognitive.microsoft.com/face/v1.0/detect'

pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(640,480))
cam.start()
img = cam.get_image()
pygame.image.save(img,"images/emo.jpg")

#image_url = 'https://qph.fs.quoracdn.net/main-qimg-bf9eb4c68e11c75179518a0ab046d325'
#headers = {'Ocp-Apim-Subscription-Key': subscription_key}
image_path = 'images/emo.jpg'
image_data = open(image_path, "rb").read()
headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
params = {
    'returnFaceId': 'false',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'emotion'
}
response = requests.post(face_api_url, params=params, headers=headers, data=image_data)

#face_api_url, params=params, headers=headers, json={"url": image_url})
faces = response.json()

#faces = [{u'faceRectangle': {u'width': 162, u'top': 141, u'height': 162, u'left': 130}, u'faceAttributes': {u'emotion': {u'sadness': 0.0, u'neutral': 0.0, u'contempt': 0.0, u'disgust': 0.0, u'anger': 0.0, u'surprise': 0.803, u'fear': 0.0, u'happiness': 0.196}}}]
happiness = faces[0]['faceAttributes']['emotion']['happiness']
sadness = faces[0]['faceAttributes']['emotion']['sadness']
print(sadness)
print(happiness)
