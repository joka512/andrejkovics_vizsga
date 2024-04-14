import json

class FileHandler():

    MUNKATARSAK = "munkatarsak.json"
    GEPJARMUVEK = "gepjarmuvek.json"
    ELADASOK = "eladasok.json"

    def load_any(path) -> list:
        with open(path,"r") as f:
            return json.load(f)
    
    
    def save_any(path,data):
        with open(path,"w") as f:
            json.dump(data,f,indent=4)
    
