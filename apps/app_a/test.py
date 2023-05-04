try:
    import unittest
    from app_a import application
except Exception as e:
    print("Some modules are missing {}".format(e))


class AppATest(unittest.TestCase):

    # Check for response 200
    def test_hello_status(self):
        tester = application.test_client(self)
        response = tester.get("/hello")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # Check if the content returned is application/json
    def test_hello_content(self):
        tester = application.test_client(self)
        response = tester.get("/hello") 
        self.assertEqual(response.content_type, "text/html; charset=utf-8")

    # Check if the string returned is Hello there
    def test_hello_text(self):
        tester = application.test_client(self)
        response = tester.get("/hello") 
        self.assertEqual(response.text, "Hello there")

        

if __name__ == "__main__":
    unittest.main()
