def has_lucky_number (nums):
    for i in nums:
        if not (i % 7):
            return True
    return False
    
def main():
    nums = [2, 6, 7, 9]
    print(has_lucky_number(nums))

if __name__ == "__main__":
    main()
    