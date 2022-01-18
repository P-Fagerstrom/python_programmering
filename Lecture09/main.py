from animal import Dog

def main():
    dog = Dog()
    dog.make_noise()
    print('Energy:', dog.energy)
    dog.play()
    print('Energy:', dog.energy)
    
if __name__ == "__main__":
    main()
    