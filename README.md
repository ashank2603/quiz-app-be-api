# QUIZ Backend REST API
The deployed version of the api can be accessed [here](https://quiz-be-fibr.onrender.com/docs)  
Please access [this](https://evening-firewall-9d5.notion.site/Fibr-Quiz-Task-API-Docs-bbc60c4104c94c189ff337db11425cbb?pvs=4) page to see how to use the API.
## How to run:
- Clone the repository and open the directory in a terminal.
- Create a virtual environment using [virtualenv](https://virtualenv.pypa.io/en/latest/) library. Run `virtualenv venv` in the terminal.
- Create a dotenv file and paste the following in it. Make sure to replace the placeholders with your values. (The HEADER_JWT_KEY value can be fetched from the login endpoint.)

    ```
    DATABASE_URL = "<YOUR_MONGODB_URL>"
    JWT_SECRET_KEY = "<JWT_SECRET_KWY>"
    API_ENDPOINT = "http://127.0.0.1:8000"
    HEADER_JWT_KEY = "<YOUR_HEADER_JWT_KEY>"
    ```  
- To activate the virtual environment:
    - For Windows:  
    `venv\scripts\activate`
    - For Linux:  
    `source venv/bin/activate`
- To run using docker:
    - Install docker from this [link](https://docs.docker.com/engine/install/).
    - Once the virtual environment is activated, run:  
    `docker image build --tag quiz-be-fibr-image .`      
    - The above command will create the image for the project. To run the image in a container, run the following:  
    `docker run -p 8000:80 quiz-be-fibr-image`
- To run without docker:
    - Run the following command in the terminal:  
    `uvicorn main:app`
- The api docs can be accessed at [localhost:8000/docs](http://localhost:8000/docs).
- To execute the tests, run the following command in the terminal:  
    `python -m pytest -v`