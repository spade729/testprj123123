class OrderDataClass:
    """объект заказ"""
    def __init__(self, orderId, amount):
       """Конструктор

       Args:
           orderId: Ид заказа
           amount: Сумма 
       """
       self.orderId = orderId
       self.amount = amount


class CustomerDataClass:
    """объект счетчик заказчика
    """

    def __init__(self, customerId, customerName):
        """Конструктор

        Args:
            customerId: Ид заказчика
            customerName: Имя заказчика
        """
        self.CustomerId = customerId
        self.CustomerName = customerName
        self.Orders = []

    def AddOrder(self, orderObject):
        """Добавить заказ

        Args:
            orderObject (OrderDataClass): объект заказа
        """
        self.Orders.append(orderObject)

    def GetTotalAmount(self):
        """Подсчет общей суммы

        Returns:
           сумма
        """
        total = 0

        #        if len(self.Orders) != 0:
        for o in self.Orders:
            total = total + o.amount

        return total


def CalculateDiscount(customerObj):
    """Расчет скидки

    Args:
        customerObj (CustomerDataClass): объект счетчик заказчика

    Returns:
        Скидка
    """
    totalAmount = customerObj.GetTotalAmount()
    #    type(totalAmount) == 'Int' and
    if totalAmount > 1000:
        discount = totalAmount * 0.1
    else:
        discount = 0
    return discount


def PrintCustomerReport(customerObj):
    """Вывод отчета

    Args:
        customerObj (CustomerDataClass): объект счетчик заказчика
    """
    print("Customer Report for:", customerObj.CustomerName)
    print("Total Orders:", len(customerObj.Orders))
    print("Total Amount:", customerObj.GetTotalAmount())
    print("Discount:", CalculateDiscount(customerObj))
    if len(customerObj.Orders) != 0:
        print("Average Order:", customerObj.GetTotalAmount() / len(customerObj.Orders))


def MainProgram():
    c1 = CustomerDataClass(1, "SAP Customer")
    o1 = OrderDataClass(101, 500)
    o2 = OrderDataClass(102, 800)
    c1.AddOrder(o1)
    c1.AddOrder(o2)

    PrintCustomerReport(c1)

    c2 = CustomerDataClass(2, "Empty Customer")
    #    c2.AddOrder(o2)
    PrintCustomerReport(c2)


MainProgram()
