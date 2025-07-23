from django.shortcuts import HttpResponse



def add_cookie(request):
    response = HttpResponse('设置cookie')

    max_age = 60*60*24*7

    response.set_cookie('username','zhiliao',max_age=max_age)

    return response




def delete_cookie(request):
    response = HttpResponse('删除cookie')

    response.delete_cookie('username')

    return response


def get_cookie(request):

    # username = request.COOKIES.get('username')
    # print(username)

    for key, value in request.COOKIES.items():
        print(key, value)


    return HttpResponse('get cookie')



def add_session(request):
    # session默认的过期时间是2周
    request.session['user_id'] = 'zhiliao'
    # 设置成0，浏览器关闭自动关闭session
    request.session.set_expiry(0)
    return HttpResponse('session add')


def get_session(request):

    username = request.session.get('user_id')
    print(username)
    return HttpResponse('session get')