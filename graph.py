import matplotlib.pyplot as plt
import numpy as np
import datetime

def graph(avgTemperature, humidity, precipitation, timestamp, y_gas, z_time):
        fig = plt.figure(figsize=(12.8, 5.5), facecolor='mediumpurple', edgecolor='black')
        ax = plt.axes()
        ax.set_facecolor('lavender')
        #plt.subplot(2, 1, 1)
        plt.xticks(rotation=30, ha='right', fontsize=8)
        plt.yticks(fontsize=8)
        plt.xlabel('Timestamp[t] -->', color='black')
        plt.ylabel('y axis -->', color='black')
        ############# Temp vs timestamp Graph ###############
        ypoints1 = np.array(avgTemperature)
        xpoints1 = np.array(timestamp)
        plt.plot(xpoints1, ypoints1, 'o-b', linewidth=0.5)
        ############# Humidity vs timestamp Graph ###############
        ypoints2 = np.array(humidity)
        xpoints2 = np.array(timestamp)
        plt.plot(xpoints2, ypoints2, 'o-r', linewidth=0.5)
        ############# Precipitation Vs. timestamp Graph ###############
        ypoints3 = np.array(precipitation)
        xpoints3 = np.array(timestamp)
        plt.plot(xpoints3, ypoints3, 'o-g', linewidth=0.5)
        plt.legend(["Temperature", "Humidity", "Precipitation"])
        plt.title("Forecasted Temperature, Humidity and Precipitation vs. Timestamp Graph", color='black', fontdict={'fontsize': 10})

        # plt.subplot(2, 1, 2)
        # ypoints4 = np.array(y_gas)
        # xpoints4 = np.array(z_time)
        # plt.plot(xpoints4, ypoints4, 'o-b', linewidth=0.5)
        # plt.ylim(0, 100)

        plt.show()