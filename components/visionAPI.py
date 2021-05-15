import os, io
from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'deltahacks-306803-01a16b6b0a26.json' 

client = vision.ImageAnnotatorClient()

#path of the image
file_name = os.path.abspath(r'C:\Users\danie\dev\deltahacks\image-test-4.png')

with io.open(file_name,'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

response = client.label_detection(image=image)

labels= response.label_annotations

for  label in labels:
    print(label)

