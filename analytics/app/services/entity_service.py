import matplotlib as plt
from dal.sql_dal import get_target_location_by_day



class Processor:
    def Process(entity_id):
        locations = get_target_location_by_day()
        Processor.plot_entity(locations)


    @staticmethod
    def plot_entity(locations):
        x = [row[0] for row in locations]
        y = [row[1] for row in locations]

        plt.figure()
        plt.plot(x, y, marker="o")
        plt.scatter(x[0], y[0], color="green", label="start")
        plt.scatter(x[0], y[0], color="red", label="end")

        plt.show()


