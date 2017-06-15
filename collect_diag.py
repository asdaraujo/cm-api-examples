# Generate and download diag bundle

import requests
from requests.auth import HTTPBasicAuth
from cm_api.api_client import ApiResource
from datetime import datetime

bundle_filename = 'bundle.zip'
bundle_size_bytes = 10 * 1024 *1024
cm_host = 'cm-host.example.com'
cm_port = 7180
use_tls = False
cm_user = 'admin'
cm_pwd = 'admin'

a = ApiResource(cm_host, cm_port, cm_user, cm_pwd, use_tls=use_tls)
cm = a.get_cloudera_manager()
cmd = cm.collect_diagnostic_data_45(datetime.now(), bundle_size_bytes).wait()

r = requests.get(cmd.resultDataUrl, auth=HTTPBasicAuth(cm_user, cm_pwd))
f = open(bundle_filename, 'w')
f.write(r.content)
f.close()

