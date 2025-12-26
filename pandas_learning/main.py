import matplotlib.pyplot as plt
import pandas as pd

file = r'D:\projects\DA\customer_shopping_behavior.csv'

df = pd.read_csv(file)


category = df.groupby('Category').size()
print(category)

plt.bar(category.index,category.values,color  = ['blue','yellow','red'])
for i,v in enumerate(category.values):
       plt.text(i,v + 10,f"{v}",ha = 'center',va = "bottom")
plt.title(" No of products by category")
plt.ylabel("Products")
plt.xlabel("category")
plt.ylim(0,category.max()+200)
plt.savefig("products_by_category.jpg")
plt.show()


# # Fill missing review ratings
# df['Review Rating'] = df['Review Rating'].fillna(0.0)

# # Clean column names
# df.columns = df.columns.str.replace(" ", "_").str.lower()

# # Create age_group column
# df['age_group'] = df['age'].apply(
#     lambda x: 'Minor' if x <= 18 else
#               'Teenage' if 19 <= x <= 25 else
#               'Adult'
# )

# # Count by age_group
# age_count = df.groupby('age_group').size()
# print(age_count)

# # Dynamic colors based on count
# colors = [
#     'green' if x > 1000 else 'orange' if x > 200 else 'red'
#     for x in age_count.values
# ]

# # Plot bar chart
# plt.bar(age_count.index, age_count.values, color=colors)

# # Add values on top of bars
# for index, value in enumerate(age_count.values):
#     plt.text(
#         index,
#         value + 20,
#         str(value),
#         ha='center',
#         va='bottom',
#         fontsize=10
#     )

# plt.title('Age Group Distribution')
# plt.xlabel('Age Group')
# plt.ylabel('Count')
# plt.ylim(0, age_count.max() + 300)
# plt.savefig("age_group.jpg")

# plt.show()


