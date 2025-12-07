import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set professional Seaborn style and context for presentation
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate realistic synthetic customer engagement metrics data
np.random.seed(42)  # For reproducibility
metrics = ['Page Views', 'Session Duration', 'Cart Adds', 'Purchase Rate', 
           'Repeat Visits', 'Support Tickets', 'NPS Score', 'CLV']

# Create 8x8 correlation matrix with realistic retail patterns
data = np.random.uniform(0.1, 0.9, (8, 8))
data = (data + data.T) / 2  # Make symmetric
np.fill_diagonal(data, 1.0)  # Perfect self-correlation

# Add business-realistic correlations (e.g., high between cart adds/purchase, 
# negative between support tickets/NPS)
data[2, 3] = data[3, 2] = 0.85  # Cart Adds ↔ Purchase Rate
data[4, 3] = data[3, 4] = 0.78  # Repeat Visits ↔ Purchase Rate
data[1, 0] = data[0, 1] = 0.72  # Session Duration ↔ Page Views
data[6, 7] = data[7, 6] = -0.65  # NPS ↔ Support Tickets (negative)

# Round to 2 decimals for clean display
corr_matrix = pd.DataFrame(data, index=metrics, columns=metrics).round(2)

# Create the heatmap
plt.figure(figsize=(8, 8))
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))  # Upper triangle mask for cleaner look
ax = sns.heatmap(corr_matrix, mask=mask, annot=True, cmap='RdYlBu_r', center=0,
                 square=True, linewidths=0.5, cbar_kws={"shrink": 0.8})

# Professional styling
plt.title('Customer Engagement Correlation Matrix\nOrtiz and Sons Analytics', 
          fontsize=20, fontweight='bold', pad=20)
ax.set_xlabel('Engagement Metrics', fontsize=14, fontweight='bold')
ax.set_ylabel('Engagement Metrics', fontsize=14, fontweight='bold')

# Tight layout and save at exactly 512x512 pixels (8x64 DPI)
plt.tight_layout()
plt.savefig('chart.png', dpi=64, bbox_inches='tight', facecolor='white')
plt.close()
