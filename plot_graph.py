
def plot_graph(dates, closes):
    import matplotlib.pyplot as plt

    x = list(range(len(closes)))  # 横軸（何日目か）

    # 株価を折れ線で描く
    plt.plot(x, closes, label="close")

    plt.title("Stock Price (Dummy Data)")
    plt.xlabel("day")
    plt.ylabel("price")
    plt.legend()
    plt.show()
