from django.db import models


# Модель типа договра
class ContractType(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Вид договора'
        verbose_name_plural = 'Виды договоров'

    def __str__(self):
        return self.name

# Модель вида расчета
class CalculationType(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Вид расчета'
        verbose_name_plural = 'Виды расчета'

    def __str__(self):
        return self.name

# Модель заказа
class Order(models.Model):
    number = models.AutoField(primary_key=True, verbose_name='Номер договора')
    type = models.ForeignKey(ContractType, on_delete=models.DO_NOTHING, verbose_name="Вид договора")
    # payment_type = models.ForeignKey(CalculationType, on_delete=models.DO_NOTHING, verbose_name="Вид расчета", null=True)
    customer_name = models.CharField(max_length=100, verbose_name="ФИО заказчика")
    customer_address = models.CharField(max_length=200, verbose_name="Адрес заказчика")
    customer_phone = models.CharField(max_length=15, verbose_name="Телефон заказчика")

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return str(self.number) + '(' + str(self.date) + ')'


