# name=M-Audio Axiom AIR 32 MINI

import midi
import ui
import transport
import channels
import mixer
import device
from time import sleep

Buttons = {
    'Stop': 0x10,
    'Start':  0x11,
    'Rec': 0x12,
    'Up': 0x13,
    'Down': 0x14,
    'Right': 0x15,
    'Left': 0x16,
    'Middle': 0x17,
    'Hyper': 0x3A,
}

#def OnMidiIn(event):
#    event.handled = False
#    if event.data1 == Buttons['Hyper']:
#        if event.data2 > 0:
#            ui.setHintMsg(SECONDAY_MODE_HINT)
#            SEC_COUNTER = 2
#        else:
#            ui.setHintMsg('')

#def OnInit():
#    print(mixer.trackNumber())

def OnMidiMsg(event):
    print(f'data1: {hex(event.data1)},\ndata2: {event.data2},\nchannel:{event.midiChan},\nport:{event.port},\nmidiId: {event.midiId}\n')  #debug

def OnControlChange(event):
    if event.data2 > 0:

        #Transport buttons
        #Start
        if event.data1 == Buttons['Start']:
            transport.start()
            event.handled = True
        #Stop
        elif event.data1 == Buttons['Stop']:
            transport.stop()
    #        transport.globalTransport(midi.FPT_Stop, 1)
            event.handled = True
        #Rec
        elif event.data1 == Buttons['Rec']:
            transport.record()
            event.handled = True

        #Channel navigation
        #Channel up
        elif (event.data1 == Buttons['Down'] and channels.selectedChannel() < channels.channelCount() - 1):
            channels.selectOneChannel(channels.selectedChannel(1) + 1)
            event.handled = True

        #Channel down
        elif (event.data1 == Buttons['Up'] and channels.selectedChannel() > 0):
            channels.selectOneChannel(channels.selectedChannel() - 1)
            event.handled = True

        #Mixer navigation
        #Right
        elif (event.data1 == Buttons['Right'] ):
            mixer.setTrackNumber(mixer.trackNumber() + 1, midi.curfxScrollToMakeVisible)

        #Left
        elif (event.data1 == Buttons['Left'] ):
            mixer.setTrackNumber(mixer.trackNumber() - 1, midi.curfxScrollToMakeVisible)
#            while event.data2 > 0:
#                sleep(1)
#                mixer.setTrackNumber(mixer.trackNumber() - 1, midi.curfxScrollToMakeVisible)