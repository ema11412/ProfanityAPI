from analisis import *
from storage import *
from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/', methods=['GET'])
def ping():
    return jsonify({"response": "Active"})



#GET method:
# Get the orders by users id
@app.route('/analyze/<string:name>', methods=['GET'])
def analyze(name):
    print(name)
    try:
        nombre = str(name)
        run_storage(nombre)
        if nombre[-1] == "f":
            print(nombre)
            b_w, t_w = fullAnalisisPdf(nombre)
        elif nombre[-1] == "x":
            b_w, t_w = fullAnalisisDocx(nombre) 
        elif nombre[-1] == "t":
            b_w, t_w = fullAnalisisTxt(nombre)
          
        p_total = b_w/t_w*100
        run_storage(nombre,0)
        return str(p_total)        

    except Exception as e:
        print(e)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)






