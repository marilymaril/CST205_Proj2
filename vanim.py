import numpy as np
import gizeh
import moviepy.editor as mpy

W,H=128,128 #width,height, in pixels
duration=2 #duration of the clip, in seconds
ncircles =20

def make_frame(t):
	surface = gizeh.Surface(W,H)

	for i in range(ncircles):
		angle = 2*np.pi*(1.0*i/ncircles+t/duration)
		center = W*(0.5+gizeh.polar2cart(0.1,angle))
		circle = gizeh.circle(r=W*(1.0-1.0*i/ncircles),
					xy=center,fill=(i%2,i%2,i%2))
		circle.draw(surface)

	return surface.get_npimage()

clip = mpy.VideoClip(make_frame, duration=duration)
clip.write_gif("circle.gif",fps=15,opt="OptimizePlus", fuzz=10)	


