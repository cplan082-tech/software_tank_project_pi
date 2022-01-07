from evdev import InputDevice, categorize, ecodes

gamepad = InputDevice('/dev/input/event7')

# button code variables
btn_a = 304
btn_b = 305
btn_x = 307
btn_y = 308

btn_leftBumper = 310
btn_rightBumper = 311

btn_leftJoy = 317
btn_rightJoy = 318

btn_start = 315
btn_back = 158
btn_home = 316 # Backlight Xbox home button
 
# analog inputs code variables
## Joystick max val = 65535 (2 bytes)
al_leftJoy_x = 0
al_leftJoy_y = 1  # Axis is inverted
al_rightJoy_x = 2
al_rightJoy_y = 5  # Axis is inverted

## Trig max val = 1023 (10 bits)
al_rightTrig = 9
al_leftTrig = 10

## D-pad val can be either 1, 0, or -1
al_dpad_x = 16
al_dpad_y = 17  # Axis is inverted


#loop and filter by event code
for event in gamepad.read_loop():
    
    if event.type == ecodes.EV_KEY:
        
        if event.value == 1:
            
            if event.code == btn_a:
                continue
#                 print("A")
                
            elif event.code == btn_b:
                continue
#                 print("B")
                
            elif event.code == btn_x:
                continue
#                 print("X")
                
            elif event.code == btn_y:
                continue
#                 print("Y")
                
            elif event.code == btn_leftBumper:
                continue
#                 print("Left Bumper")
                
            elif event.code == btn_rightBumper:
                continue
#                 print("Right Bumper")
                
            elif event.code == btn_start:
                continue
#                 print("Start")
                
            elif event.code == btn_home:
                continue
#                 print("Home")
                
            elif event.code == btn_back:
                continue
#                 print("Back")
                
            elif event.code == btn_leftJoy:
                continue
#                 print("Left Joystick")
            
            elif event.code == btn_rightJoy:
                continue
#                 print("Right Joystick")
 
