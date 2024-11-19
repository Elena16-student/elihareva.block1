import unittest
import module_12_1_2 as M
import module_12_2_2 as N

mod_12_ST = unittest.TestSuite()

mod_12_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(M.RunnerTest))
mod_12_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(N.TournamentTest))


test_runner = unittest.TextTestRunner(verbosity=2)
test_runner.run(mod_12_ST)