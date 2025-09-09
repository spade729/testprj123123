class OrderDataClass:
    def __init__(self, orderId, amount):
        self.orderId = orderId
        self.amount = amount


class CustomerDataClass:
    """_summary_
    class CustomerDataClass

    dl9 kjlnasdfolujhsdkjgbskdjg
    """

    def __init__(self, customerId, customerName):
        """_summary_

        Args:
            customerId (_type_): _description_
            customerName (_type_): _description_

        konstr
        """
        self.CustomerId = customerId
        self.CustomerName = customerName
        self.Orders = []

    def AddOrder(self, orderObject):
        """_summary_
        adasd

        Args:
            orderObject (_type_): _description_

        lklll
        """
        self.Orders.append(orderObject)

    def GetTotalAmount(self):
        total = 0

        #        if len(self.Orders) != 0:
        for o in self.Orders:
            total = total + o.amount

        return total


def CalculateDiscount(customerObj):
    """_summary_

    Args:
        customerObj (_type_): _description_

    Returns:
        _type_: _description_
    """
    totalAmount = customerObj.GetTotalAmount()
    #    type(totalAmount) == 'Int' and
    if totalAmount > 1000:
        discount = totalAmount * 0.1
    else:
        discount = 0
    return discount


def PrintCustomerReport(customerObj):
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
