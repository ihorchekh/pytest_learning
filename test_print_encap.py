import allure
import pytest
from print_encap import print_encap
import logging

logger = logging.Logger("__main__")

SUPPORTED_ENCAP_TYPES = ['v4_in_v4', 'v4_in_v6', 'v6_in_v4', 'v6_in_v6']

@pytest.fixture(scope="module", params=SUPPORTED_ENCAP_TYPES, autouse=True)
def encap_type(request):
    logger.info("encap_type fixture is working")
    yield request.param

@pytest.fixture(scope="module")
def setup(encap_type):
    # print("Setup")
    logger.info("Setup >>")
    yield encap_type
    logger.info("Cleanup >>")
    # print("Cleanup")


# @pytest.mark.parametrize("encap_type", SUPPORTED_ENCAP_TYPES)

class TestDump:
    def dump_self(self, setup):
        self.setup = setup
        logger.info(f"{self.setup} executed!")
        # print(f"{self.setup} executed!")
        assert True


class TestPrintEncap(TestDump):
    def test_print_encap(self, setup):
        """test print_encap"""
        self.dump_self(setup)
        # self.setup = setup
        # print(f" >>> Test print_encap {self.setup} executed")
        # assert print_encap(self.setup) == f'Encap: {self.setup}'

class TestTwo(TestDump):
    def test_two(self, setup):
        """test 2"""
        self.dump_self(setup)
        # self.setup = setup
        # print(f" >>> Test 2 executed for {self.setup}")
        # assert True


