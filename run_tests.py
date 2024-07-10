import unittest

if __name__ == "__main__":
    print("Starting tests...")
    result = unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().discover('src'))
    print("Finished running tests.")
    if result.wasSuccessful():
        print("...")
        print("OK")