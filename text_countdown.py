from sense_emu import SenseHat
from time import sleep

sense_emulator = SenseHat()
G = [0, 255, 0]
R = [100, 0, 0]

for i in range(9, 0, -1):
    sense_emulator.show_letter(f'{i}', R)
    R[0] += 15
    sleep(1)

P = [255, 0, 255]
sense_emulator.show_letter('0', P)