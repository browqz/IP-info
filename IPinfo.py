import requests

def get_location(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"

    response = requests.get(url)
    data = response.json()

    if data["status"] == "fail":
        return None  # Impossible de localiser l'adresse IP

    Pays = data["country"]
    Ville = data["city"]
    region = data["regionName"]
    isp = data["isp"]

    location = f"IP: {ip_address}\nPays: {Pays}\nVille: {Ville}\nRegion: {region}\nOperateur: {isp}"
    return location

ip_address = input("Entrez l'addresse IP de votre victime : ")
location = get_location(ip_address)

if location:
    print("Informations sur l'adresse IP de la victime :")
    print(location)
else:
    print("Nous n'avons pas pu localiser l'adresse ip de la victime.")