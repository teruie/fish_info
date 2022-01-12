from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid



class Category(models.Model):
    title = models.CharField(verbose_name='魚種入力', max_length=20)
    
    class Meta:
        verbose_name = 'カテゴリー'
        verbose_name_plural = 'カテゴリー'
        ordering = ('title',)

    def __str__(self):
      return str(self.title) 



class Place(models.Model):
    title = models.CharField(verbose_name='場所入力', max_length=20)

    class Meta:
        verbose_name = '場所'
        verbose_name_plural = '場所'

    def __str__(self):
      return str(self.title) 



class Article(models.Model):

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, db_index=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(verbose_name='タイトル',max_length=30)
    fish_img = models.ImageField(verbose_name='写真', upload_to='images/') #写真
    fishing_comment = models.TextField(verbose_name='釣果コメント',max_length=100) #釣果コメント
    fish_category = models.ForeignKey(Category,verbose_name='魚種', on_delete=models.SET_NULL, null=True)
    length = models.IntegerField(verbose_name='長さ', blank=True, null=True, default=0) #長さ
    weight = models.IntegerField(verbose_name='重さ', blank=True, null=True, default=0) #重さ
    place = models.ForeignKey(Place, verbose_name='場所',on_delete=models.SET_NULL, null=True) #場所
    created_at = models.DateTimeField(verbose_name='作成日',auto_now_add = True) #作成日時
    updated_at = models.DateTimeField(verbose_name='更新日',auto_now = True) #更新日時

    class Meta:
        verbose_name = '投稿'
        verbose_name_plural = '投稿'

    def __str__(self):
        return str(self.id)
        


class Comment(models.Model):
    name = models.CharField('名前', max_length=255, default='名無し')
    text = models.TextField('本文')
    target = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='対象記事')
    created_at = models.DateTimeField(verbose_name='作成日',auto_now_add = True)

    class Meta:
        db_table    = "comment"

    def __str__(self):
        return self.text[:20]



class Profile(models.Model):

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, db_index=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user_profile')
    user_name = models.CharField(default='ネーム', verbose_name='ユーザーネーム', max_length=10)
    icon = models.ImageField(default='画像が設定されていません', verbose_name='アイコン', upload_to='icon/')
    header = models.ImageField(default='画像が設定されていません', verbose_name='ヘッダー',  upload_to='header/')
    text = models.TextField(default='自己紹介文を入力してください', verbose_name='自己紹介', max_length=50)

    class Meta:
        verbose_name = 'プロフィール'
        verbose_name_plural = 'プロフィール'

    def __str__(self):
        return str(self.id)



@receiver(post_save, sender=get_user_model())
def create_profile(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.get_or_create(user=kwargs['instance'])
