import requests

def localisation(IP):
    url = f"http://ip-api.com/json/{IP}"

    response = requests.get(url)
    data = response.json()

    if data["status"] == "échec":
        return None 

    Pays = data["country"]
    Ville = data["city"]
    region = data["regionName"]
    isp = data["isp"]

    location = f"IP: {IP}\nPays: {Pays}\nVille: {Ville}\nRegion: {region}\nOperateur: {isp}"
    return location

IP = input("Entrez l'addresse IP de votre victime : ")
location = localisation(IP)

if location:
    print("Informations sur l'adresse IP de la victime :")
    print(location)
else:
    print("Nous n'avons pas pu localiser l'adresse ip de la victime.")
