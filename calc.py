def calculate_discount(price, discount_percentage):
    #checking if the discount is 20% or higher
    if discount_percentage >= 20:
        #calculate the discount amount
        discount_amount= price *(discount_percentage/ 100)
        #calculate the final price after applying the discount
        final_price = price - discount_amount
        return final_price
    else:
        #return the original price if discount is less than 20%
        return price