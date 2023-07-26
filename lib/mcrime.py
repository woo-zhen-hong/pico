import urequests

class Crime:
    def __init__(self, index, url):
        res = urequests.get(url=url)
        self.json = res.json()
        self.parse(index)
        
    def parse(self, index):
        Crime = self.json['data']
        self.cityname = 'kaohsiung'
        self.year = Crime[index]['年度']
        if(Crime[index]['月份'] == '1月份'):
            self.month = 'January'
        elif(Crime[index]['月份'] == '2月份'):
            self.month = 'February'
        elif(Crime[index]['月份'] == '3月份'):
            self.month = 'March'
        elif(Crime[index]['月份'] == '4月份'):
            self.month = 'April'
        elif(Crime[index]['月份'] == '5月份'):
            self.month = 'May'
        elif(Crime[index]['月份'] == '6月份'):
            self.month = 'June'
        elif(Crime[index]['月份'] == '7月份'):
            self.month = 'July'
        elif(Crime[index]['月份'] == '8月份'):
            self.month = 'August'
        elif(Crime[index]['月份'] == '9月份'):
            self.month = 'September'
        elif(Crime[index]['月份'] == '10月份'):
            self.month = 'October'
        elif(Crime[index]['月份'] == '11月份'):
            self.month = 'November'
        else:
            self.month = 'December'
        if(Crime[index]['案件別'] == '1全般刑案'):
            self.type = '1 general criminal case'
        elif(Crime[index]['案件別'] == '2暴力犯罪'):
            self.type = '2 violent crime'
        elif(Crime[index]['案件別'] == '3竊盜案件'):
            self.type = '3 theft case'
        elif(Crime[index]['案件別'] == '4詐欺案件'):
            self.type = '4 Fraud Case'
        elif(Crime[index]['案件別'] == '5毒品案件'):
            self.type = '5 drug case'
        self.happen = Crime[index]['發生數']
        self.clear = Crime[index]['破獲數']
        self.percent = Crime[index]['破獲率']
        
    def info(self):
        print(f'cityname: {self.cityname}')
        print(f'年度: {self.year}')
        print(f'月份: {self.month}')
        print(f'案件別: {self.type}')
        print(f'發生數: {self.happen}')
        print(f'破獲數: {self.clear}')
        print(f'破獲率: {self.percent}')
        
          

