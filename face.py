import requests
import pygame
import pygame.camera

class Face:
    def __init__(self):
        self.happiness = 0
        self.sadness = 0

    def getPhoto(self):
        pygame.camera.init()
        cam = pygame.camera.Camera("/dev/video0",(640,480))
        cam.start()
        img = cam.get_image()
        pygame.image.save(img,"images/emo.jpg")
        cam.stop()

    def getEmo(self, key, url):
        subscription_key = key
        assert subscription_key
        face_api_url = url

        self.getPhoto()
        image_path = 'images/emo.jpg'
        image_data = open(image_path, "rb").read()

        headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
        params = {
            'returnFaceId': 'false',
            'returnFaceLandmarks': 'false',
            'returnFaceAttributes': 'emotion'
        }
        response = requests.post(face_api_url, params=params, headers=headers, data=image_data)

        faces = response.json()

        self.happiness = faces[0]['faceAttributes']['emotion']['happiness']
        self.sadness = faces[0]['faceAttributes']['emotion']['sadness']
        #print(self.happiness)
        #print(self.sadness)

        return self.happiness, self.sadness
