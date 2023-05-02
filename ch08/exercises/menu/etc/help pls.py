
from pydub import AudioSegment
from pydub.playback import play


# from pygame import mixer
path = "C:\\Users\\Kimora\Desktop\\Downloads"
# mixer.init()
# mixer.music.load('Nope-Sound-Effect.mp3')


# # load the sound file
sound = AudioSegment.from_mp3("Nope-Sound-Effect.mp3")
play(sound)
