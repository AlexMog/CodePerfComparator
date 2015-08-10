from optparse import OptionParser
import importlib, time

class CodeTester:
    def __init__(self, options, args):
        self.objects = []
        self.options = options
        self.module = options.module
        self.args = args
        self.avgs = []
        self.moduleObj = None
        self.tests_results = []

    def init(self):
        self.print_verbose("==== Initialisating CodeTester modules ====")
        for arg in self.args:
            self.load_module(arg)

    def load_module(self, language):
        try:
            if self.moduleObj == None:
                self.print_verbose("Loading module %s" %self.module)
                self.moduleObj = importlib.import_module('test_modules.%s' %self.module)
            self.objects.append(getattr(self.moduleObj, self.module + "Test")(language))
        except Exception, e:
            print e
            exit()

    def print_verbose(self, msg):
        if self.options.verbose:
            print msg

    def execute_tests(self):
        start_time = time.time()
        self.print_verbose("==== Starting tests ====")
        for module in self.objects:
            module_results = []
            self.print_verbose("Executing module %s for %s langugage..." %(module.get_module_name(), module.language))
            self.print_verbose("Initialisating datas...")
            module.init()
            self.print_verbose("Executing tests...")
            test_total_time = 0
            test_num = 0
            func_call_time = time.time()
            while module.has_more_test():
                test_name = module.get_test_name()
                exec_time = time.time()
                ret = module.execute_next_test()
                exec_time = time.time() - exec_time
                self.print_verbose("Test '%s' executed in %s (python)/%s (test return) seconds." %(test_name, exec_time, ret))
                test_num += 1
                test_total_time += ret
                module_results.append((test_name, exec_time, ret))
            if test_num > 0:
                self.print_verbose("Tests total execution time: %s seconds (python method)" %(time.time() - func_call_time))
                self.print_verbose("Tests total execution time: %s seconds (ret method)" %test_total_time)
                average = test_total_time / test_num
                self.print_verbose("Average time: %s" %average)
                self.print_verbose("==========")
                self.avgs.append((module.get_module_name(), average))
            self.tests_results.append((module.language, module_results))
        self.print_verbose("==== Tests finished in %s seconds ====" %(time.time() - start_time))
    def show_results(self):
        print "RESULTS:"
        test_str = ""
        diff = []
        for test in self.tests_results[0][1]:
            test_str += "\t%s" %test[0]
            diff.append([])
        print test_str
        for module in self.tests_results:
            module_str = "%s" %module[0]
            i = 0
            for test in module[1]:
                module_str += "\t%s" %test[1]
                diff[i].append((module[0], test[1]))
                i += 1
            print module_str
        diffstr = "Best"
        for test in diff:
            diffstr += "\t%s" %self.find_best(test)
        print diffstr
        
    def find_best(self, tab):
        start = 100000
        best = "None"
        for val in tab:
            if val[1] < start:
                start = val[1]
                best = val[0]
        return best

if __name__ == "__main__":
    parser = OptionParser(usage="usage: python %prog [options] languages_to_test...", version="%prog 0.0.1")
    parser.add_option("--module", default='Allocation', type='string', action="store", dest='module', help="Module used to do the tests")
    parser.add_option("-v", action='store_true', dest='verbose', help="Verbose option")

    (options, args) = parser.parse_args()

    if (len(args) < 1):
        print "You need more than 1 argument."
        exit()

    codetester = CodeTester(options, args)
    codetester.init()
    codetester.execute_tests()
    codetester.show_results()
