import osTimer
from machine import Pin, KeyPad, ExtInt
from misc import PowerKey, Power
from usr.common import Abstract
from usr import EventMesh
import usr.all_models as mdls
import poc
# poc.speak_mode(1)
        
gpio_type =  mdls.screen_size_style[mdls.models][12]
def __key_cb(key_list):
    """矩阵键盘回调函数"""
    print('key11:',key_list)
    EventMesh.publish("btn_event", key_list)

def __pwk_callback(status):
    print('pwk event:',status)
    EventMesh.publish("pwk_event", status)

class BtnDevice(Abstract):
    """物理按键类,3*2的矩阵键盘加pwk"""

    def __init__(self):
        self.__keypad = KeyPad(3, 3)
        self.__pk = PowerKey()
        self.__longpress_flag = 0
        self.__long_timer = osTimer()
        self.__pwk_timer = osTimer()
        self.__vol_up_btn_timer = osTimer()
        self.__vol_down_btn_timer =osTimer()
        self.__ok_btn_timer = osTimer()
        self.__up_btn_timer = osTimer()
        self.__down_btn_timer = osTimer()
        self.__key1_btn_timer = osTimer()
        self.__key2_btn_timer = osTimer()
        self.__back_btn_timer = osTimer()
        self.__up_longPress_flag = False
        self.__down_longPress_flag = False
        self.__vol_up_longPress_flag = False
        self.__vol_down_longPress_flag = False
        self.__key1_longPress_flag = False
        self.__key2_longPress_flag = False
        self.__back_longPress_flag = False
        self.__PowerDownTimeOut = 2000
        self.group_count = 0
        self.group_cur = 0
        self.member_count = 0
        self.member_cur = 0

    def post_processor_after_instantiation(self):
        EventMesh.subscribe("btn_event", self.__key_event_manage)
        EventMesh.subscribe("pwk_event", self.__pwk_callback)
        self.__keypad.init()
        self.__keypad.set_callback(__key_cb)
        self.__pk.powerKeyEventRegister(__pwk_callback)
        
        self.ej_ptt = ExtInt(mdls.model_gpio[gpio_type]["ej_ptt"][0], ExtInt.IRQ_RISING_FALLING, ExtInt.PULL_PU, self.ej_ptt_cb)
        
        self.ej_ptt.enable()
        if mdls.screen_size_style[mdls.models][8] == 2:
            self.btn_ptt = ExtInt(mdls.model_gpio[gpio_type]["btn_ptt"][0], ExtInt.IRQ_RISING_FALLING, ExtInt.PULL_PU, self.ej_ptt_cb)
            self.btn_ptt.enable()
            self.btn_up = ExtInt(mdls.model_gpio[gpio_type]["btn_up"][0], ExtInt.IRQ_RISING_FALLING, ExtInt.PULL_PU, self.ej_ptt_cb)
            self.btn_up.enable()
            self.btn_down = ExtInt(mdls.model_gpio[gpio_type]["btn_down"][0], ExtInt.IRQ_RISING_FALLING, ExtInt.PULL_PU, self.ej_ptt_cb)
            self.btn_down.enable()
            self.btn_vol_up = ExtInt(mdls.model_gpio[gpio_type]["btn_vol_up"][0], ExtInt.IRQ_RISING_FALLING, ExtInt.PULL_PU, self.ej_ptt_cb)
            self.btn_vol_up.enable()
            self.btn_vol_down = ExtInt(mdls.model_gpio[gpio_type]["btn_vol_down"][0], ExtInt.IRQ_RISING_FALLING, ExtInt.PULL_PU, self.ej_ptt_cb)
            self.btn_vol_down.enable()
            self.btn_menu = ExtInt(mdls.model_gpio[gpio_type]["btn_menu"][0], ExtInt.IRQ_RISING_FALLING, ExtInt.PULL_PU, self.ej_ptt_cb)
            self.btn_menu.enable()
            self.btn_ok = ExtInt(mdls.model_gpio[gpio_type]["btn_ok"][0], ExtInt.IRQ_RISING_FALLING, ExtInt.PULL_PU, self.ej_ptt_cb)
            self.btn_ok.enable()

    def ej_ptt_cb(self, ext_info):
        print("btn_PTT:",ext_info)
        if mdls.model_gpio[gpio_type]["ej_ptt"][0] == ext_info[0] and  ext_info[1] ==1:
            self.__speak_press_handle()
            # poc.ptt_cfg(1,Pin.GPIO19,0)
        elif mdls.model_gpio[gpio_type]["ej_ptt"][0] == ext_info[0] and  ext_info[1] ==0:
            self.__speak_release_handle()
        elif mdls.model_gpio[gpio_type]["btn_ptt"][0] == ext_info[0] and  ext_info[1] ==1:
            self.__speak_press_handle()
            
        elif mdls.model_gpio[gpio_type]["btn_ptt"][0] == ext_info[0] and  ext_info[1] ==0:
            self.__speak_release_handle()
        elif mdls.model_gpio[gpio_type]["btn_up"][0] == ext_info[0] and  ext_info[1] ==1:
            self.keypad_tone()
            self.__up_long_press_handle()
        elif mdls.model_gpio[gpio_type]["btn_up"][0] == ext_info[0] and  ext_info[1] ==0:
            self.__up_press_handle()
        elif mdls.model_gpio[gpio_type]["btn_down"][0] == ext_info[0] and  ext_info[1] ==1:
            self.keypad_tone()
            self.__down_long_press_handle()
        elif mdls.model_gpio[gpio_type]["btn_down"][0] == ext_info[0] and  ext_info[1] ==0:
            self.__down_press_handle()      
        elif mdls.model_gpio[gpio_type]["btn_vol_up"][0] == ext_info[0] and  ext_info[1] ==1:
            self.keypad_tone()
            self.__vol_up_long_press_handle()
        elif mdls.model_gpio[gpio_type]["btn_vol_up"][0] == ext_info[0] and  ext_info[1] ==0:
            self.__vol_up_press_handle()
        elif mdls.model_gpio[gpio_type]["btn_vol_down"][0] == ext_info[0] and  ext_info[1] ==1:
            self.keypad_tone()
            self.__vol_down_long_press_handle()
        elif mdls.model_gpio[gpio_type]["btn_vol_down"][0] == ext_info[0] and  ext_info[1] ==0:
            self.__vol_down_press_handle()      
        elif mdls.model_gpio[gpio_type]["btn_menu"][0] == ext_info[0] and  ext_info[1] ==1:
            self.keypad_tone()
            self.__ok_long_press_handle()
        elif mdls.model_gpio[gpio_type]["btn_menu"][0] == ext_info[0] and  ext_info[1] ==0:
            self.__ok_press_handle()
        elif mdls.model_gpio[gpio_type]["btn_ok"][0] == ext_info[0] and  ext_info[1] == 1:
            self.__speak_press_handle()
        elif mdls.model_gpio[gpio_type]["btn_ok"][0] == ext_info[0] and  ext_info[1] ==0:
            self.__speak_release_handle()
        
        
    # def __key_cb(self, key_list):
    #     """矩阵键盘回调函数"""
    #     print('key11:',key_list)
    #     self.__key_event_manage(key_list)

    def keypad_tone(self):
        if not EventMesh.publish("get_poc_keypad_tone") and EventMesh.publish("get_speaker_state") == 1:
            EventMesh.publish("audio_tone")

    def __key_event_manage(self, topic, event):

        if event == 1:
            self.__pwk_timer.start(self.__PowerDownTimeOut, 0, self.__pwk_long_press_cb)
        elif event == 0:
            self.keypad_tone()
            self.__pwk_timer.stop()
        if  mdls.btn_stype[mdls.models][event[0]][event[1]][event[2]] == "PTT_press" : # ptt按下
            self.__speak_press_handle()
            # poc.ptt_cfg(mdls.screen_size_style[mdls.models][13][0],mdls.screen_size_style[mdls.models][13][1],mdls.screen_size_style[mdls.models][13][2])
        elif mdls.btn_stype[mdls.models][event[0]][event[1]][event[2]] == "PTT_release":  # ptt抬起
            self.__speak_release_handle()
        elif mdls.btn_stype[mdls.models][event[0]][event[1]][event[2]] == "menu_press":  # ok_btn按下
            self.keypad_tone()
            self.__ok_long_press_handle()
        elif mdls.btn_stype[mdls.models][event[0]][event[1]][event[2]] == "menu_release": # ok_btn抬起
            self.__ok_press_handle()
        elif mdls.btn_stype[mdls.models][event[0]][event[1]][event[2]] == "ok_release": # ok_btn抬起  # sleep_btn抬起
            self.keypad_tone()
            self.__sleep_press_handle()
        elif mdls.btn_stype[mdls.models][event[0]][event[1]][event[2]] == "vol_up_release":  # vol+抬起
            self.__vol_up_press_handle()
        elif mdls.btn_stype[mdls.models][event[0]][event[1]][event[2]] == "vol_up_press": # vol+按下
            self.keypad_tone()
            self.__vol_up_long_press_handle()
        elif mdls.btn_stype[mdls.models][event[0]][event[1]][event[2]] == "vol_down_release":  # vol-抬起
            self.__vol_down_press_handle()
        elif mdls.btn_stype[mdls.models][event[0]][event[1]][event[2]] == "vol_down_press": # vol-长按
            self.keypad_tone()
            self.__vol_down_long_press_handle()
        elif mdls.btn_stype[mdls.models][event[0]][event[1]][event[2]] == "up_press": # up 按下
            self.keypad_tone()
            self.__up_long_press_handle()
        elif mdls.btn_stype[mdls.models][event[0]][event[1]][event[2]] == "up_release" : # up 抬起
            self.__up_press_handle()
        elif mdls.btn_stype[mdls.models][event[0]][event[1]][event[2]] == "down_press" : # down 按下
            self.keypad_tone()
            self.__down_long_press_handle()
        elif mdls.btn_stype[mdls.models][event[0]][event[1]][event[2]] == "down_release":  # down 抬起
            self.__down_press_handle()
        elif mdls.btn_stype[mdls.models][event[0]][event[1]][event[2]] == "key1_release" : # 快捷键1 抬起
            self.__key1_press_handle()
        elif mdls.btn_stype[mdls.models][event[0]][event[1]][event[2]] == "key2_release" :# 快捷键2 抬起
            self.__key2_press_handle()
        elif mdls.btn_stype[mdls.models][event[0]][event[1]][event[2]] == "back_release" : # 返回键
            self.__back_press_handle()

    def __ok_longPress_handle(self, args):
        """ok 长按锁键"""
        EventMesh.publish("btn_ok_long")

    def __longPress_handle(self, *args):
        EventMesh.publish("btn_ptt_long")

    def __down_longPress_handle(self, args):
        self.__down_longPress_flag = True
        EventMesh.publish("btn_down_long")

    def __sleep_press_handle(self):
        '''
        息屏键处理方法,发送息屏事件
        '''
        EventMesh.publish("btn_sleep")

    def __ok_press_handle(self):
        '''
        KEY1:联动屏幕左下角或确认键
        '''
        self.__ok_btn_timer.stop()
        EventMesh.publish("btn_ok_on")

    def __ok_long_press_handle(self):
        '''
        KEY1:联动屏幕左下角或确认键
        '''
        EventMesh.publish("btn_ok_off")
        self.__ok_btn_timer.start(5000, 0, self.__ok_longPress_handle)

    def __pwk_long_press_cb(self, *args):
        '''KEY2:联动屏幕右下角或返回键长按关机'''
        EventMesh.publish("btn_back_long")

    def __pwk_callback(self,event, status):
        '''
        KEY2:联动屏幕右下角或返回键
        '''
        print('==pwr:',status)
        if status == 1:
            self.__pwk_timer.start(self.__PowerDownTimeOut, 0, self.__pwk_long_press_cb)
        elif status == 0:
            self.__pwk_timer.stop()
            # print("btn_back:{}".format(mdls.screen_size_style[mdls.models][1]))
            if mdls.screen_size_style[mdls.models][1] == 4 :
                EventMesh.publish("btn_back")
            else:
                EventMesh.publish("btn_shuntdown")

    def __down_press_handle(self):
        '''
        键盘S4：音量-或向右选择或向下选择 抬起
        '''
        # 主界面按下，音量-
        self.__down_btn_timer.stop()
        if not self.__down_longPress_flag:
            EventMesh.publish("btn_down_on")
        self.__down_longPress_flag = False

    def __down_long_press_handle(self):
        '''
        键盘S4：音量-长按 按下
        '''
        # 主界面按下，音量-
        self.__down_btn_timer.stop()
        self.__down_btn_timer.start(3000, 0, self.__down_longPress_handle)
        
    def __down_longPress_handle(self, args):
        self.__down_longPress_flag = True
        EventMesh.publish("btn_down_long")

    def __up_press_handle(self):
        """
        音量+或向左选择或向上选择按键回调
        """
        self.__up_btn_timer.stop()
        if not self.__up_longPress_flag:
            EventMesh.publish("btn_up")
        self.__up_longPress_flag = False
    
    def __vol_up_long_press_handle(self):
        '''
        up长按处理
        '''
        self.__vol_up_btn_timer.stop()
        self.__up_btn_timer.start(3000, 0, self.__vol_up_longPress_handle)

    def __vol_up_longPress_handle(self, *args):
        self.__up_longPress_flag = True
        EventMesh.publish("btn_vol_up_long_press")

    def __vol_up_press_handle(self):
        """
        音量+按键回调
        """
        self.__up_btn_timer.stop()
        if not self.__up_longPress_flag:
            EventMesh.publish("btn_vol_up")
        self.__up_longPress_flag = False

  
    def __vol_down_press_handle(self):
        '''
        键盘S4：音量- 抬起
        '''
        # 音量-
        self.__vol_down_btn_timer.stop()
        if not self.__vol_down_longPress_flag:
            EventMesh.publish("btn_vol_down_on")
        self.__vol_down_longPress_flag = False

    def __vol_down_long_press_handle(self):
        '''
        键盘S4：音量-长按 按下
        '''
        # 主界面按下，音量-
        self.__vol_down_btn_timer.stop()
        self.__vol_down_btn_timer.start(3000, 0, self.__vol_down_longPress_handle)
        
    def __vol_down_longPress_handle(self, args):
        self.__vol_down_longPress_flag = True
        EventMesh.publish("btn_vol_down_long")

    def __up_long_press_handle(self):
        '''
        up长按处理
        '''
        self.__up_btn_timer.stop()
        self.__up_btn_timer.start(3000, 0, self.__up_longPress_handle)

    def __up_longPress_handle(self, *args):
        self.__up_longPress_flag = True
        EventMesh.publish("btn_up_long_press")
    
    def __speak_release_handle(self, *args):
        """
        群呼按键长按松开回调函数
        结束群呼
        """
        self.__long_timer.stop()
        EventMesh.publish("btn_ptt_off")

    def __speak_press_handle(self, *args):
        """
        群呼按键长按按下回调函数
        长按300ms以上算长按,否则算误按
        """
        EventMesh.publish("btn_ptt_on")
        # EventMesh.publish("btn_ptt_long")
        self.__longPress_handle()

    def __key1_press_handle(self):
        '''
        键盘S4：快捷键1 抬起
        '''
        # 
        self.__key1_btn_timer.stop()
        if not self.__key1_longPress_flag:
            EventMesh.publish("btn_key1")
        self.__key1_longPress_flag = False

    def __key2_press_handle(self):
        '''
        键盘S4：快捷键2 抬起
        '''
        # 
        self.__key2_btn_timer.stop()
        if not self.__key2_longPress_flag:
            EventMesh.publish("btn_key2")
        self.__key2_longPress_flag = False
    
    def __back_press_handle(self):
        '''
        键盘S4：返回键 抬起
        '''
        # 
        self.__back_btn_timer.stop()
        if not self.__back_longPress_flag:
            EventMesh.publish("btn_back")
        self.__back_longPress_flag = False

    def start(self):
        self.post_processor_after_instantiation()
