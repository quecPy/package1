from machine import Pin,ExtInt
# models = "BQ100"
# models = "BQ200"
# models = "BQ300"
# models = "BQ320"
# models = "BQ338"
# models = "BQ6088"
# models = "BQ7000"
# models = "BQM18"
# models = "BQ168"
# models = "BQ510"
# models = "BQ520"
# models = "BQ500"
# models = "BQH5"
# models = "BQH3"
# models = "BQV8"
# models = "BQI8"
# models = "BQXQ"
# models = "BQ228"
# models = "BQY88"
# models = "BQV6"
# models = "BQV5"
models = "BQ79"
# models = "BQM18"
# models = "BQH5_JBT"
net_stype = "4G"
modular = "600M-LA"

#单双卡，宽，高，旋转类型
'''
----------------UI界面------------------------
0:单卡/双卡
1:开关类型:  1:独立按钮,2:旋钮,3:按压旋钮,4电源键家返回键
2:是否带充电: 0:无  1:有
3:宽
4:高
5:列表行数
6:屏幕旋转类型
7:音量等级
8:键盘类型。1:矩阵,2:按键
9:翻页键/音量键组合
10:版本号
11:更新日期
12:GPIO类型
13:PTT按键抬起
14:main 天气显示
15: welcome 字体颜色 0:白色,1:黑色
----------------------------------------------
'''
main_scree_size = {
    128:{
        1:2,
        2:24,
        3:46,
        4:68,
        5:20
    },
    160:{
        1:2,
        2:32,
        3:64,
        4:96,
        5:24
    }
}
screen_size_style = {
    "BQ520":[2,1,0,160,128,4,5,10,1,0,"BX-v1.0.3","221115",1,[0,2,1],1,1],
    "BQ338":[2,2,0,128,160,5,3,10,1,0,"BX-v1.0.2","221031",2,[0,2,1],1,1],
    "BQ320":[1,4,1,128,128,5,4,10,1,0,"BX-v1.0.2","221115",2,[0,2,1],1,1],
    "BQ79":[2,4,1,128,128,5,4,10,1,1,"BX-v1.0.2","221115",2,[0,2,1],1,1],
    "BQV6":[2,4,0,160,128,5,2,10,2,0,"BX-v1.0.1","221115",3,[0,2,1],1,1],
    "BQV5":[2,4,1,160,128,5,2,10,2,0,"BX-v1.0.2","221031",3,[0,2,1],1,1],
    "BQ300":[2,1,0,160,128,4,5,5,1,1,"BX-v1.0.2","221115",2,[0,2,1],1,1],
    "BQ6088":[2,2,0,160,128,4,5,10,1,0,"BX-v1.0.1","221102",2,[0,2,1],1,1],
    "BQ200":[2,2,0,160,128,4,2,5,1,0,"BX-v1.0.1","221102",1,[0,2,1],1,1],
    "BQH5_JBT":[2,1,0,128,128,4,4,5,1,0,"BX-v1.0.2","221115",1,[0,2,1],0,0],
    "BQXQ":[2,4,1,160,128,4,5,10,1,0,"BX-v1.0.1","221112",2,[0,2,1],0,1],
    "BQ228":[1,2,1,128,128,5,7,5,1,0,"BX-v1.0.2","221031",2,[0,2,1],1,1],
    "BQ100":[2,4,1,160,128,5,5,10,2,0,"BX-v1.0.2","221031",3,[0,2,1],1,1],
    "BQ510":[2,1,0,128,128,5,4,10,1,0,"BX-v1.0.1","221031",2,[0,2,1],1,1],
    "BQ500":[2,4,0,128,128,5,4,10,1,0,"BX-v1.0.1","221031",2,[0,2,1],1,1],
    "BQ7000":[2,4,0,128,160,5,0,10,1,0,"BX-v1.0.2","221031",2,[0,2,1],1,1],
    "BQH3":[2,2,0,128,128,5,3,5,1,0,"BX-v1.0.1","221031",2,[0,2,1],1,1],
    "BQM18":[2,3,0,128,128,5,4,5,1,0,"BX-v1.0.1","221031",2,[0,2,1],1,1],
}

