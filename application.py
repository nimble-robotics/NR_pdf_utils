from flask import Flask,request,render_template
# from utils import upload_to_aws,bucket_name
import os
from healathcheck import Healathcheck


application = app = Flask(__name__,template_folder='templates')

App_path = os.path.dirname(os.path.abspath(__file__))
@app.route('/home')
def home():
    return render_template('index.html')


health = Healathcheck(app,"/healthcheck")
health.add_check(app_status)


def app_status():
    """
    added health check
    """
    return True,"App is up and running"
if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port= 5000 )