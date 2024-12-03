from midiutil import MIDIFile

# Create a single track MIDI file
midi = MIDIFile(1)

# Tempo and time signature
track = 0
time = 0  # Start time
midi.addTempo(track, time, 90)
midi.addTimeSignature(track, time, 7, 3, 24)  # 7/8 time signature

# Note definitions (MIDI note numbers)
E5 = 40  # Low E power chord root note
A5 = 45  # A power chord root note
G5 = 43  # G power chord root note
D5 = 38  # D power chord root note
velocity = 64  # Medium volume

# Helper function to add a note or chord
def add_chord(midi, track, time, notes, duration, velocity):
    for note in notes:
        midi.addNote(track, channel=0, pitch=note, time=time, duration=duration, volume=velocity)

# Bar 1
add_chord(midi, track, time, [E5], 0.5, velocity)  # Palm mute E5
time += 0.5
add_chord(midi, track, time, [E5], 0.5, velocity)  # Palm mute E5
time += 0.5
add_chord(midi, track, time, [E5], 0.5, velocity)  # Palm mute E5
time += 0.5
add_chord(midi, track, time, [A5], 1, velocity)    # Sustain A5
time += 1

# Bar 2
add_chord(midi, track, time, [E5], 0.5, velocity)  # Palm mute E5
time += 0.5
add_chord(midi, track, time, [E5], 0.5, velocity)  # Palm mute E5
time += 0.5
add_chord(midi, track, time, [G5], 0.5, velocity)  # Transition G5
time += 0.5
add_chord(midi, track, time, [D5], 0.5, velocity)  # Transition D5
time += 0.5
add_chord(midi, track, time, [A5], 1, velocity)    # Sustain A5
time += 1

# Bar 3
add_chord(midi, track, time, [E5], 0.5, velocity)  # Palm mute E5
time += 0.5
add_chord(midi, track, time, [A5], 1, velocity)    # Sustain A5
time += 1

# Save to file
with open("guitar_code_translation.mid", "wb") as output_file:
    midi.writeFile(output_file)

print("MIDI file saved as 'guitar_code_translation.mid'")
