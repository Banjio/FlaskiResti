import unittest
import os
import json
from app import create_app, db


class BucketlistTestCase(unittest.TestCase):
    """This class represents the bucketlist test case"""

    def set_up(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.bucketlist = dict(name="Go to Ireland for vacation")

        # bind ap to current context
        with self.app.app_context():
            # create all tables
            db.create_all()

    def test_bucketlist_creation(self):
        """ Test if api cna create a bucketlist (POST request)"""
        res = self.client().post('/bucketlists/', data=self.bucketlist)
        self.assertEqual(res.status_code, 201)
        self.assertIn('Go to Ireland for vacation', str(res.data))

    def test_api_can_get_all_bucketlists(self):
        """Rest API can get a bucketlist (GET request)"""
        res = self.client().post('/bucketlists/', data=self.bucketlist)
        self.assertEqual(res.status_code, 201)
        res = self.client.get('/bucketlists/')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Go to Ireland for vacation', str(res.data))

    def test_api_can_get_bucketlist_by_id(self):
        """Test API can get a single bucketlist by using it's id"""
        rv = self.client().post('/bucketlists/',
                              data = dict(name="Eat, Beat, Sleep, Repeat"))
        self.assertEqual(rv.status_code, 201)
        rv = self.client().put('/bucketlists/1',
                               data=dict(name="Fly, High, My"))
        self.assertEqual(rv.status_code, 200)
        results = self.client().get('/bucketlists/1')
        self.assertIn('Fly', str(results.data))

    def test_bucketlist_deletion(self):
        """Test API can delete an existing bucketlist (DELETE request)"""
        rv = self.client().post(
            '/bucketlists/',
            data=dict(name="BABAJOJO")
        )
        self.assertEqual(rv.status_code, 201)
        res = self.client().delete('/bucketlists/')
        self.assertEqual(res.status_code, 200)
        # Test to see if it exists, should return a 404
        result = self.client().get('/bucketlists/')
        self.assertEqual(result.status_code, 404)

    def tear_down(self):
        """Teardown all initialized variables."""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

if __name__ == "__main__":
    unittest.main()