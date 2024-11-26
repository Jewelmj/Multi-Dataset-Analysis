
df.select_dtypes(include='number').columns 

# ## violin plot

# grouped_df = df.groupby('Contract')

# # Create subplots for each contract
# fig, axes = plt.subplots(nrows=1, ncols=len(grouped_df), figsize=(12, 6))

# # Create a violin plot for each group
# for ax, (contract, group_data) in zip(axes, grouped_df):
#     ax.violinplot(group_data['TotalCharges'].dropna(), showmedians=True)
#     ax.set_title(f'Contract {contract}')
#     ax.set_ylabel('Value')
#     ax.set_xlabel('Contract')

# # Adjust layout
# plt.tight_layout()

# # Show the plot
# plt.show()


# ## boxplot

# df_dummy = df[['TotalCharges','Contract']].groupby('Contract')

# fig, axes = plt.subplots(nrows=1, ncols=len(df_dummy), figsize=(12, 6))
# for ax, (contract, group_data) in zip(axes, df_dummy):
#     ax.boxplot(group_data['TotalCharges'].dropna(), labels=[contract])  # Drop NaN values for plotting
#     ax.set_title(f'Contract {contract}')
#     ax.set_ylabel('Value')
#     ax.set_xlabel('Contract')
# plt.tight_layout()
# plt.show()
