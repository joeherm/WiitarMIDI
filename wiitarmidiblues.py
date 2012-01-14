#Wiitar to MIDI Blues by Joe (thebroda)
#!/usr/bin/python 
#Green=16->z->52
#Red=64->x->53
#Yellow=8->c->54
#Blue=32->v->55
#Orange=128->b->56
#Plus=4096->n->57
#Minus=1024->m->58
#needs lineakd/python cwiid for usage
#16384=down
#1=up

import cwiid, os, sys,time, pygame, pygame.midi
from pygame.locals import *
pygame.init()
pygame.midi.init()
midi_out = pygame.midi.Output(0, 0)
midi_out.set_instrument(0)
print "Press 1+2 on your wiimote."
print "Connecting..."
wm = cwiid.Wiimote()
if wm:
	wm.rumble=True;time.sleep(.2);wm.rumble=False
	print "Connected Wiimote."
wm.enable(cwiid.FLAG_MESG_IFC)
wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_STATUS | cwiid.RPT_CLASSIC

note=0
okey=0
base=0
chan=input("Channel 1-16:")+143
def release(key):
	midi_out.write_short(chan,key,0)
	print chan,key
while 1:
	messages=wm.get_mesg()
	for message in messages:
		if message[0]==cwiid.MESG_CLASSIC:
			x=message[1]
			note=x['buttons']
			if x['buttons']==16:
				release(okey)				
				okey=60+base
				midi_out.write_short(chan,60+base,120)
			if x['buttons']==64:
				release(okey)				
				okey=61+base
				midi_out.write_short(chan,61+base,120)
			if x['buttons']==8:
				release(okey)				
				okey=63+base
				midi_out.write_short(chan,63+base,120)
			if x['buttons']==32:
				release(okey)				
				okey=65+base
				midi_out.write_short(chan,65+base,120)
			if x['buttons']==128:
				release(okey)				
				okey=66+base
				midi_out.write_short(chan,66+base,120)
			if x['buttons']==4096:
				release(okey)
				okey=67+base
				midi_out.write_short(chan,67+base,120)
			if x['buttons']==1024:
				release(okey)
				okey=68+base
				midi_out.write_short(chan,68+base,120)
			if x['buttons']==0:
				release(okey)
				okey=0

#octaves
			if x['buttons']==16384:
				base-=12

			if x['buttons']==1:
				base+=12

#sharps
			if x['buttons']==80:
				release(okey)
				okey=61+base
				midi_out.write_short(chan,61+base,120)
			if x['buttons']==72:
				release(okey)				
				okey=63+base
				midi_out.write_short(chan,63+base,120)
			if x['buttons']==160:
				release(okey)
				okey=66+base
				midi_out.write_short(chan,66+base,120)
			if x['buttons']==4224:
				release(okey)
				okey=68+base
				midi_out.write_short(chan,68+base,120)
			if x['buttons']==5120:
				release(okey)
				okey=70+base
				midi_out.write_short(chan,70+base,120)
			
		

				



            

