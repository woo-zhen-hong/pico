# Pico專案說明
* 目前連接的API是高雄市五大刑事案件發生數破獲數破獲率，來源是高雄市政府的資料開放平台
* https://data.kcg.gov.tw/dataset/kcgoa-00000953-02a
* 當pico板街上電源時，他會先執行記憶體裡的main.py程式
> pico板會先連接WiFi，所以如果要執行main.py程式，必須先改寫main.py連接WiFi的部分，將SSID改成WiFi名稱，PASSWORD改成該WiFi的密碼
> 成功連接上WiFi之後，LCD螢幕會顯示WiFi connected，接下來他會連接API
* 首先，LCD螢幕會先顯示高雄市五大刑事案件發生數破獲數破獲率的第一筆資料，並將結果顯示在LCD螢幕上
* LCD螢幕上資料說明，以第一筆資料為例
> 110 ：為年度，代表為民國110年
> January ：為月份，代表為1月份
> 1 ：為案件別，1為全般刑案;2為暴力犯罪;3為竊盜案件;4為詐欺案件;5為毒品案件
> 1,978 ：為發生數，代表為該年度的該月份此案件別的發生數
> 1,957 ：為破獲數，代表為該年度的該月份此案件別的破獲數
* 另外舵機會顯示出該年度的該月份此案件別的破獲率，以0~100%來表示，至於有些資料的破獲率超過100%，則用100%為代表
# 展示影片
* https://youtu.be/yvBs2KDXY3w
# 簡報
* https://docs.google.com/presentation/d/1zlfuCOp5-J4VEmNkBnkZFm8WD_7qJfnblv5-Yx5HWSY/edit#slide=id.g25bf85294e3_0_121
