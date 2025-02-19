# 导入Django的forms模块，用于创建表单
from django import forms
# 从当前应用的models模块导入Topic和Entry模型
from .models import Topic, Entry

# 定义一个继承自forms.ModelForm的TopicForm类，用于创建Topic模型的表单
class TopicForm(forms.ModelForm):
    # 定义一个内部类Meta，用于配置表单的元数据
    class Meta:
        # 指定表单关联的模型为Topic
        model = Topic
        # 指定表单中包含的字段，这里只包含'text'字段
        fields = ['text']
        # 定义字段的标签，这里将'text'字段的标签设置为空字符串，即不显示标签
        labels = {'text': ''}

# 定义一个继承自forms.ModelForm的EntryForm类，用于创建Entry模型的表单
class EntryForm(forms.ModelForm):
    # 定义一个内部类Meta，用于配置表单的元数据
    class Meta:
        # 指定表单关联的模型为Entry
        model = Entry
        # 指定表单中包含的字段，这里只包含'text'字段
        fields = ['text']
        # 定义字段的标签，这里将'text'字段的标签设置为空字符串，即不显示标签
        labels = {'text': ''}
        # 定义字段的表单控件，这里将'text'字段的控件设置为Textarea（文本区域）
        # 并通过attrs参数设置文本区域的列数为80
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}