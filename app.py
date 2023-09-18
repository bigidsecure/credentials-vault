from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/manifest', methods=['GET'])
def manifest():
    # Send our app's metadata to BigID
    manifest = {
    "app_name": "Vault App",
    "description": "This application provides data souce credentials from a user defined app",
    "category": "utility",
    "license_type":"FREE",
    "vendor": "BigID",
    "is_interactive": False,
    "actions": [{"action_id": "vault","description": "The action provides data source credentials for a vault","is_sync":True,"action_params": []}],
    "global_params": []
    }
    return jsonify(manifest)

@app.route('/execute', methods=['POST'])
def vault():
    # Initalize the request body and response user/pass
    data = request.get_json()
    username = False
    password = False
    # If the request is invalid, we kill it.
    if(data['actionName'] != "vault"):
        return jsonify({"statusEnum": "ERROR","progress": 0, "message": "NO SUCH ACTION"})
    query = data['actionParams'][0]['paramValue']
    print(query)
    # Peform whatever actions to get information from the vault here
    # This sample just expects the query to be set to "test"
    if(query == "test"):
        username = "user"
        password = "password"
    # If no user was found send error back to BigID
    if(username == False):
        return jsonify({"statusEnum": "ERROR","progress": 0, "message": "NO SUCH USER"})
    
    return jsonify({"executionId": data['executionId'], "statusEnum": "COMPLETED", "progress": 1,"message": "User found", "additionalData": {"username": username,"password": password}})

if __name__ == '__main__': 
   app.run(host="0.0.0.0",port=3000)