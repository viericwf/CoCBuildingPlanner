# -*- coding: utf-8 -*-

from flask import Flask, render_template, url_for, make_response, Response, jsonify, request

app = Flask(__name__)


###############################
##         Locations         ##
###############################

@app.route('/')
def show_index():
    return render_template( 'index.tpl' )

@app.route('/buildings/')
@app.route('/buildings')
def show_buildings():
    return render_template( 'buildings.tpl' )

if __name__ == "__main__":
    import getopt, sys

    port = 5000
    app.debug = False

    try:
        opts, args = getopt.getopt(sys.argv[1:],'p:d',['port=', 'debug'])
    except getopt.GetoptError:
        exit(2)

    for opt, arg in opts:
        if opt in ('-p', '--port'): port = int(arg.strip())
        elif opt in ('-d','--debug'): app.debug = True

    app.run(host='0.0.0.0', port=port)






