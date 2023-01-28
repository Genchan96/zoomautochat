import pyautogui
import time
import pyperclip
import psutil
import pyautogui


file_name = "name.txt"

# ファイルを開く
with open(file_name, "r",encoding="utf-8") as file:
    # ファイルの内容を読み込む
    content = file.read()
    print(content)
    
file.close()

previous_pid = 0


while True:
    # 特定の名前のプロセス名
    process_name = "CptHost.exe"

    # 実行中のプロセスを取得
    for proc in psutil.process_iter():
        try:
            # プロセス名を取得
            pinfo = proc.as_dict(attrs=['pid', 'name'])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        else:
            # 指定したプロセス名かどうか判定
            if pinfo['name'] == process_name:
                #print(f"{process_name} is running.")
                pid = pinfo['pid']
    

     
                if pid != previous_pid:
                     if previous_pid != 0:


                            time.sleep(3)
                            pyautogui.hotkey('alt', 'h')
                            
                            time.sleep(3)
                            # キーボードに文字列を入力
                            pyperclip.copy(content)
                            pyautogui.hotkey('ctrl', 'v')
                        
                            # スペースを入力
                            pyautogui.typewrite(" ")

                            # Enterを入力
                            pyautogui.press("enter")

                       


                        
                     previous_pid = pid
         
     


 












