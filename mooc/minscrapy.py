# _*_ coding: utf-8 _*_

"""
迷你爬虫小练习
爬取豆瓣50条短评, 并计算平均分值
"""

# urllib

import urllib.request
import urllib.parse
import re
import IPython



def get_comments_of_one_page(id, num):
    '获取某一个评论'
    params = urllib.parse.urlencode({
        'start': str(num-1),
        'limit': '20'
    })

    url = 'https://movie.douban.com/subject/'+ id +'/comments?{}'.format(params)
    with urllib.request.urlopen(url) as res:
        text = res.read().decode('utf-8')
        # print(text)
        # IPython.embed()
        # print(text.decode('utf-8'))

    # regex = re.compile('<div class="comment">(.*?)</div>')
    # print(text)

    text_regular = re.compile(r'<div class="comment">(.*?)</div>', re.S)
    votes_regular = re.compile(r'<span class="votes">(.*?)</span>')
    star_regular = re.compile('allstar(.*?)0')
    content_regular = re.compile(r'<p class=""> (.*?)</p>', re.S)

    lst = text_regular.findall(text)


    comment_list = []
    for item in lst:
        vote = int(votes_regular.search(item).group(1))
        content = content_regular.search(item).group(1).strip()

        comment = {
            'content':  content,
            'vote': vote
        }

        s = star_regular.search(item)
        if s is not None:
            comment['star'] = int(s.group(1))

        comment_list.append(comment)


    return comment_list



def average_star(lst):
    '获取评论的平均分'
    stars = [l['star'] for l in lst if l.get('star')]
    return round(sum(stars) / len(stars), 2)


list = []

list.extend(get_comments_of_one_page('1291561', 1))
list.extend(get_comments_of_one_page('1291561', 2))
list.extend(get_comments_of_one_page('1291561', 3))


print(len(list))
print(average_star(list))



