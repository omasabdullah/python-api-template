Python API Template
===

Use this template as a way of creating your own Python API

### Prerequisites
1. This uses docker-compose to run the API
2. Specify any environments in a .env file and it will be loaded into the container


### Running
#### Generate symmetric keys
You will need to generate a new RSA, use the following command:

`ssh-keygen -t rsa -b 4096`

This will generate a public and private key. The following environment variables should be set with the values:

```
JWT_PUBLIC_KEY - public key
JWT_PRIVATE_KEY - private key
```

#### Starting the server
Start the server with docker compose

`$ docker-compose up`

### Testing
Run tests using

`$ pytest`
