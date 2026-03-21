from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FuncFormatter


def conv_pop(value):
    """
    Convert a value from a string to float.
    Exemple: 1k becomes 1000.
    """
    value = str(value)
    if "B" in value:
        return float(value.replace("B", "")) * 1e9
    if "M" in value:
        return float(value.replace("M", "")) * 1e6
    if "K" in value:
        return float(value.replace("K", "")) * 1e3
    return float(value)


def main():
    """
    The main programme opens the life_expectancy.csv file and
    extracts the DataFrame from it to create a graph with the
    matplotlib. The graph comparate your campus's country and
    one of your choice.
    """
    try:
        df = load("population_total.csv")
        if df is None:
            exit()
        country_a = "France"
        country_b = "Bangladesh"
        country_data_a = df[df["country"] == country_a]
        country_data_b = df[df["country"] == country_b]
        years = df.columns[1:].astype(int)
        mask = years <= 2050
        years = years[mask]
        values_a = country_data_a.iloc[0, 1:][mask].apply(conv_pop)
        values_a = values_a / 1_000_000
        values_b = country_data_b.iloc[0, 1:][mask].apply(conv_pop)
        values_b = values_b / 1_000_000
        plt.plot(years, values_a, label=country_a)
        plt.plot(years, values_b, label=country_b)
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.legend(loc="lower right")
        ax = plt.gca()
        ax.yaxis.set_major_locator(MultipleLocator(20))
        ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{int(x)}M"))
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print("Error:", e)
        return None


if __name__ == "__main__":
    main()
