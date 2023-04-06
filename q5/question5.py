def main():
    def reverse_words(strg):
        def ls_strg(ls):
            result = ""
            for s in ls:
                result += s + " "
            return result
        strg = strg.split()
        rev_strg = strg[::-1]
        rev_strg = ls_strg(rev_strg)
        return rev_strg
    str1 = """Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth;"""
    str2 = """Then took the other, as just as fair, And having perhaps the better claim, Because it was grassy and wanted wear; Though as for that the passing there Had worn them really about the same,"""

    print("<input> {0}\n<output> {1}\n".format(str1,reverse_words(str1)))
    print("<input> {0}\n<output> {1}\n".format(str2,reverse_words(str2)))
    
if __name__ == '__main__':
    main()
