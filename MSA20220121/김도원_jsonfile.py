import json

try :
    fileName = open("Datalab\\mydata.json", "rb")
    tempData = json.load(fileName) 
    resultData1 = tempData["name"]
    resultData2 = tempData["age"]
    resultData3 = tempData["address"]
    resultData4 = tempData["email"]
    resultData5 = tempData["empcheck"]
except Exception as err:
    error = str(err)
    print(error)
else: 
    fileName.close()



jsonData1 = {
        "empid" : 12345678,
        "name" : "홍길동",
        "info " : [
            {"date1": "2022-01-01", "home" : "서울시"},
            {"dep": "개발", "email" : "aaa@naver.com"}
        ]
    }


try:
    writeFile = open("Datalab\\mydata2.json", "w")
    json.dump(jsonData1, writeFile)
except Exception as err:
    error =str(err)
    print(error)
else:
    writeFile.close()

try:
    writeFile = open("Datalab\\mydata3.json", "w", encoding="utf-8")
    json.dump(jsonData1, writeFile, ensure_ascii=False)
except Exception as err:
    error =str(err)
    print(error)
else:
    writeFile.close()

try:
    writeFile = open("Datalab\\mydata4.json", "w", encoding="utf-8")
    json.dump(jsonData1, writeFile,ensure_ascii=False, indent = 4)
except Exception as err:
    error =str(err)
    print(error)
else:
    writeFile.close()

temp = 0