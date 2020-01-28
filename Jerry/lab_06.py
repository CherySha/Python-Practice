import string
with open("moby_01.txt")as infile , open("moby_01_clean.txt","w") as outfile:
    for line in infile:
        cleaned_line = line.lower()
        punct=cleaned_line.maketrans("","",string.punctuation)
        cleaned_line = cleaned_line.translate(punct)
        words = cleaned_line.split()
        cleaned_words = "\n".join(words)
        outfile.write(cleaned_words)
