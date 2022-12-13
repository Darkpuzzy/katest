from django.db import models


class InFileData(models.Model):
    number_raw = models.IntegerField()
    cryptcode = models.CharField(max_length=250, verbose_name='Шифр')
    fsnb = models.CharField(max_length=250, verbose_name='Обоснование (код ФСНБ)')
    mtr = models.CharField(max_length=250, verbose_name='Наименование МТР')
    metric = models.CharField(max_length=50, verbose_name='Ед. измерения')
    all_counts = models.FloatField(verbose_name='Общее количество', default=0)
    price_not_nds = models.DecimalField(max_digits=30, decimal_places=2, default=0, verbose_name='цена за ед. без учета НДС')
    index = models.FloatField(max_length=250, default=0)
    price_smeta = models.DecimalField(max_digits=30, decimal_places=2, default=0, verbose_name='Сметная цена')
    nomenclature = models.CharField(max_length=250,)
    razdel = models.IntegerField(max_length=250, default=0)
    mtr_count = models.FloatField(max_length=250, default=0)
    price_mtr_for_ed = models.DecimalField(max_digits=30, decimal_places=2, default=0)
    price_mtr_sum = models.DecimalField(max_digits=30, decimal_places=2, default=0)
    materials_price_mtr_sum = models.DecimalField(max_digits=30, decimal_places=2, default=0)
    oborud = models.DecimalField(max_digits=30, decimal_places=2, default=0)
    mtr_count_other = models.FloatField(max_length=250, default=0)
    price_mtr_for_ed_other = models.DecimalField(max_digits=30, decimal_places=2, default=0)
    price_mtr_sum_other = models.DecimalField(max_digits=30, decimal_places=2, default=0)
    materials_price_mtr_sum_other = models.DecimalField(max_digits=30, decimal_places=2, default=0)
    oborud_other = models.DecimalField(max_digits=30, decimal_places=2, default=0)
    mtr_count_orders = models.FloatField(max_length=250, default=0)
    price_mtr_for_ed_orders = models.DecimalField(max_digits=30, decimal_places=2, default=0)
    price_mtr_sum_orders = models.DecimalField(max_digits=30, decimal_places=2, default=0)
    materials_price_mtr_sum_orders = models.DecimalField(max_digits=30, decimal_places=2, default=0, blank=True)
    oborud_orders = models.DecimalField(max_digits=30, decimal_places=2, default=0)
    operator = models.CharField(max_length=120, default='None')
    origin_mtr = models.CharField(max_length=250, default='None')
    original_file = models.ForeignKey('FileData', null=False, verbose_name='File', on_delete=models.PROTECT)


class FileData(models.Model):
    file_save = models.FileField(upload_to='exfile', null=False)







