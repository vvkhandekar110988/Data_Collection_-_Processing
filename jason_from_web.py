import urllib.request, json
with urllib.request.urlopen("https://kjsieit.somaiya.edu/en") as url:
    data = json.loads(url.read().decode())
    print(type(data))