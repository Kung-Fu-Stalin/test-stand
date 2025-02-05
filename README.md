# Student Testing Stand

## Description
This project is a test stand designed for students to practice debugging and error handling. The system intentionally contains multiple bugs, and the main goal is to identify as many cases as possible that trigger a **500 Internal Server Error** on the server.

## Objective

Explore the application and find scenarios that cause server failures.
Analyze error logs and debug issues.
Improve problem-solving skills in a real-world environment.

## How to install

For the server launch I recommend you to use docker.

1. Build the docker image:
```bash
docker build . --name test-stand
``` 
2. Launch docker image:
```bash 
docker run --rm -d -p 8080:8080 --name test-stand 
```
3. Perform tests 

If you wanna stop the cointainer:

1. Stop container command is: 

```bash 
docker ps -a -q --filter="name=test-stand"
```

You are perfect!!!

## Notes

The system is intentionally unstable.
Use different input variations and actions to trigger errors.
Document your findings and suggest fixes.

Happy debugging! 🚀
