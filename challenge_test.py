# Ken Burcham - Fun little programming challenge - Dec 18, 2016
# challenge unittest

import challenge, unittest

#test to see that our encode and decode functions produce the proper result.
class EncodeTest(unittest.TestCase):
    def testEncode(self):
        self.assertEqual(challenge.fEncode(0),"4000")
        self.assertEqual(challenge.fEncode(-8192),"0000")
        self.assertEqual(challenge.fEncode(8191),"7f7f")
        self.assertEqual(challenge.fEncode(2048),"5000")
        self.assertEqual(challenge.fEncode(-4096),"2000")

    def testDecode(self):
        self.assertEqual(challenge.fDecode("40","00"),0)
        self.assertEqual(challenge.fDecode("00","00"),-8192)
        self.assertEqual(challenge.fDecode("7f","7f"),8191)
        self.assertEqual(challenge.fDecode("50","00"),2048)
        self.assertEqual(challenge.fDecode("0a","05"),-6907)
        self.assertEqual(challenge.fDecode("55","00"),2688)

if __name__ == '__main__':
    unittest.main()
