class ListHelper:
    
    @classmethod
    def greatest_frequency(cls, my_list: list):
        nums = {}
        for number in my_list:
            if number not in nums:
                nums[number] = 1
            else:
                nums[number] += 1

        most = 0
        highest_num = 0
        for key, value in nums.items():
            if value > most:
                most = value
                highest_num = key

        return highest_num

            

    @classmethod
    def doubles(cls, my_list: list):
        nums = {}
        for number in my_list:
            if number not in nums:
                nums[number] = 1
            else:
                nums[number] += 1

        at_least_two = 0
        for key, value in nums.items():
            if value > 1:
                at_least_two += 1

        return at_least_two



if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))