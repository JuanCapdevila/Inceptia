import requests

class GeoAPI:
    
    API_KEY = "d81015613923e3e435231f2740d5610b"
    LAT = "-35.836948753554054"
    LON = "-61.870523905384076"
    UNITS = "metric"
    
    @classmethod
    def is_hot_in_pehuajo(dtAPI):
        
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={dtAPI.LAT}&lon={dtAPI.LON}&appid={dtAPI.API_KEY}&units={dtAPI.UNITS}"
        
        try:
            response = requests.get(url)
            
            data = response.json()
            
            if response.status_code.__eq__(200):
                
                temperature = data['main']['temp']
                
                if temperature > 28:
                    
                    return True, data['main']
                
                else:
                    
                    return False, data['main']
            else:
                print(response.status_code)
                return False
            
        except Exception as e:
            print(e)
            return False