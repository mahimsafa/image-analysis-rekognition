import json
import boto3
import logging
import requests
from pprint import pprint

# Initialize logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def image_analyzer(image_url):
    result = ''
    rekognition = boto3.client('rekognition')
    try:
        # Fetch the image
        response = requests.get(image_url)
        response.raise_for_status()
        image_bytes = response.content

        # Call Rekognition
        rekognition_response = rekognition.detect_labels(
            Image={'Bytes': image_bytes},
            MaxLabels=30,
            MinConfidence=70
        )

        result = rekognition_response['Labels']
        return result

    except Exception as e:
        logger.error(f'Error processing image {image_url} {str(e)}')
        return None


if __name__ == "__main__":
    image_analyzer('https://en.banglapedia.org/images/1/1e/PaharpurSomapuraMahavihara.jpg?20210617214300')