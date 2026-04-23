import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def global_context_latam(df):

        # crear diccionario: pais -> color
    palette_dict = dict(zip(df["country_region"], df["color"]))

    sns.barplot(
        data=df,
        x="value",
        y="country_region",
        palette=palette_dict
    )

    plt.xlabel("Value")
    plt.ylabel("Country Region")
    plt.title("Latam countries in a global context");