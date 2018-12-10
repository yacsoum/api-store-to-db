@@ -12,7 +12,7 @@ def get_bracelet_id(api_bracelet):
 def get_bracelet_footstep(api_bracelet, collection):
    threading.Timer(3600, get_bracelet_footstep, [collection]).start()
    threading.Timer(3600, get_bracelet_footstep, [api_bracelet, collection]).start()
     bracelet_id = get_bracelet_id(api_bracelet)
    response = requests.get('http://{}/footstep/'.format(api_bracelet) + bracelet_id)
@@ -22,7 +22,7 @@ def get_bracelet_footstep(api_bracelet, collection):
 def get_bracelet_heartbeat(api_bracelet, collection):
    threading.Timer(10, get_bracelet_heartbeat, [collection]).start()
    threading.Timer(10, get_bracelet_heartbeat, [api_bracelet, collection]).start()
     bracelet_id = get_bracelet_id(api_bracelet)
    response = requests.get('http://{}/heartbeat/'.format(api_bracelet) + bracelet_id)