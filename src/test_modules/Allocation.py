from testmodule import TestModule
import subprocess

class AllocationTest(TestModule):
    def init(self):
        self.makerule("simplealloc")
        self.makerule("bigalloc")
        self.add_test("Simple allocation", self.simple_alloc)
        self.add_test("Big allocation", self.big_alloc)

    def makerule(self, rule):
        subprocess.Popen("make -C test_modules/%s %s" %(self.language, rule), shell=True, stdout=subprocess.PIPE).stdout.read()

    def simple_alloc(self):
        subprocess.call(["./test_modules/%s/simplealloc" %self.language])
        return 0

    def big_alloc(self):
        subprocess.call(["./test_modules/%s/bigalloc" %self.language])
        return 0

    def get_module_name(self):
        return "Allocation test"
