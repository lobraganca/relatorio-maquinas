# Publica o firestore.rules no projeto relatorio-maquinas.
# Feito para o Cloud Shell do Google, onde a pessoa já está logada: abra o
# link "Open in Cloud Shell" do README e digite  python3 regra.py
#
# Existe porque colar texto na caixa de regras do console, pelo celular, não
# deu certo. Aqui não se cola nada.
import json, os, subprocess, urllib.request

P = "relatorio-maquinas"
pasta = os.path.dirname(os.path.abspath(__file__))
regra = open(os.path.join(pasta, "firestore.rules"), encoding="utf-8").read()
token = subprocess.check_output(["gcloud", "auth", "print-access-token"]).decode().strip()

def chama(metodo, url, corpo):
    r = urllib.request.Request(url, data=json.dumps(corpo).encode(), method=metodo, headers={
        "Authorization": "Bearer " + token, "Content-Type": "application/json", "x-goog-user-project": P})
    return json.load(urllib.request.urlopen(r))

base = "https://firebaserules.googleapis.com/v1/projects/" + P
try:
    rs = chama("POST", base + "/rulesets", {"source": {"files": [{"name": "firestore.rules", "content": regra}]}})["name"]
    release = {"name": "projects/" + P + "/releases/cloud.firestore", "rulesetName": rs}
    try:
        chama("PATCH", base + "/releases/cloud.firestore", {"release": release})
    except urllib.error.HTTPError:
        chama("POST", base + "/releases", release)
    print("\n  PRONTO - regra publicada. Pode voltar para o Claude.\n")
except urllib.error.HTTPError as e:
    print("\n  AINDA FALTA - mande um print desta tela.\n", e.code, e.read().decode()[:400])
