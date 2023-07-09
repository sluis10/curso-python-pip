import matplotlib.pyplot as plt


def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f'./imgs/{name}.png')
    plt.close()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.savefig('pie.png')
    plt.close()

if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [100, 200, 80]
    generate_bar_chart(labels, values)


# Lo comento todo porque con Python3.11 me sale errores cuando utilizo la librería Matplotlib
# Lo pude arreglar :)

# Para instalar pip en Python3.11
# sudo apt install python3.11-venv
# python3.11 -m ensurepip

# Para verificar: python3.11 -m pip --version
# Para instalar librería: python3.11 -m pip install (librería)
# Para instalar última version de pip: curl -sS https://bootstrap.pypa.io/get-pip.py | python3.(x)
# (x): la versión de Python