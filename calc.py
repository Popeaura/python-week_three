def calculate_discount(price, discount_percentage):
    #checking if the discount is 20% or higher
    if discount_percentage >= 20:
        #calculate the discount amount
        discount_amount= price *(discount_percentage/ 100)
        