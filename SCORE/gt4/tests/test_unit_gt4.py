from ..gt4 import GT4
from tbears.libs.scoretest.score_test_case import ScoreTestCase
from iconservice import *


class TestGT4(ScoreTestCase):

    def setUp(self):
        super().setUp()

        self.mock_score_address = Address.from_string(f"cx{'1234'*10}")
        self.score = self.get_score_instance(GT4, self.test_account1)

    def test_get_name(self):
        self.assertEqual("GT4", self.score.name())

    def test_get_symbol(self):
        self.assertEqual("GT4", self.score.symbol())

    '''
    def test_get_token_list(self):
        print(self.score.get_token_list())

    def test_set_mint(self):
        self.set_msg(self.test_account1)
        self.score.mint(self.test_account1, 1, "Honda", "1991", "NSX", "Japan", "300", "150", "2000cc")
        self.assertEqual(self.score.ownerOf(1), self.test_account1)
        print(self.score.get_token_list())
    def test_set_transfer(self):
        self.set_msg(self.test_account1)
        self.score.mint(self.test_account1, 1)
        self.score.transfer(self.test_account2, 1)
        self.assertEqual(self.score.ownerOf(1), self.test_account2)

    def test_set_approve(self):
        self.set_msg(self.test_account1)
        self.score.mint(self.test_account1, 1)
        self.score.approve(self.test_account2, 1)
        self.assertEqual(self.score.getApproved(1), self.test_account2)

    def test_set_transferFrom(self):
        self.set_msg(self.test_account1)
        self.score.mint(self.test_account1, 1)
        self.score.transferFrom(self.test_account1, self.test_account2, 1)
        self.assertEqual(self.score.ownerOf(1), self.test_account2)

    def test_get_balanceOf(self):
        self.set_msg(self.test_account1)
        self.score.mint(self.test_account1, 1)
        self.score.mint(self.test_account2, 2)
        self.score.mint(self.test_account1, 3)
        self.score.mint(self.test_account2, 4)
        self.score.mint(self.test_account1, 5)
        self.assertEqual(self.score.balanceOf(self.test_account1), 3)
        self.assertEqual(self.score.balanceOf(self.test_account2), 2)

    def test_set_burn(self):
        self.set_msg(self.test_account1)
        self.score.mint(self.test_account1, 1)
        self.score.burn(1)
        with self.assertRaises(IconScoreException) as e:
            self.score.ownerOf(1)
        self.assertEqual(e.exception.code, 32)
        self.assertEqual(e.exception.message, "Invalid owner")
        self.assertEqual(self.score.balanceOf(self.test_account1), 0)

    def test_error_transfer(self):
        self.set_msg(self.test_account1)
        self.score.mint(self.test_account1, 1)
        self.score.mint(self.test_account2, 2)
        with self.assertRaises(IconScoreException) as e:
            self.score.transferFrom(self.test_account1, self.test_account2, 2)
        self.assertEqual(e.exception.code, 32)
        self.assertEqual(e.exception.message, "You don't have permission to transfer this NFT")
    '''
