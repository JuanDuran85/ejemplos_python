import matplotlib.pyplot as plt

pelotas_fronton = [34,67,31,13,56]
nombres = ["Reanna","Raleigh","Jerel","Royce","Maudie"]
plt.pie(x=pelotas_fronton, labels=nombres, autopct="%1.1f%%")
plt.show()