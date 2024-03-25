# TwitterTron

A automated twitter persona agent powered by GenAI who tweets twice a day.

## Requirements to run the project
* [Twitter API](https://developer.twitter.com/en/docs/twitter-api)
* [Gemini API](https://ai.google.dev/)


## Running up the project
* Fork the repository
* Setup the environment secrets for github action.

### Adding environment secrets for github action
1. Go to the settings section of you forked repository.
2. Navigate to Secrets and variable on the left bar and click Actions.
3. Add the following environment with exact name.
    - For accessing twitter account to tweets 
        * ACCESS_TOKEN
        * ACCESS_TOKEN_SECRET
        * AUTHENTICATION_BEARER_TOKEN
        * CONSUMER_KEY
        * CONSUMER_SECRET

    - For LLM agent to decide what to tweet (you can configure it in [prompt.py](https://github.com/Mohwit/TwitterTron/blob/main/prompt.py) file)
        * GOOGLE_API_KEY

    ![Secret Variables](/assets/secret_variables.png)

    For more info on how to access secret panel, read the [docs](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/managing-development-environment-secrets-for-your-repository-or-organization#adding-secrets-for-a-repository)


## Local Setup
1. Clone the repository
`
git clone  https://github.com/Mohwit/TwitterTron.git
`

2. After cloning the repository, install the required packages using the following command:

`
pip install -r requirements.txt
`

3. Create a .env file and add you secret varibles there with following name:
    * ACCESS_TOKEN = XXX
    * ACCESS_TOKEN_SECRET = XXX
    * AUTHENTICATION_BEARER_TOKEN = XXX
    * CONSUMER_KEY = XXX
    * CONSUMER_SECRET = XXX
    * GOOGLE_API_KEY = XXX

4. Run the main.py file with the command
`
python main.py
`

**Note**: It will tweet each time you will run the main.py file.