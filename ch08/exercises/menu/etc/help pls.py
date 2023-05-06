import os
from pydub import AudioSegment
from pydub.playback import play
# import vlc

# p = vlc.MediaPlayer("etc/Nope-Sound-Effect.mp3")
# p.play()


# from pygame import mixer
# path = "C:\\Users\\Kimora\Desktop\\Downloads"
# mixer.init()
# mixer.music.load('Nope-Sound-Effect.mp3')


# # # load the sound file
# noise = 
# sound = AudioSegment.from_mp3("C://Users/Kimora/Desktop/Downloads/Nope-Sound-Effect.mp3")
# play(sound)
# sound.export("etc/Nope-Sound-Effect.wav", format="wav")
# sound.play()

test = AudioSegment.from_file(os.path.expanduser("~/Downloads/Nope-Sound-Effect.mp3"))
play(test)
#sound_file = AudioSegment.from_file(os.path.expanduser("~/Downloads/mysound.mp3"))
