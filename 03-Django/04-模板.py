# django处理模板会分为两个阶段
# 1.加载：根据给定的标识找到模板并预处理
# loader.get_template(template_name),返回一个template对象
# 2.渲染：使用context数据对模板插值并返回生成的字符串
# template对象的render(RequestContext)方法，使用context渲染模板
from django.template import loader, RequestContext
from django.http import HttpResponse


def index(request):
    temp = loader.get_template('test/index.html')
    context = RequestContext(request,{})
    return HttpResponse(temp.render(context))

# 以上函数的快捷函数为：
from django.shortcuts import render
# render(request,'模板',context)可一步到位完成加载和渲染工作
# render_to_string('字符串')  使页面直接返回字符串，等同于HttpResponse('字符串')
# (需要from django.template.loader import render_to_string)


# DTL：django模板语言
# 包含变量、标签{ % 代码块 % }、过滤器 | 、注释{# 代码或html #}

# 变量：{{variable}} 即表示在某个位置输出变量值
# for 标签：
# {%for ... in ...%} 循环逻辑
# {%empty%}  给出的列表不存在时，执行此处
# {%endfor%}  for标签结束
# {{forloop.counter}} 输出当前循环是第几次（在循环体中使用）

# if 标签：
# {%if ...%}  逻辑1
# {%elif ...%}  逻辑2
# {%else ...%}  逻辑3
# {%endif%}  结束if标签

# comment 标签：
# {%comment%}  多行标签
# {%endcomment%}
# {#....#}单行注释

# include：将另一个模板包含过来
# {%include"foo/bar.html"%}

# url：反向解析
# {% url 'namespace:name' p1 p2 %}  p1 p2为参数
# 即"namespace/name"

# 过滤器：
# 语法：{{变量|过滤器}}


# 模板继承：可以减少页面内容的重复定义
# 应用：网站的头部尾部是一样的，这些都可以定义在父模板中，子模版就不需要重新定义
# block标签：在父模板中预留区域，在子模版中填充
# {%block name%} 父模板中挖坑 {%endblock%}
# extends继承：继承，写在子模板文件的第一行
# {% extends 'base.html' %}
# 定义父模板：base.html
# 填坑时也要使用block标签，用法与挖坑时一样


# html转译：（<,>,",',&）
# view中通过函数传入到html中的数据默认都会转译
# 可使用过滤器来阻止/进行转译
# {{变量|escape}}  进行转译
# {{变量|safe}}   不进行转译
# {%autoescape off%}  代码块  {%endautoescape%} autoescape 可接受off或on参数，表示转译或不转译


# csrf跨站请求伪造
# 在模板内添加（post请求）csrf_token标签
# 在<form>标签内添加{%csrf_token%}
