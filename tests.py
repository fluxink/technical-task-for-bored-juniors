import unittest
from unittest.mock import patch

from bored_api import get_activity
from bored_db import BoredDB


class TestBoredAPI(unittest.TestCase):
    @patch("bored_api.requests.get")
    def test_get_activity(self, mock_get):
        mock_get.return_value.json.return_value = {
            "activity": "Learn Express.js",
            "type": "education",
            "participants": 1,
            "price": 0.1,
            "link": "https://expressjs.com/",
            "key": "3943509",
            "accessibility": 0.25,
        }
        response = get_activity(type="education", participants=1)
        self.assertEqual(response["activity"], "Learn Express.js")
        self.assertEqual(response["type"], "education")
        self.assertEqual(response["participants"], 1)
        self.assertEqual(response["price"], 0.1)
        self.assertEqual(response["link"], "https://expressjs.com/")
        self.assertEqual(response["key"], "3943509")
        self.assertEqual(response["accessibility"], 0.25)


class TestBoredDB(unittest.TestCase):
    def test_save_and_retrieve_activity(self):
        with BoredDB(":memory:") as bored_db:
            activity = {
                "activity": "Learn Express.js",
                "type": "education",
                "price": 0.1,
                "participants": 1,
                "link": "https://expressjs.com/",
                "key": "3943509",
                "accessibility": 0.25,
            }
            bored_db.save_activity(activity)
            last_activities = bored_db.get_last_activities(1)
            self.assertEqual(len(last_activities), 1)
            self.assertEqual(last_activities[0][1], "Learn Express.js")
            self.assertEqual(last_activities[0][2], "education")
            self.assertEqual(last_activities[0][3], 1)
            self.assertEqual(last_activities[0][4], 0.1)
            self.assertEqual(last_activities[0][5], "https://expressjs.com/")
            self.assertEqual(last_activities[0][6], "3943509")
            self.assertEqual(last_activities[0][7], 0.25)


if __name__ == '__main__':
    unittest.main()
