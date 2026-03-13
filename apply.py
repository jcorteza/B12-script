from os import getenv
from datetime import datetime, timezone
from json import dumps
import hmac
from requests import post

try:
    run_id = getenv("GITHUB_RUN_ID")
    data = dumps({
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "name": "Josephine Cortez-Ayala",
        "email": "josephinecrtza@gmail.com",
        "resume_link": "https://drive.google.com/file/d/1N6mQjr7ygASCrF6X2aaMJXT1REwQexAP/view?usp=sharing",
        "repository_link": "https://github.com/jcorteza/B12-script",
        "action_run_link": f"https://github.com/jcorteza/B12-script/actions/runs/{'whoops' if run_id is None else run_id }"
    }, sort_keys=True, separators=(',', ':'))
    hex_digest = hmac.new(
        "hello-there-from-b12".encode("utf-8"),
        data.encode("utf-8"),
        "sha256").hexdigest()
    headers = {
        "X-Signature-256": f"sha256={hex_digest}",
        "Content-Type": "application/json"
    }
    response = post("https://b12.io/apply/submission", data=data, headers=headers)
    print(response.json()["receipt"])

except:
    print("Failed to submit the B12 application")