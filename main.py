import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm,gamma,expon
import scipy.special as sp
from matplotlib.widgets import Slider

class Continuous_Distributions:
    def __init__(self,title):
        self.fig,self.ax=plt.subplots(figsize=(8,10))
        plt.subplots_adjust(bottom=0.25)
        self.x=np.linspace(-10,10,1000)
        self.title=title
        self.y = None
        self.graph_line = None

        self.ax.set_title(title)
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('Density')

    def show(self):
        plt.show()

class Normal_Distribution(Continuous_Distributions):
    def __init__(self,mean=1, stdev=1):
        super().__init__('Normal Distribution')
        self.mean=mean
        self.stdev=stdev

        self.fig,self.ax=plt.subplots(figsize=(8,10))
        plt.subplots_adjust(bottom=0.25)

        self.y=norm.pdf(self.x,self.mean,self.stdev)
        self.graph_line,=self.ax.plot(self.x,self.y,lw=2)

        self.create_sliders()

    def create_sliders(self):
        self.mean_ax=plt.axes([0.25, 0.1, 0.65, 0.03])
        self.st_dev_ax=plt.axes([0.25, 0.05, 0.65, 0.03])

        self.mean_slider=Slider(self.mean_ax,'Mean (μ)',-5,5,valinit=self.mean)
        self.stdev_slider=Slider(self.st_dev_ax,'Std Dev (σ)',0.1,5,valinit=self.stdev)

        self.mean_slider.on_changed(self.update)
        self.stdev_slider.on_changed(self.update)

    def update(self,val):
        self.new_mean=self.mean_slider.val
        self.new_stdev=self.stdev_slider.val

        self.y_new=norm.pdf(self.x,self.new_mean,self.new_stdev)
        self.graph_line.set_ydata(self.y_new)
      
class Exponential_Distribution(Continuous_Distributions):
    def __init__(self, lambda_rate=1):
        super().__init__('Exponential Distribution')
        self.lambda_rate=lambda_rate
    
        self.y=expon.pdf(self.x,self.lambda_rate)

        self.graph_line,=self.ax.plot(self.x,self.y,lw=2)

        self.create_sliders()

    def create_sliders(self):
        self.lambda_ax=plt.axes([0.25, 0.1, 0.65, 0.03])

        self.lambda_slider=Slider(self.lambda_ax,'Lambda (λ)',-5,5,valinit=self.lambda_rate)

        self.lambda_slider.on_changed(self.update)

    def update(self,val):
        self.new_lambda=self.lambda_slider.val

        self.y_new=expon.pdf(self.x,self.new_lambda)
        self.graph_line.set_ydata(self.y_new)

def gamma_pdf(x,k,t):
    return (x**(k-1) * np.exp(-x/t)) / (t**k * sp.gamma(k))

class Gamma_Distribution(Continuous_Distributions):
    def __init__(self,kappa=2,theta=1):
        super().__init__('Gamma Distribution')
        self.kappa=kappa
        self.theta=theta
        
        self.y=gamma.pdf(self.x,a=self.kappa,scale=self.theta)
        self.graph_line,=self.ax.plot(self.x,self.y,lw=2)

        self.create_sliders()

    def create_sliders(self):
        self.kappa_ax=plt.axes([0.25, 0.1, 0.65, 0.03])
        self.theta_ax=plt.axes([0.25, 0.05, 0.65, 0.03])

        self.kappa_slider=Slider(self.kappa_ax, 'K',-5,5, valinit=self.kappa)
        self.theta_slider=Slider(self.theta_ax, 'theta',-5,5, valinit=self.theta)

        self.kappa_slider.on_changed(self.update)
        self.theta_slider.on_changed(self.update)

    def update(self,val):
        self.new_kappa=self.kappa_slider.val
        self.new_theta=self.theta_slider.val

        self.new_y=gamma.pdf(self.x,a=self.new_kappa,scale=self.new_theta)
        self.graph_line.set_ydata(self.new_y)

