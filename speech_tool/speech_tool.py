from collections import deque
import speech_recognition as sr
import threading
from factory import speechaudio



class audioqueue:
    def __init__(self, mt=3):
        self.mt = mt
        self.aq = deque()
        self.pa = deque()

    def aa(self, filepath: str):
        self.aq.append(speechaudio(audio_file=filepath))
        # use speech recognition to

    def ia(self):
        ta = []
        while self.aq:
            for i in range(self.mt):
                sa = self.aq.popleft()
                ta.append(
                    (threading.Thread(target=sa.intp), sa)
                )
                ta[-1][0].start()
                if not self.aq:
                    break
            # wait for these threads to finish before starting new ones
            for thread, audio in ta:
                thread.join()
                self.pa.append(audio)


if __name__ == "__main__":
    aq = audioqueue()
    aq.aa("C:/Users/bobga/EC530/project4/STT/audios/1.wav")
    aq.aa("C:/Users/bobga/EC530/project4/STT/audios/2.wav")
    aq.aa("C:/Users/bobga/EC530/project4/STT/audios/3.wav")
    aq.ia()
