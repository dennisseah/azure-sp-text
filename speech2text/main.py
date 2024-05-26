import time

import azure.cognitiveservices.speech as speechsdk
import azure.cognitiveservices.speech.languageconfig as spxlangconfig
from azure.cognitiveservices.speech import SpeechRecognitionEventArgs, SpeechRecognizer

from speech2text.main_args import get_args
from speech2text.mp42wav import generate as generate_wav
from speech2text.settings import Settings


class Recognizer:
    def create_speech_recognizer(
        self, wav_file: str, spx_lang: str
    ) -> SpeechRecognizer:
        """Create a speech recognizer object.

        :param wav_file: str: Path to the wav file.
        :param spx_lang: str: Language code.
        :return: SpeechRecognizer: Speech recognizer object.
        """
        settings = Settings.model_validate({})

        auto_detect_language_config = spxlangconfig.AutoDetectSourceLanguageConfig(
            languages=[spx_lang],
        )
        speech_config = speechsdk.SpeechConfig(
            subscription=settings.spx_subscription_key,
            region=settings.spx_region,
        )
        audio_input = speechsdk.AudioConfig(filename=wav_file)
        return speechsdk.SpeechRecognizer(
            speech_config=speech_config,
            audio_config=audio_input,
            auto_detect_source_language_config=auto_detect_language_config,
        )

    def recognize(self, file_path: str, lang: str, pause_sec: int) -> str:
        """Recognize the speech from the wav file.

        :param file_path: str: Path to the MP4 file.
        :param lang: str: Language code.
        :param pause: int: Pause in seconds.
        :return: str: Recognized text.
        """
        wav_file = generate_wav(file_path)
        texts: list[str] = []
        last_text_len = 0

        def recognized_callback(evt: SpeechRecognitionEventArgs):
            if evt.result.reason == speechsdk.ResultReason.RecognizedSpeech:
                texts.append(evt.result.text)

        recognizer = self.create_speech_recognizer(wav_file=wav_file, spx_lang=lang)
        recognizer.recognized.connect(recognized_callback)
        recognizer.start_continuous_recognition_async()

        time.sleep(pause_sec)
        while last_text_len != len(texts):
            last_text_len = len(texts)
            time.sleep(pause_sec)

        recognizer.stop_continuous_recognition_async()
        return " ".join(texts)


if __name__ == "__main__":
    args = get_args()
    recognizer = Recognizer()
    text = recognizer.recognize(
        file_path=args.file_path, lang=args.lang, pause_sec=args.max_pause
    )
    print(text)
