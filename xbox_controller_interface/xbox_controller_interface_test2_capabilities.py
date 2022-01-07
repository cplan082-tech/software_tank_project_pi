import evdev

device = evdev.InputDevice('/dev/input/event7')
print(device)

print(device.capabilities(verbose=True))