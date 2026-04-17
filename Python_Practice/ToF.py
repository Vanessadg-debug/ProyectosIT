
#Initilize variables

has_license= True
has_experience= False
has_clean_record= True

#calculate condition

can_drive_car= (has_license==True and has_clean_record==True)
can_drive_truck= (has_license==True and has_experience==True and has_clean_record==True)
cannot_drive_any= (has_license==False or has_clean_record==False)

print("Can drive car:", can_drive_car)
print("Can drive truc:", can_drive_truck)
print("Cannot drive any:", cannot_drive_any)