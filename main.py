import unittest

from MolekylSyntax import *


class SyntaxTest(unittest.TestCase):

    def testKorrektMol(self):
        """ Testar BLetter, SLetter och Num """
        self.assertEqual(kollaMolekyl("Fe12"),
                         "Formeln är syntaktiskt korrekt")

    def testFelBL(self):
        self.assertEqual(kollaMolekyl("cr12"),
                         "Saknad stor bokstav vid radslutet cr12")

    def testFelSL(self):
        self.assertEqual(kollaMolekyl("a"),
                         "Saknad stor bokstav vid radslutet a")

    def testNum(self):
        self.assertEqual(kollaMolekyl("Cr0"),
                         "För litet tal vid radslutet ")


if __name__ == '__main__':
    unittest.main()
