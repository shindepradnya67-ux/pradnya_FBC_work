##4. Calculate the cost of painting the following building’s walls (both interior and
#exterior). You need to accept area (one wall) and cost of both interior and
#exterior wall.
#(Note: 1. Below diagram is of two joint rooms.
#2. It is upper view of building.)

area = float(input("Enter area of one wall: "))
interior_rate = float(input("Enter interior wall cost: "))
exterior_rate = float(input("Enter exterior wall cost: "))

interior_area = 8 * area
exterior_area = 6 * area

interior_cost = interior_area * interior_rate
exterior_cost = exterior_area * exterior_rate

total_cost = interior_cost + exterior_cost

print("Interior painting cost =", interior_cost)
print("Exterior painting cost =", exterior_cost)
print("Total painting cost =", total_cost)