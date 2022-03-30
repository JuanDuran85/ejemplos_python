"""_summary_

    Bar Chart with Matplotlib

"""

import matplotlib.pyplot as plt

def bar_chart(numbers: list, labels: list, pos: list) -> None:
    fig = plt.figure(figsize=(5,8))
    plt.bar(pos, numbers, color='blue')
    plt.xticks(ticks=pos,labels=labels)
    plt.show()
    
if __name__ == '__main__':
    numbers: list = [2,1,4,6]
    labels: list = ['Electric','Solar','Diesel','Gasoline']
    pos: list = list(range(4))
    bar_chart(numbers,labels,pos)