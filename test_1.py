import io , os
from google.cloud import vision_v1
from google.cloud.vision_v1 import types
import pandas as pd

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"propane-ripsaw-333014-81fef2c94b57.json"

client = vision_v1.ImageAnnotatorClient()
'''
def detectText(img):
    with io.open(img , 'rb') as image_file:
        content = image_file.read()

    image = vision_v1.types.Image(content=content)
    response = client.text_detection(image=image)
    textsssss =  response.text_annotations

    df = pd.DataFrame(columns=['locale', 'description'])
    for text in textsssss:
        df = df.append(
            dict(        
                locale=text.locale,
                description=text.description
            ),
            ignore_index=True
        )
    return df


FILE_NAME = 'sample3.jpg'
FOLDER_PATH = r'D:/Coding/Python/vision_api/env/Image/Text'
print(detectText(os.path.join(FOLDER_PATH, FILE_NAME)))
'''

img_url = 'http://digitalnativestudios.com/textmeshpro/docs/rich-text/line-indent.png'
image = vision_v1.types.Image()
image.source.image_uri = img_url
response = client.text_detection(image=image)
textsssss =  response.text_annotations
df = pd.DataFrame(columns=['locale', 'description'])
for text in textsssss:
    df = df.append(
        dict(        
            locale=text.locale,
            description=text.description
        ),
        ignore_index=True
    )
