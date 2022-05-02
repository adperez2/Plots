titan=pd.read_csv("titanic.csv")
print(titan.head(5))
print(titan.tail(5))        #picks last fove rows
print(titan.sample(5))      #randomly picks five rows

#identify variables
print(titan.dtypes)         #dtypes tells if data is floating, object, intg
print(titan.describe())     #it gives mean, med, max, and n for numeric value

#categorical data
print(titan.name.value_counts())

#numeric data analysts
print(titan['age'].median())

#scatter plot
x=titan['age']
y=titan['fare']
plt.xlabel('age')
plt.ylabel('fare')
plt.scatter(x,y)
plt.show()

#histogram
x=titan['age']
plt.xlabel('age')
plt.ylabel('frequency')
plt.hist(x)     #plt.hist(x, bins=15)
plt.show()

#bar diagram
x=titan['sex']
y=titan['age']
plt.bar(x,y, color='red', widt=0.5)         #customize bar width and color
plt.show()
