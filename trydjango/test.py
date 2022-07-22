from django.test import TestCase
import os
from django.conf import settings
from django.contrib.auth.password_validation import validate_password

class TryDjangoConfigTest(TestCase):
    #some base test for example:
    def test_secrete_key_strangth(self):
        #examples:
        # self.assertTrue(1==1)
        # self.assertFalse(1==2)
        # self.assertIsNone(1==1)
        # self.assertIsNotNone(1==1)
        # self.assertEqual(1, 2)
        # self.assertNotEqual(1, 2)
        # SECRET_KEY = os.environ.get('DJANGO_SECRETE_KEY')
        secret_key = settings.SECRET_KEY
        # self.assertNotEqual(secret_key, "123abc")
        try:
            is_strong = validate_password(secret_key)
        except Exception as e:
            msg = f'Bad secrete key: {e.messages}'
            self.fail(e)
            
