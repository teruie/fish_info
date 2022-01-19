from django.db import models


# 大文字を小文字に変更
class LowerCharField(models.CharField):
    
    def get_prep_value(self, value):
        return str(value).lower()