# pip install flask 설치 진행

import requests
import json
from flask import Flask

#변수 선언 - 프로그램의 이름 저장하는 변수(파일 이름 저장 변수)
#application server 개발 app 변수를 많이 사용
app = Flask(__name__)

#함수 선언
#시작할 때 경로(route) 선언해야함
@app.route("/") # 웹 사이트 경로를 지정 - 앞에서 선언한 app 변수를 사용
def FlaskLab(): # 요청 -메서드 이름 요청에서 사용하는 것 
    return "Flask 데이터 응답" #응답 - return 에서 돌려주는 데이터가 응답

@app.route("/data1")
def FlaskData():#startPage, pageCount,address
    keyValue = r"UOo4A1CIgKbZtFdio%2Ft4b0pyZ8yVvs94Xdjy7AelrmavKE6CWwZ3PMlPCzTNjk3n4sRSGkYW0O1%2FHhGtf0H7Vg%3D%3D"
    
    dataURL = "http://api.odcloud.kr/api/apnmOrg/v1/list?"
    dataURL += "page=" + str(1) + "&perPage=" + str(10)
    dataURL += "&cond" + r"%5BorgZipaddr%3A%3ALIKE%5D=%EB%8F%99%EC%9E%91%EA%B5%AC" # 또는 본인 사는 지역구
    dataURL += "&serviceKey=" + keyValue
    # dataResult = "공공데이터 요청후 데이터 받기 :flask -request /requests 기능 사용"
    dataResult = requests.get(dataURL)    
    return json.dumps(dataResult.text,ensure_ascii=False,indent = 10)

if __name__ == "__main__": 

   app.run()



