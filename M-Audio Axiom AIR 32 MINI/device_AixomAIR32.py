# name=M-Audio Axiom AIR 32 MINI

import midi
import transport
import channels
import device

Buttons = {
    'Start':  0x75,
    'Stop': 0x74,
    'Rec': 0x76,
    'ChannelUp': 0x14,
    'ChannelDown': 0x13,
}

def OnMidiMsg(event):
    print(f'data1: {hex(event.data1)},\ndata2: {event.data2},\nchannel:{event.midiChan},\nport:{event.port},\nmidiId: {event.midiId}\n')  #debug

def OnControlChange(event):

    #Transport buttons
    #Start
    if (event.data1 == Buttons['Start'] and event.data2 > 0):
        transport.start()
        event.handled = True
    #Stop
    elif (event.data1 == Buttons['Stop'] and event.data2 > 0):
        transport.stop()
#        transport.globalTransport(midi.FPT_Stop, 1)
        event.handled = True
    #Rec
    elif(event.data1 == Buttons['Rec'] and event.data2 > 0):
        transport.record()
        event.handled = True


    #Channel up
    elif (event.data1 == Buttons['ChannelUp'] and event.data2 > 0):
        if channels.selectedChannel() < channels.channelCount()-1:
            channels.selectOneChannel(channels.selectedChannel(1)+1)
        event.handled = True

    #Channel down
    elif (event.data1 == Buttons['ChannelDown'] and event.data2 > 0):
        if channels.selectedChannel() > 0:
            channels.selectOneChannel(channels.selectedChannel()-1)
        event.handled = True
    
