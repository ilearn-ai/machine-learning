import matplotlib.pyplot as plt

class TennisCourt:
    def __init__(self, length=23.77, width=8.23, service_line=6.40, net_height=0.91):
        self.length = length
        self.width = width
        self.service_line = service_line
        self.net_height = net_height

    def plot_court(self):
        fig, ax = plt.subplots()
        ax.set_aspect('equal')

        # Draw the court boundaries
        ax.add_patch(plt.Rectangle((0, 0), self.width, self.length, fill=False))

        # Draw the service boxes
        service_box_width = (self.width - self.service_line*2) / 2
        service_box_length = self.length - self.service_line
        ax.add_patch(plt.Rectangle((self.service_line, 0), service_box_width, service_box_length, fill=False))
        ax.add_patch(plt.Rectangle((self.width - self.service_line - service_box_width, 0), service_box_width, service_box_length, fill=False))

        # Draw the net
        ax.axhline(self.length/2, color='black', lw=2)
        ax.axhline(self.length/2 + self.net_height, color='black', lw=2)

        plt.show()       