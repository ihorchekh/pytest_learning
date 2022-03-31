import pytest
from print_encap import print_encap
import logging

logger = logging.getLogger(__name__)

SUPPORTED_ENCAP_TYPES = ['v4_in_v4', 'v4_in_v6', 'v6_in_v4', 'v6_in_v6']

@pytest.fixture(scope="module", params=SUPPORTED_ENCAP_TYPES, autouse=True)
def encap_type(request):
    logger.error("encap_type fixture is working")
    yield request.param

@pytest.fixture(scope="module")
def setup(encap_type):
    logger.warning("Setup >>")
    yield encap_type
    logger.warning("Cleanup >>")


class TestDump:
    def dump_self(self, test_msg):
        # self.setup = setup
        logger.info(f"{test_msg} executed!")
        # print(f"{self.setup} executed!")
        assert True


class TestPrintEncap(TestDump):
    def test_print_encap(self, setup):
        """test print_encap"""
        # self.setup = setup
        self.dump_self(f"{setup} form {self.__class__.__name__} id: {id(setup)}")

    @pytest.mark.parametrize("encap", SUPPORTED_ENCAP_TYPES)
    def test_two(self, setup, encap):
        """test 2"""
        # self.setup = setup
        self.dump_self(f"{setup} and {encap} form {self.__class__.__name__} id: {id(setup)}")

    def test_three(self, setup):
        """test 3"""
        # self.setup = setup
        self.dump_self(f"{setup} form {self.__class__.__name__} id: {id(setup)}")

    def test_four(self, setup):
        """test 4"""
        # self.setup = setup
        self.dump_self(f"{setup} form {self.__class__.__name__} id: {id(setup)}")
