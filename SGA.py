#!/anaconda3/~/bin python3
# -*- coding: utf-8 -*-
# @Time     : 2022/3/24 下午3:12
# @Project  : studyTemplate
# @File     : SGA.py
# @Author   : XuJieYa
# @version  : python3
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from abc import ABCMeta, abstractmethod


class SGAInit(metaclass=ABCMeta):
    @abstractmethod
    def problem_function(self, x, y):
        pass

    @abstractmethod
    def plot_graph(self, ax):
        pass

    @abstractmethod
    def decoding(self, population_matrix):
        pass

    @abstractmethod
    def cross(self, child, population_matrix):
        pass

    @abstractmethod
    def variation(self, child):
        pass

    @abstractmethod
    def update_population(self, population_matrix):
        pass

    @abstractmethod
    def fitness_vector(self, population_matrix):
        pass

    @abstractmethod
    def selection(self, population_matrix, fitness_vector):
        pass

    @abstractmethod
    def print_result(self, population_matrix):
        pass


class SGA(SGAInit):
    def __init__(self,
                 size=24,   # Length of the individual
                 population_size=200,   # Length of the population
                 generation_number=500,  # The number of iter generation
                 cross_rate=0.9,    # The crossover probability
                 variation_rate=0.01,   # The variation probability
                 ):
        self.size = size
        self.population_size = population_size
        self.generation_number = generation_number
        self.cross_rate = cross_rate
        self.variation_rate = variation_rate

    # This is the function, which should be solved
    def problem_function(self, x, y):
        return 3 * (1 - x) ** 2 * np.exp(-(x ** 2) - (y + 1) ** 2)\
           - 10 * (x / 5 - x ** 3 - y ** 5) * np.exp(-x ** 2 - y ** 2)\
           - 1 / 3 ** np.exp(-(x + 1) ** 2 - y ** 2)

    # This is the function of plot for iteration
    def plot_graph(self, ax):
        x_sequence = np.linspace(*[-3, 3], 100)
        y_sequence = np.linspace(*[-3, 3], 100)
        # Generate the matrix of x and y
        x_matrix, y_matrix = np.meshgrid(x_sequence, y_sequence)
        # Generate the z_matrix for plot
        z_matrix = self.problem_function(x_matrix, y_matrix)
        ax.plot_surface(x_matrix, y_matrix, z_matrix, rstride=1, cstride=1, cmap=plt.get_cmap('coolwarm'))

        # Define the initial parameters of plot
        ax.set_zlim(-10, 10)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        plt.pause(4.5)
        plt.show()

    def decoding(self, population_matrix):
        """
        :param population_matrix: The matrix of population
        :return: return the matrix of population_x/y_vector
        """
        # The matrix is split, the rows are unchanged, and the odd series are extracted as x-matrices
        x_matrix = population_matrix[:, 1::2]
        # The matrix is split, the rows are unchanged, and the even series are extracted as a y-matrix
        y_matrix = population_matrix[:, 0::2]
        decoding_vector = 2**np.arange(self.size)[::-1]
        # Population x-vector, converted from binary to decimal and mapped to the x interval
        population_x_vector = x_matrix.dot(decoding_vector)/(2**self.size - 1)\
            *([-3, 3][1] - [-3, 3][0]) + [-3, 3][0]
        # Population y-vector, converted from binary to decimal and mapped to the y interval
        population_y_vector = y_matrix.dot(decoding_vector)/(2**self.size - 1)\
            *([-3, 3][1] - [-3, 3][0]) + [-3, 3][0]
        return population_x_vector, population_y_vector

    def cross(self, child, population_matrix):
        """
        :param child: The chromosome of child
        :param population_matrix: The matrix of population
        :return:
        """
        if np.random.rand() < self.cross_rate:
            mother = population_matrix[np.random.randint(self.population_size)]
            # Random chose the position of variation
            cross_position = np.random.randint(self.size*2)
            # Reverse the xor gate
            child[cross_position] = mother[cross_position:]

    def variation(self, child):
        """
        This is the function of variation for child
        :param child: the chromosome of child
        :return: None
        """
        if np.random.rand() < self.variation_rate:
            variation_position = np.random.randint(self.size*2)
            child[variation_position] = child[variation_position] ^ 1

    def update_population(self, population_matrix):
        """
        :param population_matrix: The matrix of population
        :return: new_population_matrix
        """
        new_population_matrix = []  # Restore for the new population
        for father in population_matrix:
            child = father
            # The crossover of chromosome, which from father
            self.cross(child, population_matrix)
            # The variational chromosome of child
            self.variation(child)
            new_population_matrix.append(child)
        # Transform for the new array, and return the new population
        new_population_matrix = np.array(new_population_matrix)
        return new_population_matrix

    def fitness_vector(self, population_matrix):
        """
        :param population_matrix: The matrix of population
        :return: the fitness of population
        """
        # Get the x, y vector of the population
        population_x_vector, population_y_vector = self.decoding(population_matrix)
        # Get the fitness of population
        fitness_vector = self.problem_function(population_x_vector, population_y_vector)
        # Fix the fitness, keep the fitness > zero
        fitness_vector = fitness_vector - np.min(fitness_vector) + 1e-3
        return fitness_vector

    def selection(self, population_matrix, fitness_vector):
        """
        :param population_matrix: The matrix of population
        :param fitness_vector: the fitness of population
        :return: the selected population
        """
        index_array = np.random.choice(np.arange(self.population_size),
                                       # The number of array
                                       size=self.population_size,
                                       # Allow to choice the element repeated
                                       replace=True,
                                       # Each probability of the element in this array
                                       p=fitness_vector/fitness_vector.sum()
                                       )
        return population_matrix[index_array]

    def print_result(self, population_matrix):
        """
        :param population_matrix: The population matrix
        :return:
        """
        # Get the vector of fitness
        fitness_vector = self.fitness_vector(population_matrix)
        # Get the maximum index of fitness
        optimal_fitness_index = np.argmax(fitness_vector)
        print(f'The best fitness :{fitness_vector[optimal_fitness_index]}')
        print(f'The best genetic :{population_matrix[optimal_fitness_index]}')
        # Get the vector of population x, y
        population_x_vector, population_y_vector = self.decoding(population_matrix)
        print(f'The optimal genotype decimal representation is :'
              f'{(population_x_vector[optimal_fitness_index], population_y_vector[optimal_fitness_index])}')


if __name__ == '__main__':
    fig = plt.figure()
    ax = Axes3D(fig, auto_add_to_figure=False)
    fig.add_axes(ax)
    plt.ion()
    sga = SGA()
    sga.plot_graph(ax)
    '''
    Generate the random matrix of population, as for sga.size*2, which is due to the population
    matrix is split into x and y matrices (chromosome, individual)
    If x and y are treated as alleles, both of x and y constitute chromosome pairs, affect the individual
    '''
    population_matrix = np.random.randint(2, size=(sga.population_size, sga.size*2))
    for _ in range(sga.generation_number):
        population_x_vector, population_y_vector = sga.decoding(population_matrix)
        ax.scatter(population_x_vector,
                   population_y_vector,
                   sga.problem_function(population_x_vector, population_y_vector),
                   c='g',
                   marker='x')
        plt.show()
        plt.pause(4.5)
        population_matrix = sga.update_population(population_matrix)
        fitness_vector = sga.fitness_vector(population_matrix)
        population_matrix = sga.selection(population_matrix, fitness_vector)
    sga.print_result(population_matrix)
    plt.ioff()
    plt.show()