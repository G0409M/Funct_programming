import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

def plot_dataframe(df, output_path='output_plot.png'):

    sns.set(style="whitegrid")
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 8))

    def format_large_numbers(value, _):
        if value >= 1e6:
            return f'{value / 1e6:.1f}M'
        elif value >= 1e3:
            return f'{value / 1e3:.1f}K'
        else:
            return str(int(value))

    axes[0].bar(df['Subregion'], df['Summed Population'], color='skyblue')
    axes[0].set_title('Summed Population by Subregion')
    axes[0].set_xlabel('Subregion')
    axes[0].set_ylabel('Summed Population')
    axes[0].yaxis.set_major_formatter(FuncFormatter(format_large_numbers))

    axes[1].bar(df['Subregion'], df['Summed Area'], color='lightcoral')
    axes[1].set_title('Summed Area by Subregion')
    axes[1].set_xlabel('Subregion')
    axes[1].set_ylabel('Summed Area')
    axes[1].yaxis.set_major_formatter(FuncFormatter(format_large_numbers))
    fig.set_facecolor('#f0f0f0')

    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.show()
