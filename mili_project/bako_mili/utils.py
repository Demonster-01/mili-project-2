import matplotlib.pyplot as plt
from io import BytesIO
import base64

def get_graph():
    buffer= BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png=buffer.getvalue()
    graph=base64.b64encode(image_png)
    # print(graph)
    graph=graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x,y):
    plt.switch_backend("AGG")
    plt.figure(figsize=(6,5))
    plt.title('income and exp')
    plt.plot(x,y)
    plt.xticks(rotation=45)
    plt.xlabel("date")
    plt.ylabel('amount')
    plt.tight_layout()

    graph=get_graph()
    return graph