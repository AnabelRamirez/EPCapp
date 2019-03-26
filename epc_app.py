from flask import Flask, render_template, request, jsonify
import plotly.graph_objs as go
from plotly.utils import PlotlyJSONEncoder
import plotly.plotly as py
import json
import requests
from pprint import pprint
import requests_cache
from cassandra.cluster import Cluster
import datetime


cluster= Cluster(['cassandra'])
session=cluster.connect()
app = Flask(__name__,instance_relative_config=True)
app.config.from_object('epcconfig')
app.config.from_pyfile('epcconfig.py')

postcode_url_template='https://epc.opendatacommunities.org/api/v1/domestic/search?postcode={post}'
address_url_template='https://epc.opendatacommunities.org/api/v1/domestic/search?address={add}'

@app.route( '/epcchart/<postcode>/' , methods=[ 'GET' ])
def epcchart(postcode):
    #get time stamp:
    time=datetime.datetime.now()
    #store request in the cassandra database:
    rows=session.execute("""Insert into epc.requests(timestamp,postcode,address) values ({},{},'')""".format(time,postcode))
    epc_url = postcode_url_template.format(post=postcode)
    Auth=app.config['BASIC_AUTH']
    #header={'Accept':'text/csv', 'Authorization': 'Basic %s' %Auth}
    header={'Accept':'application/json', 'Authorization': 'Basic %s' %Auth}
    resp = requests.get(epc_url,headers=header)
    #print(resp.status_code,resp.headers,resp.request.headers)

    if resp.ok:
        resp = requests.get(epc_url,headers=header)
        epc=resp.json()
        #pprint(epc)
    else:
        print(resp.reason)

    rows=json.dumps(epc['rows'])
    columns_load=json.dumps(epc['column-names'])
    columns=columns_load.split(", ")
    columns_cleaned=[]
    values=[]
    chars=['"',"[","]"]
    for i in range(len(columns)):
        for j in chars:
            columns[i]=columns[i].replace(j,"")
        columns_cleaned.append(columns[i])
    hola2=rows.split(', ')
    for i in range(len(hola2)):
        hola3=hola2[i].split(": ")
        if hola3[0].find('current-energy-efficiency')==True:
            n=int(hola3[1].replace('"',""))
            values.append(n)
    print(values)

    graphs = [
            dict(
                data=[go.Bar(
                    #x=['current-energy-efficiency'],
                    y=values
                    )],
                    layout=dict(
                        title='Current Energy Efficiency in {}'.format(postcode)
                )
                )
                ]

    ids = ['graph-{}'.format(i) for i, _ in enumerate(graphs)]

    graphJSON = json.dumps(graphs, cls=PlotlyJSONEncoder)
    return render_template('plotholder.html',ids=ids,graphJSON=graphJSON)

@app.route('/epc/postcode/<postcode>/', methods=['GET'])
def epc(postcode):
    #get time stamp:
    time=datetime.datetime.now()
    #store request in the cassandra database:
    rows=session.execute("""Insert into epc.requests(timestamp,postcode,address) values ({},{},'')""".format(time,postcode))
    response={postcode:'Not Found!'}
    epc_url = postcode_url_template.format(post=postcode)
    Auth=app.config['BASIC_AUTH']
    #header={'Accept':'text/csv', 'Authorization': 'Basic %s' %Auth}
    header={'Accept':'application/json', 'Authorization': 'Basic %s' %Auth}
    resp = requests.get(epc_url,headers=header)

    if resp.ok:
        resp = requests.get(epc_url,headers=header)
        epc=resp.json()
        #pprint(epc)
    else:
        print(resp.reason)
    return jsonify(epc)

@app.route('/epc/address/<address>/', methods=['GET'])
def epc_dwelling(address):
    #get time stamp:
    time=datetime.datetime.now()
    #store request in the cassandra database:
    rows=session.execute("""Insert into epc.requests(timestamp,postcode,address) values ({},'',{})""".format(time,address))
    response={address:'Not Found!'}
    epc_url = address_url_template.format(add=address)
    Auth=app.config['BASIC_AUTH']
    #header={'Accept':'text/csv', 'Authorization': 'Basic %s' %Auth}
    header={'Accept':'application/json', 'Authorization': 'Basic %s' %Auth}
    resp = requests.get(epc_url,headers=header)

    if resp.ok:
        resp = requests.get(epc_url,headers=header)
        epc=resp.json()
        #pprint(epc)
    else:
        print(resp.reason)
    return jsonify(epc)


if __name__=="__main__":
    app.run(port=8080, debug=True)
