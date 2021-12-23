# name=M-Audio Axiom AIR 32 MINI

import midi
import transport
import channels

Buttons = {
    'Start':  0x75,
    'Stop': 0x74,
    'ChannelUp': 0x2b,
    'ChannelDown': 0x2a,
    'ChannelSelector': 0x16,
}

def On

def OnMidiMsg(event):
#    print(hex(event.data1), event.data2, event.midiId)  #debug
    if event.midiId == midi.MIDI_CONTROLCHANGE:

        #Transport buttons
        #Stop
        if (event.data1 == Buttons['Stop'] and event.data2 > 0):
#            transport.stop()
            transport.globalTransport(midi.FPT_Stop, 1)
            event.handled = True

        #Start
        elif (event.data1 == Buttons['Start'] and event.data2 > 0):
            transport.start()
            event.handled = True

        #Channel up
        elif ((event.data1 == Buttons['ChannelSelector'] and event.data2 > 0x40) or (event.data1 == Buttons['ChannelUp'] and event.data2 > 0)):
            if channels.selectedChannel() < channels.channelCount()-1:
                channels.selectOneChannel(channels.selectedChannel(1)+1)
            event.handled = True

        #Channel down
        elif ((event.data1 == Buttons['ChannelSelector'] and event.data2 < 0x40) or (event.data1 == Buttons['ChannelDown'] and event.data2 > 0)):
            if channels.selectedChannel() > 0:
                channels.selectOneChannel(channels.selectedChannel()-1)
            event.handled = True

    # If the script does not recognize the event, do nothing.
    # It's then passed onto FL Studio to use.
        else:
            event.handled = False