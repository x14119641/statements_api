## A POST endpoint using flask
Shows data from database as a json response
if correct username and passwor are posted
as json to "localhost:5000/read"

# Install app or requirements.txt
```
python setup.py install
pip install -r "requirements.txt"
```

# Using dockerfile
```
docker build -t statements_api .
docker run -p 5000:5000 statements_api```

# Using docker-compose
```docker-compose up --build```

# To do the POST 
```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"username":"user","password":"user"}' \
  http://localhost:500/read
```

