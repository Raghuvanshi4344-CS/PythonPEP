import calculator
import tax
import discount
import invoice

price = float(input("Enter price of one item: "))
quantity = int(input("Enter quantity: "))

subtotal = calculator.total(price, quantity)
gst = tax.gst(subtotal)
dis = discount.discount(subtotal)

final_bill = subtotal + gst - dis

invoice.print_invoice(price, quantity, subtotal, gst, dis, final_bill)