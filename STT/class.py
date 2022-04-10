import speech_recognition as sr


class speechaudio:
    def __init__(self, audio_file: str):
        self.af = sr.AudioFile(audio_file)
        self.r = sr.Recognizer()
        self.a = None
        self.t = None

    def intp(self):
        with self.af as source:
            audio = self.r.record(source)  # read the entire audio file
        # recognize speech using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            print("Words are : \n" + self.r.recognize_google(audio))
            self.text = self.r.recognize_google(audio)
        except sr.UnknownValueError:
            print("unknown words")
        except sr.RequestError as re:
            print("request response; {0}".format(re))

    @property
    def completed(self) -> bool:
        return self.t is not None

    def __repr__(self):
        return self.t if self.t is None else "None"
