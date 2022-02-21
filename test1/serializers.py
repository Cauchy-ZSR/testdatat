from attr import field
from rest_framework import serializers
from  .models import demo


class demoSerializer(serializers.ModelSerializer):
    class Meta:
        # 需要序列化的模型
        model = demo
        # 需要序列化的字段，“_all_”表示所有字段
        fields = "__all__"
