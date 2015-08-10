class TestModule:
    def __init__(self, language):
        self.tests = []
        self.language = language

    def init(self):
        pass

    def add_test(self, testname, func):
        self.tests.append((testname, func))

    def has_more_test(self):
        return True if len(self.tests) > 0 else False

    def get_test_name(self):
        return self.tests[0][0]

    def execute_next_test(self):
        test = self.tests[0]
        self.tests.pop(0)
        return test[1]()

    def get_module_name(self):
        return "Undefined name"
