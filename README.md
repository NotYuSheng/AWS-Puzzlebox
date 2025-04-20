# AWS-PuzzleBox: FastAPI CTF

Puzzle Box is a lightweight FastAPI app where users upload `.txt` files to search for a secret **code word** hidden inside. If the word is found, users can submit their guess and unlock a final **completion word** as proof of success.

## Live Demo

> [!IMPORTANT]
> The AWS instances have been disabled.

The app is publicly available for a limited time:

~~**[http://52.63.142.42:8000/docs](http://52.63.142.42:8000/docs)**~~

Explore the interactive API docs and play along!

## Project Purpose
This project serves as a learning journey for AWS, designed to explore how containerized applications (like FastAPI) can be deployed and integrated with core AWS services such as ECS Fargate, S3, IAM, and more.

The goal is to progressively build an understanding of how modern cloud-native apps can be deployed, managed, and scaled within the AWS ecosystem — starting from simple Docker apps all the way to production-grade cloud architectures.

## AWS Services Checklist

- [x]	ECR
- [x]	EC2
- [x]	ECS + Fargate
- [x] CloudWatch
- [ ]	S3
- [ ]	CodeBuild
- [ ]	Lambda

## Docker Image on Amazon ECR Public Gallery

You can find the latest public image for this app on Amazon ECR here:

[📁 View on ECR Public Gallery](https://gallery.ecr.aws/m0n2s0x1/puzzlebox-dev/puzzlebox)

To pull the image directly:
```bash
docker pull public.ecr.aws/m0n2s0x1/puzzlebox-dev/puzzlebox:latest
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.
