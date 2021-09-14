from django.db import models
from user.models import AuthUser
from bookitem.models import Chapter
from payment.models import Order
from product.models import Top_up_item


# 此处所有支付选项均基于Creader币
class Transaction_History(models.Model):  # Creader 币支付记录
    # purchase item - Creader购买的物品
    item = models.ForeignKey(Top_up_item, default=None, on_delete=models.CASCADE,null=True)
    # 购买用户
    user = models.ForeignKey(AuthUser, default=None, on_delete=models.CASCADE)
    # 接受币用户
    to_user = models.ForeignKey(AuthUser, related_name='TO_USER', default=None, on_delete=models.CASCADE)
    # 购买的章节
    chapter = models.ForeignKey(Chapter, related_name='Chapter_Purchased', default=None, on_delete=models.CASCADE,
                                verbose_name='Chapter', blank=True, null=True)
    # 书币价格
    price = models.FloatField(default=0)
    # 购买状态
    PENDING = 'Pending' #暂定
    COMPLETED = 'Completed' #完成
    FAILED = 'Failed' #失败(作者提现失败的情况下)

    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
        (FAILED, 'Failed'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    # 购买时间
    Purchase_Time = models.DateTimeField(auto_now_add=True, blank=True)
    # 新的余额
    New_balance = models.FloatField(default=0)
    #------------消费币类型---------------------
    TRANSFER = 'Transfer' #转账
    PURCHASE_CHAPTER = 'Purchased Chapter' #购买章节
    PURCHASE_ITEM = 'Purchased item' #购买物品
    DONATE = 'Donation' #打赏

    TRANSACTION_CHOICES = (
        (TRANSFER, 'Transfer'),
        (PURCHASE_CHAPTER, 'Purchased Chapter'),
        (PURCHASE_ITEM, 'Purchased item'),
        (DONATE, 'Donation'),
    )
    Transaction_type = models.CharField(max_length=20, choices=TRANSACTION_CHOICES, default=None)

    # 数据库信息
    class Meta:
        verbose_name = 'Transaction_History'
        verbose_name_plural = 'Transaction_Histories'
        db_table = "Transaction_History"

# 作者收入记录
class Income_History(models.Model):  # 收入记录
    # 作者
    Author = models.ForeignKey(AuthUser, default=None, related_name='Author_ID', on_delete=models.CASCADE)
    # 打赏/购买人
    from_user = models.ForeignKey(AuthUser, default=None, related_name='Buyer_ID', on_delete=models.CASCADE)
    # 订单
    transaction = models.ForeignKey(Transaction_History, default=None, on_delete=models.CASCADE)
    # 章节
    chapter = models.ForeignKey(Chapter, related_name='Chapter_Income', default=None, on_delete=models.CASCADE,
                                verbose_name='Chapter', blank=True, null=True)
    # 收入时间
    DateTime = models.DateTimeField(auto_now_add=True, blank=True)
    # -------------收入类型-----------------------
    # 购买章节
    PURCHASE = 'Purchase Chapter'
    # 打赏
    DONATE = 'Donation'
    # 转账
    TRANSFER = 'Transfer'
    TYPE_CHOICES = (
        (PURCHASE, 'Purchase Chapter'),
        (DONATE, 'Donation'),
        (TRANSFER, 'Transfer')
    )
    # 类型
    Type = models.CharField(max_length=20, choices=TYPE_CHOICES, default=None)
    # 金额
    Amount = models.FloatField(default=0)

    #数据库信息
    class Meta:
        verbose_name = 'Income_History'
        verbose_name_plural = 'Income_Histories'
        db_table = "Income_History"


# 作者收入池子
class Author_Pool(models.Model):
    # 作者
    Author = models.ForeignKey(AuthUser, default=None, related_name='Pool_User_ID', on_delete=models.CASCADE)
    # 池中的总量
    Pool_total = models.FloatField(default=0)
    # TODO 重新设计Book_Pool的model, 可能需要新建一个表
    # 书的池量
    Book_pool = models.FloatField(default=0)
    #TODO 重新设计Chapter_Pool的model, 可能需要新建一个表
    # 章节池量
    Chapter_Pool = models.FloatField(default=0)
    #---------------打赏----------------------
    # 打赏总量
    Donation_total = models.FloatField(default=0)
    # 打赏人数
    Donation_count = models.FloatField(default=0)

    # 数据库信息
    class Meta:
        verbose_name = 'Author_Pool'
        verbose_name_plural = 'Author_Pools'
        db_table = "Author_Pool"
