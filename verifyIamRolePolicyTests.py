import unittest
from verifyIamRolePolicy import verify_iam

class TestIAMRolePolicyVerification(unittest.TestCase):
    def test_valid_policy(self):
        file_path = 'valid_policy.json'
        self.assertTrue(verify_iam(file_path)) #returns true

    def test_invalid_policy_single_asterisk(self):
        file_path = 'invalid_policy_single_asterisk.json'
        self.assertFalse(verify_iam(file_path)) #returns false

    def test_invalid_policy_multiple_asterisks(self):
        file_path = 'invalid_policy_multiple_asterisks.json'
        self.assertFalse(verify_iam(file_path)) #returns true

    def test_missing_resource_field(self):
        file_path = 'missing_resource_field.json'
        self.assertTrue(verify_iam(file_path)) #returns true

    def test_non_string_resource_field(self):
        file_path = 'non_string_resource_field.json'
        self.assertFalse(verify_iam(file_path)) #returns false

    def test_invalid_json_format(self):
        file_path = 'invalid_json_format.json'
        self.assertFalse(verify_iam(file_path)) #returns false

    def test_nonexistent_file(self):
        file_path = 'nonexistent_file.json'
        self.assertFalse(verify_iam(file_path)) #returns false

if __name__ == '__main__':
    unittest.main()