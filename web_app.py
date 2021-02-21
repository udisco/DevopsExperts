import os
import signal
from flask import Flask
from db_connector import get_user_name_from_db

app = Flask(__name__)


# accessed via <HOST>:<PORT>/users/get_user_data
@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server Stopped'

@app.route("/users/get_user_data/<user_id>")
def get_user_name(user_id):
    user_name = get_user_name_from_db(user_id)
    if user_name is None:
        return "<H1 id='error'>user id does not exist: " + user_id + "</H1>", 500
    else:
        return "<H1 id='user'>" + user_name + "</H1>", 200


app.run(host='127.0.0.1', debug=True, port=5001)
