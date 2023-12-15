import requests
from .prototype import Song

MUSIC_DATA_API = "https://www.diving-fish.com/api/maimaidxprober/music_data"
CHART_STATS_API = "https://www.diving-fish.com/api/maimaidxprober/chart_stats"
    
def getMusicData():
    req = requests.get(MUSIC_DATA_API)
    return req.json()

def getChartStats():
    req = requests.get(CHART_STATS_API)
    return req.json()