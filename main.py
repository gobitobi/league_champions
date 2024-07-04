import requests
import json



class ChampionsData():
    
    def __init__(self, url):
        self.URL = url
        
        self.raw_data = self.fetch_data()
        self._type = self.raw_data["type"] # in self.raw_data.keys()
        self._format = self.raw_data["format"] # in self.raw_data.keys()
        self._version = self.raw_data["version"] # in self.raw_data.keys()
        self.data = self.raw_data['data'] # in self.raw_data.keys()
        
        self.champions = self.data.keys()
    
    def fetch_data(self):
        response = requests.get(self.URL)
        data = response.json()
        
        return data
    
    def fetch_champion_data(self, champion):
        assert type(champion) == str, "champion must be a string"
        assert champion in self.champions, "champion not found"
        # if champion not in self.champions:
        #     print("champion not found")
        #     return None
        
        base_link = "https://ddragon.leagueoflegends.com/cdn/14.13.1/data/en_US/champion/"
        champ_json = f"{champion}.json"
        link = base_link + champ_json
        response = requests.get(link)
        data = response.json()
        champ_data = data["data"][f"{champion}"]
        print("***********: ", champ_data["spells"])
        return champ_data
        
        
    def sort_champions(self, order="alphabetical"):
        pass
    
    def get_champion(self, champion):
        if champion not in self.champions:
            print("no champion found")
            return
        
        champion_data = self.data[champion]
        # print(champion_data['info'])
        
        
        
        
if __name__ == "__main__":
    DATA_URL = "https://ddragon.leagueoflegends.com/cdn/14.13.1/data/en_US/champion.json"
    
    data = ChampionsData(DATA_URL)
    data.get_champion('Nidalee')
    data.fetch_champion_data("Teemo")
    