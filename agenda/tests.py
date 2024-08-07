from django.test import TestCase
from agenda.models import Talk, Track
from conference_auth.models import ConferenceUser

class TalkSubmittedTestCase(TestCase):
    def setUp(self):
        self.track = Track.objects.create(name="Track 1", description="Description for Track 1")
        self.speaker = ConferenceUser.objects.create_user(username="speaker", password="password")
        self.talk = Talk.objects.create(
            title="Talk 1",
            abstract="Abstract for Talk 1",
            track=self.track,
            speaker=self.speaker
        )

    def test_talk_submission(self):
        self.assertEqual(self.talk.title, "Talk 1")
        self.assertEqual(self.talk.abstract, "Abstract for Talk 1")
        self.assertEqual(self.talk.track, self.track)
        self.assertEqual(self.talk.speaker, self.speaker)
        self.assertEqual(self.talk.status, "submitted")
