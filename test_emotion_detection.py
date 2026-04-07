import unittest
from EmotionDetection.emotion_detection import emotion_detector

class EmotionDetectionTest(unittest.TestCase):

    def test_emotion_detector(self):
        resp = emotion_detector("I am glad this happened")
        dominant_emotion = resp["dominant_emotion"]
        self.assertEqual(dominant_emotion, "joy")

        resp = emotion_detector("I am really mad about this")
        dominant_emotion = resp["dominant_emotion"]
        self.assertEqual(dominant_emotion, "anger")

        resp = emotion_detector("I feel disgusted just hearing about this")
        dominant_emotion = resp["dominant_emotion"]
        self.assertEqual(dominant_emotion, "disgust")

        resp = emotion_detector("I am so sad about this")
        dominant_emotion = resp["dominant_emotion"]
        self.assertEqual(dominant_emotion, "sadness")

        resp = emotion_detector("I am glad this happened")
        dominant_emotion = resp["dominant_emotion"]
        self.assertEqual(dominant_emotion, "joy")

        resp = emotion_detector("I am really afraid that this will happen")
        dominant_emotion = resp["dominant_emotion"]
        self.assertEqual(dominant_emotion, "fear")


if __name__ == '__main__':
    unittest.main()