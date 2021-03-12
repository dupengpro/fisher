# 'http://localhost:81/book/search/9787501524044/1'
from fisher import app
from flask.json import jsonify

from helper import is_isbn_or_key
from yushu_book import YuShuBook


@app.route('/book/search/<q>/<page>')
def search(q, page):
    """
    :param q: 关键字或者 isbn（图书编号，isbn13 由13个0到9的数字组成，isbn10 由 '-' 和10个0到9的数字组成）
    :param page:
    :return:
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    # return json.dumps(result), 200, {'content-type': 'application/json'}
    # API 把数据用 json 格式返回到客户端
    return jsonify(result)