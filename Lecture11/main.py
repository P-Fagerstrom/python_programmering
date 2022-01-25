import imageanalyser as imga


def main():
    cat = imga.ImageAnalyser("cat.jpg")
    cat.plot() 
    cat.analyse_image()
    
if __name__=="__main__":
    main()


