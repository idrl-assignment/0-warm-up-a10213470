import numpy as np
import matplotlib.pyplot as plt


def generate_random_matrix(m, n):
    matrix1 = np.random.randint(0, 2, (m, n))
    return(matrix1)


def save_matrix(matrix, file_name):
    plt.imshow(matrix) 
    plt.savefig(file_name)
    plt.show()


if __name__ == "__main__":
    matrix = generate_random_matrix(10, 10)
    save_matrix(matrix, "example.jpg")
