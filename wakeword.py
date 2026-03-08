import pvporcupine
import pyaudio
import struct

WAKE_WORD = "jarvis"

def listen_for_wake_word():

    print("Listening for wake word...")

    porcupine = pvporcupine.create(
        keywords=[WAKE_WORD]
    )

    pa = pyaudio.PyAudio()

    audio_stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )

    try:
        while True:

            pcm = audio_stream.read(porcupine.frame_length)

            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            keyword_index = porcupine.process(pcm)

            if keyword_index >= 0:

                print("Wake word detected!")

                return True

    finally:

        audio_stream.close()

        pa.terminate()

        porcupine.delete()