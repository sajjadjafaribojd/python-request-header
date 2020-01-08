from flask import Flask,request,jsonify

app=Flask(__name__)

def error_result(status,message):
    results={}
    results["error"]={}
    results["error"]["status"]=status
    results["error"]['message']=message
    return jsonify(results)

@app.route('/api/v1/getdomain',methods=['GET'])
def getdomain():
    try:
       	if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        	ip = request.environ['REMOTE_ADDR']
        else:
        	ip = request.environ['HTTP_X_FORWARDED_FOR']
        domain = request.values["domain"]
        ouput= {"domain":domain,"Result":"from app1.py",'remote_addr':request.remote_addr,"X-forward":ip,"sajjad header":request.headers.get('X-Sajjd-For'),"X-Jafari":request.headers.get('X-Jafari-For')}
        return jsonify(ouput)
    except Exception as e:
        return error_result("fail","insert error%s"%e)


if __name__ == '__main__':
   #app.run(debug = True) #defualt port: 5000
   app.run(debug=True,host="0.0.0.0",port=2020)





