import requests
def phishtank_check(url, app_key=None):
    data = {'url': url, 'format': 'json'}
    if app_key: data['app_key'] = app_key
    try:
        r = requests.post("https://checkurl.phishtank.com/checkurl/", data=data)
        resp = r.json().get('results', {})
        key = next(iter(resp), None)
        return resp[key]['in_database'] if key else False
    except:
        return False

def virustotal_check(url, api_key):
    headers = {"x-apikey": api_key}
    try:
        r = requests.post("https://www.virustotal.com/api/v3/urls", headers=headers, data={"url": url})
        scan_id = r.json()['data']['id']
        report = requests.get(f"https://www.virustotal.com/api/v3/urls/{scan_id}", headers=headers)
        return report.json()['data']['attributes']['last_analysis_stats']
    except:
        return None

def truecaller_check(phone, api_key):
    headers = {"apikey": api_key}
    try:
        r = requests.get("https://api.apilayer.com/number_verification/validate", headers=headers, params={"number": phone})
        return r.json()
    except:
        return None