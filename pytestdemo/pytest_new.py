class Test_Case1:
    def jiafa(self,a,b):
        c = a + b
        return c
    def test_case1(self):
        case_data = [[111,222,333],[222,333,555],[455,666,1121]]
        for i in range(0,len(case_data)):
            c = self.jiafa(case_data[i][0],case_data[i][1])
            assert c == case_data[i][2]
