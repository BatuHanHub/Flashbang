# I added the libraries
from tkinter import * # add window library
import pygame # add game engine and media player library so I using music player

pygame.init() # Added game engine/media player

# Sound process {
sound1 = pygame.mixer.Sound('trowflash.mp3')
sound2 = pygame.mixer.Sound('flash.mp3')
sound1.set_volume(100.0)
sound2.set_volume(100.0)

channel = pygame.mixer.Channel(0)  
pygame.time.delay(500)
channel.play(sound1)  
pygame.time.delay(1000)
channel.play(sound2)
# }

window = Tk() # Create window
window.attributes('-fullscreen', True) # window fullscreen
window.attributes('-topmost', True) # window priority
window.after(4000, window.destroy)  # After 5 seconds the window will disappear.

window.mainloop() # window is looped. If i don't use window closes immediately.

pygame.quit() # exit game engine/media player
