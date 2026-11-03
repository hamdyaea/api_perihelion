# Developer: Hamdy Abou El Anein
# Contact: hamdy.aea@protonmail.com
import unittest
from app import create_app
from data import perihelion


class ApiTests(unittest.TestCase):
    def setUp(self):
        self.client = create_app().test_client()

    def test_collection_and_zero_alias(self):
        for url in ("/", "/0"):
            self.assertEqual(self.client.get(url).json, perihelion)

    def test_every_object(self):
        for item in perihelion:
            self.assertEqual(self.client.get("/" + str(item["id"])).json, item)

    def test_missing_object(self):
        missing = max(item["id"] for item in perihelion) + 1
        response = self.client.get("/" + str(missing))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, "Object not found")

    def test_writes_not_allowed(self):
        self.assertEqual(self.client.post("/").status_code, 405)


if __name__ == "__main__":
    unittest.main()
