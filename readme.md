## Description
Flask-based backend search/chat pkg integrated with openai chat and openai embedding


## Run docker-compose to start app locally
Before starting the app, an OPENAI API account is required. (set up an account on [openai.com](https://openai.com), and find you keys in [here](https://platform.openai.com/account/api-keys)) 

Copy your key in the `.env` file for `OPENAI_API_KEY`

```
docker-compose up --build
```