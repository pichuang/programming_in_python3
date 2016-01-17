import unittest
from DP_Abstract_Factory.abstract_factory import *

class TestPetShop(unittest.TestCase):
    def test_DogFactory(self):
        dogshop = PetShop(DogFactory())
        dogshop.show_pet()

    def test_CatFactory(self):
        catshop = PetShop(CatFactory())
        catshop.show_pet()


if __name__ == "__main__":
    unittest.main()
