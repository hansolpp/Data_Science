from matplotlib import pyplot as plt
from collections import Counter

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
decile = lambda grade: (grade // 10) * 10
histogram = Counter(decile(grade) for grade in grades)
print(histogram)
plt.bar(histogram.keys(), histogram.values(), 8)

#x축 범위 : (-5, 105), y축 범위 : (0, 5)
plt.axis([-5, 105, 0, 5])

plt.xticks([10*i for i in range(11)])
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of ExAM 1 Grades")
plt.show()
