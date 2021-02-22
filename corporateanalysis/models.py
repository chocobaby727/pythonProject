from django.db import models


# Create your models here.

class Company(models.Model):
    class Meta:
        db_table = 'company'

    name = models.CharField(verbose_name='会社名', max_length=255)
    date = models.DateField(verbose_name='年月日')


class Data(models.Model):
    class Meta:
        db_table = 'data'

    company = models.ManyToManyField(Company, verbose_name='会社')

    roa = models.CharField(verbose_name='ROA', max_length=255)
    roe = models.CharField(verbose_name='ROE', max_length=255)
    gross_profit_margin = models.CharField(verbose_name='売上高総利益率', max_length=255)
    operating_income_margin = models.CharField(verbose_name='売上高営業利益率', max_length=255)
    ordinary_rate_of_return_on_sales = models.CharField(verbose_name='売上高経常利益率', max_length=255)
    sg_and_a_interest_ate_on_sales = models.CharField(verbose_name='売上高販売管理費利率', max_length=255)
    inventories_turnover = models.CharField(verbose_name='棚卸資産回転率', max_length=255)
    current_ratio = models.CharField(verbose_name='流動比率', max_length=255)
    quick_ratio = models.CharField(verbose_name='当座比率', max_length=255)
    debt_ratio = models.CharField(verbose_name='負債比率', max_length=255)
    capital_adequacy_ratio = models.CharField(verbose_name='自己資本比率', max_length=255)
    sales_growth_rate = models.CharField(verbose_name='売上高増加率', max_length=255)
    profit_growth_rate = models.CharField(verbose_name='利益増加率', max_length=255)
    total_capital_increase_rate = models.CharField(verbose_name='総資本増加率', max_length=255)
    net_asset_growth_rate = models.CharField(verbose_name='純資産増加率', max_length=255)
    employee_growth_rate = models.CharField(verbose_name='従業員増加率', max_length=255)
    total_asset_turnover = models.CharField(verbose_name='総資本回転率', max_length=255)
    fixed_asset_turnover_rate = models.CharField(verbose_name='固定資産回転率', max_length=255)
    inventories_turnover = models.CharField(verbose_name='棚卸資産回転率', max_length=255)
