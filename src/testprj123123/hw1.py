"""DZ1."""

class OrderDataClass:
    """объект заказ."""
    def __init__(self, orderid, amount):
       """Конструктор.

       Args:
           orderid: Ид заказа
           amount: Сумма 
       """
       self.orderid = orderid
       self.amount = amount


class CustomerDataClass:
    """объект счетчик заказчика."""

    def __init__(self, customerid, customername):
        """Конструктор.

        Args:
            customerid: Ид заказчика
            customername: Имя заказчика
        """
        self.customerid = customerid
        self.Customername = customername
        self.Orders = []

    def addorder(self, orderobject):
        """Добавить заказ.

        Args:
            orderobject (OrderDataClass): объект заказа
        """
        self.Orders.append(orderobject)

    def gettotalamount(self):
        """Подсчет общей суммы.

        Returns:
           сумма
        """
        total = 0

        #        if len(self.Orders) != 0:
        for o in self.Orders:
            total = total + o.amount

        return total


def calculatediscount(customerobj):
    """Расчет скидки.

    Args:
        customerobj (CustomerDataClass): объект счетчик заказчика

    Returns:
        Скидка
    """
    totalamount = customerobj.gettotalamount()
    discount = totalamount * 0.1 if totalamount > 1000 else 0
    return discount


def printcustomerreport(customerobj):
    """Вывод отчета.

    Args:
        customerobj (CustomerDataClass): объект счетчик заказчика
    """
    print('Customer Report for:', customerobj.Customername)
    print('Total Orders:', len(customerobj.Orders))
    print('Total Amount:', customerobj.gettotalamount())
    print('Discount:', calculatediscount(customerobj))
    if len(customerobj.Orders) != 0:
        print('Average Order:', customerobj.gettotalamount() / len(customerobj.Orders))


def mainprogram():
    """Главная программа."""
    c1 = CustomerDataClass(1, 'SAP Customer')
    o1 = OrderDataClass(101, 500)
    o2 = OrderDataClass(102, 800)
    c1.addorder(o1)
    c1.addorder(o2)

    printcustomerreport(c1)

    c2 = CustomerDataClass(2, 'Empty Customer')
    #    c2.addorder(o2)
    printcustomerreport(c2)


mainprogram()
