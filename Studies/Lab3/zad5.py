def histogram(file_path):
    histogramZnaki = {}
    with open(file_path, 'r') as file:
        tekst = file.read()

        for znak in tekst:
            if znak in histogramZnaki:
                histogramZnaki[znak] += 1
            else:
                histogramZnaki[znak] = 1

    return histogramZnaki


print(histogram("tekstHistogram.txt"))
