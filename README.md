
# Create your own ChatGPT App in seconds.

URL : [mygpt-client.vercel.app](https://mygpt-client.vercel.app/)

Everyone should have the ability to create custome chatbots that can solve our pwn problems. I am creating this AI platform so that Everyone can create powerfull OpenAI powered custome chatbots that will help Everyone to solve their unique problems.

![alt text](https://redshop.s3.ap-south-1.amazonaws.com/dash.png)


## Installation

I separetd Api and Frontend independently. Frontend for this project will be available
[here](https://github.com/shahriarsohan/mygpt-client)

To install the backend
```bash
  git clone https://github.com/shahriarsohan/mygpt-api
  cd mygpt-api
  pip install -r requirements.txt
  python manage.py migrate
  python manage.py runserver
```

Then go to [http://127.0.0.1:8000](http://127.0.0.1:8000) . You are DONE!
    
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SECRET_KEY`

`MYDB_NAME`

`MY_DB_USER`

`MY_DB_PASSWORD`

`MY_DB_HOST`

`MY_DB_PORT`


## License

[MIT](https://choosealicense.com/licenses/mit/)

