import json, fb, requests, sys
from facepy import GraphAPI

class warna:
    ungu = '\033[95m'
    biru = '\033[94m'
    hijau = '\033[92m'
    oren = '\033[93m'
    merah = '\033[91m'

def banner():
    print warna.biru+"\t\t\                                          /"
    print warna.biru+"\t\t \                                        /"
    print warna.biru+"\t\t  \                                      /"
    print warna.biru+"\t\t   "+"#" * 38
    print warna.biru+"\t\t   "+"#" * 12+warna.hijau+" Reactions FB "+warna.biru+"#" * 12
    print warna.biru+"\t\t   "+"#" * 38
    print warna.biru+"\t\t   "+"#"+warna.merah+" Author  : D3n0l Ganz               "+warna.biru+"#"
    print warna.biru+"\t\t   "+"#"+warna.merah+" Team    : Indonesian Sad Cyber     "+warna.biru+"#"
    print warna.biru+"\t\t   "+"#"+warna.merah+" Contact : deniibrahim111@gmail.com "+warna.biru+"#"
    print warna.biru+"\t\t   "+"#" * 38
    print warna.biru+"\t\t  /                                      \ "
    print warna.biru+"\t\t /                                        \ "
    print warna.biru+"\t\t/                                          \ "
    print ""

def react():
    print warna.hijau+"Input Token"
    token = raw_input(warna.oren+"---> "+warna.biru)
    print warna.hijau+"ID Target"
    target = raw_input(warna.oren+"---> "+warna.biru)
    print warna.hijau+"Limit"
    limit = raw_input(warna.oren+"---> "+warna.biru)
    print warna.merah+"""
    [1] Like
    [2] Haha
    [3] Sad
    [4] Angry
    [5] Wow
    [6] Love
    """
    print warna.hijau+"Pilih No"
    tipe = raw_input(warna.oren+"---> "+warna.biru)
    if tipe == "1":
        tipe = "LIKE"
    elif tipe == "2":
        tipe = "HAHA"
    elif tipe == "3":
        tipe = "SAD"
    elif tipe == "4":
        tipe = "ANGRY"
    elif tipe == "5":
        tipe = "WOW"
    elif tipe == "6":
        tipe = "LOVE"
    else:
        print warna.merah+"Not!!!"
    ba = requests.get("https://graph.facebook.com/"+target+"/feed?limit="+limit+"&access_token="+token)
    cot = json.loads(ba.text)
    for cok in cot['data']:
        params = {'access_token' : token , 'type' : tipe}
        asu = requests.post("https://graph.facebook.com/"+cok['id']+"/reactions", data = params).text
        if "true" in asu:
            try:
                print warna.hijau+"Berhasil "+warna.ungu+"=> "+warna.biru+"["+warna.merah+cok['id']+warna.biru+"] "+cok['message']
            except KeyError:
                print warna.merah+"Gagal"
        else:
            print warna.merah+"Error"
##########################
banner()
react()
