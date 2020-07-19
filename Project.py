fleet = {"truck01": input("Enter mileage for truck 1\n"), "truck02": input("Enter mileage for truck 2\n"),
"truck03": input("Enter mileage for truck 3\n"), "truck04": input("Enter mileage for truck 4\n")}

def service_required(miles):
    if miles < 8000:
        return False
    if miles >= 8000:
        return True

for truck in fleet:
    service = service_required(int(fleet[truck]))
    if service:
        print(f"{truck} Report for maintenance")
    else:
        print(f"{8000 - int(fleet[truck])} Miles since last service")
