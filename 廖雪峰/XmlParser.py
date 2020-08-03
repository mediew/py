#利用ParserCreate模块解析xml获得实时天气


from xml.parsers.expat import ParserCreate
from urllib import request

class WeatherHexHandler():

    weather = {'city': 1, 'cityname': [], 'forecast': []}

    def StartElementHandler(self, name, attrs):
        if name == 'beijing':
            self.weather['city'] = '北京'
        if name == 'city':
            self.weather['cityname'].append(attrs['cityname'])
            self.weather['forecast'].append({
                'coordinate': (attrs['cityX'], attrs['cityY']),
                'weatherDetails': attrs['stateDetailed'],
                'high_and_low_temp': (attrs['tem1'], attrs['tem2'])
                })

def Xmlparser(xml_str):
    parser = ParserCreate()
    handler = WeatherHexHandler()
    parser.StartElementHandler = handler.StartElementHandler
    parser.Parse(xml_str)
    print('city:'+ handler.weather['city'])
    for (x, y) in zip(handler.weather['cityname'],handler.weather['forecast']):
        print('Region:'+x)
        print(y)

URL = 'http://flash.weather.com.cn/wmaps/xml/beijing.xml'

with request.urlopen(URL, timeout = 4) as f:
    data = f.read()

result = Xmlparser(data.decode('utf-8'))
