from asyncio.windows_events import NULL
from flask import Flask, render_template, url_for, request,Response,json
app = Flask(__name__)
import hostdetection
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/os-informations')
def osInfo():
    return "os informations"

@app.route('/host-detection', methods=['GET','POST']) 
#def active_hosts():
 #   pool = request.args['pool']
  #  return Response(json.dumps({'active hosts': hostdetection.activeHosts(pool)}))

def host():
    resp=""
    domain=NULL
    if request.method=='POST':    
        domain=request.form.get('domain')
        resp=json.dumps({'active hosts': hostdetection.activeHosts(domain)})

    
    return render_template("host.html",resp=resp)





    



@app.route('/firewalls')
def firewallDetails():
    return "hello firewalls details"



if __name__=="__main__":
    app.run(debug=True)
    