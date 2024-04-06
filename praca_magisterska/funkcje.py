import matplotlib.pyplot as plt
import base64
from io import BytesIO


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_plot(x, y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10, 5))
    plt.pie(x, labels=y, autopct="%.2f%%", radius=1.2)
    graph = get_graph()
    return graph


def get_bar_plot(x, y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(12, 7))
    plt.bar(x, y)
    plt.ylabel("MPa")
    graph = get_graph()
    return graph
