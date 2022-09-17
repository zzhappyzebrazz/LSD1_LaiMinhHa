def elementwise_greater_than (L, thresh):
    result = ['True' if i > thresh else 'False' for i in L]
    return result
    
def main():
    L = [1, 2, 3, 4]
    thresh = 2
    print(elementwise_greater_than(L, thresh))

if __name__ == "__main__":
    main()
    