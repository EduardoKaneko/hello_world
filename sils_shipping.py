def ground_shipping(weight):
  cost = 0
  
  if weight <= 2.0:
    cost = weight * 1.5
    return cost + 20
  
  elif 2 < weight <= 6:
    cost = weight * 3
    return cost + 20
		
  elif 6 < weight <= 10:
    cost = weight * 4
    return cost + 20
		
  else:
    cost = weight * 4.75
    return cost + 20

premium_shipping = 125

def drone_shipping(weight):
  cost = 0
  
  if weight <= 2.0:
    cost = weight * 4.5
    return cost 
  
  elif 2 < weight <= 6:
    cost = weight * 9
    return cost 
		
  elif 6 < weight <= 10:
    cost = weight * 12
    return cost 
		
  else:
    cost = weight * 14.25
    return cost 

def cheapest_ship(weight):
  ground = ground_shipping(weight)
  drone = drone_shipping(weight)
  premium = 125
  
  if (ground > drone) and (drone < premium):
    return print("Method is drone! Cost: " + str(drone))
  
  elif (ground < drone) and (ground < premium):
    return print("Method is ground! Cost: " + str(ground))

  elif (premium < drone) and (premium < ground):
    return print("Cheapest method is premium - Cost: " + str(premium))

weight = float(input())

cheapest_ship(weight)