from flask import Flask
from flask import request

# from heapq import nlargest
# from heapq import nsmallest

app = Flask(__name__)
# global identifier


@app.route("/")
def index():
    return "Python Microservice To fetch sentiment score"

@app.route("/sum",methods=["POST"])
def sum(num1,num2):
    sum = int(num1) + int(num2)
    
# Display the sum
    print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

    return sum
    
        
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
    # sentiment_anlysis()


