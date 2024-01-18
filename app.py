from flask import Flask ,jsonify,render_template,request
from bs4 import BeautifulSoup
import requests

app=Flask(__name__)
@app.route('/')
def hello_world():
    return "hello world"
@app.route('/find',methods=['POST','GET'])
def find():
    if request.method=="POST":
        data=request.get_json
        url=data['url']
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        answer=""
        para=soup.find_all('p')
        for i in  para:
            answer +=i.text 
        return answer





if __name__== '__main__':
    app.run(debug=True)