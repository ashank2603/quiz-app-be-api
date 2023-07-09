# QUIZ Backend REST API
The deployed version of the api can be accessed [here]()
## How to run:
- Clone the repository and open the directory in a terminal.
- Create a virtual environment using [virtualenv](https://virtualenv.pypa.io/en/latest/) library. Run `virtualenv venv` in the terminal.
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