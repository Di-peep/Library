"""
This module defines the test cases for department service
"""
# standard library imports

# local imports

from app import database
from app.models.admin import Admin
from app.service import admin
from app.tests.ConfigurationTests import ConfigurationTest


class TestAdminService(ConfigurationTest):
    """
    This is the class for admin service test cases
    """

    def test_get_all_admins(self):
        """
        Adds  test records and tests the result
        """
        admin1 = Admin(username="12345", password="admin", avatar=None, full_name='Name')
        admin2 = Admin(username="admin", password="12345", avatar=None, full_name='Name2')
        database.session.add(admin1)
        database.session.add(admin2)
        database.session.commit()
        self.assertEqual(2, len(admin.get_all_admin()))

    def test_get_admin_by_username(self):
        """
        Adds  test records and tests the result
        """
        admin1 = Admin(username="12345", password="admin", full_name='Name1', avatar=None)
        admin2 = Admin(username="admin", password="12345", full_name='Name2', avatar=None)
        database.session.add(admin1)
        database.session.add(admin2)
        database.session.commit()
        self.assertEqual(1, len([admin.get_admin_by_name('admin')]))

    def test_check_if_is_available(self):
        """
        This module tests if file format is posiible to download
        """
        filename = 'test.png'
        file = filename.rsplit('.', 1)[1]
        self.assertEqual('png', file)

    def test_check_if_is_not_available(self):
        """
        This module tests if file format is not posiible to download
        """
        filename = 'test.jpg'
        file = filename.rsplit('.', 1)[1]
        self.assertNotEqual('png', file)

    def test_not_updated_avatar(self):
        """
        This module tests not updated avatar
        """
        admin1 = Admin(username="12345", password="admin", full_name='Name1', avatar=None)
        database.session.add(admin1)
        database.session.commit()
        result = admin.update_avatar('something', '12345')
        self.assertEqual(False, result)

    def test_updated_avatar(self):
        """
        This module tests  updated avatar
        """
        admin1 = Admin(username="admin", password="admin", full_name='Name1', avatar=None)
        database.session.add(admin1)
        database.session.commit()
        result = admin.update_avatar(bytes('avatar.png', encoding='utf8'), 'admin')
        self.assertEqual(True, result)

    def test_get_avatar(self):
        """
        This module test getting avatar
        """
        avatar = 'avatar.png'
        admin1 = Admin(username="admin", password="admin", full_name='Name1',
                       avatar=bytes(avatar, encoding='utf8'))
        database.session.add(admin1)
        database.session.commit()
        is_get = admin.get_avatar('admin')
        self.assertEqual(avatar, is_get.decode("utf-8"))
