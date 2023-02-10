import os
import pyautogui

fname = '../settings1.txt'
if os.path.exists(fname):
    with open(fname, 'r', encoding='shift_jis') as f:
        lines = f.read().splitlines()

    lines = [x.strip() for x in lines if x != '']
    lines = [x.split('#') for x in lines]
    
    for line in lines:
        if len(line) >= 2:
            if line[1][:5] == 'enter':
                pyautogui.press('enter')
            
            elif line[1][:5] == 'click':
                position = line[0].split(',')
                if len(position) == 2:
                    if position[0].strip().isdecimal() and position[1].strip().isdecimal():
                        pyautogui.moveTo(int(position[0].strip()), int(position[1].strip()), duration=0.1)
                        pyautogui.click()
                
                elif len(position) == 3:
                    if position[0].strip().isdecimal() and position[1].strip().isdecimal():
                        try:
                            time = float(position[2])
                        except ValueError:
                            time = 0.1
                        pyautogui.moveTo(int(position[0].strip()), int(position[1].strip()), duration=time)
                        pyautogui.click()
                        
            elif line[1][:5] == 'input':
                pyautogui.write(line[0].strip())

            elif line[1][:5] == 'ctrlv':
                pyautogui.hotkey('ctrl', 'v')
