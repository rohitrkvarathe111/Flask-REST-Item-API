from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/armstrong/<int:n>')
def armstrong(n):
    sum = 0
    order = len(str(n))
    copy_n = n
    while(n > 0):
        digit = n % 10
        sum += digit ** order
        n = n // 10

    if sum == copy_n:
        print(f"{copy_n} is an armstrong number")
        result = {
            "Number": copy_n,
            "Armstrong": True,
            "Server IP": "122.234.5",
            "other number": [9,8,7,6,5,4,3,2,1],
            "date time": "01/01/2011"
            
        }
    else:
        print(f"{copy_n} is not an armstrong number")
        result = {
            "Number": copy_n,
            "Armstrong": False,
            "Server IP": "122.234.213.589.5",
            "other number": [1,2,5,7,9,3,8],
            "date time": "29/10/2000"
            
        }

    return jsonify(result)     
    

if __name__ == "__main__":
    app.run(debug=True)
