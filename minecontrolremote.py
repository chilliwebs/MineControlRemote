import re
import logging
from mctools import RCONClient
from flask import Flask, abort, request, Response

app = Flask(__name__)
logging.basicConfig(filename='minecontrolremote.log', level=logging.DEBUG, format=f'%(asctime)s %(message)s')
logging.getLogger('werkzeug').setLevel(logging.WARNING)

def escape_ansi(line):
    ansi_escape = re.compile(r'(?:\x1B[@-_]|[\x80-\x9F])[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', line)

@app.route("/log", methods=['OPTIONS'])
def optslog():
    resp = Response("OK")
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route("/log", methods=['GET'])
def getlog():
    msg = request.args.get('msg')
    app.logger.info(msg)
    print(msg)
    resp = Response("OK")
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route("/rcon", methods=['OPTIONS'])
def optsrcon():
    resp = Response("OK")
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route("/rcon", methods=['GET'])
def getrcon():
    command = request.args.get('cmd')
    host = request.args.get('host')
    port = request.args.get('port')
    pazz = request.args.get('pass')
    if command != "list":
        app.logger.info('-=rcon request=-')
        print('-=rcon request=-')
    try:
        rcon = RCONClient(host, port)
        if rcon.login(pazz):
            cmdresp = ""
            try:
                for cmd in command.splitlines():
                    if cmd != "list":
                        app.logger.info(' cmd: %s' % cmd)
                        print(' cmd: %s' % cmd)
                    resp = escape_ansi(rcon.command(cmd, length_check=False))
                    cmdresp += resp + "\n"
                    if cmd != "list":
                        app.logger.info('resp: %s' % resp)
                        print('resp: %s' % resp)
                resp = Response(cmdresp)
                resp.headers['Access-Control-Allow-Origin'] = '*'
                return resp
            except Exception as e:
                app.logger.error(e)
                print(e)
                abort(500)
    except Exception as e:
        app.logger.error(e)
        print(e)
        abort(504)
    abort(500)

@app.errorhandler(500)
def server_error(e):
    # note that we set the 404 status explicitly
    resp = Response("SERVER ERROR", 500)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.errorhandler(504)
def server_error(e):
    # note that we set the 404 status explicitly
    resp = Response("GATEWAY TIMEOUT", 504)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3210)
