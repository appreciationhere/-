from tkinter import Frame
import requests
import base64
import time
import cv2 as cv
from linkkit import linkkit
import time
import json
import random 
#连接阿里云
ProductKey="hhdihh6HMnA" #你的产品key
DeviceName="loongsom"   #你的设备名称
DeviceSecret="fb6c51f599cbc28abbc1c46c28a6a34d"#你的设备密码
def on_connect(session_flag, rc, userdata):
    print("on_connect:%d,rc:%d,userdata:" % (session_flag, rc))
    pass
    #取消连接阿里云
def on_disconnect(rc, userdata):
    print("on_disconnect:rc:%d,userdata:" % rc)
    
def on_subscribe_topic(mid, granted_qos, userdata):#订阅topic
    print("on_subscribe_topic mid:%d, granted_qos:%s" %
          (mid, str(','.join('%s' % it for it in granted_qos))))
    pass
    #接收云端的数据
def on_topic_message(topic, payload, qos, userdata):
    #设备端的接收到的数据却是b:"123"用了一个切片去处理数据
    print("阿里云上传回的数值是:", str(payload))
    #拿到接收来的数据
    data=str(payload)[2:-1]
    print("阿里云上传回的数值是:",data)
    dataDict=json.loads(data)
    print("阿里云上传回的数值是:",type(dataDict))   #切片左闭右开 取头不取尾
    #print(dataDict["jiang"])
    #多层解析
    #{"temp":{"value":62}}
    print(dataDict["temp"]["value"]) #解析多层数据

    pass
#终止订阅云端数据
def on_unsubscribe_topic(mid, userdata):
    print("on_unsubscribe_topic mid:%d" % mid)
    pass
#发布消息的结果，判断是否成功调用发布函数
def on_publish_topic(mid, userdata):
    print("on_publish_topic mid:%d" % mid)
#设置连接参数，方法为“一机一密”型
lk = linkkit.LinkKit(
    host_name="cn-shanghai",#填自己的host_name
    # host_name="180.76.57.172",
    product_key=ProductKey,#填自己的product_key
    device_name=DeviceName,#填自己的device_name
    device_secret=DeviceSecret)#填自己的device_secret
#注册接收到云端数据的方法
lk.on_connect = on_connect
#注册取消接收到云端数据的方法
lk.on_disconnect = on_disconnect
#注册云端订阅的方法
lk.on_subscribe_topic = on_subscribe_topic
#注册当接受到云端发送的数据的时候的方法
lk.on_topic_message = on_topic_message
#注册向云端发布数据的时候顺便所调用的方法
lk.on_publish_topic = on_publish_topic
#注册取消云端订阅的方法
lk.on_unsubscribe_topic = on_unsubscribe_topic

#连接阿里云的函数（异步调用）
lk.connect_async()
time.sleep(2)
#订阅主题
rc, mid = lk.subscribe_topic(lk.to_full_topic("user/get"))
#发布主题
akt = '24.25a42c864e17187f538a66f7eb55c809.2592000.1660271500.282335-26688706' # 30天更换一次的Access Token
""" face_detect_demo()函数用于将人脸圈出并标注人脸的信息"""
def face_detect_demo(img):
    img1 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    face = cv.CascadeClassifier("../opencv-3.4.13/data/haarcascades/haarcascade_frontalface_alt2.xml")
    face1 = face.detectMultiScale(img1, 1.1, 5, 0, (100, 100), (300, 300),)
    for x,y,w,h in face1:
        cv.rectangle(img, (x,y), (x + w,y + h), color=(0,0,255), thickness=2)
        cv.putText(img,name, (x + 10, y - 10), cv.FONT_HERSHEY_SIMPLEX,0.75,(0,255,0),1)
    cv.imshow('w', img)

""" recognition()函数运用百度智能云线上api来检测该人脸是否注册和所属id"""
def recognition(image):
    png = open(image,'rb')
    res = png.read()
    encoded1 = base64.b64encode(res)
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/search"
    params = {
            "image": str(encoded1,'utf-8'),
            "image_type": "BASE64",
            "group_id_list": "schools"
        }
    access_token = akt
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, data=params, headers=headers)
    name1 = "unknown"
    cout1 = {}
    if response:
        cout1 = response.json()
        if cout1['error_code'] == 0:
            cout1 = cout1['result']['user_list']
            if (cout1[0]['score']) > 80:
                name1 = cout1[0]['user_id']
        else :
            print("error to get message from server !")
    return name1

""" register() 函数用于提供姓名注册人脸"""
def register(image, name):
    encoded1 = base64.b64encode(open(image, 'rb').read())
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/add"
    params = {
            "image": str(encoded1,'utf-8'),
            "image_type": "BASE64",
            "group_id": "schools",
            "user_id" : name,
            "user_info": "creat tiame:" + time.strftime("%Y-%m-%d",time.localtime(time.time()))
        }
    access_token = akt
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print (response.json())


name = "wyz" #获取到的人脸姓名
cap = cv.VideoCapture(0) #打开摄像头
if __name__ == '__main__':
    cnt = 0
    buf1 = 0 #the accumulation of unkowned people
    """sent data to aliyun"""
    data={"id":int(time.time()),
    "params":{"success_recognition:success_recognition":"200"},
    "version":"1.0",
    "method":"thing.event.property.post"}
    while True:
        flag1,frame = cap.read()
        if not flag1:
            print("no")
            break
        k = cv.waitKey(5) & 0xff
        if cnt == 20:
            cv.imwrite("1.jpg", frame)
            name = recognition("1.jpg")
            print(name)
            """人脸检测的数据错误"""
            if name == "1":
                buf1 = 0
                pass
            elif name == "unknown":
                buf1 += 1
            else :
                buf1 = 0
                data={"id":int(time.time()),
                "params":{"recog":name + " opend the door"},
                "version":"1.0",
                "method":"thing.event.property.post"}
                topic="/sys"+lk.to_full_topic("thing/event/property/post")
                rc, mid = lk.publish_topic(topic, str(data))
            if buf1 == 5:
                buf1 = 0
                data={"id":int(time.time()),
                "params":{"recog":"unkowned people is wandering"},
                "version":"1.0",
                "method":"thing.event.property.post"}
                topic="/sys"+lk.to_full_topic("thing/event/property/post")
                rc, mid = lk.publish_topic(topic, str(data))
            cnt = 0
        face_detect_demo(frame)
        cnt += 1
