from twttr import shorten

def main():

    test_novow()

    test_nocapvow()

    test_omnum()

    test_ompunc()


def test_novow():
   assert shorten("Twitter") == "Twttr"

def test_nocapvow():
   assert shorten("TwittEr") == "Twttr"

def test_omnum():
   assert shorten("well 102") == "wll 102"

def test_ompunc():
   assert shorten(",Twitter.") == ",Twttr."



if __name__ == "__main__":
    main()