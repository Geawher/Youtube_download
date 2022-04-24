from pafy import new 
url = input ('enter your url here')
video = new(url)

# To dowload video as music use this 
audio = video.audiostreams
audio[0].download()
# To download it as a video use this 
'''
d1 = video.getbest()
d1.download()'''
