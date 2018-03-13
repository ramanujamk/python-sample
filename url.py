import sys
from urllib.request import urlopen


# http://sixty-north.com/c/t.txt

def split_words(url):
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words
    
    
def print_words(words):
    """Prints the list of words passed to the function 
        Args:
            words: A list

        Returs:
            None
    """
    print(words)
    return

def main(url): 
    new_words = split_words(url)
    print_words(new_words)



if __name__ == "__main__":
    main(sys.argv[1])
    print("called")
else:
    print("not main")