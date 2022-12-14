import os
import time

from flask import Flask

app = Flask(__name__)
DEPLOY_TIME = time.time()

@app.route('/redeploy')
def index():
        global DEPLOY_TIME
        current_time = time.time()
        if current_time - DEPLOY_TIME > 300:
            DEPLOY_TIME = current_time
            msg = os.popen('bash /root/deploy.sh').read()
            return msg
        else:
            return "The application was deployed recently, please try again after 5 minutes"

app.run(host='0.0.0.0', port=8001)
