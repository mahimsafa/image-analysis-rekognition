# Simple image recognition with Amazon Rekognition

![Application Home](/SS/app-demo.gif)

# Prerequisites

Make sure you have configured the environment variables for AWS. 
Learn more: [https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-envvars.html#envvars-set](https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-envvars.html#envvars-set)

# Run the app:

- Clone the repo
- Install the dependencies
`pip install -r requirements.txt`
- Run the app.
`python main.py`
- Visit the app on [http://localhost:5000](http://localhost:5000)

# Run with docker

- Clone the repo
- Build the docker image
`docker buildx build -t image-rekognition .`
- Run the container
`docker run --rm -p 5000:5000 image-rekognition`
- Visit the app on [http://localhost:5000](http://localhost:5000)

# Deploy 

You can use the Dockerfile.lambda to deploy the app on AWS Lambda