def is_isbn_or_key(word):
    """
    判断输入的是关键字还是图书编号
    :param word:
    :return:
    """
    isbn_or_key = 'key'
    # isdigit() 判断字符串是否由数字组成
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit:
        isbn_or_key = 'isbn'
    return isbn_or_key

