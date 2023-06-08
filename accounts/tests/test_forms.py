from django.test import TestCase
from django.http import HttpRequest

from accounts.forms import CustomSignUpForm


class CustomSignUpFormTest(TestCase):
    """
    Test for CustomSignUpForm
    """

    def test_form_fields(self):
        """
        Test that the form has the correct fields
        """

        form = CustomSignUpForm()
        self.assertTrue(form.fields['first_name'])
        self.assertTrue(form.fields['last_name'])
        self.assertTrue(form.fields['email'])
        self.assertTrue(form.fields['password1'])
        self.assertTrue(form.fields['password2'])
        self.assertTrue(form.fields['remember_me'])

    def test_required_fields(self):
        """
        Test that the form has the correct required fields
        """

        form = CustomSignUpForm()
        self.assertTrue(form.fields['first_name'].required)
        self.assertTrue(form.fields['last_name'].required)
        self.assertTrue(form.fields['email'].required)
        self.assertTrue(form.fields['password1'].required)
        self.assertTrue(form.fields['password2'].required)
        self.assertFalse(form.fields['remember_me'].required)

    def test_init_method(self):
        """
        Test that the form has the correct labels
        """

        form = CustomSignUpForm()
        self.assertEqual(form.fields['email'].required, True)
        self.assertEqual(form.fields['first_name'].label, False)
        self.assertEqual(form.fields['last_name'].label, False)
        self.assertEqual(form.fields['email'].label, False)
        self.assertEqual(form.fields['password1'].label, False)
        self.assertEqual(form.fields['password2'].label, False)
        self.assertEqual(
            form.fields['password2'].widget.attrs['placeholder'], 'Confirm Password')

    def test_save_method(self):
        """
        Test that the form saves the correct data
        """
        request = HttpRequest()
        request.session = {}
        form = CustomSignUpForm({'first_name': 'Test',
                                 'last_name': 'User',
                                 'email': 'testuser@mail.com',
                                 'password1': 'qwerty123.!',
                                 'password2': 'qwerty123.!'})
        self.assertTrue(form.is_valid())
        user = form.save(request)
        self.assertEqual(user.first_name, 'Test')
        self.assertEqual(user.last_name, 'User')
