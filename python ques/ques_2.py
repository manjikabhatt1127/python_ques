class Sum:
    def func(self,nums:list[int])->int:
        count = 0
        for item in nums:
            count=count+item
        print(count)
        

abc = Sum()

abc.func([1,5,3,8])


        



