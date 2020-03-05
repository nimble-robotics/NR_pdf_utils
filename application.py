from flask import Flask,request,render_template
from utils import upload_to_aws,bucket_name
import os
# local_filename = 'error.html'
# s3_filename = 'error.html'
# uploaded = upload_to_aws(local_filename, bucket_name, s3_filename, "text/html")

application = app = Flask(__name__,template_folder='templates')

App_path = os.path.dirname(os.path.abspath(__file__))
@app.route('/home')
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug = True)#, host='0.0.0.0', port= 8000 )