model_gpio = {
    1:{
        "ej":[Pin.GPIO6],
        "mic":[Pin.GPIO7],
        "ext_mic":[ExtInt.GPIO6],
        "lcd":[Pin.GPIO14],
        "AUDIO_PA_EN" :[Pin.GPIO18],
        "NET_MODE_LED":[Pin.GPIO11],
        "NET_LED" :[Pin.GPIO12],
        "ej_ptt" :[ExtInt.GPIO19]
    },
    2:{
        "ej":[Pin.GPIO30],
        "mic":[Pin.GPIO20],
        "ext_mic":[ExtInt.GPIO30],
        "lcd":[Pin.GPIO14],
        "AUDIO_PA_EN":[Pin.GPIO18],
        "NET_MODE_LED":[Pin.GPIO11],
        "NET_LED" :[Pin.GPIO12],
        "ej_ptt" :[ExtInt.GPIO19]
    },
    3:{
        "ej":[Pin.GPIO8],
        "mic":[Pin.GPIO8],
        "ext_mic":[ExtInt.GPIO8],
        "lcd":[Pin.GPIO15],
        "AUDIO_PA_EN" :[Pin.GPIO1],
        "NET_MODE_LED":[Pin.GPIO11],
        "NET_LED" :[Pin.GPIO12],
        "ej_ptt" :[ExtInt.GPIO5],
        "btn_ptt":[ExtInt.GPIO5],
        "btn_up":[ExtInt.GPIO21],
        "btn_down":[ExtInt.GPIO22],
        "btn_vol_up":[ExtInt.GPIO4],
        "btn_vol_down":[ExtInt.GPIO3],
        "btn_menu":[ExtInt.GPIO10],
        "btn_ok":[ExtInt.GPIO23]
    }

}
'''
     PTT:       "PTT_press":           按下,    "PTT_release":             抬起,
     vol+       "vol_up_press":         按下,    "vol_up_release":          抬起,
     vol-       "vol_down_press":       按下,    "vol_down_release":        抬起,
     up         "up_press":             按下,    "up_release":              抬起,
     down       "down_press":           按下,    "down_release":            抬起,
     menu       "menu_press":           按下,    "menu_release":            抬起,
     ok         "ok_press":             按下,    "ok_release":              抬起,
     back       "back_press":           按下,    "back_release":            抬起,
    switch_type "switch_type_press":    按下,    "switch_type_release" :    抬起,
     key1       "key1_press":           按下,    "key1_release" :           抬起,
     key2       "key2_press":           按下,    "key2_release" :           抬起,
     key3       "key3_press":           按下,    "key3_release" :           抬起,
     key4       "key4_press":           按下,    "key4_release" :           抬起,

     0 :{
            0:{0:"",1:"",2:""},
            1:{0:"",1:"",2:""},
            2:{0:"",1:"",2:""}
        },
        1 :{
            0:{0:"",1:"",2:""},
            1:{0:"",1:"",2:""},
            2:{0:"",1:"",2:""}
        },
        2 :{
            0:{0:"",1:"",2:""},
            1:{0:"",1:"",2:""},
            2:{0:"",1:"",2:""}
        }
'''
btn_stype ={
    "BQ520":{
        0 :{
            0:{0:"menu_release",1:"key1_release",2:"vol_down_release"},
            1:{0:"up_release",1:"down_release",2:"vol_up_release"},
            2:{0:"back_release",1:"key2_release",2:"PTT_release"}
        },
        1 :{
            0:{0:"menu_press",1:"",2:"vol_down_press"},
            1:{0:"up_press",1:"down_press",2:"vol_up_release"},
            2:{0:"",1:"",2:"PTT_press"}
        },
        
    },
    "BQ338":{
        0 :{
            0:{0:"menu_release",1:"down_release",2:""},
            1:{0:"ok_release",1:"up_release",2:""},
            2:{0:"back_release",1:"PTT_release",2:""}
        },
        1 :{
            0:{0:"menu_press",1:"down_press",2:""},
            1:{0:"ok_press",1:"up_press",2:""},
            2:{0:"back_press",1:"PTT_press",2:""}
        },
        
    },
    "BQ320":{
        0 :{
            0:{0:"menu_release",1:"vol_down_release",2:""},
            1:{0:"up_release",1:"vol_up_release",2:""},
            2:{0:"down_release",1:"PTT_release",2:""}
        },
        1 :{
            0:{0:"menu_press",1:"vol_down_press",2:""},
            1:{0:"up_press",1:"vol_up_press",2:""},
            2:{0:"down_press",1:"PTT_press",2:""}
        },
        
    },
    "BQ79":{
        0 :{
            0:{0:"menu_release",1:"down_release",2:""},
            1:{0:"ok_release",1:"up_release",2:""},
            2:{0:"down_release",1:"PTT_release",2:""}
        },
        1 :{
            0:{0:"menu_press",1:"down_press",2:""},
            1:{0:"ok_press",1:"up_press",2:""},
            2:{0:"down_press",1:"PTT_press",2:""}
        },
       
    },
    "BQ300":{
        0 :{
            0:{0:"menu_release",1:"down_release",2:""},
            1:{0:"ok_release",1:"up_release",2:""},
            2:{0:"back_release",1:"PTT_release",2:""}
        },
        1 :{
            0:{0:"menu_press",1:"down_press",2:""},
            1:{0:"ok_press",1:"up_press",2:""},
            2:{0:"back_press",1:"PTT_press",2:""}
        },
        
    },
    "BQ6088":{
        0 :{
            0:{0:"up_release",1:"back_release",2:""},
            1:{0:"PTT_release",1:"ok_release",2:""},
            2:{0:"down_release",1:"menu_release",2:""}
        },
        1 :{
            0:{0:"up_press",1:"back_press",2:""},
            1:{0:"PTT_press",1:"ok_press",2:""},
            2:{0:"down_press",1:"menu_press",2:""}
        },
        
    },
    "BQ200":{
        0 :{
            0:{0:"back_release",1:"down_release",2:""},
            1:{0:"menu_release",1:"up_release",2:""},
            2:{0:"ok_release",1:"PTT_release",2:""}
        },
        1 :{
            0:{0:"back_press",1:"down_press",2:""},
            1:{0:"menu_press",1:"up_press",2:""},
            2:{0:"ok_press",1:"PTT_press",2:""}
        },
        
    },
    "BQH5_JBT":{
        0 :{
            0:{0:"menu_release",1:"ok_release",2:"vol_down_release"},
            1:{0:"up_release",1:"down_release",2:"vol_up_release"},
            2:{0:"back_release",1:"PTT_release",2:"PTT_release"}
        },
        1 :{
            0:{0:"menu_press",1:"ok_press",2:"vol_down_press"},
            1:{0:"up_press",1:"down_press",2:"vol_up_press"},
            2:{0:"back_press",1:"PTT_press",2:"PTT_press"}
        },
        
    },
     "BQXQ":{
        0 :{
            0:{0:"menu_release",1:"vol_down_release",2:"vol_down_release"},
            1:{0:"up_release",1:"vol_up_release",2:"vol_up_release"},
            2:{0:"down_release",1:"PTT_release",2:"PTT_release"}
        },
        1 :{
            0:{0:"menu_press",1:"vol_down_press",2:"vol_down_press"},
            1:{0:"up_press",1:"vol_up_press",2:"vol_up_press"},
            2:{0:"down_press",1:"PTT_press",2:"PTT_press"}
        },
        
    },
    "BQ228": {
        0: {
            0: {0: "PTT_release", 1: "menu_release", 2: ""},
            1: {0: "up_release", 1: "ok_release", 2: ""},
            2: {0: "down_release", 1: "back_release", 2: ""}
        },
        1: {
            0: {0: "PTT_press", 1: "menu_press", 2: ""},
            1: {0: "up_press", 1: "ok_press", 2: ""},
            2: {0: "down_press", 1: "back_press", 2: ""}
        },

    },
    "BQ510": {
        0: {
            0: {0: "PTT_release", 1: "key1_release", 2: "menu_release"},
            1: {0: "vol_up_release", 1: "down_release", 2: "up_release"},
            2: {0: "vol_down_release", 1: "", 2: "back_release"}
        },
        1: {
            0: {0: "PTT_press", 1: "key1_press", 2: "menu_press"},
            1: {0: "vol_up_press", 1: "down_press", 2: "up_press"},
            2: {0: "vol_down_press", 1: "", 2: "back_press"}
        },

    },
    "BQ500": {
        0: {
            0: {0: "PTT_release", 1: "menu_release", 2: ""},
            1: {0: "up_release", 1: "ok_release", 2: ""},
            2: {0: "down_release", 1: "", 2: ""}
        },
        1: {
            0: {0: "PTT_press", 1: "menu_press", 2: ""},
            1: {0: "up_press", 1: "ok_press", 2: ""},
            2: {0: "down_press", 1: "", 2: ""}
        },

    },
    "BQ7000": {
        0: {
            0: {0: "menu_release", 1: "vol_down_release", 2: ""},
            1: {0: "up_release", 1: "vol_up_release", 2: ""},
            2: {0: "down_release", 1: "PTT_release", 2: ""}
        },
        1: {
            0: {0: "menu_press", 1: "vol_down_press", 2: ""},
            1: {0: "up_press", 1: "vol_up_press", 2: ""},
            2: {0: "down_press", 1: "PTT_press", 2: ""}
        },

    },
    "BQH3": {
        0: {
            0: {0: "", 1: "down_release", 2: ""},
            1: {0: "back_release", 1: "up_release", 2: ""},
            2: {0: "menu_release", 1: "PTT_release", 2: ""}
        },
        1: {
            0: {0: "", 1: "down_press", 2: ""},
            1: {0: "back_press", 1: "up_press", 2: ""},
            2: {0: "menu_press", 1: "PTT_press", 2: ""}
        },

    },
    "BQM18": {
        0: {
            0: {0: "menu_release", 1: "down_release", 2: ""},
            1: {0: "ok_release", 1: "up_release", 2: ""},
            2: {0: "back_release", 1: "PTT_release", 2: ""}
        },
        1: {
            0: {0: "menu_press", 1: "down_press", 2: ""},
            1: {0: "ok_press", 1: "up_press", 2: ""},
            2: {0: "back_press", 1: "PTT_press", 2: ""}
        },

    },
}

volume_levels = {
    5:{
        0:0,
        1:2,
        2:4,
        3:6,
        4:8,
        5:10
    },
    10:{
        0: 0,
        1: 2,
        2: 3,
        3: 4,
        4: 5,
        5: 6,
        6: 7,
        7: 8,
        8: 9,
        9: 10,
        10: 11
    }
     
}
adc_volume_levels = {
    5:{
        3:[0,0],
        10: [0,0],
        45:[1,2],
        75: [1,2],
        120:[2,4],
        155: [2,4],
        200:[3,6],
        240: [3,6],
        420:[4,8],
        810: [4,8],
        1190:[5,10]
    },
    10:{
        3: [0,0],
        10: [1,2],
        45: [2,3],
        75: [3,4],
        120: [4,5],
        155: [5,6],
        200: [6,7],
        240: [7,8],
        420: [8,9],
        810: [9,10],
        1190:[10,11]
    }
     
}