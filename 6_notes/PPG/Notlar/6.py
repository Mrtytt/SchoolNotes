def dispbanner(s,ch='-'):
    if (isinstance(s,int)):
        s = str(s)
    print(ch*len(s))
    print(s)
    print(ch*len(s))
    
# dispbanner('Hello')
# dispbanner(120)